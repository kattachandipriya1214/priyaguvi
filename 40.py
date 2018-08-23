result=[]
n=int(input(""))
c,d=0,1
while d<=n:
    result.append(d)
    c,d=d,c+d
o=(str(result)[1:-1])
print(o.replace(',',' '))
