import datetime
import natsort as ns
import numpy as np
import pandas as pd
import seaborn as sns
import sys
import YamlStudies as ys
import yaml
from icecream import ic

CORDEX_DOMAIN = sys.argv[1]

def synthesis_sum_failures(binvalues, test = False):
  if test:
    return(binvalues == 0)
  else:
    return(np.sum(1-binvalues, axis=1, initial=0, where=~np.isnan(binvalues.astype(float))))

def synthesis_proportion_right(binvalues, test = False):
  if test:
    return(binvalues > 0.2)
  else:
    n = binvalues.shape[1]
    return(np.sum(binvalues, axis=1, initial=0, where=~np.isnan(binvalues.astype(float)))/n)

def synthesis_any_failure(binvalues, test = False):
  if test: 
    return(binvalues == 1)
  else:
    return(np.logical_and.reduce(binvalues, axis=1, initial=True, where=~np.isnan(binvalues.astype(float)))*1)

synthesis = synthesis_sum_failures

with open('CMIP6_studies_config.yaml') as fp:
  config = yaml.load(fp, Loader=yaml.FullLoader)

def get_from_config(config, label, domain):
  '''Get configuration option for domain considering the default value'''
  return(config[label].get(domain, config[label]['default']))

alldata = ys.load_from_files('CMIP6_studies/*.yaml', skip_disabled = True, skip_disabled_domain = CORDEX_DOMAIN)
# filter and sort
alldata = [x for x in alldata if x.spatial_scope in config['spatial_scope_filter'][CORDEX_DOMAIN]]
alldata.sort(key=lambda x: config['spatial_scope_filter'][CORDEX_DOMAIN].index(x.spatial_scope))

# Performance
tableperf = pd.concat([x.data for x in alldata if x.type=='performance'], axis=1)

# Plausible range rows
tableprange= pd.concat(
  [x.get_plausible_values() for x in alldata if x.type in ('performance')],
  axis=1
)
tableprange.index = pd.MultiIndex.from_tuples(
  [('. Plausible values', idx) for idx in tableprange.index],
  names = ['model','run']
)

# Classes table (when available)
tableclass = pd.concat([x.get_class_data() for x in alldata], axis=1)
tableclass = tableclass.reindex(ns.natsorted(tableclass.index))

# Binary table
tablebin = pd.concat([x.get_plausible_mask() for x in alldata if x.type=='performance'], axis=1) * 1
# Add synthesis column
tableperf.insert(0, column='Synthesis', value=synthesis(tablebin.values))
tableprange = pd.concat([tableprange, tableperf])
# sort synthesis column first
synthfirst = list(tableprange.columns)
synthfirst.insert(0, synthfirst.pop(synthfirst.index('Synthesis')))
tableprange = tableprange.reindex(synthfirst, axis=1)

# Spread
tablespread = pd.concat(
  [x.get_formatted_data() for x in alldata if x.type=='future_spread'],
  axis=1
)

# Other
tableother = pd.concat(
  [x.data for x in alldata if x.type=='other'],
  axis=1
)

# Availability
tableavail = pd.read_csv('docs/CMIP6_for_CORDEX_availability_ESGF.csv').set_index(['model', 'run'])
non_esgf = pd.read_csv('CMIP6_for_CORDEX_availability_non_ESGF.csv').set_index(['model', 'run'])
tableavail.update(non_esgf)
# - update synthesis column
mandatory_scenarios = ['historical','ssp126', 'ssp370']
lbc_for_source_type = get_from_config(config, 'lbc_for_source_type', CORDEX_DOMAIN)
tableavail.loc[:,'synthesis'] = np.logical_and.reduce(
  tableavail.loc[:,mandatory_scenarios] == lbc_for_source_type, axis=1
) * 1
tableavail.loc[:,'synthesis'] = tableavail.loc[:,'synthesis'].astype(int)
# - filter out entries with less than 2 scenarios unless a metric is available for it
availscenarios = ['ssp126', 'ssp245', 'ssp370', 'ssp585']
tableavail_row_filter = np.sum(tableavail.loc[:,availscenarios] == lbc_for_source_type, axis=1) >= 2
row_filter = set(tableavail.index[tableavail_row_filter]).union(
  tableprange.index,
  tablespread.index,
  tableother.index
).intersection(tableavail.index)
tableavail = tableavail.loc[row_filter]

