# pyhton operators



#Arithematic Operators

print(10+20) #addition
print(20-10) #subraction
print(10*20) #multiplication
print(10/20) #division
print(20%10) #modules(gives us remainder)
print(3**2) # exponential form (3*3)

print(15//2) # floor division (7.5 but it still rounds the result to the nearest whole number)

print(15//4)


#Assignment Operators

a = 20 # =

a += 5 # same as a= a +5
print(a)

a = 20 
a -= 5# same as a= a-5
print(a)

a = 20 
a *= 5# same as a= a*5
print(a)

a = 20 
a /= 5# same as a= a/5

a = 20 
print(a)

a = 20 
a %= 5 # same as a= a/5 ( remainder)
print(a)

a = 20 
a //= 3
print(a)


a **= 2
print(a)

# Comparision operations

print(3 == 4) # equals to

print(3 != 4) #Not equal to

print(3 > 4) # greater than

print(3 < 4) # less than

print(3 >= 4) # great than equal

print(3 <= 4) # less than equal

#Logical operators

x = 2

print(x < 5 and x < 8)

print(x > 5 and x > 8)

print(x < 5 or x > 8 )

print(x > 3 or x > 10)

print(not(x < 5 and x < 8)) # reverses the result for example if the result is true it will return false and vice versea

# Identity Operators 

a = [10, 20]
b = [10, 20]
c = a
c = b
c = b = a

a.remove(20)

print(a)
print(b)
print(c)

print(a is c) # it returns true if both variables are the same object pointing to the same memory

print(b is c)

