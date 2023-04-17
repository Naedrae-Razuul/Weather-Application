import requests, json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

base_url = "http://api.weatherapi.com/v1/current.json?"
key = "6df2711ec1d74300bb1143444231604"
city = "United States, Florida, Haines City&aqi=no"
url = base_url + "key=" + key + "&q=" + city

response = requests.get(url)
data = response.json()
city = data['location']['name']
state = data['location']['region']
country = data['location']['country']
latitude = data['location']['lat']
longitude = data['location']['lon']
time_zone = data['location']['tz_id']
last_updated = data['current']['last_updated']
temp_c = data['current']['temp_c']
temp_f = data['current']['temp_f']
condition = data['current']['condition']['text']
icon = data['current']['condition']['icon']
wind_mph = data['current']['wind_mph']
wind_kph = data['current']['wind_kph']
gust_mph = data['current']['gust_mph']
gust_kph = data['current']['gust_kph']
wind_degree = data['current']['wind_degree']
humidity = data['current']['humidity']
feelslike_c = data['current']['feelslike_c']
feelslike_f = data['current']['feelslike_f']
uv_levels = data['current']['uv']
print(wind_mph)
