#!/usr/bin/env python

from sys import argv
#args = sys.argv

# remove empty lists
# create tuples (.zip?)
# from tuples create a dictionary.
# using a tuple as a key in a dictionary, and a list as the value.
    




def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    corp_dicto = {} # initalize empyt dictionary
    corpus_list = corpus.split() # splits single string into Words
    for i in range(len(corpus_list) - 2): 

        t = (corpus_list[i],corpus_list[i + 1]) ## this creates a tuple 
        print t

        corp_dicto[t] = corpus_list[i + 2] # this makes that tuple the dictionary key, the following word 
                                           # becomes the respective value to that key. 


    print corp_dicto    
    return corp_dicto

    pass

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""


    #pick a random starting tuple
    #random[key] + value
    #
    return "Here's some random text."
    pass

def main():

    f = open("austen.txt")
    input_text = f.read() # returns one long string -->goes to def make chains... 



    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()