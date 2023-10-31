from django.shortcuts import render
from .models import City
from .forms import CityForm
import requests
# Create your views here.
def openWeatherApi(request):
    Cities=City.objects.all().last()
    url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=youropenweatherkeyhere'
    if request.method=='POST':
        form =CityForm(request.POST)
        form.save()
    else:
        form =CityForm()
    weather_date=[]
    if Cities:
        city_weather=requests.get(url.format(Cities)).json()
        weather={
            'city':Cities,
            'temperature':city_weather['main']['temp'],
            'description':city_weather['weather'][0]['description'],
            'icon':city_weather['weather'][0]['icon'],
            'humidity':city_weather['main']['humidity'],
            'pressure':city_weather['main']['pressure'],
            'windspeed':city_weather['wind']['speed'],
        }
        weather_date.append(weather)
    context={'weather_data':weather_date,'form':form}

    return render(request,'index.html',context)
