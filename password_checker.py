import re

'''
atleast 8 characters long

contain any sort of letters, numbers and symbols

has to end with a number
'''

pattern = re.compile(r"[A-Za-z0-9$%#@&!]{8,}\d")

password = input('enter the password which should be atleast 8 character long and should end with a digit: ')

check = pattern.fullmatch(password)

if check:
    print('Password is valid ')

else:
    print('enter the valid password')