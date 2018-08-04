"""
Second assignment program
"""
S = input()
I = 0
A = len(S)
Q = ""
while I < A:
    if S[I] == '!' or S[I] == '@' or S[I] == '#' or S[I] == '$' or S[I] == '%' or S[I] == '^' or S[I] == '&' or S[I] == '*':
        Q = Q + " "
    else:
        Q = Q + S[I]
    I = I + 1
print(Q)