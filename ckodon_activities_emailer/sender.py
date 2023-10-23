"""Extract email addresses from all documents in the /data/activities directory and send emails to each address. """
from os import listdir
from email.message import EmailMessage
from smtplib import SMTP
from time import sleep
import json
import docx2txt
import re

# recipient addresses and their corresponding activities documents (as paths).
recipients = {}

# Obtain  path and recipients email address for each activities document
for filename in listdir("../data/activities/"):
    # define path to each activities document
    doc_path = "../data/activities/" + filename

    # extract all text from word document at path
    search_string = docx2txt.process(doc_path)

    # search for email in text
    pattern = "[A-Za-z0-9.+\-_]+@[A-Za-z0-9.+\-_]+[A-Za-z]{2,}"  # regular expression for email
    matches = re.search(pattern, search_string)
    email_address = matches.group(0)

    # add email address and path to `recipients` dictionary
    recipients[email_address] = doc_path



# define SMTP server credentials
credentials = json.loads(open("../data/credentials.json").read())
server_name = credentials["server_name"]
server_port = credentials["server_port"]
username = credentials["username"]
password = credentials["password"]

# instantiate SMTP client
smtp = SMTP(server_name, server_port)
smtp.starttls()
smtp.login(username, password)

# send email message for each recipient
send_counter = 0
for recipient_address, path in recipients.items():
    # create the email message
    msg = EmailMessage()
    msg["To"] =  "franciskohara@gmail.com" #recipient_address
    msg["Subject"] = "Ckodon Reviewed Activities Documents"
    msg_body = f"""Dear Ckodon Mentee,

Find attached your reviewed activities document.

Best,
The Ckodon Foundation Team.
"""
    msg.set_content(msg_body)

    with open(path, "rb") as attachment:
        attachment_name = path.split("/")[-1]
        attachment_data = attachment.read()
        msg.add_attachment(attachment_data, filename=attachment_name, maintype="application", subtype="msword")

    # send the email message
    try:
        smtp.send_message(msg)
        print("SENT")
        send_counter += 1


    except Exception as exception:
        print(exception)
        print(attachment_name)

    # delay for 1 minute every 40 emails
    if send_counter == 40:
        send_counter = 0
        print("WAITING 1 MINUTE")
        sleep(60)
