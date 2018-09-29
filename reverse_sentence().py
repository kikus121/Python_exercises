def reverse_sentence(x):
    x=x.split()
    for i in range(1,len(x)):
        print(" {}".format(x[-i]),end="")
    print(" {}".format(x[0]))
        
    
    

while(True):
    x=input("Type a sentence")
    reverse_sentence(x)
 
