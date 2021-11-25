import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
def getWeather(CITY):
    API_KEY = "bfed0791e67286d26ba01ac5781e20ca"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       humidity = main['humidity']
       pressure = main['pressure']
       report = data['weather']
       print(f"{CITY:-^30}")
       recommendToTravel = "False"
       if report[0]['description']=="haze" or report[0]['description']=="clear sky" or report[0]['description']=="scattered clouds":
           recommendToTravel = "True"
       content = {'temp' : {temperature - 273.5}, 'weatherRecommendation' : report[0]['description'], 'recomennded?' : recommendToTravel}
       return content
    else:
        print("Error in the HTTP request")
        return None
# getWeather("Coimbatore")