'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	h_fr = sorted(dictionary.keys())
    for i in range(len(h_fr)):
    	if h_fr[i] in dictionary:
    		b = ''
    		count = len(dictionary(h_fr[i]))
    		for i in count:
    			b += '#'
    	print(h_fr[i],b,dictionary[h_fr[i]])
    return ''
def main():
    dictionary = eval(input())
    print(frequency_graph(dictionary))

if __name__ == '__main__':
    main()
