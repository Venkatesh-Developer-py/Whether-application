from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    return render(request, 'home.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        api_key = "1ea0b64ca311bec03157a7b1ea088949"
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return render(request, "home.html", {
                "error": data.get("message", "API error")
            })

        weather_data = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }

        return render(request, "home.html", {
            "weather": weather_data
        })

    return HttpResponse("Invalid request method", status=400)

# Create your views here.
