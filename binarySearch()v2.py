for x in range(0,100):
    
    high=100
    low=0
    guess=(high+low)/2
    trys=0

    while(x!=guess):
        
        if x<guess:
            trys=trys+1
            high=guess
            guess=int((high+low)/2)
        elif x>guess:
            trys=trys+1
            low=guess
            guess=int((high+low)/2)
        else:
            break
    print("")
    print("For {}".format(x))
    print("It took {} trys".format(trys))
            
