from django.http import HttpResponse
import urllib.request, json
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the weather app index.")

def current_weather(request):
    if request.method == 'POST': 
        city = request.POST['city']
        
        coordinates = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q='+ city + '&appid=352350089cd0815f99eb9fc26635d7fd')

        # list_of_cordinates = json.load(coordinates)
        # c = {
        #     "latitude": str(list_of_cordinates['lat']),
        #     "longitude": str(list_of_cordinates['long'])
        # }

        list_of_coordinates = json.load(coordinates)
        latitude = list_of_coordinates[0]['lat']
        longitude = list_of_coordinates[0]['lon']


        source = request.urlopen('https://api.openweathermap.org/data/2.5/weather?lat='+ latitude 
                                 + '&lon=' + longitude + '&appid=352350089cd0815f99eb9fc26635d7fd').read()
        list_of_data = json.loads(source)

        final_data={
            'curren_temperature': str(list_of_data['main']['temp']) + ' °C',
            'feels_like': str(list_of_data['main']['feels_like']) + ' °C',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'wind': str(list_of_data['wind']['speed']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(final_data)
    else:
        final_data = {}

    return render(request, "templates/current_weather_template/index.html", final_data)

def forcast_weather(request):
    if request.method == 'POST': 
        city = request.POST['city']
        
        coordinates = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q='+ city + '&appid=352350089cd0815f99eb9fc26635d7fd')

        # list_of_cordinates = json.load(coordinates)
        # c = {
        #     "latitude": str(list_of_cordinates['lat']),
        #     "longitude": str(list_of_cordinates['long'])
        # }

        list_of_coordinates = json.load(coordinates)
        latitude = list_of_coordinates[0]['lat']
        longitude = list_of_coordinates[0]['lon']


        source = request.urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?lat='+ latitude + 
                                 '&lon=' + longitude +'&cnt=' + 10 + '&appid=352350089cd0815f99eb9fc26635d7fd').read()
        list_of_data = json.loads(source)

        final_data={ 
            'temp_day' : str(list_of_data['temp']['day']),
            'temp_min' : str(list_of_data['temp']['min']),
            'temp_max' : str(list_of_data['temp']['max']),
            'temp_night':  str(list_of_data['temp']['night']),
            'pressure' : str(list_of_data['pressure']),
            'humidity' : str(list_of_data['humidity']),
            'weather_main' : str(list_of_data['weather'][0]['main']),
            'weather_description' : str(list_of_data['weather'][0]['description']),
            'weather_icon' : str(list_of_data['weather'][0]['icon']),
        }
        print(final_data)
    else:
        final_data = {}

    return render(request, "templates/forcast_weather_template/index.html", final_data)


def history_weather(request):
    if request.method == 'POST': 
        city = request.POST['city']
        
        coordinates = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q='+ city + '&appid=352350089cd0815f99eb9fc26635d7fd').read()

        # list_of_cordinates = json.load(coordinates)
        # c = {
        #     "latitude": str(list_of_cordinates['lat']),
        #     "longitude": str(list_of_cordinates['long'])
        # }

        list_of_coordinates = json.load(coordinates)
        latitude = list_of_coordinates[0]['lat']
        longitude = list_of_coordinates[0]['lon']


        source = request.urlopen('https://history.openweathermap.org/data/2.5/history/city?lat' + latitude + '&lon=' + 
                                 longitude + '&type=hour&cnt=' + 10+ '&appid=352350089cd0815f99eb9fc26635d7fd').read()
        list_of_data = json.loads(source)

        final_data={ 
            'dt' : str(list_of_data['dt']),
            'temp' : str(list_of_data['main']['temp']),
            'feels_like' : str(list_of_data['main']['feels_like']),
            'pressure' : str(list_of_data['main']['pressure']),
            'humidity' : str(list_of_data['main']['humidity']),
            'temp_min' : str(list_of_data['main']['temp_min']),
            'temp_max' : str(list_of_data['main']['temp_max']),
            'wind_speed' : str(list_of_data['wind']['speed']),
            'wind_deg' : str(list_of_data['wind']['deg']),
            'clouds' : str(list_of_data['clouds']['all']),
            'weather_main' : str(list_of_data['weather'][0]['main']),
            'weather_description' : str(list_of_data['weather'][0]['description']),
            'weather_icon' : str(list_of_data['weather'][0]['icon']),
        }
        print(final_data)
    else:
        final_data = {}

    return render(request, "templates/history_weather_template/index.html", final_data)

