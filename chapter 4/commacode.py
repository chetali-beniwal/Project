l=[]
s=''
n=int(input('enter the size of list-'))
for a in range(1,n+1):
    b=input('enter element-')
    l.append(b)
for i in l:
    if l.index(i)==(len(l)-2):
        s=s+i+', and '
    else:
        s=s+i+', '
c=s[:len(s)-2]
print(c)
