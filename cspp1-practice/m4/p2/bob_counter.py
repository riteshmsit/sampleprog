s=input()
m=len(s)
b="bob"
n=len(b)
i=0
c=0
while (i<=m-n+1):
    j=i
    k=1
    c1=s[j:j+3]
    c2=b
    if(c1==c2):
        c=c+1
    i=i+1
print(c)
