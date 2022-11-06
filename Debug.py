def printNumber(num):
    if num:
        return num + printNumber(num - 1)
    else:
        return 0

x = printNumber(10)
print(x)