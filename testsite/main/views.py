from django.shortcuts import render
from django.http import HttpResponse
import requests,json
import urllib.request
from .forms import City_Form
# Create your views here.

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Athens'
    if city == '':
        city = 'Athens'
    api_id = 'Your_api_id'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    list_data = requests.get(url.format(city,api_id)).json()

    data = {
        "country_code" : str(list_data['sys']['country']),"coordinate_lon" : str(list_data['coord']['lon'])
        + ',' + str(list_data['coord']['lon']),
        "temperature" : str(list_data['main']['temp']) + 'Celsius',
        "pressure": str(list_data['main']['pressure']),
        "humidity": str(list_data['main']['humidity']),
        "main": str(list_data['weather'][0]['main']),
        "description": str(list_data["weather"][0]["description"]),
        "icon":list_data["weather"][0]['icon'],
        'city':city
    }
    print(data)
    return render(request,'main/index.html',data)