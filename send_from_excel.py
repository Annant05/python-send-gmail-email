import pandas as pd
import os
from email_func import send_email

'''
Change these to your credentials and name
'''
# your_name = "Bill Butlicker"
# your_email = "william.m.butlicker@gmail.com"

# Read the file
email_excel = pd.read_excel("EmailList.xlsx",
                            usecols=['Name', 'Email', 'Subject', 'Message', 'FilePath'])

# print(email_excel)
email_dict_list = email_excel.to_dict(orient='records')
print('Excel Sheet to Dict:',email_dict_list )

success_list = []
failed_list = [] 


current_path = os.getcwd()
# file_path = f'{current_path}/attachments/{email_dict_list[0]["FilePath"]}'
# print  (file_path)
# print(current_path)
for email_info in email_dict_list:
    file_path = f'{current_path}/attachments/{email_info["FilePath"]}'
    status = send_email(email_info['Email'],email_info['Subject'],email_info['Message'], file_path)

    if status:
        success_list.append(email_info['Email'])
    else:
        failed_list.append(email_info['Email'])

    print(email_info)
    print("\n")

print("Success List", success_list)
print("Failed List", failed_list)


# print(email_excel['EmpName'].tolist())

# email_list = {}
# all_names = email_list['Name']
# all_emails = email_list['Email']
# all_subjects = email_list['Subject']
# all_messages = email_list['Message']
# all_Paths = email_list['FilePath']

# print(all_names)
# print(all_emails)
# print(all_subjects)
# print(all_messages)
# print(all_Paths)


# for elem in email_list:
#     print(elem)
#     print(elem['Name'])
#     print(elem['Email'])
#     print(elem['Subject'])
#     print(elem['Message'])

# Get all the Names, Email Addreses, Subjects and Messages
# all_names = email_list['Name']
# all_emails = email_list['Email']
# all_subjects = email_list['Subject']
# all_messages = email_list['Message']
# all_Paths = email_list['FilePath']

# Loop through the emails
# for idx in range(len(all_emails)):

#     # Get each records name, email, subject and message
#     name = all_names[idx]
#     email = all_emails[idx]
#     subject = all_subjects[idx]
#     message = all_messages[idx]

#     # Create the email to send
#     full_email = ("From: {0} <{1}>\n"
#                   "To: {2} <{3}>\n"
#                   "Subject: {4}\n\n"
#                   "{5}"
#                   .format(your_name, your_email, name, email, subject, message))

#     # In the email field, you can add multiple other emails if you want
#     # all of them to receive the same text
#     try:
#         server.sendmail(your_email, [email], full_email)
#         print('Email to {} successfully sent!\n\n'.format(email))
#     except Exception as e:
#         print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))

# # Close the smtp server
# server.close()
