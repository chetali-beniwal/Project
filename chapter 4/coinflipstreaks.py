import random
nos=0
l=[]
for a in range(10000):
    for b in range(1,101):
        l.append(random.randint(0,1))
    for c in range(1,95):
        if l[c]==l[c+1]==l[c+2]==l[c+3]==l[c+4]==l[c+5]:
            nos+=1
            break
    l=[]
print('Chance of streak: %s%%' % (nos / 100))