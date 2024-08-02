#Geodetic latitude, longitude, and altitude above the WGS 84 ellipsoid
from pyproj import Transformer, CRS
# Define the WGS 84 ECEF CRS
crs_ecef = CRS.from_epsg(4978) # WGS 84 ECEF
# Define the WGS 84 Geodetic CRS
crs_geodetic = CRS.from_epsg(4326) # WGS 84
# Create a transformer to convert ECEF coordinates to geodetic coordinates
transformer_ecef_to_geodetic = Transformer.from_crs(crs_ecef, crs_geodetic)
# Given ECEF coordinates for the start of the runway
rwy30Start = [-2694685.473, -4293642.366, 3857878.924]
# Perform the transformation from ECEF to geodetic coordinates
lat_start, lon_start, alt_start = transformer_ecef_to_geodetic.transform(*rwy30Start,direction='FORWARD')
# Print the results
print(f"Latitude: {lat_start} degrees")
print(f"Longitude: {lon_start} degrees")
print(f"Altitude: {alt_start} meters")
