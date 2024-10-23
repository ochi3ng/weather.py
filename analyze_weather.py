
import seaborn as sns
import matplotlib.pyplot as plt
from fetch_data import fetch_weather_data

def analyze_temperature():
    data = fetch_weather_data()

    # Plot temperature trends for each city
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='temperature', hue='city', data=data)
    plt.title("Temperature Trends by City")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.show()

def analyze_humidity():
    data = fetch_weather_data()

    # Plot humidity trends for each city
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='humidity', hue='city', data=data)
    plt.title("Humidity Trends by City")
    plt.xlabel("Timestamp")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.show()

def analyze_pressure():
    data = fetch_weather_data()

    # Plot pressure trends for each city
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='timestamp', y='pressure', hue='city', data=data)
    plt.title("Pressure Trends by City")
    plt.xlabel("Timestamp")
    plt.ylabel("Pressure (hPa)")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    analyze_temperature()
    analyze_humidity()
    analyze_pressure()
