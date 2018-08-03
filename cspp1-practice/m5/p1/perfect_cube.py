GUESS = 1
N = int(input(""))
FLAG = 0
while GUESS<N+1:
    if GUESS**3==N:
        print(str(N) + " " + "is a perfect cube")
        FLAG = 1
        break
    GUESS = GUESS + 1
if(FLAG == 0):
    print(str(N) + " " + "is not a perfect cube")