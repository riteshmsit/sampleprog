"""
Program to calculate square of a number
"""
def square(N):
    return N*N
def main():
    N = float(input())
    T = str(N).split('.')
    if T[1] == '0':
        print(int(square(N)))
    else:
        print(square(N))
main()
