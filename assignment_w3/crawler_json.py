import urllib.request as request
import json

url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(url) as response:
    data = json.load(response)

print(type(data))

# 目標是要景點名稱 stitle, latitude, longitude, file裏第一個
extract = data["result"]["results"]

with open("data1.txt", "w", encoding="utf-8") as f:
    for i in range(len(extract)):
        title = extract[i]["stitle"] 
        latitude = extract[i]["latitude"]
        longitude = extract[i]["longitude"]
        fig = "http" + extract[i]["file"].split("http")[1]
        text = title + "," + latitude + "," + longitude + "," + fig + "\n"
        f.write(text)
    