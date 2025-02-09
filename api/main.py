from flask import Flask, request
import os
import logging
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configure logging
log_file = os.path.join(os.path.dirname(__file__), '../api.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filename=log_file)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

@app.route('/', methods=['GET'])
def health_check():
    logging.info("Health check endpoint was called")
    return {'message': 'API is working'}

@app.route('/confirm-email', methods=['POST'])
def confirm_email():
    logging.info(f"Starting subscription flow request: {request.json}")
    # get the body of the request
    body = request.json
    message = Mail(
        from_email="dom@itsyourturn.news",
        to_emails=body["email"],
        subject="It's Your Turn",
        html_content=open(os.path.join(os.path.dirname(__file__), f"../templates/{body['template']}")).read()
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        if response.status_code == 202:
            logging.info("Email sent")
            return {'message': 'email sent'}
        else:
            logging.error(f"Failed to send email, status code: {response.status_code}")
            return {'message': 'email not sent'}, 500
    except Exception as e:
        logging.error("Error occurred while sending email", exc_info=True)
        return {'message': 'email not sent'}, 500

if __name__ == '__main__':
    logging.info("Starting Flask app...")
    app.run(host='0.0.0.0', port=5000)