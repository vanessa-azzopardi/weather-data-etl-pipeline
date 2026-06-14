# Extract Transform Load (ETL) Project

# Import libraries
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt


# Extract
# Send a request to OpenWeatherMap API and pull weather data for the specified cities
def extract_weather_data(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Load API key
load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

# Extract the weather data for some cities
cities = ['Valletta', 'Santa Venera', 'London', 'Paris', 'New York']
weather_data = [extract_weather_data(city, api_key) for city in cities]
print(weather_data)

#---------------------------------------------------------------------------------

#  Transform
def transform_weather_data(raw_data):
    transformed_data = []      
    for data in raw_data:
        if 'main' in data:    
            city_data = {
                'country': data['sys']['country'],
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'weather': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            transformed_data.append(city_data)
    return pd.DataFrame(transformed_data)

# Transform the extracted data
weather_df = transform_weather_data(weather_data)
print(weather_df)

#---------------------------------------------------------------------------------

# Load
from sqlalchemy import create_engine

# Create a SQLite database connection
engine = create_engine('sqlite:///weather_data.db')

# Load the transformed data into SQL table
weather_df.to_sql('weather', con=engine, if_exists='replace', index=False)

print("Data loaded into SQLite successfully!")

# Query the data from the SQLite database
query = "SELECT * FROM weather"

result = pd.read_sql(query, con=engine)
print(result)

#---------------------------------------------------------------------------------

# Visualise
# Visualise the data using Matplotlib

# Plot the temperature data
plt.figure(figsize=(8, 5))
plt.bar(weather_df['city'], weather_df['temperature'], color='blue')
plt.xlabel('City')
plt.ylabel('Temperature (oC)')
plt.title('Temperature Comparison of Cities')
plt.show()
