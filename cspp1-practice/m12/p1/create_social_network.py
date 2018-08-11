'''
    Assignment-1 Create Social Network
'''

def create_social_network(st,lines,l):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    Adict={}
    b=st.split("follows ")
    l=[]
    l=l[str]
    for i in range(len(st)):
        if l[0] not in Adict:
            Adict[l[0]]= [l[1]]
        else:
            Adict[l[0]].append(l[1])
    return Adict


def main():
    '''
        handling testcase input and printing output
    '''
    st = ''
    lines = int(input())
    for i in range(lines):
        st += input()
        st+=' '
        i=i+1
    print(create_social_network(st,lines))

if __name__ == "__main__":
    main()
