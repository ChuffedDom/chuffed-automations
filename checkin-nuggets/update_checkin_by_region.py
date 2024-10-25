import requests
import sys

def update_check_in(region_time_zone):
    url = "https://europe-west1-checkin-nuggets.cloudfunctions.net/updateCheckInByRegion"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "regionTimeZone": region_time_zone
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Successfully updated users in region: {region_time_zone}")
        else:
            print(f"Failed to update users. Status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_checkin.py <region_time_zone>")
    else:
        region_time_zone = sys.argv[1]
        update_check_in(region_time_zone)
