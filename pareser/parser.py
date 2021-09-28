# Python avito parser 1.0

import requests

proxy = {"http": "localhost:8080", "https": "localhost:8080"}

headers = {
    "User-Agent": "Chrome"
}

r = requests.get("https://ya.ru", proxies=proxy, verify=False)

if r.ok:            # if r.status = 200
    print("ok")     # print("ok")
#TEST GIT2 22



