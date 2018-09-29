def fibanaci_sequance(x):
    b=[1,1]
    k=1
    if x==1:
        b.remove(b[-1])
        print("C: \n{}".format(b))
        return
    
    for i in range(0,x):
        b.append((b[k]+b[k-1]))
        k=k+1
		
    b.remove(b[-1])
    b.remove(b[-1])
    print("C: \n{}".format(b))

while(True):
    x=input("How many numbers in the sequance ?")
    fibanaci_sequance(int(x))


