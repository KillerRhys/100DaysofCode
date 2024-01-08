""" Weather add-on
    Coded by TechGYQ
    www.mythosworks.com
    2023.11.13-1808 """

# Imports
from pyowm import OWM as METEOR


def daily_weather(area):
    # TODO format message better.
    owm = METEOR('5d15de47fc9b057d0dd9d4892cf6a516')
    mgr = METEOR.weather_manager(owm)

    observation = mgr.weather_at_place(area)
    w = observation.weather
    forecast = (f" %s with a temperature of %s. A low of %s with a high of %s" % (w.detailed_status, round(w.temperature(
        'fahrenheit')['temp']), round(w.temperature('fahrenheit')['temp_min']),
        round(w.temperature('fahrenheit')['temp_max'])))

    return forecast
