
url = "http://api.openweathermap.org/data/2.5/weather?q=Colombo&appid=e9185b28e9969fb7a300801eb026de9c"

import requests

response = requests.get(url)

response.json()

