from email.mime.multipart import MIMEMultipart  # mime --> multipurpose internet mai
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "vinothannc4@gmail.com"
message["to"] = "vinothanlearn4nc@gmail.com"
message["subject"] = "this mail send using python program"
body = template.substitute(name="Vinothan NC")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("photo.png").read_bytes()))  # --> to send image
# --> if the receiver has html support, it will show content in html otherwise it default show in plain text

# message.attach(MIMEText("here you have to send the html content", "html"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:  # smtp --> simple mail transfer protocol
    smtp.ehlo()  # communication between client and smtp server starts with hello message
    smtp.starttls()  # transport layer security
    smtp.login('vinothannc4@gmail.com', "evaxtuwpxczuivui")
    smtp.send_message(message)
    print("message is send")
