from django.shortcuts import render
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.contrib import messages

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendemail(receiver_email, name, otp):
    sender_email = "projectcollege273@gmail.com"
    password = "agpp myat cyhd ovxo"  # Your App password

    # Create MIME message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "OTP Verification"

    # Email body
    html = f"""
    <html>
        <body>
            <p>Dear {name},</p>
            <p>Your Email Verification code is: <strong>{otp}</strong></p>
            <p>Please use this code to complete your email verification.</p>
            <p>Thanks and regards,<br>IdharBidder Auction</p>
        </body>
    </html>
    """
    message.attach(MIMEText(html, 'html'))  # Attach HTML content

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Log in to the server
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        server.quit()  # Quit the server connection
        print("Email sent successfully!")
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        return False




# def sendemail(to, name, otp):
#     sender = "IdharBidder Auction"
#     toemail = to
#     toname = name
#     fromemail = 'bhaskarbhuwan646@gmail.com'
#     subject = "OTP Verification"
#     message = "Dear "+ name +", Your Email Verification code is : "+str(otp)
#     configuration = sib_api_v3_sdk.Configuration()
#     configuration.api_key['api-key'] = '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'
#     api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
#     subject = subject
#     html_content = message
#     sender = {"name": sender, "email": fromemail}
#     to = [{"email": toemail, "name": toname}]
#     headers = {"Some-Custom-Name": "unique-id-1234"}
#     send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
#     try:
#         api_response = api_instance.send_transac_email(send_smtp_email)
#         pprint(api_response)
#         return True
#     except ApiException as e:
#         print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)