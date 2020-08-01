from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

import os
import mimetypes

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']
 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
 
def send_email(to,subject,text_body):
  message = MIMEMultipart()
  
  file = "hello.txt"

  message['to'] =    to #'annantguptaneema@gmail.com'
  message['subject'] = subject #'You won'

  emailMsg =   text_body  # 'Test Email' 
    
  msg = MIMEText(emailMsg)
  message.attach(msg)


  content_type, encoding = mimetypes.guess_type(file)

  if content_type is None or encoding is not None:
    content_type = 'application/octet-stream'
  
  main_type, sub_type = content_type.split('/', 1)
  
  fp = open(file, 'rb')
  msg = MIMEBase(main_type, sub_type)
  msg.set_payload(fp.read())
  fp.close()
  filename = os.path.basename(file)
  msg.add_header('Content-Disposition', 'attachment', filename=filename)
  message.attach(msg)

  # message.attach(MIMEText(emailMsg, 'plain'))
  raw_string = base64.urlsafe_b64encode(message.as_bytes()).decode()
  
  message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
  print(message)


send_email('annantguptaneema@gmail.com', 'attached file' , 'are you able to see the attached file')