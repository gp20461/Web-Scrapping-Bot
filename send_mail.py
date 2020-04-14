'''
Sending Email through SMTPLIB......

import smtplib

sender_id = 'gp20461@gmail.com'
receiver_id = 'gp20461@gmail.com'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_id,'atbgikmyqyaecsdg')

message = "kem cho"
server.sendmail(sender_id,receiver_id,message)

server.quit()
'''

#Sending text mail through Email module

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    sender_id = 'gp20461@gmail.com'
    receiver_id = 'gp20461@gmail.com'
    subject = 'Finance Stock Report'

    msg = MIMEMultipart()

    # Header 
    msg['From'] = sender_id
    msg['To'] = receiver_id
    msg['subject'] = subject

    # Body
    body = "<b>Today's Finance Report Attached</b>"

    # File
    msg.attach(MIMEText(body,'html'))
    my_file = open(filename,'rb')

    # Code for sending attachment through Email
    part = MIMEBase('application','octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename = '+filename)
    msg.attach(part)


    message = msg.as_string()



    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_id,'atbgikmyqyaecsdg')


    server.sendmail(sender_id,receiver_id,message)

    server.quit() 