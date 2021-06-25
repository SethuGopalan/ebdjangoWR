from django.shortcuts import render
import requests






def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8b65e9ccfc145bb26cedb47690ed20e2'

    city = 'Woburn'
    
    r = requests.get(url.format(city)).json()

    # print(r.text)

    city_weather = {

        'city' : city ,

        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
         'icon'       : r['weather'][0]['icon']
    }

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=15a620071d9a016f64293138aab1045a'

    city = 'Bedford'
    
    r = requests.get(url.format(city)).json()

    # print(r.text)

    city_weather1 = {

        'city' : city,

        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
         'icon'       : r['weather'][0]['icon']
    }
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=15a620071d9a016f64293138aab1045a'

    city = 'Massachusetts'

    # for x in city: 
    #     if x == 'Massachusetts':
    #         r = requests.get(url.format(city)).json()
    #         if x == "NewYork":
    #             r = requests.get(url.format(city)).json()
    #             if x == "Maine":
    r = requests.get(url.format(city)).json()

    # print(r.text)

    city_weather2 = {

        'city' : city,

        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
         'icon'       : r['weather'][0]['icon']
    }
    print(city_weather)
    context ={
        'city_weather':city_weather,
        'city_weather1':city_weather1,
        'city_weather2':city_weather2

    }
    return render(request, 'index.html',context)
