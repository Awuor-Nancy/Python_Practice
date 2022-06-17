
num1 = 20
num2 = 12

sum = num1 + num2
print(sum)
diff = num1 - num2
print(diff)
prod = num1 *  num2
print(prod)
mod = num1 % num2
print(mod)
result = num1 // num2
print(result)
expo = num1 ** num2
print(expo)
div = num1 / num2
print(div)

  #calculate the area of a circle
radius = 10
area_circle = 3.142 * radius**2
print(area_circle)

def circumference():
    radius = 15
    circumference = 2*3.142 *radius **2
    print(circumference)
    


#Area of a triangle
length = 10
width = 12
area = length * width
print(area)

#calculate weight of an object
mass = 30
gravity = 9.81
weight = mass * gravity
print(weight)

#calculate density of a liquid
mass = 20
volume = 2.345
density = mass/volume
print(density)

#triangle
def area(b,h):
    side_b= 10
    side_h = 5
    front = input("enter sides")
    g = side_b * side_h
    print(g)

area(2,5)   

#perimeter
def perimeter(a,b,c):
    perimeter = a+ b+ c
    print(perimeter)

    perimeter(3,5,2)
    
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
name = "Python"
type = "dragon"
print(len(name) != len(type))
print("on" in ("Python") and "on" in ("dragon")) 

#There is no 'on' in both dragon and python
print("on" not in("python")) and "on" not in ("dragon")

#Use in operator to check if jargon is in the sentence.
word = "I hope this course is not full of jargon."
print("on" in word)

#Find the length of the text python and convert the value to float and convert it to string
x = "Python"
print(float(len(str(x))))
print((x))

#Even numbers are divisible by 2 and the remainder is zero,check
def evens():
    for x in range(1,20):
        if x %2==0:
            print(x)
evens()  

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

#Check if type of '10' is equal to type of 10
a = '10'
b = 10
print(10 =='10')

#Check if int('9.8') is equal to 10
c = '9.8'
d = 10
print(c == d)

#Write a script that prompts the user to enter hours and 
# rate per hour. Calculate pay of the person?
def pay (hours,rate):
    amount = input("Enter amount")
    earning = hours * rate
    return amount

pay(15,30)





 






   




