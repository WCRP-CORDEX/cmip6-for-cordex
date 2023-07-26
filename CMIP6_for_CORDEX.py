"$run.json.js"
".$_-0/@{D9/N9/W9/9d}`, @moneyman573 , @lostleolotus"
"vi_vi_vi_1-9-Cc-3-9.json"
@@ "-1,3 +1,6" @@
$ 
  ~_
~'build.json'
~ build.Cc-3-9
_L
-
@@ -119,3 +122,6 @@ krCaoG4Hx0zGQG2ZFpHrSrZTVy6lxvIdfi0beMgY6h78p6M9eYZHQHc02DjFkQXN
bXb5c6gCHESH5PXwPU4jQEE7Ib9J6sbk7ZT2Mw==
=j+4q
-----END PGP PUBLIC KEY BLOCK-----
_
  ~- key: Tok20 Constrained TCR
  doi: 10.1126/sciadv.aaz9549
  metric:
    name: TCR
    long_name: Transient Climate Response
    units: K
    variables: tas
    comment: >
      For the TCR values of the individual GCM, we do not use the values proposed initially in Tokarska et al. 2020 but the values provided by th IPCC WGI AR6 on Table 7.SM.5 (https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Material.pdf), completed by some values from the original article
  disabled: 
    cause: preferred_source
    preferred: Rib21 Constrained TCR
    comment: More conservative estimate than preferred source
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  period:
    reference: 1981-2014
    comment: >
      This is not the period for the metric values (these are model years at
      the time of doubling CO2), but the one used in the observational constraint.
  plausible_values:
    min: 0.9
    max: 2.27
    source: reference
    comment: >
      Constrained TCR using 1981-2014 temperature past trends, 90% likely range
      (5-95%) for the TCR. See Table S3. On this Table there are also TCR ranges
      based on 1981-2017.
      This period was selected because it leads to a wider, more conservative
      plausible range.
  data_source: reference
  data:
    ACCESS-CM2_r1i1p1f1: 2.10
    ACCESS-ESM1-5_r1i1p1f1: 1.95
    AWI-CM-1-1-MR_r1i1p1f1: 2.06
    BCC-CSM2-MR_r1i1p1f1: 1.72
    BCC-ESM1_r1i1p1f1: 1.77
    CAMS-CSM1-0_r1i1p1f1: 1.73
    CAS-ESM2-0_r1i1p1f1: 2.04
    CESM2_r2i1p1f1: 2.06
    CESM2-FV2_r1i1p1f1: 2.05
    CESM2-WACCM_r1i1p1f1: 1.98
    CESM2-WACCM-FV2_r1i1p1f1: 2.01
    CIESM_r1i1p1f1: 2.39
    CMCC-CM2-SR5_r1i1p1f1: 2.09
    CNRM-CM6-1_r1i1p1f2: 2.14
    CNRM-CM6-1-HR_r1i1p1f2: 2.48
    CNRM-ESM2-1_r1i1p1f2: 1.86
    CanESM5_r1-3i1p2f1: 2.74
    E3SM-1-0_r1i1p1f1: 2.99
    EC-Earth3_r1i1p1f1: 2.30
    EC-Earth3-Veg_r1-3i1p1f1: 2.62
    FGOALS-f3-L_r1i1p1f1: 1.94
    FGOALS-g3_r1i1p1f1: 1.54
    FIO-ESM-2-0_r1i1p1f1: 2.22
    GFDL-ESM4_r1i1p1f1: 1.61 # Missing in AR6 (this is from Ribes et al., 2021)
    GISS-E2-1-G_r1i1p1f1: 1.80
    GISS-E2-1-H_r1i1p1f1: 1.93
    GISS-E2-2-G_r1i1p1f1: 1.71
    HadGEM3-GC31-LL_r1i1p1f1: 2.55
    HadGEM3-GC31-MM_r1i1p1f1: 2.58
    IITM-ESM_r1i1p1f1: 1.71
    INM-CM4-8_r1i1p1f1: 1.33
    INM-CM5-0_r1i1p1f1: 1.39 # Missing in AR6 (this is from Ribes et al., 2021)
    IPSL-CM6A-LR_r1-6i1p1f1: 2.32
    IPSL-CM6A-LR_r14i1p1f1: 2.32
    KACE-1-0-G_r1i1p1f1: 1.41
    MCM-UA-1-0_r1i1p1f1: 1.94
    MIROC-ES2L_r1i1p1f1: 1.55
    MIROC6_r1i1p1f1: 1.55
    MPI-ESM-1-2-HAM_r1i1p1f1: 1.80
    MPI-ESM1-2-HR_r1i1p1f1: 1.66
    MPI-ESM1-2-LR_r1i1p1f1: 1.84
    MRI-ESM2-0_r1i1p1f1: 1.64
    NESM3_r1i1p1f1: 2.72
    NorCPM1_r1i1p1f1: 1.56
    NorESM2-LM_r1i1p1f1: 1.48
    NorESM2-MM_r1i1p1f1: 1.33
    SAM0-UNICON_r1i1p1f1: 2.27
    TaiESM1_r1i1p1f1: 2.34
    UKESM1-0-LL_r1-3i1p1f2: 2.79
  "$run.json-.js"
