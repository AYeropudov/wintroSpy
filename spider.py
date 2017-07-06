from urllib.request import urlopen, Request
from urllib.parse import urlencode

headers = {
    "User-Agent": "WintroSpider/1.0",
    "Accept": "text/html, text/html, application/xml, application/json",
    "Accept-Charset": "utf-8"
}
url = "http://gogo.ru"
request = Request(url, headers=headers)
result = urlopen(request)

print(result.read().decode("utf-8"))
result.close()