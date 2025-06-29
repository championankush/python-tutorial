# Project 3: Weather Application

A weather application that fetches real-time weather data from APIs and provides a user-friendly interface.

## 📋 Project Overview

This project creates a weather application that allows users to:
- Get current weather information for any city
- View weather forecasts for upcoming days
- Display weather data in a formatted, readable way
- Handle API errors gracefully
- Cache weather data to reduce API calls
- Convert between different temperature units

## 🎯 Learning Objectives

By completing this project, you will learn:
- **API Integration**: Working with external APIs and HTTP requests
- **JSON Data Handling**: Parsing and processing JSON responses
- **Error Handling**: Managing API failures and network issues
- **Data Caching**: Implementing simple caching mechanisms
- **User Interface**: Creating user-friendly command-line interfaces
- **Data Validation**: Validating and processing user input
- **Configuration Management**: Handling API keys and settings

## 🚀 Features

### Core Features
- ✅ Get current weather for any city
- ✅ Display temperature, humidity, wind speed, and conditions
- ✅ Show weather forecast for multiple days
- ✅ Handle API errors and network issues
- ✅ Cache weather data to reduce API calls
- ✅ Convert between Celsius and Fahrenheit
- ✅ Search for cities with autocomplete

### Advanced Features
- 🌡️ Temperature unit conversion
- 📍 Location-based weather (using coordinates)
- ⏰ Weather alerts and warnings
- 📊 Weather statistics and trends
- 🗺️ Multiple weather data sources
- 📱 Command-line and web interface options

## 📁 Project Structure

```
03_weather_app/
├── README.md              # This file
├── weather_app.py         # Main application file
├── weather_api.py         # API integration module
├── weather_cache.py       # Caching functionality
├── weather_utils.py       # Utility functions
├── config.py              # Configuration settings
├── tests/                 # Test files
│   ├── test_weather_api.py
│   └── test_weather_app.py
├── data/                  # Data storage
│   ├── cache.json         # Cached weather data
│   └── cities.json        # City database
└── requirements.txt       # Dependencies
```

## 🔧 Implementation Details

### API Integration
The application uses the OpenWeatherMap API to fetch weather data:
- **Current Weather**: Real-time weather conditions
- **Forecast**: 5-day weather forecast
- **Geocoding**: Convert city names to coordinates

### Data Structure
Weather data is structured as:
```python
{
    'city': 'New York',
    'country': 'US',
    'current': {
        'temperature': 22.5,
        'feels_like': 24.0,
        'humidity': 65,
        'wind_speed': 5.2,
        'description': 'Partly cloudy',
        'icon': '02d'
    },
    'forecast': [
        {
            'date': '2023-12-01',
            'temp_min': 18.0,
            'temp_max': 25.0,
            'description': 'Sunny',
            'icon': '01d'
        }
    ]
}
```

### Caching System
Weather data is cached to:
- Reduce API calls and costs
- Improve response time
- Handle offline scenarios
- Respect API rate limits

## 🎮 Usage Examples

### Basic Usage
```bash
# Run the application
python weather_app.py

# Get current weather
> weather "New York"

# Get weather forecast
> forecast "London" 5

# Search for cities
> search "San"

# Convert temperature
> convert 25 C F
```

### Advanced Usage
```bash
# Get weather by coordinates
> weather --lat 40.7128 --lon -74.0060

# Get weather with specific units
> weather "Tokyo" --units metric

# Clear cache
> cache clear

# Show cache status
> cache status
```

## 📊 Sample Output

```
=== Weather Application ===

Commands:
  weather <city> [options]       - Get current weather
  forecast <city> [days]         - Get weather forecast
  search <query>                 - Search for cities
  convert <temp> <from> <to>     - Convert temperature
  cache <command>                - Manage cache
  help                           - Show this help
  quit                           - Exit application

Options for weather:
  --units <unit>                 - Units (metric/imperial)
  --lat <latitude>               - Latitude coordinate
  --lon <longitude>              - Longitude coordinate

> weather "New York"
🌆 New York, US
🌡️ Temperature: 22°C (72°F)
🌡️ Feels like: 24°C (75°F)
💧 Humidity: 65%
💨 Wind: 5.2 km/h
☁️  Conditions: Partly cloudy
🕐 Last updated: 2023-12-01 14:30:00

> forecast "London" 3
🌆 London, GB - 3-Day Forecast

📅 2023-12-01
   🌡️ High: 15°C (59°F) | Low: 8°C (46°F)
   ☁️  Partly cloudy
   
📅 2023-12-02
   🌡️ High: 12°C (54°F) | Low: 6°C (43°F)
   🌧️  Light rain
   
📅 2023-12-03
   🌡️ High: 14°C (57°F) | Low: 7°C (45°F)
   ☀️  Sunny

> convert 25 C F
25°C = 77°F
```

## ✅ Success Criteria

- [ ] Application connects to weather API successfully
- [ ] Can fetch current weather for any city
- [ ] Can display weather forecast
- [ ] Handles API errors gracefully
- [ ] Implements caching system
- [ ] Converts between temperature units
- [ ] Provides user-friendly interface
- [ ] Validates user input
- [ ] Shows helpful error messages
- [ ] Code is well-organized and documented

## 🚀 Bonus Features

1. **Weather Alerts**: Display weather warnings and alerts
2. **Historical Data**: Show weather trends and statistics
3. **Multiple APIs**: Support for different weather data sources
4. **Weather Maps**: Generate simple ASCII weather maps
5. **Location Services**: Auto-detect user location
6. **Weather Widgets**: Create embeddable weather displays
7. **Data Export**: Export weather data to various formats
8. **Notifications**: Weather alerts and notifications

## 💡 Implementation Tips

1. **API Key Management**: Store API keys securely in environment variables
2. **Error Handling**: Implement comprehensive error handling for network issues
3. **Rate Limiting**: Respect API rate limits and implement backoff strategies
4. **Data Validation**: Validate API responses before processing
5. **Caching Strategy**: Implement smart caching with expiration times
6. **User Experience**: Provide clear feedback and loading indicators

## 🔗 Related Topics

- HTTP Requests and APIs
- JSON Data Processing
- Error Handling
- Data Caching
- Configuration Management
- User Interface Design

## 📚 Additional Resources

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Python Requests Library](https://requests.readthedocs.io/)
- [JSON Processing in Python](https://docs.python.org/3/library/json.html)
- [Environment Variables](https://docs.python.org/3/library/os.html#os.environ)

## 🔑 API Setup

To use this application, you'll need an API key from OpenWeatherMap:

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Set it as an environment variable:
   ```bash
   export OPENWEATHER_API_KEY="your_api_key_here"
   ```
4. Or create a `.env` file in the project directory

---

**Ready to build your weather application? Let's get started!** 🌤️ 