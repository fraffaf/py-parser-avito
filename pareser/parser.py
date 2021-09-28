# Python avito parser 1.0
import requests

exmaplesite1 = "https://ya.ru"
exmaplesite2 = "https://www.avito.ru/"
exmaplesite3 = "http://ww1.coffeecupykt.com/"

proxy = {"https": "localhost:8080", "https": "localhost:8080"}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/46.0.2490.80 Safari/537.36',
    'Content-Type': 'text/html',
}

r = requests.get(exmaplesite1, headers=headers)
rr = requests.get(exmaplesite3, headers=headers)

if r.ok:            # if r.status = 200
    print("ok")     # print("ok")

c = rr.text
f = open("result.txt", "w")
for index in rr.text:
    f.write(c)
f.close()





