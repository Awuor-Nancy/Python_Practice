from operator import index
from re import A
from unicodedata import name


vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
#Accessing List Items Using Negative Indexing
print(vegetables[-4])
print(len(vegetables))
print(vegetables[-2])

# Unpacking List Items
list = ['item','item2','item3', 'item4', 'item5']
print(list[4:6]) # result =['item5']

print(list[1:6]) # result = ['item2', 'item3', 'item4', 'item5']
print("item2")

#Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[2:5])
print(fruits[:4])
print(fruits[4:])

#Modifying Lists /Adding items
fruits = ['banana', 'orange', 'mango', 'lemon']
x = fruits.append('Guava')
print(x)
a = fruits.append('pearl')
print(a)

#Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
'banana' in fruits
print(fruits)
'mango' in fruits
print(fruits)
'apple' in fruits
print(fruits)
print(len(fruits))
fruits.insert(3,'monera')
print(fruits)
fruits.insert(5,"guava")
print(fruits)
fruits.insert(6,'xoxo')
print(fruits)

#Removing Items from a List
list = ['apple','disc','cotton','girl']
w =list.remove('disc')
print(w)
list.pop()
print(list)
fruits.remove('xoxo')
print(fruits)
fruits.remove('monera')
print(fruits)

fruits.clear()
print(fruits)

#Copying a List
list.copy()
print (list)


#Joining Lists using + 
positive_numbers = [1, 2, 3, 4, 5]
code = [12,43,65,89,90]
pets = ['popsi','rex','lipi','jack']

c = positive_numbers + code + pets
print(c)

#Joining Lists using extend method()
list1 = ['item1', 'item2','item3']
list2 = ['rice','meat','yams','chicken']
list1.extend(list2)

#Counting Items in a List
list2 = ['rice','meat','yams','chicken']
list2.count('yams')
print(list2)

#Finding Index of an Item
list = ['item1', 'item2','drum','guitar']
name = (list.index('guitar'))
print(name)

#Reversing a List
items = ['item1', 'item2','drum','guitar']
y = items.reverse()
print(y)

#Sorting List Items
#Get the first item, the middle item and the last item of the list
name = ['n','a','n','c','v','i','d']
ind =name[0]
print(name)

friends = ["John,","Michael","Terry","Graham"]
#accesing items
print([1],friends[3])
print(friends[:4])
print(len(friends)) #finding length
print(friends.index("Terry"))
print(friends.count('m'))

#lists can contain any type of elements
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
#reverse
friends.sort(reverse = True)
print(cars)
cars.reverse()

#lowest number
print(min(friends))
print(max(cars))

#adding elements
friends.append("Erick")
friends.insert(1, "Jojo")

#add a list to a list
friends.extend(cars)
print(friends)

#Removing elements
friends.remove("Terry")
print(friends)

friends.pop()
print(friends)

#clear the list
# friends.clear()
# print(friends)

del friends[3]
print(friends)

#copying a list
new_list = friends.copy()
print(cars)


sales_wk1 = [7,3,42,67,3,9]
sales_wk2 = [12,4,26,10,7,45]
sales = []
new_data = input("enter a number")

sales_wk2.append(int(new_data))
sales.extend(sales_wk1)
sales.extend(sales_wk2)
sales.sort()

worst_day = sales[0] * 1.5
best_day = sales[-1] * 5

print(f"worst_day profit is{worst_day} ")
print(f"best day profit is {best_day}  ")
print(f"combined profit is{worst_day + worst_day} ")

#Splitting and joining strings
msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())

#splitting converts a list to a strng and
#join converts to a string by default

#loop through and print even nums
nums = [5,3,7,8,20,15,2,6,10,1]
x = len(nums)

for a in nums:
    if a % 2 ==0:
        del(nums)
        print(a)





 















