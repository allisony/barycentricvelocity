from astropy.time import Time, TimePlotDate
from astropy.coordinates import SkyCoord, solar_system, EarthLocation, ICRS, Galactic
from astropy.coordinates import UnitSphericalRepresentation, CartesianRepresentation
from astropy import units as u
import numpy as np

## BASED ON THIS: https://pyastronomy.readthedocs.io/en/latest/pyaslDoc/aslDoc/baryvel.html

def main(skycoord_object, step_size_days=1, year=2023, site="apo"):

    time_array = initialize_time_array(step_size_days,year)
    location = initialize_location(site)

    vel_array = np.zeros(len(time_array))
    t_plot_date_array = np.zeros(len(time_array))

    for j, time in enumerate(time_array):

        t_obj = Time(time,format='mjd')
        ep, ev = solar_system.get_body_barycentric_posvel('earth', t_obj)
        op, ov = location.get_gcrs_posvel(t_obj)
        velocity = ev + ov
        sc_cartesian = skycoord_object.icrs.represent_as(UnitSphericalRepresentation).represent_as(CartesianRepresentation)
        vel_output = sc_cartesian.dot(velocity).to(u.km/u.s)

        vel_array[j] = vel_output.value
        t_plot_date_array[j] = t_obj.plot_date

    return time_array, t_plot_date_array, vel_array


def initialize_time_array(step_size_days = 1, year=2023): # the year doesn't matter!

    t = Time(str(year) + '-01-01T00:00:00',format='isot')

    time_array = np.arange(t.mjd,t.mjd+365.,step_size_days)

    return time_array


def initialize_location(site="apo"): # location doesn't really matter for most applications!
    # see https://docs.astropy.org/en/stable/api/astropy.coordinates.EarthLocation.html

    location = EarthLocation.of_site(site)

    return location




