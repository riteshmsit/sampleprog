S = input()
M = len(S)
B = "bob"
N = len(B)
I = 0
C = 0
while I <= M-N+1:
    J = I
    K = 1
    C1 = S[J:J+3]
    C2 = B
    if C1 == C2:
        C = C+1
    I = I+1
print(C)
