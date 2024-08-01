import requests

url = "http://ip-api.com/json/"
key = requests.get(url)
print(key.text)
if "United Arab Emirates" in key.text or "Dubai" in key.text or "Sharjah" in key.text:
    print("IP change unsuccessful !!!")
    safe = False
else:
    safe = True

if safe == True:
    import ahmiascraper
    ahmiascraper.Scraper()
else:
    print("IP change failed, try again later.")