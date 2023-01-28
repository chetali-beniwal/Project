import pyinputplus as pip
p={'wheat':12,'white':15,'sour dough':15,'chicken':25,'turkey':28,'ham':30,'tofu':33,'cheddar':10,'swiss':15,'mozzarella':20,'mayo':5,'mustard':10,'lettuce':12,'tomato':10}
for k,v in p.items():
    print(k,v,sep=':')
bread=pip.inputMenu(['wheat','white','sourdough'],'Which type of bread-\n')
meat=pip.inputMenu(['chicken','turkey','ham','tofu'],'Which type of meat-\n')
cheese=pip.inputYesNo('Do you want cheese-')
if cheese=='yes':
    ct=pip.inputMenu(['cheddar','swiss','mozzarella'],'Which type of cheese-\n')
mayo=pip.inputYesNo('Do you want mayo?\n')
mustard=pip.inputYesNo('Do you want mustard?\n')
lettuce=pip.inputYesNo('Do you want lettuce?\n')
tomato=pip.inputYesNo('Do you want tomato?\n')
sand=pip.inputInt('Enter no. of sandwiches you want to order-',min=1)
a,b,c,d,e,f,g=0,0,0,0,0,0,0
if bread=='wheat':
    a+=12
elif bread=='white':
    a+=15
elif bread=='sour dough':
    a+=15
if meat=='chicken':
    b+=25
elif meat=='turkey':
    b+=28
elif meat=='ham':
    b+=30
elif meat=='tofu':
    b+=33
if cheese=='yes':
    if ct=='cheddar':
        c+=10
    elif ct=='swiss':
        c+=15
    elif ct=='mozzarella':
        c+=20
if mayo=='yes':
    d=5
if mustard=='yes':
    e=10
if lettuce=='yes':
    f=12
if tomato=='yes':
    g=10
price=(a+b+c+d+e+f+g)*sand
print('Your total price is:',price)