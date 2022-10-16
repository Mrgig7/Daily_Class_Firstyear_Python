# Is not operator ( returns true if both variables are not the same object)


a = [10, 20]
b = [10, 20]

c = a

print(a is not c) # it returns false as it is the same object

print(b is not c) # it returns true as b is not the same objects as c

print(a != b) # it returns false as a is equal to b

# Membership Operators

# these operatorsare used to test sequence is present or not in an object

a = [10,20,30,40]

print(20 in a)

print(20 not in a)

#in ->it returns true if an object is present in a sequence
# not in -> it returns true if an object is not present in a sequence


#Bitwise Operators

# they are used to compare binary numbers

# & => AND => sets each bits are 1, it sets each bit to ONE (OR) MORE

# | => OR => if one of the two bits or any bits is 1, it sets to 1

# ^ => XDR => if only one of the two bits is 1, it sets each bit to 1

# ~ => NOT => inverts all the bits ( compliment operator, it returns one's compliment of the number)
# A = -(A+1) => Complement of number

# << => Zero fill left shift => The binary number is appeded with 0's at the end

# >> => Right shift => The right side of the bits are removed

x=10
y=7

print(x & y)

print(x | y)

print(x ^ y)

print(~(x & y))

print(x << y)

print(x >> y)