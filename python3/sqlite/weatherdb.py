# Credit goes to a student of mine, Patrick, for this idea.

from noaa_sdk import noaa
import sqlite3
from pprint import pprint

locations = {
    'chicago': [41.8781, -87.6298],
    'new york': [40.7128, -74.0060],
}

n = noaa.NOAA()
c = sqlite3.connect('weatherdb.db')

try:
    c.execute('''
CREATE TABLE weather(
  id    INTEGER   PRIMARY KEY,
  loc   STRING
)
''')
except sqlite3.OperationalError: # Table already exists.
    pass

(lat, long) = locations['new york']

pprint(n.points_forecast(lat, long))