import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

URL =  "https://api.waitwhile.com/v2/public/visits/chromehearts/first-available-slots"

now = datetime.now(ZoneInfo("America/New_York"))

search_end = now + timedelta(days=14)
params = {
    "fromDate": now.strftime("%Y-%m-%dT%H:%M"),
    "toDate": search_end.strftime("%Y-%m-%dT%H:%M"),
    "maxNumSlots": 10,
    "serviceDuration": 1800,
    "partySize": 1,
    "serviceIds": "WHmjBONC1Mcf8VSqjWar"
}

def get_available_slots():
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status
    return response.json()

slots = get_available_slots()
print(slots)
print(type(slots))

print("New York time: ", now)
print("Searching from: ", params["fromDate"])
print("Search until: ", params["toDate"])

print("Searching from:", params["fromDate"])
print("Searching until:", params["toDate"])

if slots:
    print("Appointment(s) Found: ")
    for slot in slots:
        print(
            f'{slot["date"]} - '
            f'{slot["numAvailableSpots"]} - '
        )
else:
    print("No appointments available.")

