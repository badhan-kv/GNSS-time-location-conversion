from datetime import datetime, timedelta
# Function to convert local time to TAI (International Atomic Time)
def local_time_to_tai(local_time_str, leap_seconds=37):
# Convert the local time string to a datetime object
local_time = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')
# Add the current number of leap seconds to get TAI
# As of the last update in April 2023, the total was 37 seconds
tai_time = local_time + timedelta(seconds=leap_seconds)
return tai_time
# Example usage
local_time_str = '2023-10-29 00:00:00'
tai_time = local_time_to_tai(local_time_str)
# Convert TAI time to string for display
tai_time_str = tai_time.strftime('%Y-%m-%d %H:%M:%S')
print(f"TAI time: {tai_time_str}")
