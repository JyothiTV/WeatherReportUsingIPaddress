import json
import requests
import IP2Location
from pprint import pprint
import os

LocObj=IP2Location.IP2Location(os.path.join("data","IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-SAMPLE.BIN"))

res=LocObj.get_all("66.169.43.209")
print(res.country_long)
print(res.region)
print(res.city)
print(res.longitude)
print(res.latitude)
print(res.zipcode)
city=res.city
weatherurl='http://api.openweathermap.org/data/2.5/weather?'
cityurl=weatherurl+'q='+city+'&APPID=d1ca8022853423d1ea4574d483c630a4'
response=requests.get(cityurl)
pyform=response.json()
pprint(pyform)