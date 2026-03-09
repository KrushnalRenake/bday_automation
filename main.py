import pandas
import datetime as dt
import random
import smtplib

##################### Extra Hard Starting Project ######################

EMAIL = "Krushnalcop10@gmail.com"
PASSWORD = "afwqofi"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
print(now)

data = pandas.read_csv("C:\\Takeda\\Python\\Birthday Wisher_Day 32\\birthdays.csv")
bdays_dict = data.to_dict(orient="records")

for bday in bdays_dict:
    if f"{now.month}-{now.day}" == f"{bday["month"]}-{bday["day"]}":
        letter_num = random.randint(1,3)
        with open(f"C:\\Takeda\\Python\\Birthday Wisher_Day 32\\letter_templates\\letter_{letter_num}.txt", "r") as file:
            letter_content = file.read()
            new_content = letter_content.replace("[NAME]",bday["name"])
            print(new_content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr= EMAIL,
                to_addrs= bday["email"],
                msg=new_content
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

