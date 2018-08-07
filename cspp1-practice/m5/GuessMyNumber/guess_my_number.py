
num = input("please think of a number between 1 to 100 and click enter")
	print(" enter h if the given number is greater than your number , l if the given less tahn your number, else c then if it equals to your number")
	print("is your  number 50?")
	low = 0
	high = 100
	mid = ((low+high)//2)
	while True:
		r = input("Enter your response :")
		if r == 'h':
			high = mid
		elif r == 'l':
			low = mid
		elif r == 'c':
			break
		mid = ((low+high)//2)
		print(" is your number",mid)
	print("your number is :",mid)
