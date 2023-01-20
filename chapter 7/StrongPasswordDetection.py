import re
pswd=input("Enter password-")
char=re.compile(r'\w{8}')
u=re.compile(r'[A-Z]')
l=re.compile(r'[a-z]')
d=re.compile(r'[0-9]')
if char.findall(pswd)==[] or u.findall(pswd)==[] or l.findall(pswd)==[] or d.findall(pswd)==[]:
    print('Password is not strong.')
else:
    print('Password is strong.')