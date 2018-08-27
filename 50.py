def ispower(num):
   if(num==0):
      return false
   else:
      for i in range(num):
          i=2**i
          if(i==num):
               print("yes")
               break
      else:
          print("no")
m=int(input())
ispower(m)
