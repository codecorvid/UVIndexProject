#Rudimentary test file to allow me to test things without constantly messing with the main file

import requests
from bs4 import BeautifulSoup

monthDays = {"Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30, "May" : 31, "Jun" : 30, 
             "Jul" : 31, "Aug" : 31, "Sep" : 30, "Oct" : 31, "Nov" : 30, "Dec" : 31}

numericMonth = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", 
             "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}


#==========Testing searching using City name==========
#Cities tested: ALBUQUERQUE (beginning of list), WICHITA (end), JACKSONVILLE, MIAMI (both FL), HONOLULU, PHOENIX
#Need to account for the 2 PORTLAND, 2 CHARLESTON -> will only return the first one -> COMPLETE

"""setURL = "https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2014/uv.2014012612.uvbull"

req = requests.get(setURL)
soup = BeautifulSoup(req.content, 'html.parser')
indexCity = soup.text.find('PORTLAND')
fullLine = soup.text[indexCity:indexCity + 29] #bulletin lines are of set length
uvIndex = fullLine[-2:]
print("Full Line: ", fullLine)
print("UV: ", uvIndex)

"""


#==========Testing User Input==========
#Tested: portland, or/me; phoenix; charleston, sc/wv; HOUSTON
"""state = ""
city = input("Enter a city: ")
city = city.upper()
print(city)
if city == 'PORTLAND' or city == 'CHARLESTON':
    state = input("Enter state abbreviation: ")
    state = state.upper()
    print(state)"""


#==========Testing Find with Duplicate City Names==========
#Tested: Portland, OR; Portland, ME; Charleston, WV; Charleston, SC
setURL = "https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2014/uv.2014012612.uvbull"
city = "CHARLESTON"
state = "SC"

req = requests.get(setURL)
soup = BeautifulSoup(req.content, 'html.parser')
indexCity = soup.text.find(city)
fullLine = soup.text[indexCity:indexCity + 29] #bulletin lines are of set length
            
if state != "" and fullLine.find(state, 10) == -1: #starting at index 10 in the line to get past the city name
    newIndexCity = soup.text.find(city, indexCity + 29)
    fullLine = soup.text[newIndexCity:newIndexCity + 29]

uvIndex = fullLine[-2:]

print(fullLine)
print(uvIndex)