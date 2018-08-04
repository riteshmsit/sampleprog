"""
Third program
"""
N = int(input())
I = 1
P = 1
if N < 0:
    N = abs(N)
    while N != 0:
        I = N % 10
        P = P * I
        N = N//10
    P = P * -1
    print(P)
    N = N * -1
if N > 0:
    while N != 0:
        I = N % 10
        P = P * I
        N = N // 10
    print(P)
    
