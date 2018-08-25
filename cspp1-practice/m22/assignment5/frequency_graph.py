'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	h = sorted(dictionary.keys())
    for i in range(len(h)):
    	b = ''
    	if h[i] in dictionary:
    		count = dictionary(h[i])
    		for i in count:
    			b += '#'
    	print(h[i],'-',b)
    return ''
def main():
    dictionary = eval(input())
    print(frequency_graph(dictionary))

if __name__ == '__main__':
    main()
