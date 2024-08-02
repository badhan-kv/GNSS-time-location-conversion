import numpy as np
from pyproj import Transformer, CRS
transformer_ecef_to_geodetic = Transformer.from_crs(CRS.from_epsg(4978), CRS.from_epsg(4326))
# Function to convert ECEF coordinates to ENU coordinates
def ecef_to_enu(x, y, z, lat_ref, lon_ref, alt_ref):
# Convert reference point to radians
lat_ref_rad = np.radians(lat_ref)
lon_ref_rad = np.radians(lon_ref)
# Reference ECEF coordinates
x0, y0, z0 = transformer_ecef_to_geodetic.transform(lat_ref, lon_ref, alt_ref, direction='INVERSE')
# ECEF vector
dx = x - x0
dy = y - y0
dz = z - z0
# Trigonometric shortcuts
slat = np.sin(lat_ref_rad)
clat = np.cos(lat_ref_rad)
slon = np.sin(lon_ref_rad)
clon = np.cos(lon_ref_rad)
# ENU transformation matrix
t = np.array([[-slon, clon, 0], [-slat*clon, -slat*slon, clat], [clat*clon, clat*slon,slat]])
# Perform the transformation
east, north, up = t @ np.array([dx, dy, dz])
return east, north, up
# Define ECEF coordinates for rwy30Start and rwy30End
rwy30Start = [-2694685.473, -4293642.366, 3857878.924]
rwy30End = [-2694892.460, -4293083.225, 3858353.437]
# Get geodetic coordinates for rwy30Start
lat_start, lon_start, alt_start = transformer_ecef_to_geodetic.transform(*rwy30Start)
# Calculate ENU coordinates of rwy30End relative to rwy30Start
easting, northing, upping = ecef_to_enu(rwy30End[0], rwy30End[1], rwy30End[2], lat_start,lon_start, alt_start)
print(f"Easting: {easting} meters, Northing: {northing} meters, Upping: {upping} meters")
