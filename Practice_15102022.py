#Python Operators

#Arithematic Operators

print(154+5132) #addition
print(5135-1241) #subraction
print(26*99) #multiplication
print(1055/55) #division
print(5202%512) #modules(gives us remainder)
print(612**52) # exponential form (3*3)

print(1662//52) # floor division (7.5 but it still rounds the result to the nearest whole number)

print(552//552)

#Assignment Operators

a = 125 # =

a += 25 # same as a= a +5
print(a)

a = 125 
a -= 25# same as a= a-5
print(a)

a = 125 
a *= 25# same as a= a*5
print(a)

a = 125 
a /= 25# same as a= a/5
print(a)

a = 125
a %= 25 # same as a= a/5 ( remainder)
print(a)

a = 125
a //= 25 # same as floor division 

a = 125
a **= 25 # same as exponential form
print(a)

# Comparision operations

print(25 == 55) # equals to

print(55 != 96) #Not equal to

print(526 > 556) # greater than

print(22 < 411) # less than

print(852 >= 3222) # great than equal

print(52 <= 85) # less than equal

#Logical operators

x = 55

print(x < 5465 and x < 822)

print(x > 522 and x > 22)

print(x < 223 or x > 8652 )

print(x > 365 or x > 1)

print(not(x < 544 and x < 882)) # reverses the result for example if the result is true it will return false and vice versea

# Identity Operators 

a = [258, 999]
b = [258, 999]
c = a
c = b
c = b = a

a.remove(999)

print(a)
print(b)
print(c)

print(a is c) # it returns true if both variables are the same object pointing to the same memory

print(b is c)

