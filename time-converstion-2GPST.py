from datetime import datetime, timedelta
# Define the function to convert local time to GPST (GPS week and seconds of the week)
def local_time_to_gpst(local_time_str):
# GPS time starts from January 6, 1980 at 00:00 UTC
gps_start = datetime(1980, 1, 6)
# Convert the local time string to a datetime object assuming the string is in UTC
local_time = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')
# Calculate the time difference between the local time and the GPS start time
delta = local_time - gps_start
# Calculate the total number of seconds from the GPS start time to the local time
total_seconds = delta.total_seconds()
# Determine the GPS week by dividing the total seconds by the number of seconds in a week
gps_week = total_seconds // (7 * 24 * 3600)
# Calculate the seconds into the week by taking the remainder of the total seconds divided
by the number of seconds in a week
seconds_of_week = total_seconds % (7 * 24 * 3600)
return int(gps_week), int(seconds_of_week)
# Example usage
local_time_str = '2023-10-29 00:00:00'
gpst_week, gpst_seconds_of_week = local_time_to_gpst(local_time_str)
print(f"GPS Week: {gpst_week}")
print(f"Seconds into the GPS week: {gpst_seconds_of_week}" )
