default:
	echo "You probably want to 'make update'"

update: update-esgf update-tables

CMIP6_downscaling_plans.csv:
	wget https://raw.githubusercontent.com/WCRP-CORDEX/simulation-status/main/CMIP6_downscaling_plans.csv

update-esgf:
	python3 CMIP6_for_CORDEX.py
	python3 CMIP6_for_CORDEX_availability_RCM.py

update-tables: AUS EUR MED NAM SEA

AUS: CMIP6_downscaling_plans.csv
	python3 CMIP6_studies_table.py AUS
	python3 CMIP6_studies_list.py AUS > docs/CMIP6_studies_list_AUS.md
EUR: CMIP6_downscaling_plans.csv
	python3 CMIP6_studies_table.py EUR
	python3 util/row_tooltips.py EUR
	python3 CMIP6_studies_list.py EUR > docs/CMIP6_studies_list_EUR.md
MED: CMIP6_downscaling_plans.csv
	python3 CMIP6_studies_table.py MED
	python3 util/row_tooltips.py MED
	python3 CMIP6_studies_list.py MED > docs/CMIP6_studies_list_MED.md
NAM: CMIP6_downscaling_plans.csv
	python3 CMIP6_studies_table.py NAM
	python3 util/row_tooltips.py NAM
	python3 CMIP6_studies_list.py NAM > docs/CMIP6_studies_list_NAM.md
SEA: CMIP6_downscaling_plans.csv
	python3 CMIP6_studies_table.py SEA
	python3 CMIP6_studies_list.py SEA > docs/CMIP6_studies_list_SEA.md
