# if else conditions

#some imp logical conditions

# Equals x == y
# Not Equals x != y
# less than x < y
# greater than x > y
# less than equals x <= y
# greater than equals x >= y

# if(condition):
#   code if the condition is true

# x = 20
# y = 10

# if(x < y):
#     print("20 is greater than 10")

# if(x > y):
#     print("20 is greater than 10")
# else:# rest of the condition will be executed except the if part
#     print("x is equal to or less than y")


# if(20 < 10):
#     print("20 is greater than 10")

# student can only enter the collage  if student enter time is less than collage entry time
#if student coes at collage entrey time the student is allowed to enter the collage but with late remarks
collegeEntryTime = 9
studentEnterTime = 10

collegeEntryTime = 9
studentEnterTime = 8

collegeEntryTime = 9
studentEnterTime = 9

collegeEntryTime = 9
studentEnterTime = 13

if(studentEnterTime < collegeEntryTime):
    print("You can enter in the collage")
elif(studentEnterTime == collegeEntryTime):
    print("You can enter with late remarks")
elif (studentEnterTime > 12):
    print("allowed to enter in the collage with proper felicitation")
else:
    print("You can go back home")

# short hand if conditions

#if(10>5): print("10 isgreater than 5")

# short hand if-else condition
x= 20
y = 10

print("x") if x > y else print("y")

# and and or keywords. , logical operators

x = 10
y = 20
z = 30

if (x < y) and ( x < z):
    print("only if both are true")

x = 10
y = 20
z = 5

if (x < y) or ( x < z):
    print("if any one of the conditions is true")

#nested condition

age = 12

if (age < 18):
    print("age is less than 18")

    if (age < 10)
        print("The person is a minor. No entry is allowed")
    else:
        print("The person is a major. Entry is allowed")
else:
    print("Age is greater than or equal to 18")

