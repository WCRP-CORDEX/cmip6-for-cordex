## Incomplete entries

 * [Fas20](CMIP6_studies/Fas20.yaml)
 * [Beo21](CMIP6_studies/Beo21.yaml)
 * [Cob21](CMIP6_studies/Cob21.yaml)
## Globally disabled entries

 · [Atlas Dtas world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dtas world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world DJF](CMIP6_studies/AtlasIPCC.yaml)
 · [Atlas Dpr world JJA](CMIP6_studies/AtlasIPCC.yaml)
 · [Tok20 Constrained TCR](CMIP6_studies/Tok20.yaml)
 · [Fas20](CMIP6_studies/Fas20.yaml)
 · [Beo21](CMIP6_studies/Beo21.yaml)
 · [Rib21 Constrained TCR](CMIP6_studies/Rib21.yaml)
 · [Cob21](CMIP6_studies/Cob21.yaml)
## Entries disabled in NAM

## Available entries (NAM scope)
### Plausibility
#### AR6 TCR

Located in [CMIP6_studies/AR6.yaml](../CMIP6_studies/AR6.yaml)

None

```
- key: AR6 TCR
  doi: None
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: TCR
    long_name: Transient Climate Response
    units: K
    variables: tas
    comment:
      TCR as provided by th IPCC WGI AR6 on Table 7.SM.5 (https://www.ipcc.ch/re
      port/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Materi
      al.pdf).
  plausible_values:
  - min: 1.2
    max: 2.4
    source: reference
    comment:
      This is a 90% (very likely) range for the TCR according to AR6 Technical
      Summary: Based on  process understanding, warming over the instrumental
      record, and emergent constraints, the best estimate of TCR is 1.8 degC,
      the likely range is 1.4 to 2.2 degC and the very likely range is 1.2 to
      2.4 DegC. There is a high level of agreement among the different lines of
      evidence (Figure TS.16c) (high confidence). {7.5.5}

```

#### Bru20 perf

Located in [CMIP6_studies/Bru20.yaml](../CMIP6_studies/Bru20.yaml)

10.5194/esd-11-995-2020

```
- key: Bru20 perf
  doi: 10.5194/esd-11-995-2020
  type: performance
  spatial_scope: Global
  data_source: reference
  metric:
    name: perf
    long_name: None
    units: None
    variables: ['tas', 'psl']
    comment:
      Evaluation of the model using global criteria performance criteria (past
      trends + spatial pattern) Model with performance scores below 0.006 are
      considered as irrealistic.  This study is based on multi-member for each
      model, not on only one member. Wrt to the original article, we consider
      here only the performance criteria and not the combined criteria that
      takes also into account the independence.
  period:
    reference: 1980-2014
  plausible_values:
  - min: 0.006
    max: 0.2
    source: author
    comment:
      The 0.006 threshold has been provided by the author (expert judgment)
      after email exchanges with S. Somot

```

#### Dalelane MNQS

Located in [CMIP6_studies/Dalelane.yaml](../CMIP6_studies/Dalelane.yaml)

['pers. comm.', 'C. Dalelane', 'DWD']

```
- key: Dalelane MNQS
  doi: ['pers. comm.', 'C. Dalelane', 'DWD']
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: author
  metric:
    name: MNQS
    long_name: Multivariate Network Quality Score for Global Teleconnections
    units: 1
    variables: tos, z500
    comment:
      Data is converted to seasonal anomalies, detrended with season-reliant
      trend-EOFs.  Seasonal variances normalized.  Adjacency-matrix between all
      pairs of grid cell with Spearman's rank correlation.  Maximal domains in
      tos (z500) with average pairwise rank correlation>0.95(0.93)- quantile of
      all pairwise correlations are found. All pairwise links between domains
      (area weighted average time series) calculated with Distance correlation
      in tos,  z500 and cross-links between tos and z500. Tested to level 0.05
      with control of  False Discovery Rate=0.05. New adjacency matrices
      constructed based on domain links. Adjacency matrices compared to
      references with Structural Similarity Index (SSIM).       Exponential
      transform wrt. value 1 for all 3 variables (individual Network Quality
      Score-NQS). Geometric mean of NQSs over variables (Multivariate Network
      Quality Score, MNQS). Average of MNQSs over references.
    best: 1
    worst: 0
  plausible_values:
  - min: 0
    max: 1
    source: author
    comment:
      the higher the better, MNQS between references in the table for comparison

```

#### Qasmi Constr Global Dtas ssp245 2050

