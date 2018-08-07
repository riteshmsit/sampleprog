
"""
sum of digits by recursion
"""
def sumofdigits(number_n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if number_n <= 0:
        return 0
    number_sum = number_n % 10
    return number_sum + sumofdigits(number_n//10)
def main():
    """
    main function
    """
    number_a = input()
    print(sumofdigits(int(number_a)))
if __name__ == "__main__":
    main()
