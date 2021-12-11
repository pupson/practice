##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import smtplib
import pandas
import random

g_email = '####@gmail.com'
g_smtp = 'smtp.gmail.com'
g_password ='#####'
y_email = '######@yahoo.com'
y_smtp = 'smtp.mail.yahoo.com'
y_password = '#####'

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today_tuple = (month, day)

def bday_greet():
    bday_greeting = ''
    data = pandas.read_csv('birthdays.csv')
    # bday_dict = bday_df.to_dict(orient='records')
    bday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
    return bday_dict

def quote_maker():
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt', 'r') as bday_letters:
        bday_letter = bday_letters.readlines()

    return bday_letter

#---------------------EMAIL OPS----------------#

bday_dict = bday_greet()

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    letter = ''.join(quote_maker())
    letter = letter.replace('[NAME]', bday_person['name'])
    letter = letter.replace('[SENDER]', 'Pomelo')
    email = bday_person['email']

    with smtplib.SMTP(y_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=y_email, password=y_password)
        connection.sendmail(
            from_addr=y_email,
            to_addrs=email,
            msg=f'Subject: Happy Caturday!\n\n{letter}')

    letter = ''.join(quote_maker())
    letter = letter.replace('[NAME]', bday_person['name'])
    letter = letter.replace('[SENDER]', 'Sarabi')
    email = bday_person['email']

    with smtplib.SMTP(g_smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=g_email, password=g_password)
        connection.sendmail(
            from_addr=g_email,
            to_addrs=email,
            msg=f'Subject: Happy Caturday!\n\n{letter}')

#--------------------------------------------------------#