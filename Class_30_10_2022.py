# pass statement

x = 20
y = 30

if(x < y):
    pass
else:
    print("Hello")

#loop

#print 1 to 6

for i in range(1, 6):
    print(i)

# while loop (in while loop we can execute a set if statement s as long as the while condition is true)

while True:
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
    print(6)
    print(7)
    print(8)
    print(9)

x = 1

while x < 6:
    print(x)
    x = x + 1

#break statement

x = 1

while x < 6:
    print(x)
    if x == 4:
        break
    print(x)
    x = x + 1

#continue statement

x = 0
while x < 6: # this loopis running 5 times, 5 iterations
    x = x + 1
    if x == 3:
        continue # it will skip the current iteratio and move on to next
    print(x)

# else

x = 1

while x < 6:
    print(x)
    x = x + 1
else:
    print("x is now equalto or greater than 6")


#for loop (we use for loop to iteratte over a sequence , list, tuple, dictionary, string, etc.)

num = [10,20,30]

for a in num:
    print(a)

for x in 'hello':
    print(x)

num = [10,20,30]
result = 0
for a in num:
    result = result + a

print(result)

num = [10,20,30,40]

for a in num:
    print(a)
    if a == 20:
        break
    print(a)

num = [10,20,30,40]

for a in num:
    if a == 20:
        continue
    print(a)


#range

for x in range(6):
    print(x)

for x in range(2 ,10, 2):
    print(x)

for x in range(6):
    print(x)
else:
    print('x is out of range now')

for x in range(6):
    pass
print("Hello")