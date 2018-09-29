import random
from random import shuffle
import timeit
alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='01223456789'
symbol='!"£$%^&*()+=~#@.,?/\|{}]['
print(len(symbol))

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)
    

def index_alphabet():
    c = random.sample(range(51), 1) # .sampler returns list of unique items of sequence.
    return c[0]

def index_num():
    c = random.sample(range(9), 1) # .sampler returns list of unique items of sequence.
    return c[0]
    
def index_symbol():
    c = random.sample(range(24), 1) # .sampler returns list of unique items of sequence.
    return c[0]

while(True):
    string=''
    x=input('Press enter to generate passwoerd')
    for i in range(0,3):
        string=string+alphabet[index_alphabet()]
    for i in range(0,2):
        string=string+num[index_num()]
    for i in range(0,2):
        string=string+symbol[index_symbol()]
    
    print(shuffle_word(string))
