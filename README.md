# 🌤️ Simple Weather Info Fetcher using WeatherAPI

This Python script allows users to input a **city name** and instantly fetches the **current weather** using [WeatherAPI](https://www.weatherapi.com/).

---

## 📌 Features

- Get current weather by entering any city name.
- Shows:
  - 🌡️ Temperature in Celsius
  - 💨 Wind speed in kilometers per hour
  - ⛅ Weather condition description

---

## 🧰 Requirements

- Python 3.x
- `requests` library (install using pip if not already installed)

pip install requests
## 🔑 API Key
This script uses a free WeatherAPI key (demo):

python
Copy
Edit
key = "9370edf3d0494843bff94116252106"

## ⚠️ For production use, please get your own API key to avoid quota issues.

## 🚀 How to Run
Copy the code into a .py file (e.g., weather.py)

Run the script:

Copy
Edit
python weather.py
Enter a city name when prompted.

## 🧪 Sample Output
yaml
Copy
Edit
Enter city name: london

📍 Weather in London:
🌡️ Temperature: 19°C
💨 Wind: 11.2 kph
⛅ Condition: Partly cloudy
## 📂 Project Structure

bash
Copy
Edit
weather_app/
│
├── weather.py        # Main Python script
├── README.md         # Documentation
bash

## 🛡️ License
This script is for educational/demo purposes. Use your own API key for production use.

yaml
Copy
Edit

---
bash
Want help with [saving this as a README file](f), [turning it into a GUI app](f), or [adding forecast support](f)?
