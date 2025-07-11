import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageEnhance # For image processing
import requests
import geocoder
from weather_codes import weather_conditions # Import weather conditions from weather_codes.py
from dotenv import load_dotenv
from datetime import datetime

# Load API key from .env file
load_dotenv("id.env")
API_KEY = os.getenv("API_KEY")
is_celsius = True

# Format timestamp to readable format
def format_time(timestamp, mode="time"):
    dt = datetime.fromisoformat(timestamp[:-1])
    return dt.strftime("%I %p") if mode == "time" else dt.strftime("%a")

# Fetch weather info and update UI
def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    result_label.config(text=""); icon_label.config(image=""); icon_label.image = None
    hourly_label.config(text=""); daily_label.config(text="")

    try:
        # Real-time weather
        url = f"https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={API_KEY}"
        res = requests.get(url); res.raise_for_status()
        v = res.json()["data"]["values"]

        temp = v["temperature"] if is_celsius else v["temperature"] * 9 / 5 + 32
        unit = "°C" if is_celsius else "°F"

        # Weather Summary
        result_text = f"📍 {city.title()}\n\n🌡️ Temp: {temp:.1f}{unit}\n💧 Humidity: {v['humidity']}%\n💨 Wind: {v['windSpeed']} km/h\n☁️ Condition: {weather_conditions.get(v['weatherCode'], 'Unknown')}"
        result_label.config(text=result_text)

        # Weather Icon
        icon_path = os.path.join("icons", f"{v['weatherCode']}.png")
        if os.path.exists(icon_path):
            img = Image.open(icon_path).resize((64, 64))
            icon_label.image = ImageTk.PhotoImage(img)
            fade_in_icon(img)
        else:
            icon_label.config(text="Icon not found")

        # Forecasts
        forecast_url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={API_KEY}"
        res = requests.get(forecast_url); res.raise_for_status()
        forecast = res.json()["timelines"]

        # Hourly Forecast (Next 5 hours)
        hourly_text = "\n🕓 Hourly Forecast:\n"
        for h in forecast["hourly"][:5]:
            t = h["values"]["temperature"]
            t = t if is_celsius else t * 9 / 5 + 32
            hourly_text += f"{format_time(h['time'])}: {t:.1f}{unit}\n"
        hourly_label.config(text=hourly_text)

        # Daily Forecast (Next 3 days)
        daily_text = "\n📅 3-Day Forecast:\n"
        for d in forecast["daily"][:3]:
            tmin = d["values"]["temperatureMin"]
            tmax = d["values"]["temperatureMax"]
            if not is_celsius:
                tmin = tmin * 9 / 5 + 32
                tmax = tmax * 9 / 5 + 32
            day = format_time(d["time"], mode="day")
            daily_text += f"{day}: {tmin:.1f}{unit} - {tmax:.1f}{unit}\n"
        daily_label.config(text=daily_text)

    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Convert between °C and °F
def toggle_unit():
    global is_celsius
    is_celsius = not is_celsius
    get_weather()

# Detect user location automatically
def detect_location():
    city = geocoder.ip('me').city
    if city:
        city_entry.delete(0, tk.END)
        city_entry.insert(0, city)
        get_weather()
    else:
        messagebox.showerror("Location Error", "Could not detect location.")

# Icon fade-in animation
def fade_in_icon(image, alpha=0):
    if alpha > 1: return
    img = image.copy()
    faded_img = ImageEnhance.Brightness(img).enhance(alpha)
    tk_img = ImageTk.PhotoImage(faded_img)
    icon_label.config(image=tk_img)
    icon_label.image = tk_img
    root.after(50, lambda: fade_in_icon(image, alpha + 0.1))

# Create vertical gradient background
def create_gradient(w, h, c1, c2):
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    for y in range(h): ImageDraw.Draw(mask).line([(0, y), (w, y)], fill=int(255 * y / h))
    return ImageTk.PhotoImage(Image.composite(top, base, mask))

# GUI setup

root = tk.Tk()
root.title("Weather App")
root.geometry("420x700")  # Increased height 
root.resizable(False, False)

canvas = tk.Canvas(root, width=420, height=700)
canvas.pack(fill="both", expand=True)
canvas_bg = canvas.create_image(0, 0, anchor="nw", image=create_gradient(420, 700, "#FFEFEF", "#FADADD"))

container = tk.Frame(canvas, bg="#FFEFEF")
canvas.create_window((0, 0), window=container, anchor="nw", width=420, height=700)

# App Title
tk.Label(container, text="Weather App", font=("Helvetica", 20, "bold"), bg="#FFEFEF", fg="#FF7F7F").pack(pady=(20, 10))

# Input field
city_entry = tk.Entry(container, font=("Helvetica", 13), justify="center", width=30, bd=2, relief="groove")
city_entry.pack(pady=10)
city_entry.bind("<Return>", lambda e: get_weather())

# Button style
btn_style = dict(font=("Helvetica", 11), bg="#D96459", fg="white", activebackground="#b9584b", relief="flat", width=20)

# Buttons
tk.Button(container, text="Get Weather", command=get_weather, **btn_style).pack(pady=5)
tk.Button(container, text="Toggle °C/°F", command=toggle_unit, **btn_style).pack(pady=5)
tk.Button(container, text="Detect Location", command=detect_location, **btn_style).pack(pady=5)

# Weather icon
icon_label = tk.Label(container, bg="#FFEFEF")
icon_label.pack(pady=10)

# Main weather result
result_label = tk.Label(container, text="", font=("Helvetica", 12), bg="#FFEFEF", justify="center")
result_label.pack(pady=5)

# Hourly Forecast
hourly_label = tk.Label(container, text="", font=("Helvetica", 11), bg="#FFEFEF", justify="left", fg="#444")
hourly_label.pack(pady=(10, 5))

# Daily Forecast
daily_label = tk.Label(container, text="", font=("Helvetica", 11), bg="#FFEFEF", justify="left", fg="#444")
daily_label.pack(pady=5)

# Divider and Footer
tk.Frame(container, height=2, bd=1, relief="sunken", bg="#B07BAC").pack(fill="x", padx=20, pady=15)
tk.Label(container, text="Made by Sakshi | 2025", font=("Helvetica", 9, "italic"), bg="#FFEFEF", fg="#B07BAC").pack(side="bottom", pady=10)

# Start the application
root.mainloop()
