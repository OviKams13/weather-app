from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
        json_date = json.loads(source)
        data = {
            "country_code" : str(json_date['sys']['country']),
            "temp" : str(round(json_date['main']['temp']- 273.15, 2)),
            "pressure" : str(json_date['main']['pressure']),
            "humidity" : str(json_date['main']['humidity']),
            "wind" : str(json_date['wind']['speed']),
            "feels_like" : str(round(json_date['main']['feels_like']- 273.15, 2)), 
            "temp_min" : str(round(json_date['main']['temp_min']- 273.15, 2)),
            "temp_max" : str(round(json_date['main']['temp_max']- 273.15, 2)),        
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city':city, 'data':data})