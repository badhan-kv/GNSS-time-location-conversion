def decimal_to_dms(decimal_degrees):
degrees = int(decimal_degrees)
minutes_full = abs(decimal_degrees - degrees) * 60
minutes = int(minutes_full)
seconds = (minutes_full - minutes) * 60
return degrees, minutes, seconds
print("lat ", decimal_to_dms(lat)) # lat = lattitude
print("lon ", decimal_to_dms(lon)) # lon = longitude