"<.$_-build.py-config"
".config.py"
".$_-!.py"
".$_-!py/usr/bin/env.py"= "python3"
`<".$_-0/.py
"import datetime
"from pyesgf.search import SearchConnection
"import logging
"import natsort as ns
"import numpy as np
"import pandas as pd
"import re">`
loglevel = logging.INFO
logger = logging.getLogger('root')
logger.setLevel(loglevel)
loghandler = logging.StreamHandler()
loghandler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(loghandler)

scenarios = ['ssp119', 'ssp126', 'ssp245', 'ssp370', 'ssp585']
contexts = {
  '6hrLev' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'table_id': '6hrLev',
  },
  '3Dpl' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['ua','va','ta','zg','hus','hur'],
    'table_id': 'day',
  },
  'LowerBoundaries' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['tos','siconc','od550aer'],
  },
   'AerosolExtra' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': [
      # P2 (different types of aerosols, strongly advised)
      'od550bb', 'od550bc', 'od550dust', 'od550no3',
      'od550oa', 'od550so4', 'od550ss', 'od550so4so',
      # P3 (in option)
      'aerasymbnd', 'aeroptbnd', 'aerssabnd'
    ],
  },
  'Basic' : {
    'project': 'CMIP6',
    'experiment_id': ['historical']+scenarios,
    'variable_id': ['tas','pr','psl','tasmax','tasmin'],
    'frequency': 'day',
  },
}
facets = (
  'project', 'activity', 'institution', 'model', 'experiment',
  'run', 'table', 'variable', 'grid', 'version'
)
tags = { # Values are python sets
  'RCM': {'hus-ml', 'ta-ml', 'ua-ml', 'va-ml', 'tos', 'siconc', 'od550aer'},
  '3Dml': {'hus-ml', 'ta-ml', 'ua-ml', 'va-ml'},
  'ESD': [
    {'hus', 'zg', 'ta', 'ua', 'va', 'psl', 'pr', 'tas', 'tasmax', 'tasmin'},
    {'hur', 'zg', 'ta', 'ua', 'va', 'psl', 'pr', 'tas', 'tasmax', 'tasmin'},
    ],
  'Basic': {'pr', 'tas'},
}

def aggfun(x):
  xset = set(x)
  for k in tags:
    if type(tags[k]) != type([]):
      alternative_sets = [tags[k]]
    else:
      alternative_sets = tags[k]
    for altset in alternative_sets:
      if altset.issubset(xset):
        return(k)
  return('-')

#
#   Load search results
#
conn = SearchConnection('http://esgf-data.dkrz.de/esg-search', distrib=True)
logging.getLogger('pyesgf.search.connection').setLevel(loglevel)
df = pd.DataFrame()
for context in contexts.keys():
  logger.info(f'Retrieving {context} variables ...')
  ctx = conn.new_context(**contexts[context])
  dids = [result.dataset_id for result in ctx.search(batch_size=1000, ignore_facet_check=True)]
  open('CMIP6_for_CORDEX__%s.txt' % context, 'w').writelines([did+'\n' for did in sorted(dids)])
  datanode_part = re.compile('\|.*$')
  dataset_ids = [datanode_part.sub('', did).split('.') for did in dids]
  df = df.append(pd.DataFrame(dataset_ids))

df.columns = facets
df['modelrun'] = df[['model','run']].apply(lambda x: '_'.join(x), axis = 1)
# Add ml and pl tags to distinguish model and pressure level variables
df[df[['table']]=='6hrLev'] = '-ml'
df[(df[['table']]!='-ml') & (df[['table']]!='-pl')] = ''
df['variable'] = df[['variable', 'table']].apply(lambda x: ''.join(x), axis = 1)
# Sort the runs naturally
df['nsrun'] = ns.natsort_key(df.run)
df.sort_values(by=['model','experiment','nsrun','variable'], inplace = True)
# Drop unnecessary columns
df.drop(
  ['project', 'activity', 'grid', 'version', 'table', 'nsrun'],
  axis = 'columns', inplace = True
)
# Disregard replicas and different versions and different tables (frequencies!)
df.drop_duplicates(inplace = True)
df.to_csv('df.csv', float_format = '%g', sep = ';', decimal = ',', index = False)

#
#   Variable availability table
#
# One-liner to tag variable availability by model run and experiment
varcount = df.groupby(['modelrun', 'experiment'])['variable'].agg(aggfun).unstack()
# Sort also this table by runs in a natural way
varcount['nsmodelrun'] = ns.natsort_key(varcount.index)
varcount.sort_values(by=['nsmodelrun'], inplace = True)
varcount.drop(['nsmodelrun'], axis = 'columns', inplace = True)
# Split model and run
varcount.index = varcount.index.str.split('_', expand = True)
# Add synthesis column (ssp126 and ssp370 available for dyn. downscaling)
varcount.insert(0, 'synthesis',
  np.multiply((varcount['ssp126'] == 'RCM') & (varcount['ssp370'] == 'RCM'),1)
)
#
#   CSV output
#
varcount.to_csv('docs/CMIP6_for_CORDEX_availability_ESGF.csv', float_format = '%g',
  index_label = ['model', 'run']
)
#
#   Time stamp
#
with open('LASTUPDATE', 'w') as fp:
  fp.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
