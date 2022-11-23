import math
#Imput
a = int(input("a = "))
b = int(input("b = "))
c = int(input ("c = "))

#Calculate
d = (b**2) - (4*a*c)
if d<0:
  print ("No Real Solutions " )
else:
  x1 = (-b + math.sqrt(d)) / (2*a)
  x2 = (-b - math.sqrt(d)) / (2*a)

#Display Soluation 
print(x1,x2)
