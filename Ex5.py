# Creats random integer list
import random
import timeit
a = [random.randrange(0, 50, 1) for i in range(0, 51, 1)] # duplicates are possible
b = [random.randrange(0, 50, 1) for i in range(0, 51, 1)]# duplicates are possible
p=[]

c = random.sample(range(100), 5) # .sampler returns list of unique items of sequence.
print("C: \n{}".format(c)) 
d = random.sample(range(50), 5) # .sampler returns list of unique items of sequence.
print("D: \n{}".format(d))# good way to print a list


print('\n')


# Bad way to print a list
print( "a=[" , end="" )

for i in range(0,len(a)):
    print( " {}".format(a[i]) , end="" )

print( " ]" , end="" )

print('\n')

print( "b=[" , end="" )

for i in range(0,len(b)):
    print( " {}".format(b[i]) , end="" )

print( " ]" , end="" )

print('\n')
print('\n')


#Compering lits below


for i in range(0,len(a)):
    if a[i] in b  and (a[i] not in p):

         p.append(a[i])
        

for i in range(0,len(p)):
    print(p[i])        

 