Located in [CMIP6_studies/Qasmi.yaml](../CMIP6_studies/Qasmi.yaml)

10.1126/sciadv.abc0671

```
- key: Qasmi Constr Global Dtas ssp245 2050
  doi: 10.1126/sciadv.abc0671
  type: performance
  spatial_scope: Global
  temporal_scope: Annual
  data_source: author
  metric:
    name: Constrained-Dtas
    long_name: Observationally-contrained future climate change
    units: binary
    variables: tas
    comment:
      Constrained global annual temperature future climate change range,
      2041-2060 vs 1850-1900, SSP245 (adapted from Ribes et al. 2021, Science
      Advances by S. Qasmi). In particular by adding recently available CMIP6
      GCM, now 40 GCMs.
  period:
    reference: 1850-1900
    target: 2041-2060
  plausible_values:
  - min: 1
    max: 1
    source: author
    comment:
      models lying outside the observationally-constrained 90% interval obtained
      by the method are considered as implausible. The 90% interval is [1.5 ;
      2.1]degC for the period 2041-2060 vs 1850-1900, SSP245. Multi-member
      ensemble mean is used in this study for every model. Note that this
      criteria is very strict and can potentially eliminate a large number of
      GCMs.

```

### Spread of future outcomes
#### AR6 TCR as spread

Located in [CMIP6_studies/AR6.yaml](../CMIP6_studies/AR6.yaml)

None

```
- key: AR6 TCR as spread
  doi: None
  type: future_spread
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: TCR
    long_name: Transient Climate Response
    units: K
    variables: tas
    comment:
      TCR as provided by th IPCC WGI AR6 on Table 7.SM.5 (https://www.ipcc.ch/re
      port/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter_07_Supplementary_Materi
      al.pdf).
  classes:
  - limits: [-10, 1.2, 1.6, 2.0, 2.4, 10]
    labels: ['very low', 'low', 'moderate', 'high', 'very high']
    source: eurocordex_gcm_selection_team
    comment:
      A proposal with 0.4 degree bins in the very likely range (1.2, 2.4)
      provided by the IPCC AR6

```

#### Mindlin21 tropampl

Located in [CMIP6_studies/Mindlin2021.yaml](../CMIP6_studies/Mindlin2021.yaml)

10.1029/2021GL092568

```
- key: Mindlin21 tropampl
  doi: 10.1029/2021GL092568
  type: future_spread
  spatial_scope: Global
  temporal_scope: Annual
  metric:
    name: tropampl
    long_name: Tropical Amplification
    units: K_K-1
    variables: ta250
    comment:
      These metrics are inspired by the work done in Mindlin and Shepherd, 2020,
      Clim Dyn but for CMIP6 GCMs and in Mindlin et al. 2021, GRL. It includes
      29 CMIP6 GCMs for SSP585 and extended to include 37 models Tropical
      warming (TW), the latter evaluated as the long-term change in temperature
      (ta) at 250 hPa zonally averaged between 15°S and 15°N (ΔT trop ) divided
      by the global surface temperature change (ΔT). Here Δ indicates the
      difference between 2070–2099 in the SSP5-8.5 experiment and 1950–1979 in
      the historical experiment. The limit between weak and strong tropical
      warming is not easy to set. We use the value of 1.7 K/K, choosing to have
      only 2 categories
  period:
    reference: 1950-1979
    target: 2070-2099
  classes:
  - limits: [0, 1.7, 10]
    labels: ['weak tropical warming', 'strong tropical warming']
    source: author

```

#### Sch20 ECS

Located in [CMIP6_studies/Sch20.yaml](../CMIP6_studies/Sch20.yaml)

10.5194/esd-11-1233-2020

```
- key: Sch20 ECS
  doi: 10.5194/esd-11-1233-2020
  type: future_spread
  spatial_scope: Global
  temporal_scope: Annual
  data_source: reference
  metric:
    name: ECS
    long_name: Equilibrium climate sensitivity
    units: K
    variables: tas
    comment:
      ECS is calculated with ESMValTool (Gregory method). CMIP5 range is [2.08,
      4.67]. Ensemble member added to make it comparable to scenarioMIP runs,
      although ECS is derived from 4xCO2 runs, unrelated to scenarioMIP.

```

### Other criteria
#### Bru20 mfamily

Located in [CMIP6_studies/Bru20.yaml](../CMIP6_studies/Bru20.yaml)

10.5194/esd-11-995-2020

