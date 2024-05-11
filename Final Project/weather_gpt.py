# Importing libraries that help us work with geolocation, make web requests, create graphical interfaces, and handle errors.
from geopy.geocoders import Nominatim  # Library for finding latitude and longitude of places.
import requests  # Library for making web requests.
import tkinter as tk  # Library for creating graphical interfaces.
import geopy.exc  # Library for handling errors.

# Function to get the latitude and longitude of a location.
def get_lat_long(address):
    # Creating a geolocator object to find the location.
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Finding the location based on the address provided.
    location = geolocator.geocode(address)
    # If the location is found, return its latitude and longitude.
    if location:
        return location.latitude, location.longitude
    # If the location is not found, return None.
    else:
        return None

# Function to get weather information based on latitude and longitude.
def get_weather_info(latitude, longitude):
    # Constructing a URL to access weather data from an API.
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid=d4963da6687b3fdbb6bf937ccac38e6e&units=metric'
    try:
        # Sending a request to the API to get weather data.
        response = requests.get(url)
        response.raise_for_status()  # Checking for any errors in the response.
        data = response.json()  # Parsing the response into JSON format.
        # Extracting relevant weather information from the JSON data.
        temp = f'Temperature: {data["list"][0]["main"]["temp"]}°C'
        pressure = f'Pressure: {data["list"][0]["main"]["pressure"]}hPa'
        humidity = f'Humidity: {data["list"][0]["main"]["humidity"]}%'
        rain = f'Rain: {data["list"][0]["clouds"]["all"]}%'
        wind_speed = f'Wind Speed: {data["list"][0]["wind"]["speed"]}km/h'
        # Returning the extracted weather information.
        return temp, pressure, humidity, rain, wind_speed
    except requests.exceptions.HTTPError as err:
        # Handling HTTP errors and providing a generic error message.
        error_message = 'An error occurred while fetching weather data. Please try again later.'
        return error_message, error_message, error_message, error_message, error_message

# Function to handle the button click event and initiate weather data retrieval.
def start_program():
    # Retrieving the address entered by the user.
    address = location_input.get()
    # Obtaining latitude and longitude coordinates for the entered address.
    latitude, longitude = get_lat_long(address)
    # Checking if the coordinates are valid.
    if latitude is None or longitude is None:
        # Displaying an error message if the address is not found.
        weather_info = ("Address not found", "", "", "", "")
    else:
        # Retrieving weather information based on the obtained coordinates.
        weather_info = get_weather_info(latitude, longitude)
    # Updating the labels to display weather information or error messages.
    temp_label.config(text=weather_info[0])
    pressure_label.config(text=weather_info[1])
    humidity_label.config(text=weather_info[2])
    rain_label.config(text=weather_info[3])
    wind_speed_label.config(text=weather_info[4])

# Creating the main window for the weather forecast application.
window = tk.Tk()
window.title('Weather Forecast')  # Setting the title of the window.
window.minsize(width=400, height=300)  # Defining the minimum size of the window.

# Creating a frame to hold the location input elements.
frame_location = tk.Frame(window)
frame_location.grid(column=0, row=0, padx=10, pady=10, sticky='new')

# Label and input field for entering the location.
location_label = tk.Label(frame_location, text="Location:")
location_label.grid(column=0, row=0, sticky='ew')
location_input = tk.Entry(frame_location)
location_input.grid(column=1, row=0, padx=10, sticky='ew')

# Button to initiate the weather forecast retrieval process.
location_button = tk.Button(frame_location, text='Search', command=start_program)
location_button.grid(column=2, row=0, sticky='ew')

# Labels to display weather information or error messages.
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

# Starting the application loop to handle user interactions.
window.mainloop()