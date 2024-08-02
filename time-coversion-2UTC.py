from datetime import datetime
# Function to convert a local time to UTC Julian Date (JD) and Modified Julian Date (MJD)
def local_time_to_utc_jd_mjd(local_time_str):
# Convert the local time string to a datetime object
local_time = datetime.strptime(local_time_str, '%Y-%m-%d %H:%M:%S')
# Extract year, month, day, hour, minute, and second
year = local_time.year
month = local_time.month
day = local_time.day
hour = local_time.hour
minute = local_time.minute
second = local_time.second
# Calculate Julian Date (JD) using the formula
if month <= 2:
year -= 1
month += 12
A = year // 100
B = 2 - A + A // 4
jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
jd += (hour + minute / 60 + second / 3600) / 24
# Calculate Modified Julian Date (MJD)
mjd = jd - 2400000.5
return jd, mjd
# Example usage:
local_time_str = '2023-10-29 00:00:00'
utc_jd, utc_mjd = local_time_to_utc_jd_mjd(local_time_str)
print(f"Julian Date (JD): {utc_jd}")
print(f"Modified Julian Date (MJD): {utc_mjd}")
