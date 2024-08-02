import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'

# Function to create the email content
def create_email_content():
    # Replace with your data collection logic
    report_data = "This is your daily report data."

    # Create email content
    email_content = f"""
    <html>
    <body>
        <h1>Daily Report for {datetime.now().strftime('%Y-%m-%d')}</h1>
        <p>{report_data}</p>
    </body>
    </html>
    """
    return email_content

# Function to send email
def send_email(subject, content, to_address):
    # Create a MIME object
    message = MIMEMultipart()
    message['From'] = EMAIL_ADDRESS
    message['To'] = to_address
    message['Subject'] = subject

    # Attach the HTML content
    message.attach(MIMEText(content, 'html'))

    # Send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_address, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Main function to run the script
if __name__ == "__main__":
    email_subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    email_content = create_email_content()
    recipient_email = "recipient_email@example.com"
    send_email(email_subject, email_content, recipient_email)