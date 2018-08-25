'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
	str_list = string.split(' ')
	my_dict = {}
	for i in range(len(str_list)):
		if '.' or ';' in str_list[i]:
			str_list[i] = str_list[i][:len(str_list[i]-1)]
		if str_list[i] not in my_dict:
			my_dict[str_list[i]] = 1
		else:
			my_dict[str_list[i]] += 1
	return my_dict


def main():
    lines = int(input())
    str_input = ""
    for i in range(lines):
    	str_input += input()
    a = print(tokenize(str_input))
if __name__ == '__main__':
    main()
