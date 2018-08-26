'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    h = sorted(dictionar.keys())
    for i in range(len(h)):
        if h[i] in dictionary:
            print(h[i],'-',int(len(dictionary[h[i]]) * '#'))
    return ''
def main():
    dictionar = eval(input())
    print(frequency_graph(dictionary))

if __name__ == '__main__':
    main()
