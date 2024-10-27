import sys
import requests
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Load service account credentials and set up Gmail API
SERVICE_ACCOUNT_FILE = '/home/chuffed-automations/chuffed-automations-key.json'
USER_TO_IMPERSONATE = 'dom@chuffed.solutions'
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate and build the Gmail service
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_creds = creds.with_subject(USER_TO_IMPERSONATE)
service = build('gmail', 'v1', credentials=delegated_creds)

# Define functions to create and send messages
def create_message(sender, to, subject, body_text):
    message = MIMEText(body_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(to, subject, body_text):
    message = create_message(USER_TO_IMPERSONATE, to, subject, body_text)
    service.users().messages().send(userId="me", body=message).execute()

# Define the main function
def main(region_time_zone):
    # Make the API call to retrieve email data
    response = requests.post(
        'https://europe-west1-checkin-nuggets.cloudfunctions.net/getEmailsByRegionCheckInStatus',
        headers={'Content-Type': 'application/json'},
        json={'regionTimeZone': region_time_zone}
    )
    email_data = response.json()  # Parse JSON response

    # Loop through the email data and send appropriate emails
    for entry in email_data:
        email = entry['email']
        checked_in_today = entry['checkedInToday']
        
        if checked_in_today:
            # Send congratulatory email
            subject = "🎉 Great Job"
            body = ("Hey, good on you for turning up today. 6 people celebrated that. "
                    "Look forward to seeing you tomorrow.\n\nDom")
        else:
            # Send nudge email
            subject = "👉🏾 Nudge"
            body = ("Hey, you haven't checked in today. 8 people nudged you. "
                    "All you need to do is 5 minutes towards your big goal and check-in here: "
                    "https://app.checkinnuggets.xyz/\n\nDom")

        # Send the email
        send_email(email, subject, body)
        print(f"Email sent to {email} with subject '{subject}'")

# Run the script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python send_emails.py <regionTimeZone>")
    else:
        region_time_zone = sys.argv[1]
        main(region_time_zone)
