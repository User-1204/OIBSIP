# Weather-App
A Python desktop application that delivers live weather updates, hourly and daily forecasts, and automatic location detection, all presented through an intuitive and visually engaging interface. This project demonstrates effective API integration, clean modular code design, and thoughtful user experience elements such as gradient backgrounds and animated weather icons.


## Purpose

The Weather App was designed to simplify how users access real-time weather data and short-term forecasts.
It combines reliable external data from the Tomorrow\.io API with a lightweight local interface to create a seamless, quick, and user-friendly experience.


## Key Capabilities

* **Live Weather Updates**
  Instantly retrieve current temperature, humidity, wind speed, and weather conditions based on the user's input or detected location.

* **Short-Term Forecasts**

  * Displays temperature forecasts for the next five hours.
  * Shows minimum and maximum temperatures for the upcoming three days.

* **Unit Switching**
  Toggle effortlessly between Celsius and Fahrenheit; updates apply across all displayed data.

* **Automatic Location Detection**
  Determines the user's city using IP-based geolocation for quicker access without manual entry.

* **Animated Visual Elements**
  Smooth fade-in weather icons and a vertical gradient background elevate the visual presentation.

* **Reliable Error Handling**
  Provides user feedback for invalid input, missing icons, or connection errors to maintain usability.


## Technology Overview

* **Python 3** – Core programming language
* **Tkinter** – User interface components
* **Pillow (PIL)** – Image processing and icon animation
* **Requests** – Communicating with the Tomorrow\.io API
* **Geocoder** – IP-based city detection
* **dotenv** – Securely loads API keys
* **Tomorrow\.io API** – Provides real-time and forecast weather data


## Project Structure

```
weather-app/
├── Code.py                # Main application logic and UI setup
├── weather_codes.py       # Mapping of weather codes to human-readable descriptions
├── icons/                 # Weather condition icons (PNG format)
├── id.env                 # API key storage 
└── README.md              # Project documentation
```


## Installation and Setup

1. **Install required dependencies**:

   ```bash
   pip install requests pillow python-dotenv geocoder
   ```

2. **Configure your API key**:

   * Sign up at [Tomorrow.io](https://www.tomorrow.io/) to obtain your API key.
   * Create a file named `id.env` in the project directory:

     ```
     API_KEY=your_api_key_here
     ```

3. **Add weather icons**:

   * Place relevant weather condition icons (e.g., `1000.png`, `1101.png`) in the `icons/` folder.
   * Ensure filenames match the codes listed in `weather_codes.py`.


## How to Use

Run the application:

```bash
python Code.py
```

* Enter a city name and click "Get Weather".
* Use "Toggle °C/°F" to switch between temperature units.
* Click "Detect Location" to fetch local weather automatically.

The interface will display:

* Current weather summary
* Five-hour hourly temperature forecast
* Three-day daily temperature range


## Preview

<img width="516" height="912" alt="Image" src="https://github.com/user-attachments/assets/2e479e39-2fee-4a08-ba80-430f25cfab04" />


## Design Considerations

* **Clarity and Simplicity**: Intuitive controls and clean layout
* **Visual Balance**: Gradient backgrounds and icon animations add depth without distraction
* **Modularity**: Separates data mapping, UI design, and API logic for easier updates
* **User Feedback**: Clear messages for missing data, connectivity issues, or invalid input
