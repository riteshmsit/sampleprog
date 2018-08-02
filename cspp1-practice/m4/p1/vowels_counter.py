S = input("")
I = 0
L = len(S)
C = 0
while (I < L):
    if(S[I] == 'a' or S[I] == 'e' or S[I] == 'o' or S[I] == 'u' or S[I] == 'i'):
        C = C+1
    I = I+1
print(C)
