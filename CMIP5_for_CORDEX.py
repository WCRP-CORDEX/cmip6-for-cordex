#!/usr/bin/env python3
import datetime
from pyesgf.search import SearchConnection
import logging
import natsort as ns
import numpy as np
import pandas as pd
import re

loglevel = logging.INFO
logger = logging.getLogger('root')
logger.setLevel(loglevel)
loghandler = logging.StreamHandler()
loghandler.setFormatter(logging.Formatter('[%(asctime)s] %(message)s'))
logger.addHandler(loghandler)

scenarios = ['rcp26', 'rcp45', 'rcp60', 'rcp85']
contexts = {
  '6hrLev' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': '6hr',
    'realm': 'atmos',
    'variables': ['ta', 'ua', 'va', 'hus'],
  },
  '3Dpl' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': 'day',
    'realm': 'atmos',
    'variables': ['zg', 'ta', 'ua', 'va', 'hus'],
  },
  'LowerBoundaries' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': 'mon',
    'variables': ['tos', 'sic', 'od550aer'],
  },
  'Ocean' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': 'mon',
    'realm': 'ocean',
    'variables': ['thetao', 'bigthetao', 'so', 'zos'],
  },
   'AerosolExtra' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': 'mon',
    'realm': 'atmos',
    'variables': [
      'od550bb', 'od550bc', 'od550dust', 'od550no3',
      'od550oa', 'od550so4', 'od550ss', 'od550so4so',
      'aerasymbnd', 'aeroptbnd', 'aerssabnd'
    ],
  },
  'Basic' : {
    'project': 'CMIP5',
    'experiment': ['historical'] + scenarios,
    'time_frequency': 'day',
    'realm': 'atmos',
    'variables': ['tas', 'pr', 'psl', 'tasmax', 'tasmin'],
  },
}
facets = (
  'project', 'product', 'institute', 'model', 'experiment',
  'time_frequency', 'realm', 'table', 'ensemble', 'version'
)
tags = { # Values are python sets
  'AORCM': [
    {'thetao', 'zos', 'so', 'hus-ml', 'ta-ml', 'ua-ml', 'va-ml', 'tos', 'sic', 'od550aer'},
    {'bigthetao', 'zos', 'so', 'hus-ml', 'ta-ml', 'ua-ml', 'va-ml', 'tos', 'sic', 'od550aer'},
    ],
  'ARCM': {'hus-ml', 'ta-ml', 'ua-ml', 'va-ml', 'tos', 'sic', 'od550aer'},
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
dflist = []
for context, params in contexts.items():
  for variable in params['variables']:
    logger.info(f'Retrieving {context} variable {variable} ...')
    query = {
      'project': params['project'],
      'experiment': params['experiment'],
      'time_frequency': params['time_frequency'],
   #   'realm': params['realm'],
      'variable': variable,
    }
    ctx = conn.new_context(**query)
    dids = [result.dataset_id for result in ctx.search(batch_size=1000, ignore_facet_check=True)]
    open(f'CMIP5_for_CORDEX__{context}_{variable}.txt', 'w').writelines([did + '\n' for did in sorted(dids)])
    datanode_part = re.compile('\|.*$')
    dataset_ids = [datanode_part.sub('', did).split('.') for did in dids]
    df_context = pd.DataFrame(dataset_ids)
    df_context['variable'] = variable  # Add variable explicitly
    dflist.append(df_context)

df = pd.concat(dflist)
df.columns = list(facets) + ['variable']  # Align columns
df['modelrun'] = df[['model', 'ensemble']].apply(lambda x: '_'.join(x), axis=1)
# Add ml and pl tags to distinguish model and pressure level variables based on table
df['level'] = ''
df.loc[df['table'] == '6hrLev', 'level'] = '-ml'
df.loc[df['table'] == '6hrPlev', 'level'] = '-pl'
df['variable'] = df[['variable', 'level']].apply(lambda x: ''.join(x), axis=1)
# Sort the runs naturally
df['nsrun'] = ns.natsort_key(df.ensemble)
df.sort_values(by=['model', 'experiment', 'nsrun', 'variable'], inplace=True)
# Drop unnecessary columns
df.drop(
  ['project', 'product', 'version', 'realm', 'time_frequency', 'nsrun', 'level'],
  axis='columns', inplace=True
)
# Disregard replicas and different versions and different tables (frequencies!)
df.drop_duplicates(inplace=True)
df.to_csv('df.csv', float_format='%g', sep=';', decimal=',', index=False)

#
#   Variable availability table
#
# One-liner to tag variable availability by model run and experiment
varcount = df.groupby(['modelrun', 'experiment'])['variable'].agg(aggfun).unstack()
# Sort also this table by runs in a natural way
varcount['nsmodelrun'] = ns.natsort_key(varcount.index)
varcount.sort_values(by=['nsmodelrun'], inplace=True)
varcount.drop(['nsmodelrun'], axis='columns', inplace=True)
# Split model and run
varcount.index = varcount.index.str.split('_', expand=True)
# Add synthesis column (rcp26 and rcp85 available for dyn. downscaling)
varcount.insert(0, 'synthesis',
  np.multiply((varcount['rcp26'] == 'RCM') & (varcount['rcp85'] == 'RCM'), 1)
)
#
#   CSV output
#
varcount.to_csv('docs/CMIP5_for_CORDEX_availability_ESGF.csv', float_format='%g',
  index_label=['model', 'run']
)

