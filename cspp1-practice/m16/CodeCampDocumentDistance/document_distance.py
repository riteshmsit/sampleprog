'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1_list=dict1.split(" ")
    dict2_list=dict2.split(" ")
    for i in dict1:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    for j in dict2:
        if j in dict2:
            dict2[j]+=1
        else:
            dict2[j]=1

    Numerator = sum(2 * 2, 2 * 2, 1 * 1, 1 * 1, 1 * 0, 1 * 0, 0 * 1, 0 * 1)
Denominator = sqrt(sum(2^2, 2^2, 1^2, 1^2, 1^2, 1^2, 0^2, 0^2)) * sqrt(sum(2^2, 2^2, 1^2, 1^2,
1^2, 1^2, 0^2, 0^2))

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
