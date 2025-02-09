import time
import datetime
import requests

def api_up_request(url):
    print("\n" + 100 * "=")
    print(f"📋 Testing GET request to {url}...")
    try:
        # Send a GET request
        response = requests.get(url)
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the message field from the response
            message = data.get('message', '')
            
            # Print the test result based on the message field
            if message == "API is working":
                print("✅ Test passed")
            else:
                print("❌ Test failed")
        else:
            # Print an error message if the request was not successful
            print(f"❌ Failed to retrieve data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to retrieve data: {e}")

def send_subscribe_email(url, email, template):
    print("\n" + 100 * "=")
    print(f"📋 Testing email subscribe request {url} for {email} with template {template}...")
    try:
        # Send a POST request with the email and template
        response = requests.post(
            url,
            json={"email": email, "template": template}
        )
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the message field from the response
            message = data.get('message', '')
            
            # Print the test result based on the message field
            if message == "email sent":
                print("✅ Test passed")
            else:
                print("❌ Test failed")
        else:
            # Print an error message if the request was not successful
            print(f"❌ Failed to send email. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send email: {e}")

# The tests to run
print("\n" + 100 * "=")
print(f"🚦 Running tests at {datetime.datetime.now()} ...")
api_up_request("http://localhost:5000/")
time.sleep(1)
api_up_request("http://automations.chuffed.app")
time.sleep(1)
api_up_request("https://automations.chuffed.app")
time.sleep(1)
send_subscribe_email("http://localhost:5000/confirm-email", "dom@chuffed.solutions", "its-your-turn-subscription.html")
time.sleep(1)
send_subscribe_email("https://automation.chuffed.app/confirm-email", "dom@chuffed.solutions", "its-your-turn-subscription.html")

