"""
First assignment program
"""
N = int(input())
I = 1
while I <= N: 
    if I % 3 == 0 and I % 5 == 0:
        print("Fizz")
        print("Buzz")
    elif I % 5 == 0 and I % 3 != 0:
        print("Buzz")
    elif I % 3 == 0 and I % 5 != 0:
        print("Fizz")
    else:
        print(I)
    I = I + 1
