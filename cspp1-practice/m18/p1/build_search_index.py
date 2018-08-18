
'''
    Tiny Search Engine - Part 1 - Build a search index
    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.
    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''

# helper function to load the stop words from a file
import re
def remove_stopwords(document_list):
    '''
    This function removes the stopwords
    '''
    stop_words = load_stopwords("stopwords.txt")
    temp_doclist = document_list[:]
    for each_word in temp_doclist:
        if each_word in stop_words:
            document_list.remove(each_word)
    return document_list

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(documents):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    for each_word in documents:
        document_list[each_word] = documents.split(" ")
    for each_word in documents:
        document_list[each_word] = documents.lower(" ")
        document_list[each_word] = re.sub("[^a-z]", "", document_list[each_word])
    return document_list
    

def build_search_index(documents):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    document_list = word_list(documents)
    updated_list = remove_stopwords(document_list)
    count = 0
    temp_updated_list = updated_list[:]
    for each_word in temp_updated_list:
        if each_word == '0' or each_word == '1' or each_word == '2'or each_word == '3'or each_word == '4'or each_word == '5':
            updated_list.split(each_word)
    for each_letter in updated_list:
        for d in each_letter:
            if updated_list[each_letter] in adict:
                updated_list[each_letter] = (d, 0)
            else:
                updated_list[each_letter][1] += 1
    return updated_list

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append("nextline")
        documents.append(input())
    # call print to display the search index
    print(print_search_index(build_search_index(documents)))