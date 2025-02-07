# Get Daily Station Data from xmACIS
## Written By Jared Rennie (@jjrennie)

Taps into the ACIS API to get daily station data for its period of record.

- API: https://www.rcc-acis.org/docs_webservices.html
- Query Builder: https://builder.rcc-acis.org/

### What You Need

First off, the entire codebase works in Python 3. In addition to base Python, you will need the following packages installed: 
- requests (to access the api)
- pandas (to slice annd dice the data)
    
The "easiest" way is to install these is by installing <a href='https://www.anaconda.com' target="_blank">anaconda</a>, and then applying <a href='https://conda-forge.org/' target="_blank">conda-forge</a>. Afterward, then you can install the above packages. 

### Importing Packages
Assuming you did the above, it should (in theory) import everything no problem:

### Launch right now with binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jjrennie/xmacis_daily/HEAD?urlpath=%2Fdoc%2Ftree%2Fxmacis_getDailyData-por.ipynb)