# All together
main_headers = ['1. Availability', '2. Plausibility', '3. Spread of future outcomes', '4. Other criteria']
tablefull = pd.concat(
  [tableavail, tableprange,tablespread, tableother], axis=1, 
  keys=main_headers
)
tablefull = tablefull.reindex(ns.natsorted(tablefull.index))
# Dump final CSV
csvout = f'docs/CMIP6_studies_table_{CORDEX_DOMAIN}.csv'
tablefull.to_csv(csvout, float_format = '%.2f', index_label = ['model', 'run'])
# Some fixes for Google Spreadsheet
fp = open(csvout, 'r')
lines = fp.readlines()
fp.close()
lines[1] = lines[1].replace(',,','model,run,')
fp = open(csvout, 'w')
fp.writelines([lines[0]]+lines[3:5]+[lines[1]]+lines[5:])
fp.close()

#
# Automatic styling (rendered as HTML)
#
def hide_nan(df):
  attr = 'color: white'
  rval = df.copy()
  rval.fillna(attr, inplace=True)
  #rval.where(str(rval) != 'nan', attr, inplace=True)
  rval.where(rval == attr, '', inplace=True)
  return(rval)

def greyout_non_rcm(df):
  attr = 'color: grey'
# Bug in pandas https://github.com/pandas-dev/pandas/issues/35429
#  return(df.where(df == 'RCM', attr))
  rval = df.copy()
  rval.iloc[:] = np.where((rval == lbc_for_source_type).fillna(False), rval, attr)
  return(rval)

def greyout_unplausible(df):
  attr = 'color: grey'
  is_out = (df > df.iloc[0]) | (df < df.iloc[1])
  return([attr if v else '' for v in is_out.fillna(False)])

def greyout_unplausible_rows(df):
  global filter_plausible
  attr = 'color: grey'
  rval = df.copy().astype('string')
  rval.update(filters['filter_plausible'].map({False: attr, True: ''}))
  return(rval)

def highligh_plausible_range(df):
  attr = 'background-color: lightgrey'
  return([(attr if '. Plausible values' in v else '') for v in df.index])

def color_classes(df):
  class_data = get_class_info(df)
  rval = df.copy().astype('string')
  rval.iloc[:] = ''
  if class_data:
    levels, classes = class_data
    colors = sns.color_palette("Spectral_r", len(levels)).as_hex()
    rval.update(classes.astype('string').map(dict(zip(levels,[f'background-color:{c}' for c in colors]))))
  return(rval)

def remove_trailing_ssp(string):
  rval = string
  if rval[-6:-3] == 'ssp':
    rval = rval[:-7]
  return(rval)

def get_class_info(series):
  global alldata
  key = remove_trailing_ssp(series.name[1])
  entry = alldata[[x.key for x in alldata].index(key)]
  if entry.has_classes():
    return(entry.classes[0].labels,entry.get_class_data().loc[:,series.name[1]])
  else: # Terciles
    return([f'T{x}' for x in range(1,3+1)],entry.get_class_data().loc[:,series.name[1]])

def get_cols_under(header, df, drop=''):
  values = df.columns.get_loc_level(header, level=0)[1]
  if drop:
    values = values.drop(drop)
  return([(header,x) for x in values])

def single_member(filt):
  # Select the member with the smallest amount of missing evaluation metrics
  filter_single_member = ~filter_all.copy()
  perfscores = tablefull[main_headers[1]].iloc[:,1:]
  # Avoid selecting members that would disappear when filt'ered
  perfscores.loc[~filt] = np.nan
  member = np.sum(np.isnan(perfscores), axis=1).groupby(level=0).idxmin()
  filter_single_member.loc[member] = True
  return( filt & filter_single_member )

