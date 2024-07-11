import datetime
import requests
from datetime import datetime

MY_LATITUDE=43.653225
MY_LONGITUDE=-79.383186
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
#
# # Returns information about error codes
# response.raise_for_status()
#
# # Returns JSON output
# data = response.json()
# print(data)
#
# # Returns specific information from JSON output
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
#
# iss_position = (longitude,latitude)
# print(iss_position)

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
print(data)

sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
print(sunrise)
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now()
print(time_now.hour)