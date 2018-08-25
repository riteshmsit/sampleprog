'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
	'''
	Program to print the input
	'''
    lines = int(input())
    str_input = ""
    for i in range(lines):
    	str_input += str(input()) + str('\n')
    print(str_input)
if __name__ == '__main__':
    main()