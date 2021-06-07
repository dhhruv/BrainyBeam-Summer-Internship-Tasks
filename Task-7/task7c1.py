import re

phonenumber = input("Enter Phone Number: ")

regex = "\d{3}\d{3}\d{4}"

if re.search(regex, phonenumber):
    print("Valid phone number")
else:
    print("Invalid phone number")
