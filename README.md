# barycentricvelocity
 A wrapper for computing Earth's velocity when looking toward different sightlines throughout the year

```
from astropy.coordinates import SkyCoord, ICRS, Galactic
from astropy import units as u
import matplotlib.pyplot as plt
from barycentricvelocity import barycentricvelocity
plt.ion()

coord = SkyCoord(342.9000167199435, -26.2075980302058, frame=Galactic, unit=(u.deg, u.deg))
t_mjd,t_plot_date, velocity = barycentricvelocity.main(coord)

plt.figure()
plt.plot_date(t_plot_date, velocity)
plt.xlabel('Date')
plt.ylabel('Radial Velocity (km/s)')
```
