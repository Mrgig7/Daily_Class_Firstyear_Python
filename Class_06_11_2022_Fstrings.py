

# #.format(value1, value2, value3,......)
# # it formats a specific value and put them inside the placeholder

# # {} => placeholder

# text = "My name is {}, I am {} years old".format('John' , 20)

# print(text)

# text = "My name is {}, I am {} years old".format(20 , 'John')

# print(text)

# text = "My name is {name}, I am {age} years old".format(name ='John' ,age = 20)

# print(text)

# text = "My name is {name}, I am {age} years old".format(age = 20, name = 'John')

# print(text)

# text = "My name is {0}, I am {1} years old".format('John', 20)

# print(text)

# text = "My name is {1}, I am {0} years old".format(20 ,'John')

# print(text)

# Formatting types

# Insdie the placeholder you can write different formatting types to format the result

# some of the types are mentioned below
# :<
# :>
# :^
# :f
# :F

# :f => fix pint number format

# text = "The price of this product {:f} dollars"

# text = "The price of this product {:.2f} dollars"

# text = "The price of this product {:50.2f} dollars"

# print(text.format(25))

# numbers = [20.33, 40.45, 0.2345, 9.2356]

# for x in numbers:
#     print("{:.4f}".format(x))
#     print("{:10.2f}".format(x))

# :%

text = "I scored {:%} percentage in the test"

text = "I scored {:.0%} percentage in the test"

print(text.format(0.25)) 
