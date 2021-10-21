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
Parameter list: https://www.epa.gov/aqs/aqs-code-list
Parameters of common compounds:
O3            44201
PM2.5         88101
PM10          81102
SO2           42401
NO2           42602
CO            42101
CO2           42102
Acetone       43551
Formaldehyde  43502
Acetaldehyde  43503
Benzene       45201
Toluene       45202

City code: https://aqs.epa.gov/aqsweb/documents/codetables/cities.html
Common city codes: 
Syracuse        73000
East Syracuse   23052
North Syracuse  53660
New York        51000

Return all sites in the county: https://aqs.epa.gov/data/api/list/sitesByCounty?email=jshen20@syr.edu&key=orangecrane46&state=36&county=067
Common site codes:
East Syracuse   1015

NY Data
http://www.nyaqinow.net/
'''
