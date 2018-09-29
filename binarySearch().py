x=int(input("Type number beetween 0 & 100"))
high=100
low=0
guess=int((high+low)/2)
trys=0


responce=input("Is the number {} ?".format(guess))

if responce=="y":
        trys=trys+1
        print("It took me {} trys to get the right number".format(trys))



while(guess!=x):
    responce=input("Is the number High(h) or Low(l)")

    if responce=="h":
        trys=trys+1
        high=guess
        guess=int((high+low)/2)

    elif responce=="l":
        trys=trys+1
        low=guess
        guess=int((high+low)/2)

    responce=input("Is the number {} ?".format(guess))


print("It took me {} trys to get the right number".format(trys))
