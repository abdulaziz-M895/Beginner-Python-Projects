from geopy.geocoders import Nominatim
import requests
import tkinter as tk
import geopy.exc

def get_weather_info(address):
    def get_lat_long(address):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None

    while True:
        try:
            latitude, longitude = get_lat_long(address)
            print('Address Found')
            break
        except TypeError:
            print(f"Could not find the location of {address}")
            return f"Could not find the location of {address}", "", "", "", ""

        except geopy.exc.GeocoderInsufficientPrivileges:
            print("GeocoderInsufficientPrivileges: The geocoding service rejected the request due to insufficient privileges.")
            return "Geocoder error. Please try again later.", "", "", "", ""

    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid=d4963da6687b3fdbb6bf937ccac38e6e&units=metric'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        temp = f'The Temperature: {data["list"][0]["main"]["temp"]}°C'
        pressure = f'Pressure: {data["list"][0]["main"]["pressure"]}hPa'
        humidity = f'Humidity: {data["list"][0]["main"]["humidity"]}%'
        rain = f'Precipitation: {data["list"][0]["clouds"]["all"]}%'
        wind_speed = f'Wind speed: {data["list"][0]["wind"]["speed"]}km/h'
    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors
        print(f"HTTP Error: {err}")
        temp = 'There was an error. Please try again later.'
        pressure = temp
        humidity = temp
        rain = temp
        wind_speed = temp

    return temp, pressure, humidity, rain, wind_speed

def start_program():
    address = location_input.get()
    weather_info = get_weather_info(address)

    # Update labels with weather information or error message
    temp_label.config(text=weather_info[0])
    pressure_label.config(text=weather_info[1])
    humidity_label.config(text=weather_info[2])
    rain_label.config(text=weather_info[3])
    wind_speed_label.config(text=weather_info[4])

window = tk.Tk()
window.title('Weather Forecast')
window.minsize(width=400, height=300)

frame_location = tk.Frame(window)
frame_location.grid(column=0, row=0, padx=10, pady=10, sticky='new')

location_label = tk.Label(frame_location, text="Location:")
location_label.grid(column=0, row=0, sticky='ew')

location_input = tk.Entry(frame_location)
location_input.grid(column=1, row=0, padx=10, sticky='ew')

location_button = tk.Button(frame_location, text='Search', command=start_program)
location_button.grid(column=2, row=0, sticky='ew')

# Labels to display weather information or error message
temp_label = tk.Label(window, text="")
temp_label.grid(column=0, row=1, padx=10, pady=5, sticky='w')

pressure_label = tk.Label(window, text="")
pressure_label.grid(column=0, row=2, padx=10, pady=5, sticky='w')

humidity_label = tk.Label(window, text="")
humidity_label.grid(column=0, row=3, padx=10, pady=5, sticky='w')

rain_label = tk.Label(window, text="")
rain_label.grid(column=0, row=4, padx=10, pady=5, sticky='w')

wind_speed_label = tk.Label(window, text="")
wind_speed_label.grid(column=0, row=5, padx=10, pady=5, sticky='w')

window.mainloop()