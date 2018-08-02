s=input("")
i=0
l=len(s)
c=0
while(i<l):
    if(s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='u' or s[i]=='i'):
        c=c+1
    i=i+1
print(c)
