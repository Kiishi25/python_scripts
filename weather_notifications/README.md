# Weather Notification Script

This will set up and automate the process of fetching daily weather data from an API and sending email notifications with the weather forecast using Python.

## Step 1: Set Up

### 1. Create an account and get an API key

Use a weather service provider like [OpenWeatherMap](https://openweathermap.org/api). After signing up, you will get an API key.

### 2. Email Service and Credentials

We will use Gmail's SMTP server for sending emails. Ensure you have enabled "Less secure app access" or have an app-specific password.

## Step 2: Install Required Libraries

You will need the `requests` library to fetch data from the API and `smtplib` and `email` libraries to send emails. You can install `requests` using pip:

```sh
pip install requests

