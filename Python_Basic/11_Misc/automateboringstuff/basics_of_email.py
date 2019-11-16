import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587) # 587 :TLS encryption
print(type(smtp_obj))

# ehlo() is the first step in SMTP and is important for establishing a connection to the server.
smtp_obj.ehlo()
smtp_obj.starttls() # Enables encryption for connection

user_name = input('Enter your user name: ')
password = input('Enter your password: ')
smtp_obj.login(user_name, password)

smtp_obj.sendmail(user_name, 'recipient@gmail.com',
                 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')

smtp_obj.quit()





