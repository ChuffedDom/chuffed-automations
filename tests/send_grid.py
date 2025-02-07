import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

messege = Mail(
    from_email="dom@itsyourturn.news",
    to_emails="dom@chuffed.solutions",
    subject="It's Your Turn",
    # Read /templates/subscription.html into a string and pass it the argument html_content
    html_content=open("../templates/subscription.html").read()
)

try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(messege)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    print("Email sent")
except Exception as e:
    print(e)
    print("Email not sent")