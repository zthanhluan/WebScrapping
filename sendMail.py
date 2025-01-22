# sendMail.py
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import certifi

def send_email(sender_email, receiver_email, password, subject, body):
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add the body of the email
    message.attach(MIMEText(body, "plain"))

    context = ssl.create_default_context(cafile=certifi.where())

    # Connect to Yahoo's SMTP server and send the email
    try:
        with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465, context=context) as server:
            server.login(sender_email, password)  # Login to the SMTP server
            server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")