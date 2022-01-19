import requests
city_name = input('Enter city name: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=f3eca5ffcbe04676b42ff5c5c971e350'
response = requests.get(url)
print(response)
json_str = response.json()
print(json_str)
print(json_str['main']['temp'])
print(json_str['main']['pressure'])
print(json_str['wind']['speed'])
print(json_str['wind']['deg'])