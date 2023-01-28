import random,time,pyinputplus as pip
numberOfQuestions=10
correctAnswers=0
for questionNumber in range(1,numberOfQuestions+1):
    num1=random.randint(0, 9)
    num2=random.randint(0, 9)
    print('#%s: %s x %s = ' % (questionNumber, num1, num2))
    try:
        a=pip.inputInt(allowRegexes=['%s'],timeout=8,limit=3)
    except pip.TimeoutException:
        print('Out of time!')
        continue
    except pip.RetryLimitException:
        print('Out of tries!')
        continue
    if a==num1*num2:
        print('correct')
        correctAnswers+=1
    else:
        print('Incorrect!')
    time.sleep(1) 
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))