import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print(data)
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude,latitude)
print(iss_position)
print("go to latlong.net/geo-tools to see where it is")

#if the iss is close to my current position
# and it is currently dark
# then send me an email to tell me to look up.
# Bonus:  run the code every 60 seconds.


