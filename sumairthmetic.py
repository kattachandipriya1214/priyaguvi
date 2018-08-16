def sumOfAP( A,D,N) :
    sum = 0
    i = 0
    while i < n :
        sum = sum + A
        A=A+D
        i = i + 1
    return sum

N= int(input(""))
A = int(input(""))
D = int(input(""))
print (sumOfAP(A,D,N))
 
