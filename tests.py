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
    html_content="""
        <!-- table for the main layout-->
    <table align="center" border="0" cellpadding="20" cellspacing="0" width="600"
        style="
            border-collapse: collapse;
            font-family: Arial, Helvetica, sans-serif;
            padding: 20px;
        " >
    <!-- header -->
    <tr>
      <td align="center" bgcolor="#267326" style="padding: 20px 0;">
        <h1 style="color:#f2f3f2; font-size: 24px;">Welcome, It's Your Turn</h1>
      </td>
    </tr>
    <!-- body -->
    <tr>
      <td bgcolor="#f2f3f2" style="padding: 20px;">
        <h1 style="color:#0a1f0a; font-size: 18px;">Hello!</h1>
        <p style="color:#0a1f0a; font-size: 16px;">
          Thank you for signing up to my newsletter. I am thrilled to have you
          on board and I hope I can help you on your quest. You can expect to receive monthly updates on the latest.
        </p>
        <p style="color:#0a1f0a; font-size: 16px;">
          If you have any questions, feel free to reply to this email. We're
          always happy to help out.
        </p>
      </td>
    </tr>
    <!-- footer -->
    <tr>
      <td bgcolor="#267326" style="padding: 20px;">
        <p style="color: #ffffff; font-size: 14px; text-align: center;">
          You received this email because you signed up on our website. If you
          did not sign up, please ignore this email.
        </p>
      </td>
    </tr>
    """
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