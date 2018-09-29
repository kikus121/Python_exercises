import random
import timeit

def random_integerlist(x):
    string=""
    a = [random.randrange(0, x, 1) for i in range(0, x, 1)]
    for i in range(0,4):
        string=string+str(a[i])
    return(string)  
print(" For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” ")    
number=str(random_integerlist(4))
print(number)

while True:

    guesses=0
    cow=0
    bull=0
    z=str(input("Guess a digit number"))
        
    if z==number:
          
          guesses=guesses+1
          print("Well done you won in {} guesses.".format(guesses))
          number=random_integerlist(4)
          print(number)
          
    else:
        guesses=guesses+1
        for i in range(0,4):
       

           if z[i] in number:
                bull=bull+1
          
           if z[i]==number[i]:
               bull=bull-1
               cow=cow+1
             
          
    print(" {} bulls {} cows.".format(bull,cow))      
          
            
          
   
       
            
            
