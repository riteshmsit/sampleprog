"""
odd program with functions
"""
def odd(x):
    if (x%2!=0):
    	return True
    else:
    	return False
    

def main():
    data = input()
    print(odd(int(data)))

if __name__== "__main__":
    main()
