'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
	updated_string = re.sub("[a-z,A-Z,0,1,2,3,4,5,6,7,8,9]","",string)
	return updated_string
    

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
