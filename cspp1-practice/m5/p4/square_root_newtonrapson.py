"""
Newton Raphson Method
"""
E = 0.01
A = int(input())
G = A/2.0
while abs(G*G - A) >= E:
    G = G - (((G**2) - A)/(2*G))
print(G)
