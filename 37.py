c=input()
l=list(map(int,c.split(' ')))
r=l[0]
s=l[1]
r=r^s
s=r^s
r=r^s
print(r,s)
