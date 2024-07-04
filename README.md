Calculates aphelion and perihelion dates to hour precision based on JPL ephemeris

## Requires
tested with Python 3.11.9.  Basic enough to work with most any Python3

## Installation

1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.
4. python earth_sun_apsis.py

## Example

```
% earth_sun_apsis.py 2024
Aphelion 2024-07-05 05:00:00 UTC
152,099,968.25 km (94,510,509.37 miles)

Perihelion 2024-01-03 01:00:00 UTC
152,099,968.25 km (94,510,509.37 miles)

a difference of 4,999,335.69 km (3,106,442.21 miles) or 3.29%
```