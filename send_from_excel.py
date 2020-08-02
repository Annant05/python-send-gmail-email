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
print('Excel Sheet to Dict:', email_dict_list)

success_list = []
failed_list = []

current_path = os.getcwd()
# file_path = f'{current_path}/attachments/{email_dict_list[0]["FilePath"]}'
# print  (file_path)
# print(current_path)
for email_info in email_dict_list:
    file_path = f'{current_path}/attachments/{email_info["FilePath"]}'
    status = send_email(email_info['Email'], email_info['Subject'], email_info['Message'], file_path)

    if status:
        success_list.append(email_info['Email'])
    else:
        failed_list.append(email_info['Email'])

    print(email_info)
    print("\n")

print("Success List", success_list)
print("Failed List", failed_list)
