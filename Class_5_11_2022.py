# #Function
# # functions are a block of code that will be executed when called



# def myFunction():
#     print("Hello")
#     print("Hi")
#     print("Bye")



# print(1)
# myFunction()

# print(2)
# print(3)
# print(4)
# myFunction()


# print(5)
# print(6)
# myFunction()

# print(7)
# myFunction()

def printFirstName(name, age):
    print(' my name is : ' + name + " My age is: " + age)

# arguments are data that are passed during the function calling
printFirstName('John' , '30')
printFirstName('Peter', '30')


#function either do something or return something
# create a function that prints sum of two numbers
# # 
# def printSum(num1, num2):
#     print(num1 + num2) 

def printSum(num1, num2):
    return num1 + num2
    print('')

print(printSum(10 , 20))
print(printSum(40, 20))
