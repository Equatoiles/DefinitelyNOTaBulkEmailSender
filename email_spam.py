import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Mailjet SMTP server configuration
smtp_server = "in-v3.mailjet.com"
smtp_port = 587  # TLS port
sender_email = "enter_email"  # Your email address
smtp_username = "enter_username"  # Your Mailjet SMTP username
smtp_password = "enter_password"  # Your Mailjet SMTP password

# List of recipient email addresses
recipient_list = ["DEIA@opm.gov"]

# Email subject and body content
subject = "Subject goes here"
body = "Body goes here" 
def send_bulk_email():
    try:
        # Connect to the Mailjet SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security

        # Login using your Mailjet SMTP credentials
        server.login(smtp_username, smtp_password)

        # Outer loop for sending emails multiple times
        for i in range(1):  # This will repeat sending i times, this number can be changed as needed
            print(f"Sending email batch {i+1}")

            # Loop through all the recipients and send emails
            for recipient_email in recipient_list:
                # Create the email message
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = recipient_email
                message['Subject'] = subject
                personalized_body = f"Hi {recipient_email.split('@')[0]},\n\n" + body

                # Attach the body to the email
                message.attach(MIMEText(personalized_body, 'plain'))

                # Send the email
                server.sendmail(sender_email, recipient_email, message.as_string())
                print(f"Email sent to {recipient_email} in batch {i+1}")

        # Quit the server once all emails are sent
        server.quit()

    except Exception as e:
        print(f"Error: {e}")

# Run the function to send the emails
send_bulk_email()
