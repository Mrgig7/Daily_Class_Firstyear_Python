#Sliciing


x = " Nice To Meet You"

print(x[:4])
print(x[:9])
print(x[0:15])

#Negative Index

print(x[-16])
print(x[-11:-8])

#Modify the string

print(x.lower()) 
print(x.upper()) 

#Split text

splittedText = x.split()

print(splittedText[3])

#Replace a string with another one

print(x.replace("T","D")) 
print(x.replace("You","Me")) 

x = 'Nice To Meet You'
y = 'How Are You'



z = x + " " + y
print(z)

#Boolens

#True 

print(bool('Nice'))
print(bool('77'))
print(bool(['Nitesh','Joseph']))

#False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#Random

print(77 > 52)
print(85 == 65)
print(750 < 82)
myList = [85,33,True,False,'Nitesh']
print(bool(myList))


#Python list

myList= [65,95,26,42,78,13,'nitesh','joseph']
print(myList)
print(myList[5])


print(len(myList))
print(type(myList))


#Using a list constructor

myList = list((85,64,33,13))
print(myList)


#Access list items

myList= [65,95,26,42,78,13,'nitesh','joseph']

print(myList[-1])
print(myList[1:6])
print(myList[-3:-1])

#Change, Add, Remove List Items

myList= [65,95,26,42,78,13,'nitesh','joseph']
myList[0] = 'Hi'
print(myList)

# Change a range of items in a list

myList[1:3] = [265456,54651]
print(myList)

#If you insert more items than you replace, then the new items then new items will add

myList[1:3] = [265456,54651,468545]
print(myList)

# Only need to insert new items

myList= [65,95,26,42,78,13,'nitesh','joseph']
myList.insert(2,77)
print(myList)

# (OR)

myList= [65,95,26,42,78,13,'nitesh','joseph']

myList.append(62132)
myList.append(5661)
myList.append('How')

print(myList)

#Extend

myList_1= [65,95,26,42,78,13,'nitesh','joseph']#current list
myList_2 = [50,60,70,80,'jeyaram','vijay']#another list


myList_1.extend(myList_2)
print(myList_1)



myList_2.extend(myList_1)
print(myList_2)

myList = [79,84,92,75]
myTuple =(542,8978)

myList.extend(myTuple)

print(myList)

#Remove

myList= [65,95,26,42,78,13,'nitesh','joseph']

myList.remove('nitesh')
print(myList)

#Using POP

myList.pop(3)
myList.pop()
print(myList)


#Using del word

myList= [65,95,26,42,78,13,'nitesh','joseph']

del myList[2]
print(myList)

#Using clear

myList= [65,95,26,42,78,13,'nitesh','joseph']

myList.clear()
print(myList)