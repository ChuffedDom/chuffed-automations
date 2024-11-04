from datetime import datetime
import requests


# Dummy users and hour to update
user_checkin_schedule = {
    "db46689b-104c-4e39-a750-02b8b0673485": 0,
    "d433aff8-3322-4598-9a34-7c799aba5e71": 1,
    "81ef9029-a363-4ae8-b73d-a605bfe45580": 2,
    "d6089b72-dcee-42ec-a045-c167a03c67c3": 3,
    "c7331bf1-f77d-4826-9ac8-cb29aed96b8d": 4,
    "7385aebd-79bd-44ea-82f0-23483533c404": 5,
    "c10703cc-0e5c-4bb2-b8bf-1d5f519f2f60": 6,
    "c9ce26f8-9274-4153-bae6-911da7b5a484": 7,
    "eb47be24-751c-474c-abd1-a0e7942e402f": 8,
    "ccf56a30-7e96-410c-bd27-caceee5d83f3": 9,
    "47c7bd47-0796-4acf-a6bb-20b7280b158a": 10,
    "b220c8a7-7789-40e9-89db-b01d1e10c846": 11,
    "813d1e87-114c-46f6-bcc3-a9be0cf484a5": 12,
    "c6da1fa1-e961-4d67-992c-99f38b0a1caf": 13,
    "449d7c75-313f-41d9-928d-eb002ee08267": 14,
    "80c19491-c50f-4bfb-8d5e-02966549400a": 15,
    "fb8a42f0-1fc5-4acb-8775-a605241f2816": 16,
    "e2dc70f7-37bd-4ead-8142-9f660166e7aa": 17,
    "2958b0fc-6e0c-4773-873d-78914c5d850b": 18
    # You can adjust these hours based on when you want each user to check in
}


# Function to update checkedInToday status via API
def update_checkin_status(user_id):
    url = 'https://europe-west1-checkin-nuggets.cloudfunctions.net/updateCheckInStatusForUser'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "userID": user_id,
        "checkedInToday": True
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"Successfully updated check-in for user {user_id}")
    else:
        print(f"Failed to update check-in for user {user_id}: {response.status_code} - {response.text}")

# Get the current hour
current_hour = datetime.now().hour

# Check if any user should be updated at this hour
for user_id, hour in user_checkin_schedule.items():
    if hour == current_hour:
        update_checkin_status(user_id)