from django.shortcuts import render
import requests






def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=15a620071d9a016f64293138aab1045a'

    city = 'Massachusetts'
    
    r = requests.get(url.format(city)).json()

    # print(r.text)

    city_weather = {

        'city' : city ,

        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
         'icon'       : r['weather'][0]['icon']
    }

    print(city_weather)
    context ={
        'city_weather':city_weather
    }
    return render(request, 'index.html',context)
