import re

email = input("Enter the email: ")

regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"

if re.search(regex, email):
    print("Valid Email")
else:
    print("Invalid Email")
