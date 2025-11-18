import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

YOUR_GOOGLE_EMAIL = os.getenv(
    "GMAIL_USERNAME"
)  # The email you setup to send the email using app password
YOUR_GOOGLE_EMAIL_APP_PASSWORD = os.getenv(
    "GMAIL_APP_PW"
)  # The app password you generated


def generate_email_message(email_body):
    """
    Generates the email message to be sent."""

    message = MIMEMultipart("alternative")
    message["Subject"] = "Tableau Alert"
    message["From"] = YOUR_GOOGLE_EMAIL
    message["To"] = YOUR_GOOGLE_EMAIL

    # Create the plain-text and HTML version of your message
    text = "Tableau Alert - Please view this email in an HTML-compatible email viewer!"
    html = email_body

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    return message


def attach_pdf_to_email(message, pdf_bytes, pdf_filename):
    """
    Attaches a PDF file to the email message.
    """

    part = MIMEApplication(pdf_bytes, _subtype="pdf")
    part.add_header(
        "Content-Disposition",
        f"attachment; filename={pdf_filename}",
    )
    message.attach(part)


def send_email(message):
    """
    Sends the email message via SMTP server.
    """

    smtpserver = smtplib.SMTP(os.getenv("GMAIL_SERVER"), os.getenv("GMAIL_PORT"))
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)

    # Test send mail
    sent_from = YOUR_GOOGLE_EMAIL
    sent_to = sent_from  #  Send it to self (as test)
    smtpserver.sendmail(sent_from, sent_to, message.as_string())

    # Close the connection
    smtpserver.close()

    return "Email sent successfully!"
