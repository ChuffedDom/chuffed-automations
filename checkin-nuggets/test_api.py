import requests
import json

url = "https://europe-west1-checkin-nuggets.cloudfunctions.net/getEmailsByRegionCheckInStatus"

payload = json.dumps({
  "regionTimeZone": "Europe (West)"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
