A = int(input())
E = 0.01
L = 0.0
H = A
ANS = (H + L)/2.0
while abs(ANS**2 - A) >=E:
    if ANS**2 < A:
        L = ANS
    else:
        H = ANS
    ANS = (H + L)/2.0
print(ANS)


x = 25
epsilon = 0.01
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print(str(ans))