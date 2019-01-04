
from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
lookup = weather.lookup_by_latlng(45.35,25.27)
condition = lookup.condition

print(condition.temp)
print(condition.text)
