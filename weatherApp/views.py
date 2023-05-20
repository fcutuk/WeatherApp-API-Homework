from django.http import HttpResponse
import urllib.request, json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache



def index(request):
    return HttpResponse("Hello, world. You're at the weather app index.")

def current_weather(request):
    final_data = {}
    if request.method == 'POST': 
        city = str(request.POST.get('city'))
        key = '352350089cd0815f99eb9fc26635d7fd'

        cache_key = f'weather_data_{city}'
        cached_data = cache.get(cache_key)
        if cached_data:
            # If cached data exists, return it directly
            return JsonResponse(cached_data)

        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key + "&units=metric")
        content = source.read().decode('utf-8')
        final_data = json.loads(content)

    print(final_data)

    cache.set(cache_key, final_data, 300)

    if final_data:
        return HttpResponse("Data retrieved successfully")
    else:
        return HttpResponse("You have entered an invalid location")


def forcast_weather(request):
    final_data = {}
    if request.method == 'POST': 
        city = str(request.POST.get('city'))
        key = '352350089cd0815f99eb9fc26635d7fd'

        cache_key = f'weather_data_{city}'
        cached_data = cache.get(cache_key)
        if cached_data:
            # If cached data exists, return it directly
            return JsonResponse(cached_data)

        source = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + key + "&units=metric")
        content = source.read().decode('utf-8')
        final_data = json.loads(content)

    print(final_data)

    cache.set(cache_key, final_data, 300)

    if final_data:
        return HttpResponse("Data retrieved successfully")
    else:
        return HttpResponse("You have entered an invalid location")

def history_weather(request):
    final_data = {}
    if request.method == 'POST': 
        city = str(request.POST.get('city'))
        key = '352350089cd0815f99eb9fc26635d7fd'

        cache_key = f'weather_data_{city}'
        cached_data = cache.get(cache_key)
        if cached_data:
            # If cached data exists, return it directly
            return JsonResponse(cached_data)

        coordinates = urllib.request.urlopen('http://api.openweathermap.org/geo/1.0/direct?q=' + city + '&limit=5&units=metric&appid=352350089cd0815f99eb9fc26635d7fd')
        coordinates_data = coordinates.read().decode('utf-8')
        list_of_coordinates = json.loads(coordinates_data)
        latitude = str(list_of_coordinates[0]['lat'])
        longitude = str(list_of_coordinates[0]['lon'])

        source = urllib.request.urlopen("https://history.openweathermap.org/data/2.5/history/city?lat=" + latitude + "&lon=" + longitude + "&type=hour&appid=" + key)
        content = source.read().decode('utf-8')
        final_data = json.loads(content)

    print(final_data)

    cache.set(cache_key, final_data, 300)

    if final_data:
        return HttpResponse("Data retrieved successfully")
    else:
        return HttpResponse("You have entered an invalid location")
    