import urllib.request as req
from bs4 import BeautifulSoup
import json

#取得網址
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
browser = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"

#對網站發出一個 request
request = req.Request(url, headers={
    "User-Agent":browser
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

#用 html 解析網站
root = BeautifulSoup(data, "html.parser")

# 將文字部分轉成 json 檔案
data_json = json.loads(root.text)
print(type(data_json))
print(len(data_json["result"]["results"])) #319 個景點

# 目標是要景點名稱 stitle, latitude, longitude, file裏第一個
extract = data_json["result"]["results"]

with open("data.txt", "w") as f:
    for i in range(len(extract)):
        title = extract[i]["stitle"] 
        latitude = extract[i]["latitude"]
        longitude = extract[i]["longitude"]
        fig = "http" + extract[i]["file"].split("http")[1]
        text = title + "," + latitude + "," + longitude + "," + fig + "\n"
        f.write(text)





