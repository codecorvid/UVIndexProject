import requests
from bs4 import BeautifulSoup
import time
import csv

start = time.time()

monthDays = {"Jan" : 31, "Feb" : 29}

with open("DailyUVIndexData2020.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Month", "Day", "UVIndex"])

    for month in monthDays:
        print(month)
        #get month's number of days
        numDays = monthDays[month]

        for day in range(1, numDays + 1):
            print(day)
            if day < 10:
                url = 'https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2020/uv.2020010' + str(day) + '12.uvbull'
            if day >= 10:
                url = 'https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2020/uv.202001' + str(day) + '12.uvbull'

            req = requests.get(url)
            soup = BeautifulSoup(req.content, 'html.parser')
            indexState = soup.text.find('AZ')
            currIndex = soup.text[indexState + 6:indexState + 8]

            #writing to CSV file
            csv_writer.writerow([month, str(day), currIndex])


end = time.time()

print((end - start), ' seconds')