# Column subsets
availcols = get_cols_under(main_headers[0], tablefull, drop = 'synthesis')
perfcols = get_cols_under(main_headers[1], tablefull, drop = 'Synthesis')
spreadcols = get_cols_under(main_headers[2], tablefull)
othercols = get_cols_under(main_headers[3], tablefull)
# Row filters
filters = dict()
filters['filter_avail'] = tablefull[(main_headers[0], 'synthesis')] == 1
filters['filter_plausible'] = synthesis(tablefull[(main_headers[1], 'Synthesis')], test = True)
filters['filter_avail_and_plausible'] = filters['filter_avail'] & filters['filter_plausible']
filter_all = filters['filter_avail'].copy()
filter_all.iloc[:] = True
filters['filter_all'] = filter_all
plans = pd.read_csv('CMIP6_downscaling_plans.csv')
selected = plans[plans['domain'].str.startswith(CORDEX_DOMAIN)]
filter_selected = filter_all.copy()
filter_selected.iloc[:] = filter_selected.index.isin(set(zip(selected['driving_model'],selected['ensemble'])))
filters['filter_selected'] = filter_selected
show_single_member = get_from_config(config, 'show_single_member', CORDEX_DOMAIN)
if show_single_member:
  # Convert some filters to show a single member
  single_member_in_title = ' (single member)'
  for filtname in ['filter_avail', 'filter_avail_and_plausible', 'filter_plausible']:
    filters[filtname] = single_member(filters[filtname])
else:
  single_member_in_title = ''
