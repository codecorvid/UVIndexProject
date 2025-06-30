import requests
from bs4 import BeautifulSoup
import time
import csv

sum = 0

start = time.time()

with open("DailyUVIndexData2020.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Month", "Day", "UVIndex"])

    #first go, loop through just the month of January
    for i in range(1, 32):
        print(i)
        if i < 10:
            url = 'https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2020/uv.2020010' + str(i) + '12.uvbull'
        if i >= 10:
            url = 'https://www.cpc.ncep.noaa.gov/products/stratosphere/uv_index/Bulletin/2020/uv.202001' + str(i) + '12.uvbull'

        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        indexAZ = soup.text.find('AZ')
        currIndex = soup.text[indexAZ + 6:indexAZ + 8]

        #writing to CSV file
        csv_writer.writerow(["Jan", str(i), currIndex])

        sum += int(currIndex)
        #print(currIndex) #get the UV Index value for PHX, AZ accounting for double digits

end = time.time()

average = sum/31
print(average)
print((end - start), ' seconds')