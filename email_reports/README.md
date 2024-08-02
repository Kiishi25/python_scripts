# Daily Email Report Automation

This is to set up and automate the process of sending daily email reports using Python. The steps include setting up your email service and credentials, writing the script, and scheduling the script to run daily.

## Step 1: Email Service and Credentials

For this example, we will use Gmail's SMTP server to send emails. Please follow these steps to configure your Gmail account:

1. **Enable "Less secure app access"**:
   - Go to your [Google Account](https://myaccount.google.com/).
   - Navigate to the "Security" tab.
   - Scroll down to "Less secure app access" and turn it on.

2. **Gmail Configuration**:
   - **SMTP server**: `smtp.gmail.com`
   - **SMTP port**: `587`
   - **Your email address**: `your_email@gmail.com`
   - **Your email password**: `your_password`