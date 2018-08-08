def square(val):
    val=val**2
    return val
    
def apply_to_each(L, f):
    for i in range(len(L)):
        L[i]=f(L[i])
    print(L)
    
    
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, square)

if __name__== "__main__":
	main()
