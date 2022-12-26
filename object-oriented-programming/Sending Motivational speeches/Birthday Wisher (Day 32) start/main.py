# Sending motivational quotes from the quotes.txt file
import datetime as dt
import random
import smtplib

my_email = "joseph.olagabriel@gmail.com"
password = "123455"
receiver = "joseph.olagabriel@hotmail.com"
gmail = "smtp.gmail.com"


now = dt.datetime.now()
weekday = now.weekday()
# Note 0 signifies Monday
if weekday == 0:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    connection = smtplib.SMTP(gmail)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver,
        msg=f"subject: Monday Motivation\n\n{quote}")
    connection.close()





#To send an Email:

# import smtplib
#
#
# my_email = "joseph.olagabriel@gmail.com"
# password = "123455"
# receiver = "joseph.olagabriel@hotmail.com"
# gmail = "smtp.gmail.com"
#
#
# connection = smtplib.SMTP(gmail)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=receiver, msg="subject: SMTP TEST MAIL\n\nHello, this is a test email")
# connection.close()



# import datetime as dt
#
# now = dt.datetime.now()
# # PRINT ONLY THE YEAR
# year = now.year
# # PRINT ONLY THE MONTH
# month = now.month
#
# # To set your own date
# date_of_birth = dt.datetime(year=1986, month=February, day=20th, hour=4pm)
# print(date_of_birth)


