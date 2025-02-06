# Python Code to get Daily Station Data from the ACIS API.
# Input is Station ID, and outputs data into a csv file.

# Import Packages
import json,requests,sys
import pandas as pd

# Read in Arguments (Station ID)
if len(sys.argv) < 2:
    sys.exit("USAGE: <STATION ID>")  
stationID = sys.argv[1]

# DEFINE ACIS URL 
# API Info: https://www.rcc-acis.org/docs_webservices.html
# Query Builder: https://builder.rcc-acis.org/
acis_url = 'http://data.rcc-acis.org/StnData'

# Build JSON to access ACIS API
# Gets 5 Variables (MaxT, MinT, Precip, Snow, Snow Depth)
# To get more, use the API Info or Query Builder above.
payload = {
"output": "json",
"params": {"elems":[{"name":"maxt","interval":"dly","prec":1},
                    {"name":"mint","interval":"dly","prec":1},
                    {"name":"pcpn","interval":"dly","prec":2},
                    {"name":"snow","interval":"dly","prec":1},
                    {"name":"snwd","interval":"dly","prec":1}],
           "sid":stationID,
           "sdate":"por",
           "edate":"por"
          } 
}

# Make Request
r = requests.post(acis_url, json=payload,timeout=5)
outData = r.json()

# Convert to Pandas
acisPandas = pd.DataFrame(outData['data'], columns=['DATE','TMAX','TMIN','PRCP','SNOW','SNWD'])

# Send to CSV
outFile='./'+stationID+'_Daily_POR.csv'
acisPandas.to_csv(outFile,index=False)

# If you made it this far. Success!
print('SUCESSFULLY GOT DATA AND PUT IN:',outFile)
sys.exit()