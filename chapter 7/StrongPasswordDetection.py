pswd=input('enter password-')
l,u,d=0,0,0
if len(pswd)==8:
    for a in pswd:
        if a.islower():
            l+=1
        elif a.isupper():
            u+=1
        elif a.isdigit():
            d+=1
    if u>0 and l>0 and d>0:
        print('strong password')
    elif u>0 and d>0:
        print("password must contain lowercase character")
    elif l>0 and d>0:
        print("password must contain uppercase character")
    elif u>0 and l>0:
        print('password must contain atleast one digit')
    else:
        print('not a strong password')
else:
    print('password must contain 8 characters')

                

