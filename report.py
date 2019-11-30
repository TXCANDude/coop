import smtplib
from gpiozero import LED, Button

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' 
SMTP_PORT = 587 
GMAIL_USERNAME = 'email'
GMAIL_PASSWORD = 'yourPassword'  
 
class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
 
sender = Emailer()
sendTo = 'sendto'
emailSubject = "Chicken Coop Status Report"
emailContent = "This is a test of the Coop Monitoring"
 
#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
sender.sendmail(sendTo, emailSubject, emailContent)
