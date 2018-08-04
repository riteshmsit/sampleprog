"""
Second assignment program
"""
S = input()
I = 0
A = len(S)
while I <= A:
    if S[I] == '!' or S[I] == '@' or S[I] == '#' or S[I] == '$' or S[I] == '%' or S[I] == '^' or S[I] == '&' or S[I] == '*':
        print(" ")
    else:
        print(S[I])
    I = I + 1