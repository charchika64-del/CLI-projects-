import requests
from datetime import datetime

locations = {
    "Mumbai": {"lat": 19.0760, "lon": 72.8777},
    "Delhi": {"lat": 28.6139, "lon": 77.2090},
    "Bangalore": {"lat": 12.9716, "lon": 77.5946},
    "Chennai": {"lat": 13.0827, "lon": 80.2707},
    "Kolkata": {"lat": 22.5726, "lon": 88.3639},
    "Hyderabad": {"lat": 17.3850, "lon": 78.4867},
    "Pune": {"lat": 18.5204, "lon": 73.8567},
    "Jaipur": {"lat": 26.9124, "lon": 75.7873},
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Tokyo": {"lat": 35.6762, "lon": 139.6503},
    "Sydney": {"lat": -33.8688, "lon": 151.2093},
    "Dubai": {"lat": 25.2048, "lon": 55.2708},
    "Paris": {"lat": 48.8566, "lon": 2.3522},
    "Singapore": {"lat": 1.3521, "lon": 103.8198}
}

# NEW: Added `city_name` as the first parameter
def get_data(city_name, lat, lon, date=None):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lon}"
    if date:
        url += f"&date={date}"
    
    data = requests.get(url).json()

    sunrise = datetime.fromisoformat(data["sunrise"]).strftime('%I:%M %p')
    sunset = datetime.fromisoformat(data["sunset"]).strftime('%I:%M %p')

    # Use city_name instead of the global variable
    print(f" City: {city_name}🏭 ")
    print(f" Date: {data['date']}🗓️ ")
    print(f"  Timezone: {data['tzid']}⏰")
    print(f"  Day Length: {round(data['day_length'] / 3600, 2)} hours⏳ ")
    print(f"  Sunrise: {sunrise}🌄")
    print(f"  Sunset: {sunset}🌆 ")


print("Welcome to sunrise and sunset teller.☀️")
while True:
    print("\n--- Menu ---")
    print("Type 1 to get today's data")
    print("Type 2 to get data for a specific day 🗓️")
    print("Type 3 to Exit🔚")
    
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("❌ Please enter a number (1, 2, or 3).")
        continue

    if number == 3:
        print("Exiting...")
        break

    city = input("Enter your city: ")
    
    if city not in locations:
        print(f"❌ City '{city}' not found in our database.")
        continue

    lat = locations[city]["lat"]
    lon = locations[city]["lon"]

    if number == 1:
        # Pass `city` into the function
        get_data(city, lat, lon)

    elif number == 2:
        year = input("Enter year (e.g. 2026): ")
        month = input("Enter month (e.g. 09): ")
        day = input("Enter day 📅 (e.g. 09): ")
        date_str = f"{year}-{month}-{day}"
        # Pass `city` into the function
        get_data(city, lat, lon, date_str)

    else:
        print("❌ Invalid option. Please type 1 or 2.")
