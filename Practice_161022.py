a = [52, 622]
b = [52, 622]

c = a

print(a is not c) 

print(b is not c) 

print(a != b) 

# Membership Operators


a = [899,924,322,750]

print(322 in a)

print(322 not in a)


#Bitwise Operators

# they are used to compare binary numbers

# & => AND => sets each bits are 1, it sets each bit to ONE (OR) MORE

# | => OR => if one of the two bits or any bits is 1, it sets to 1

# ^ => XDR => if only one of the two bits is 1, it sets each bit to 1

# ~ => NOT => inverts all the bits ( compliment operator, it returns one's compliment of the number)
# A = -(A+1) => Complement of number

# << => Zero fill left shift => The binary number is appeded with 0's at the end

# >> => Right shift => The right side of the bits are removed

x=193
y=85

print(x & y)

print(x | y)

print(x ^ y)

print(~(x & y))

print(x << y)

print(x >> y)