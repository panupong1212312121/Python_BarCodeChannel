#python sending email

import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "12345678"
subject = "Python email test"
body = "I wrote an email"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}
{body}

"""

sever = smtplib.SMTP("smtp.gamil.com",587)
sever.starttls()

sever.login(sender,password)
print("Logging in...")

sever.sendmail(sender,receiver,message)
print("Email has been sent")