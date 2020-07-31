import requests

api_id = 'http://api.openweathermap.org/data/2.5/weather?appid=d1485393c4a606f62866cebf56b945e3&q='
city_name = input("Enter name of city: ")

url = api_id + city_name

json_data = requests.get(url).json()

geo_coord = str(json_data['coord']['lat']) + ", " + str(json_data['coord']['lon'])
weath = json_data['weather'][0]['main']
temp = json_data['main']['temp'] - 273.15
humid = json_data['main']['humidity']
wind_speed = json_data['wind']['speed'] * 2.237
country_name = json_data['sys']['country']

print('Geographic Coordinates: {}'.format(geo_coord))
print('Weather: {}'.format(weath))
if country_name == "US":
    print('Temperature: {:.2f} degrees fahrenheit'.format(temp*1.8+32))
else:
    print('Temperature: {:.2f} degrees celsius'.format(temp))
print('Humidity: {} %'.format(humid))
print('Wind Speed: {:.2f} mph'.format(wind_speed))