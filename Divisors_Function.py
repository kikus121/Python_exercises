def divisors():
    x=input('Number plz (<100,000)')
    results=[]
    x=int(x)
    divisors=range(1,100001)

    for i in divisors:
         if x%divisors[i-1]==0:
            results.append(divisors[i-1])
              
      
  
        
    print('\n')
    print('\n')

    if len(results)==2:
        print('{} is a prime number:'.format(x))
    
    else:
        print('Divisors are for {} are:'.format(x))
    

    for i in range(0,len(results)):

        print('{}'.format(results[i]))

    print('There are {} divisors'.format(len(results)))
    
while(True):
    divisors()  
    
 

    

    
