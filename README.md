# Weather_search-web

This project provides weather information for a given city or country using a Flask web application. Weather data is retrieved from WeatherAPI.

![Screen](https://github.com/S1avv/weather_search-web/assets/151785734/9d087dcc-55c8-4a47-a315-819dcd77808f)


## Features

- Get current weather information for any city or country.
- Supports multiple languages for weather information.
- Simple API endpoint to fetch weather data.

## Requirements

- Python 3.12 or higher
- Poetry for dependency management

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/S1avv/weather_search-web.git
    cd weather_search-web
    ```

2. Install Poetry if you haven't already:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install dependencies:

    ```bash
    poetry install
    ```

4. Update a `settings.py` file in the root directory with your WeatherAPI key:

    ```python
    api_key = 'your_weatherapi_key_here'
    ```

## Usage

1. Run the Flask application:

    ```bash
    python main.py
    ```

2. Go to the website and enter the city

## Project Structure

```plaintext
weather_search-web/
├── weathersearch /
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
├── main.py
├── settings.py
└── index.html
