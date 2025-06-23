import requests

def weather(city):
    url= "https://api.openweathermap.org/data/2.5/weather?q=jaipur&appid=30f5f498611580da50a52d18563261b6"

    try:
        response = requests.get(url)
        data=response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

city = input("enter the city")