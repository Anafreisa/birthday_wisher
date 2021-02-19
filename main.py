import datetime as dt
import smtplib
import random

my_email = EMAIL
password = PASSWORD
quotes_list = []
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as quotes:
    for line in quotes:
        quotes_list.append(line)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=EMAIL,
        msg=f"Subject:It's {days_of_week[day_of_week]}\n\n{random.choice(quotes_list)}"
    )
