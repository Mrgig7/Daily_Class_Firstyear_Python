#arbitary arguments

# def printSum(a , b ):
#     print(a + b)

# printSum(10,20,30)## Shows error as only 2 arguments are given 



# def printName(*name):
#     print(name)

# printName('john','peter','abc')
# print(type(printName))

# def printName(*name):
#     # print(name[0])

#     for x in name:
#         print(x)

# printName('john','peter','abc')
# printName('john','peter')


# #Keyword arguments

# def printNumbers(num2,num1,num3):
#     print(num2)

# printNumbers(2,10,20)

# printNumbers(num1 = 2, num2 = 10, num3 = 20)

# arbitrary keyword arguments

# def printNumbers(**num):
#     print(num["num2"])

# printNumbers(num1 = 2, num2 = 10, num3 = 20) # data type - dictionary
# printNumbers(num1 = 0, num2 = 40)

# default parameter values

def printNumbers(num1, num2 = 10):
    print(num1, num2)

printNumbers(10 , 20)
printNumbers(17)

# you can pass string, number, list, tuple etc 

def myFunc(nums):
    # print(nums)
    for x in nums:
        print(x)

nums = [10,20,30]
myFunc(nums)