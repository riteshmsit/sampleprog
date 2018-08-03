S1 = input()
START = 0
END = 0
COUNT = 0
X = 0
T = X
FLAG = 0
while X < (len(S1)-1):
	Y = X + 1
	if(S1[X] > S1[Y]):
		FLAG = 1
	if Y == (len(S1) - 1):
			Y += 1
	if (X == (len(S1)-2) and COUNT < (Y-T)):
		FLAG = 1
	if FLAG == 1:
		if COUNT < (Y-T):
			START = T
			END = Y
			COUNT = END - START
		T = X + 1
		FLAG = 0
	X = X + 1
print(S1[START:END])
