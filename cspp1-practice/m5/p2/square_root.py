"""
square root approximation
"""
N = int(input())
E = 0.1
A = 0
A = int(A)
while (N - (A*A) > E) and A < N:
    if N - (A*A) > E:
        A = A+E
print(A)
