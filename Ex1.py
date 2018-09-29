age=input("How old are you ? ")
n=input('How many ?')
print(age)

import datetime
now=datetime.datetime.now()
x=int(now.year)
print(x)

hundred_in=(100-int(age))+x


    
for i in range(0,int(n)):
    
    print('\n')
    print('You will be onehundreth in {}'.format(hundred_in))
    print(i)
 
 
