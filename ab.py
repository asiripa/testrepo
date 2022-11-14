s=int(input())
a=0
for i in range(3):
    if s%(10**(i+1))==1:
        a=a+1
        s=s-10**i
print(a)