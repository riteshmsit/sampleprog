# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

"""
string problem
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    low = 0
    high = len(aStr) - 1
    if low <= high:
        mid = (low + high) // 2
        if aStr[mid] == char:
            return "True"
        elif aStr[mid] <= char:
            return isIn(char, aStr[mid + 1:])
        else:
            return isIn(char, aStr[:mid - 1])
    return "False"
   

def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))

main()
