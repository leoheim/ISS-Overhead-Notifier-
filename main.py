import requests
from datetime import datetime
import smtplib

# The email adress that will sent the mail
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "EMAIL PASSWORD"

MY_LAT = -7.119496  # Your latitude
MY_LONG = -34.845013  # Your longitude


def iss_is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 >= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 >= iss_latitude <= MY_LAT + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now > sunset and time_now < sunrise:
        return True


# If the ISS is close to my current position and it is currently dark

if iss_is_above() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(to_addrs="leomont11@hotmail.com",
                            from_addr=MY_EMAIL,
                            msg='SUBJECT: ISS IS ABOVE YOU\n\nHello, the ISS Satelite is above you, look up!')
# Then email me to tell me to look up.
