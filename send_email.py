from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

# Path to your service account credentials JSON file
SERVICE_ACCOUNT_FILE = 'chuffed-automations-key.json'

# Email of the user to impersonate (must be in your domain)
USER_TO_IMPERSONATE = 'dom@chuffed.solutions'

# Set up Gmail API send scope
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Authenticate with the service account and impersonate the user
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_creds = creds.with_subject(USER_TO_IMPERSONATE)
service = build('gmail', 'v1', credentials=delegated_creds)

# Function to create and send an email
def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# Compose and send the email
message = create_message(USER_TO_IMPERSONATE, 'dom.maurice@gmail.com', 'Test Subject 2', 'Hello, this is a test email!')
service.users().messages().send(userId="me", body=message).execute()