pd.set_option('precision', 2)
format_dict = { # Format exceptions
                         ('2. Plausibility', 'Nabat EUR AOD hist trend'): '{:.3f}',
  ('3. Spread of future outcomes', 'Nabat EUR AOD future change ssp585'): '{:.3f}'
}
d1 = dict(selector=".level0", props=[('min-width', '150px')])
f = open(f'docs/CMIP6_studies_table_{CORDEX_DOMAIN}.html','w')
f.write(f'''<!DOCTYPE html>
<html><head>
<style>
body {{ }}
tr:hover {{background-color:#f5f5f5;}}
th, td {{text-align: center; padding: 3px;}}
table {{border-collapse: collapse;}}
a {{color: DodgerBlue}}
a:link {{ text-decoration: none; }}
a:visited {{ text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:active {{ text-decoration: underline;}}
</style>
</head><body>
<h1> CMIP6 for CORDEX summary tables (domain {CORDEX_DOMAIN})</h1>
<p style="font-size: smaller; text-align: right;">(Version: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")})</p>
<p style="font-size: smaller; text-align: justify;">
Summary of CMIP6 ScenarioMIP simulation (1) availability, (2) plausibility, (3) spread of future outcomes and (4) other criteria relevant for GCM selection for downscaling in the context of the CORDEX {CORDEX_DOMAIN} domain.
<b>Availability</b> is labeled according to the variables and frequency available:
RCM (6h 3D model level data, along with SST, sea ice and AOD),
3Dml (6h 3D model level data),
ESD (6h specific or relative humidity, geopotential height, temperature and wind at pressure levels, and mean sea level pressure, precipitation, near-surface mean, minimum and maximum air temperature),
Basic (daily precipitation and mean near-surface air temperature).
A dash (-) indicates that the simulation exists in ESGF, but none of the conditions to get one of the previous labels applied.
Empty cells represent unavailable simulations (either at ESGF or the producing center).
The synthesis column indicates whether the CORDEX-CMIP6 protocol mandatory scenarios (SSP3-7.0 and SSP1-2.6) are available (1) or not (0).
<b>Plausibility</b> is measured by different performance metrics (in columns), usually against reanalysis or other observational data.
Additional metrics can be contributed at <a href="https://github.com/WCRP-CORDEX/cmip6-for-cordex/tree/main/CMIP6_studies">https://github.com/WCRP-CORDEX/cmip6-for-cordex/tree/main/CMIP6_studies</a>
The range of plausible values (top two rows) determine the values of the metrics which are considered unplausible (these values are greyed out).
Column headers are links to full details of the metric definitions, scope, plausible ranges and their origin.
Columns are sorted according to the spatial scope of the metrics (global metrics to the left).
The synthesis column indicates the number of unplausible metric values for a given model simulation.
Note that low synthesis values represent plausible models, but also models included in few evaluation studies.
The <b>spread of future outcomes</b> is also based on published metrics, but usually referred to differences between a future period from a scenario simulation and a historical period (delta change).
Cell background is coloured according to categories clustering the range of outcomes.
Numbers for simulations showing some unplausible performace metric are greyed out.
<b>Other criteria</b> include other aspects, such as model family, complexity, or resolution.
The values for simulations showing some unplausible performace metric are also greyed out.
</p>
<ul>''')
filter_metadata = {
  'filter_avail_and_plausible': dict(
    id='avail-and-plausible',
    header='Filter: available and plausible' + single_member_in_title,
    text=''
  ), 
  'filter_avail': dict(
    id='avail',
    header='Filter: available' + single_member_in_title,
    text=''
  ),
  'filter_plausible': dict(
    id='plausible',
    header='Filter: plausible' + single_member_in_title,
    text=''
  ),
  'filter_selected': dict(
    id='selected',
    header='Selected GCMs + institutional plans',
    text='See institutional plans at <a href="https://github.com/WCRP-CORDEX/simulation-status/blob/main/CMIP6_downscaling_plans.csv" target="_blank">CMIP6_downscaling_plans.csv</a><br>'
  ),
  'filter_all': dict(
    id='all',
    header='All members with 2 or more scenarios and/or some metric available',
    text=''
  )
}
domain_filters = get_from_config(config, 'tables_filter', CORDEX_DOMAIN)
f.write('\n'.join([f'\n<li><a href="#{filter_metadata[filtname]["id"]}">{filter_metadata[filtname]["header"]}</a></li>' for filtname in domain_filters]))
f.write('</ul>')
for filtname in domain_filters:
  if ~filters[filtname].any(): # Skip empty tables
    continue
  filters[filtname].iloc[0:2] = True # keep plausible value rows
  id = filter_metadata[filtname]['id']
  header = filter_metadata[filtname]['header']
  text = filter_metadata[filtname]['text']
  f.write(f'<h2 id="{id}">{header}</h2>\n{text}')
  f.write(tablefull
    .loc[filters[filtname]]
    .convert_dtypes(convert_string = False, convert_boolean = False)
    .style
      .format(format_dict)
      .set_properties(**{'font-size':'8pt', 'border':'1px lightgrey solid !important'})
      .set_table_styles([d1,{
        'selector': 'th',
        'props': [('font-size', '8pt'),('border-style','solid'),('border-width','1px')]
      }])
      .apply(greyout_non_rcm, axis=None, subset=availcols)
      .apply(greyout_unplausible, axis=0, subset=perfcols)
      .apply(greyout_unplausible_rows, axis=0, subset=spreadcols+othercols)
      .apply(highligh_plausible_range, axis=0)
      .apply(color_classes, axis=0, subset=spreadcols)
      .render()
      .replace('nan','')
  )
f.write('</body></html>')
f.close()

# Headers as links (dirty stuff...)
baseurl = f'https://github.com/WCRP-CORDEX/cmip6-for-cordex/blob/main/docs/CMIP6_studies_list_{CORDEX_DOMAIN}.md'
with open(f'docs/CMIP6_studies_table_{CORDEX_DOMAIN}.html','r') as f:
  fulltext = f.read()

for head in [x[1] for x in spreadcols+perfcols+othercols]:
  anchor = remove_trailing_ssp(head)
  anchor = anchor.lower()
  anchor = anchor.replace(' ', '-')
  anchor = anchor.replace('.', '')
  fulltext = fulltext.replace('>'+head+'<', f'><a href="{baseurl}#{anchor}" target="_blank">{head}</a><')

with open(f'docs/CMIP6_studies_table_{CORDEX_DOMAIN}.html','w') as f:
  f.write(fulltext)

