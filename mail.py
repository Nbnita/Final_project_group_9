import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender_email = "nabantaborkakoti@gmail.com"
rec_email = "nabanitaborkakati.riki@gmail.com"

password = input(str("Enter passrord:"))

message = MIMEMultipart()
message['From'] = sender_email
message['to'] = rec_email
message['Sub']= "hi"

body = "Body"
message.attach(MIMEText(body,'plain'))

filename ="attendence.csv"
attachment = open(filename,"rb")

p = MIMEBase('application','octet-stream')
p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition',"attachment; filename=%s" % filename)
message.attach(p)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email, password)
print("login email")
text = message.as_string()
server.send_message(message)
server.quit()
#server.sendmail(sender_email, rec_email, message)
#print("Email has been send to ", rec_email)