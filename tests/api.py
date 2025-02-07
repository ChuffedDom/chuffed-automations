import time
import datetime
import requests

def test_up_request(url):
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


# The tests to run
print("\n" + 100 * "=")
print(f"🚦 Running tests at {datetime.datetime.now()} ...")
test_up_request("http://localhost:5000/")
