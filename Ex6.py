while(True):
    string=input("Type a string:")
    x=1
    for i in range(0,int(len(string)/2)):
        if string[i]!=string[-(i+1)]:
              x=0
    if x==0:
         print('{} is not a palindrome'.format(string))
   

    else:
         print('{} is a palindrome'.format(string))
   





