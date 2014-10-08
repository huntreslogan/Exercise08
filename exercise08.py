#!/usr/bin/env python

import random
from sys import argv
from random import choice
punks = ['.', '?', '!']
#args = sys.argv

# remove empty lists
# create tuples (.zip?)
# from tuples create a dictionary.
# using a tuple as a key in a dictionary, and a list as the value.
    




def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains = {} # initalize empyt dictionary
    corpus_list = corpus.split() # splits single string into Words
    for i in range(len(corpus_list) - 2): 

        key = (corpus_list[i],corpus_list[i + 1]) ## this creates a tuple 
        #print key
        chains[key] = [corpus_list[i + 2]] # treat this third value as a LIST object.
        #print chains[key] # this makes that tuple the dictionary key, the following word 
                                           # becomes the respective value to that key. 
    #print chains    
    return chains

    

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    list_upper = []
    corp_keys = chains.keys()
    #print corp_keys
    for key in corp_keys:
        if key[0][0].isupper():
            list_upper.append(key)
    #print list_upper
    key = choice(list_upper)
    #print key

    sentence = [] # marko
    word1, word2 = key 
    sentence.append(word1)
    sentence.append(word2)



    #print sentence 
    while True:
        try:
            word3 = choice(chains[key])
            #print word3
        except KeyError:
            break
        sentence.append(word3)

        if word3[-1] in punks:
            break


        #print sentence
        key = (word2, word3)
        word1, word2 = key


        
    return ' '.join(sentence)
    #print sentence
    #     try: # try is a statement will default to the expect if it cant do what your asking
    #         third = choice(chains[key])
    #         print third
    #     except KeyError:
    #         break

 


    #pick a random starting tuple
    #random[key] + value
    #
     
    
def main():

    f = open("austen.txt")
    input_text = f.read() # returns one long string -->goes to def make chains... 

    #print "%r" %input_text

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()