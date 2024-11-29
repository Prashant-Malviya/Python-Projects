import requests
import json
import os

city = input("enter the name of the city \n")


url = f"http://api.weatherapi.com/v1/current.json?key=key&q={city}"

r = requests.get(url)

# print(r.text)

weatherDic = json.loads(r.text)

print(weatherDic['current']['temp_c'])
