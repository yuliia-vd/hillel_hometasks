import requests

city = input('Choose one city: Kyiv or Paris ')
url1 = 'https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=f3eca5ffcbe04676b42ff5c5c971e350'
url2 = 'https://api.openweathermap.org/data/2.5/weather?q=Paris&appid=f3eca5ffcbe04676b42ff5c5c971e350'
if city == 'Kyiv' :
    response = requests.get(url1)
    print(response)
    json_str = response.json()
    print(json_str)
    print(json_str['main']['temp'])
    print(json_str['main']['pressure'])
    print(json_str['wind']['speed'])
    print(json_str['wind']['deg'])

elif city == 'Paris' :
    response = requests.get(url2)
    print(response)
    json_str = response.json()
    print(json_str)
    print(json_str['main']['temp'])
    print(json_str['main']['pressure'])
    print(json_str['wind']['speed'])
    print(json_str['wind']['deg'])
