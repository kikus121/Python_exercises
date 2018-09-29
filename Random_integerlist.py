import random
import timeit

def random_integerlist(x):
    a = [random.randrange(0, x, 1) for i in range(0, x, 1)]
    print("A: \n{}".format(a))
    c = random.sample(range(1010), x) # .sampler returns list of unique items of sequence.
    print("C: \n{}".format(c))#C list seems more random

while(True):
    x=input("How many random integers ?")
    random_integerlist(int(x))

