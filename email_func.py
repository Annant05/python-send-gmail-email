from g_authentication import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import os

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


def send_email(to, subject, text_body, file_path):
    message = MIMEMultipart()

    # file = "hello.txt"

    message['to'] = to  # 'annantguptaneema@gmail.com'
    message['subject'] = subject  # 'You won'

    # emailMsg = text_body  # 'Test Email'

    msg = MIMEText(text_body)
    message.attach(msg)

    fp = open(file_path, 'rb')
    filename = os.path.basename(file_path)

    fmsg = MIMEApplication(fp.read(), _subtype="pdf")
    fp.close()

    fmsg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(fmsg)

    raw_string = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print(message)
        return True
    except e:
        print("error", e)
        return False

# send_email('annantguptaneema@gmail.com', 'attached file' , 'are you able to see the attached file') ,