```
- key: Bru20 mfamily
  doi: 10.5194/esd-11-995-2020
  type: other
  spatial_scope: Global
  data_source: reference
  metric:
    name: mfamily
    long_name: None
    units: categorical
    variables: ['tas', 'psl']
    comment:
      From Figure 5. Model family tree for all 33 CMIP6 models, similar to
      Knutti et al. (2013). Models branching further to the left are more
      dependent, and models branching further to the right are more independent.
      The analysis is based on global, horizontally resolved tasCLIM and pslCLIM
      in the period from 1980 to 2014. Labels with the same color indicate
      models with obvious dependencies, such as shared components or the same
      origin, whereas models with no clear dependencies are labeled in black.
      Using this figure 5, we have put in the same family, the GCM lines that
      merge before the dashed line, that correponds to the independence shape
      parameter. We have given family names only to families with at least 2
      members. Note that we are not using the Figure 5 color code to determine
      the family. This leads to some surprise such as  Strangely, ACCESS-CM2 is
      in the same family as UKESM and HadGEM3, but not ACCESS-ESM1-5. This was
      confirmed as ok by the Australian group. Also the two FGOALS model are not
      belonging to the same family with this criteria. TaiESM1 is not evaluated
      by Brunner et al. 2020. However it is published that TaiESM1 belongs to
      the CESM2 family (Lee et al. 2020,
      https://gmd.copernicus.org/articles/13/3887/2020/, The development of
      TaiESM is based on CESM1.2.2, in which the ocean, sea ice, and river
      components, as well as the infrastructure of the model, remain unchanged.)
  period:
    reference: 1980-2014

```

#### Aer. species

Located in [CMIP6_studies/Aerosol.yaml](../CMIP6_studies/Aerosol.yaml)

['pers. comm.', 'Jesus Fernandez']

```
- key: Aer. species
  doi: ['pers. comm.', 'Jesus Fernandez']
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: aer_species
    long_name: Aerosol species for which AOD available at ESGF
    units: categorical
    variables: od550bb, od550bc, od550dust, od550no3, od550oa, od550so4, od550ss, od550so4so, aerasymbnd, aeroptbnd, aerssabnd
    comment:
      Data extracted from ESGF using  https://github.com/jesusff/cmip6-for-
      cordex/blob/main/util/aerosol_species.py which feeds from
      https://github.com/jesusff/cmip6-for-cordex/blob/main/CMIP6_for_CORDEX.py
      Also, some pers. comm. for certain models that do not provide AOD by
      aerosol species. S. Yang for the EC-Earth consortium models.
    best: bb, bc, dust, no3, oa, so4, ss, so4so, aerasymbnd, aeroptbnd, aerssabnd

```

#### Bra21 complexity

Located in [CMIP6_studies/Bra21.yaml](../CMIP6_studies/Bra21.yaml)

10.5194/gmd-2020-418

```
- key: Bra21 complexity
  doi: 10.5194/gmd-2020-418
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: reference
  metric:
    name: complexity
    long_name: Complexity of model components
    units: categorical
    variables: []
    comment:
      Model complexity from Table 1 is coded with ternary values   0 - not
      considered   1 - prescribed   2 - interactive component in the following
      order Atm-Lnd-Ocn-SI-Veg-Tbgc-Aer-Chem-Obgc-Gla
  plausible_values:
  - min: 2222000000
    max: 2222222222
    source: eurocordex_gcm_selection_team
    comment:
      At least coupled Atm-Lnd-Ocn-SI with some form of aerosol consideration

```

#### Calendar

Located in [CMIP6_studies/Calendar.yaml](../CMIP6_studies/Calendar.yaml)

['pers. comm.', 'Andreas Dobler']

```
- key: Calendar
  doi: ['pers. comm.', 'Andreas Dobler']
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: calendar
    long_name: Model calendar
    units: categorical
    variables: None
    comment:
      Data extracted from ESGF

```

#### atm. res. km

Located in [CMIP6_studies/Resolution.yaml](../CMIP6_studies/Resolution.yaml)

None

```
- key: atm. res. km
  doi: None
  type: other
  spatial_scope: special
  temporal_scope: Annual
  data_source: author
  metric:
    name: resolution
    long_name: Nominal resolution of the atmospheric component
    units: km
    variables: None
    comment:
      Data extracted from the CMIP github https://github.com/WCRP-
      CMIP/CMIP6_CVs/blob/master/CMIP6_source_id.json using
      util/resolution_to_yaml.py Manually edited to include appropriate runs.
    best: 0
  plausible_values:
  - min: 0
    max: 300
    source: eurocordex_gcm_selection_team
    comment:
      Test value

```

