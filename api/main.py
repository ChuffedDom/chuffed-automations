from flask import Flask, request
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

@app.route('/', methods=['GET'])
def health_check():
    return {'message': 'API is working'}

@app.route('/confirm-email', methods=['POST'])
def confirm_email():
    print(f"Starting subscription flow request: {request.json}")
    # get the body of the request
    body = request.json
    message = Mail(
        from_email="dom@itsyourturn.news",
        to_emails=body["email"],
        subject="It's Your Turn",
        html_content=open(os.path.join(os.path.dirname(__file__), f"../templates/{body["template"]}")).read()
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code == 202:
            print("Email sent")
            return {'message': 'email sent'}  
    except Exception as e:
        print(e)
        print("Email not sent")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)