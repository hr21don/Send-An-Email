import smtplib #To connect to SMTP servers for sending email messages

#Your Email + Password
SENDER_EMAIL = 'XXXXXXX@gmail.com'
SENDER_PASSWORD = 'gadgAGAGAGAGGAAGAGAGAGAG'

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}' .format(subject, body) #subject line + body text
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server: #Using smtp_SSL function to open a secure connection to Gmail's SMTP server  on port 465
        server.login(SENDER_EMAIL, SENDER_PASSWORD) #login with the senders credentials
        server.sendmail(SENDER_EMAIL, receiver_email, message)#Using the sendmail method to send the formatted message string from the sender email address to the reciever.

        
