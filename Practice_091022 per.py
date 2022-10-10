# Modify Strings in python using set of built in methods

#upper case 

# x = 'Hi everyone'

# print(x.upper())
# print(x.lower()) #lowercase
#remove whitespaces

# x =  "   Lets study python"
# print(x.strip())

#replace

# x = 'Hello World'
# print(x.replace('H','A'))

#splitting a string

#x = 'Hello World'
#print(x.split())


#x = 'Hello World'
#y =  x.split()
#print(y[1])
# String concatenation

#x = "Hello"
#y = "World"

#z = x + " " + y
#print(z)



#slice a string

#you can return a range of characters by using slice

#="Hello World"

#x[startIndex : endIndex] but not include end index
#print(x[2:5])

# print(x[:5]) #slice from the start
# print(x[2:]) #slice till end

#Negative Index

#print(x[-11])

#print(x[-6:-3])

#modify the string

#x= "We Are stuyding python"

#print(x.lower()) #lowercase

#print(x.upper()) #uppercase

#x= "Hello World"

#splittedText = x.split()

#print(splittedText[1])

#x= "My Name Is John"

#splittedText = x.split()

#print(splittedText[2])

#replace a string with another one

#x='Hello World'
#print(x.replace("e","A")) 

#x = 'Hello'
#y = 'World'

#z = x + "   " + y
#print(z)

#Booleans

# True or False bool

#print(20 > 11)

#print(20 == 9)
#print(20 < 9)

#bool(expression) will return either true or false

#print(bool("Hello"))

#print(bool(20))

# In which case values are true

#Almost any kind of value will result in true, if it has some content
# any string passes is true except empty string
# any namber passes is true. except 0
# Any list, tuple, dictionary willl result in true except the empty ones

# print(bool('Hello'))
# print(bool('20'))
# print(bool(['john','peter']))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

#Python list

# list are used to store multiple items of either same or different data types into a single variable

#Ordered collection -> items are in defined order
#changable -> add, remove items from the list
#allow duplicates -> 

# myList= [10,20,30,40,40,50,'john','peter']
# print(myList)
# print(myList[4])

# myList = [10,20,True,False,'john']
# print(len(myList))
# print(type(myList))

# myList=[]

# #using a list constructor

# myList = list((10,20,30,40))

# print(myList)

#access list items

# myList = [10,20,True,False,'John']
# #print(myList[-3])

# print(myList[2:5])

# print(myList[-4:-1])

#change, add, remove list items

# my_list = [10,20,30,40,50]
# #my_list[0] = 300 #changing the value of items based on index
# # print(my_list)



# # change a range of items in a list

# my_list[1:3] = [200,300]
# print(my_list)

#if you insert more items than you replace, then the new items 




# my_list = [10,20,30,40]

# my_list[1:2] = [200,300]
# print(my_list)

# only need to insert new items

# my_list = [10,20,30,40]

# my_list.insert(2,500)

# print(my_list)


# my_list = [10,20,30,40]

# my_list.append(50)
# my_list.append(60)
# my_list.append(70)

# print(my_list)

#extend()
# to add the elements rom another list to current list we use ths function
#extend methios can append or add any kind of iterable objest (tuple,sets, dictonary)
# myList1 = [10,20,30,40]#current list
# myList2 = [50,60,70,80]#another list


# myList1.extend(myList2)
# print(myList1)

# myList2.extend(myList1)
# print(myList2)

# myList = [ 10,20,30]
# myTuple =(40, 50)

# myList.extend(myTuple)

# print(myList)

# myList = ['apples','oranges','banana']

# myList.remove('banana')

# print(myList)

#remove an item by specifying its index
#pop()

# myList = ['apples','oranges','banana']
# myList.pop()# if ntg is mentioned then last element will be removed
# print(myList)

# del word

# myList = ['apples','oranges','banana']
# del myList[2]
# del myList[]#it will erase the complete list
# print(myList)

# myList,clear()

# print(myList)




