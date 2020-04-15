'''
EPA API for accessing AQI data in the US

Example: (access all the ozone data of East Syracuse Site from 20190101 to 20191231)
https://aqs.epa.gov/data/api/sampleData/bySite?email=jshen20@syr.edu&key=orangecrane46&param=44201&bdate=20190101&edate=20191231&state=36&county=067&site=1015

email: jshen20@syr.edu
key: orangecrane46
param: code for specific pollutant (44201 for ozone)
bdate: beginning date
edate: ending date
state: state (36 for NY)
county: county (067 for Onadaga)
site: site code (1015 for East Syracuse)

document via https://aqs.epa.gov/aqsweb/documents/data_api.html#cbdate
'''
