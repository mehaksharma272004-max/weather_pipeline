import requests
import pandas as pd
from pathlib import Path
import time

CITIES = [
    ("New Delhi", 28.6139, 77.2090),
    ("London", 51.5072, -0.1276),
    ("Paris", 48.8566, 2.3522),
    ("Tokyo", 35.6762, 139.6503),
    ("Beijing", 39.9042, 116.4074),
    ("Washington, D.C.", 38.9072, -77.0369),
    ("Canberra", -35.2809, 149.1300),
    ("Ottawa", 45.4215, -75.6972),
    ("Brasilia", -15.7939, -47.8828),
    ("Buenos Aires", -34.6037, -58.3816),
    ("Mexico City", 19.4326, -99.1332),
    ("Berlin", 52.5200, 13.4050),
    ("Rome", 41.9028, 12.4964),
    ("Madrid", 40.4168, -3.7038),
    ("Lisbon", 38.7223, -9.1393),
    ("Amsterdam", 52.3676, 4.9041),
    ("Brussels", 50.8503, 4.3517),
    ("Vienna", 48.2082, 16.3738),
    ("Bern", 46.9480, 7.4474),
    ("Stockholm", 59.3293, 18.0686),
    ("Oslo", 59.9139, 10.7522),
    ("Copenhagen", 55.6761, 12.5683),
    ("Helsinki", 60.1699, 24.9384),
    ("Reykjavik", 64.1466, -21.9426),
    ("Warsaw", 52.2297, 21.0122),
    ("Prague", 50.0755, 14.4378),
    ("Budapest", 47.4979, 19.0402),
    ("Athens", 37.9838, 23.7275),
    ("Ankara", 39.9334, 32.8597),
    ("Moscow", 55.7558, 37.6173),
    ("Kyiv", 50.4501, 30.5234),
    ("Cairo", 30.0444, 31.2357),
    ("Nairobi", -1.2921, 36.8219),
    ("Addis Ababa", 8.9806, 38.7578),
    ("Abuja", 9.0765, 7.3986),
    ("Accra", 5.6037, -0.1870),
    ("Dakar", 14.7167, -17.4677),
    ("Rabat", 34.0209, -6.8416),
    ("Algiers", 36.7538, 3.0588),
    ("Tunis", 36.8065, 10.1815),
    ("Riyadh", 24.7136, 46.6753),
    ("Abu Dhabi", 24.4539, 54.3773),
    ("Doha", 25.2854, 51.5310),
    ("Islamabad", 33.6844, 73.0479),
    ("Dhaka", 23.8103, 90.4125),
    ("Kathmandu", 27.7172, 85.3240),
    ("Bangkok", 13.7563, 100.5018),
    ("Hanoi", 21.0278, 105.8342),
    ("Seoul", 37.5665, 126.9780),
    ("Jakarta", -6.2088, 106.8456),
]

def main():
    rows = []

    for city, latitude, longitude in CITIES:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,relative_humidity_2m,"
                "apparent_temperature"
            ),
            "timezone": "auto",
        }

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            current = response.json()["current"]

            rows.append({
                "city": city,
                "latitude": latitude,
                "longitude": longitude,
                "temperature_c": current["temperature_2m"],
                "humidity_percent": current["relative_humidity_2m"],
                "apparent_temperature_c": current["apparent_temperature"],
                "time": current["time"],
            })
            print(f"Weather fetched: {city}")

        except requests.RequestException as error:
            print(f"Could not fetch {city}: {error}")

        time.sleep(0.2)

    Path("data").mkdir(exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv("data/weather.csv", index=False)

    print(f"\nSaved weather data for {len(df)} cities.")
    print("File: data/weather.csv")

if __name__ == "__main__":
    main()
