from skyfield.api import Loader
import sys
import numpy as np
import datetime


def km_to_mi(km):
    # convert km to mi
    return km * 0.621371


def main(year=2024):
    """
    Calculate the sun-earth distance in kilometers for a given year and determine the aphelion and perihelion points.
    """
    from skyfield.api import load, Topos
    load = Loader('/var/data')
    eph = load(
        'de421.bsp')  # JPL Development ephemeris 421 covers 1899-07-28 through 2053-10-08 with reasonable resolution

    ts = load.timescale()
    t = ts.utc(year, 1, 1, range(365 * 24))  # range of all hours in the given year
    sun = eph['sun']
    earth = eph['earth']
    difference = (earth - sun).at(t).distance().km  # sun-earth distance in km

    i = np.argmax(difference)  # index of maximum
    j = np.argmin(difference)  # index of minimum

    # aphelion is min earth-sun distance to sun, perihelion is max earth-sun distance
    for label, idx in zip(('Aphelion', 'Perihelion'), (i, j)):
        print(f"{label} {t[idx].utc_strftime()}")
        print(f"{difference[i]:,.2f} km ({km_to_mi(difference[i]):,.2f} miles)")
        print()
    delta = difference[i] - difference[j]
    pct = (delta / difference[i]) * 100
    print(f"a difference of {delta:,.2f} km ({km_to_mi(delta):,.2f} miles) or {pct:.2f}%")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        year = int(sys.argv[1])
    else:
        year = datetime.datetime.now().year
    main(year)
