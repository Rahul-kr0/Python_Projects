# A RegEx, or Regular Expression,
# is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Email validator using regex
# a-z
#0-9
# . _ 1 time
# @ 1 time
# . 2,3

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your email: ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email ")
