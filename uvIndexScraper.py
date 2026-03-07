import requests
from bs4 import BeautifulSoup
import time
import csv

state = ""
city = input("Enter a city: ")
city = city.upper()
if city == "PORTLAND" or city == "CHARLESTON":
    state = input("Enter state abbreviation: ")
    state = state.upper()

year = input("Enter year: ")

start = time.time()

monthDays = {"Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30, "May" : 31, "Jun" : 30, 
             "Jul" : 31, "Aug" : 31, "Sep" : 30, "Oct" : 31, "Nov" : 30, "Dec" : 31}

numericMonth = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", 
             "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

filename = "DailyUVIndexData" + year + city + state + ".csv"
with open(filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Month", "Day", "UVIndex"])

    for month in monthDays:
        print(month)
        #get month's number of days
        numDays = monthDays[month]
        numMonth = numericMonth[month]

        for day in range(1, numDays + 1):
            print(day, end = " ", flush=True)
            if day < 10:
                url = "https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/" + year + "/uv." + year + numMonth + "0" + str(day) + "12.uvbull"
            if day >= 10:
                url = "https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/" + year + "/uv." + year + numMonth + str(day) + "12.uvbull"
            req = requests.get(url)
            soup = BeautifulSoup(req.content, "html.parser")
            indexCity = soup.text.find(city)
            fullLine = soup.text[indexCity:indexCity + 29] #bulletin lines are of set length
            
            if state != "" and fullLine.find(state, 10) == -1:
                newIndexCity = soup.text.find(city, indexCity + 29)
                fullLine = soup.text[newIndexCity:newIndexCity + 29]

            uvIndex = fullLine[-2:]

            #writing to CSV file
            csv_writer.writerow([month, str(day), uvIndex])

        print()


end = time.time()

print((end - start), " seconds")