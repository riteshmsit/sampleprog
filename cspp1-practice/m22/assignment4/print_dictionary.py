'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    a = sorted(dictionary.keys())
    for i in range(len(a)):
    	if a[i] in dictionary:
    		return(a[i],'-',dictionary[a[i]])

def main():
    dictionary = eval(input())
    print(print_dictionary(dictionary))

if __name__ == '__main__':
    main()
