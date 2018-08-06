"""
Program to calculate quadratic 
"""
def evalQuadratic(a, b, c, x):
    return a*(x**2)+b*x+c
def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	for x in range(len(data)):
		temp = str(data[x]).split('.')
		if(temp[1] == '0'):
			data[x] = int(float(str(data[x])))
		else:
			data[x] = data[x]
	print(evalQuadratic(data[0],data[1],data[2],data[3]))
main()
