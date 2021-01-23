

city = input("Enter the city name: ")


url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e9185b28e9969fb7a300801eb026de9c"

import requests

response = requests.get(url)

jsondata = response.json()


print (jsondata['main']['temp'])


currencyapi = "https://free.currencyconverterapi.com/api/v7/convert?q=USD_PHP&compact=ultra&apiKey=850078702a1f23db35ed"

response = requests.get(currencyapi)

jsondata = response.json()



Host = "http://httpbin.org/post"

import requests
import json

data = {"firstname": "Vidura",
 "lang": "Python"
 }

headers = {"Content-Type":"application/json", "Content-Length": len(data), "data" : json.dumps(data)}


response = requests.post(Host, data, headers)


