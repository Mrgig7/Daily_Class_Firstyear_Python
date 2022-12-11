import datetime

print(dir(datetime.datetime))
print(datetime.datetime.now())

currentDate = datetime.datetime.now()
print(currentDate) #time
print(currentDate.year) #year
print(currentDate.strftime("%A")) #day
print(currentDate.strftime("%a")) #day shortform
print(currentDate.strftime("%w")) #weekday number 0 to 6
print(currentDate.strftime("%B")) #month name
print(currentDate.strftime("%b")) #month shortform


