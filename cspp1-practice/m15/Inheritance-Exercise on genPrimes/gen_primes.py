#define the gen_primes function here
def genPrimes():
    number = 2
	while True:
		if prime(number_prime):
			yield number
		number += 1
def prime(number_prime):
	for value in range(2, number):
		if number % value == 0:
			return False
	return True

def main():
	data=raw_input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.next()
	    if(i%b==0):
	        print p
	
if __name__== "__main__":
	main()
