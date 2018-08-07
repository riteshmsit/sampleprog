# Exercise: Assignment-1
"""
factorial by recursion
"""
def factorial(value_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n
    '''
    if value_n in [0, 1]:
        return 1
    return value_n * factorial(value_n-1)
def main():
    """
    main function
    """
    value_a = int(input())
    print(factorial(int(value_a)))
if __name__ == "__main__":
    main()
