

#This is first class content that I studied
print("Hello World")
print ("My name is Harish"),  print ("I am learning Python")
print (100), print (3.14), print (2+3), #Python does the maths as well
print ("I am" ,12 ,"years old")

# This is a comment - Python ignores this line print("Comments help explain your code")
# Inline comment # you can use comments to disable code temporarily # print("This line will not run")


"""
below is the exercise for the first class of day 1 learning Python,
I am solving 4 questions here
"""
#First question is to write a program to print your school name and class
print ("my name is harish and I study in 8th grade")

#Print the number 1,2,3 each on a separate line using three print () statements.
print (1)
print (2)
print (3)

#what is the output of : print(5+3*2)?
print (5+4*3)

#print your full name , age and favourite subject using single print statement
"""
print("Harish Mittal",47,"Maths")


name = "Harish"
age = 47
height = 5.9
is_student = False

print (name)
print (age)
print(height)
print (is_student)


print (type(name), type(age), type(height), type(is_student))

score = 0
print("Start:", score)
score = 50
print("After level 1:", score)
print ("After level 2:", score + 30) # add 30 to current score print("After level 2:", score)

a, b, c = 10, 20, 30
print(a, b, c) # Assign same value to many variables x = y = z = 100
x=a
y=b
z=c
print(x, y, z)

name = input("Enter your name: ")
age = int(input("Enter your age: ")) # convert string to int!
print("Hello,", name, "You are", age, "years old")


below is the exercise for the second class of day 2 learning Python,
I am solving 4 questions here

# Create variables for your name, age, city, and whether you like cricket. Print all of them.
name = "Harish"
age = 47
city = "Gurugram"
like_cricket = True
print(name, age, city, like_cricket)

#Ask the user to enter two numbers and print their sum.

nbr1 = int(input("Enter first number: "))
nbr2 = int(input("Enter second number: "))
Sum = nbr1 + nbr2
print(Sum)

#What is the data type of: 3.0, 'True', True, 100? Check with type().

print(type(3.0))
print(type('True'))
print(type(True))
print(type(100))

#Write a program that swaps the values of two variables a=5 and b=10 without using a third variable.
#a=5
#b=10

#Create a variable called temperature = 98.6 and print: 'Your temperature is X degrees.'

temperature = 98.6
print("your temperature is ", temperature, "degrees")


a, b = 17, 5
print(a + b) # Addition → 22
print(a - b) # Subtraction → 12
print(a * b) # Multiplication → 85
print(a / b) # Division → 3.4 (always float)
print(a // b) # Floor division → 3 (drops decimal)
print(a % b) # Modulus → 2 (remainder)
print(a ** b) #Exponent → 1419857 (17 to the power 5)

x, y = 10, 20
print(x == y) # Equal to? → False
print(x != y) # Not equal to? → True
print(x < y) # Less than? → True
print(x > y) # Greater than? → False
print(x <= 10) # Less than or equal → True
print(x >= 20) # Greater or equal → False

age = 15
has_id = True
print(age >= 18 and has_id) # False (age fails) --> both are true
print(age >=18 or has_id) # True (has_id is True) --> either is true
print(not has_id) # False
can_enter = (age >= 13) and (has_id == True)
print("Can enter:",can_enter)

# Python follows BODMAS: Brackets, Orders, Division, # Multiplication, Addition, Subtraction
result1 = 2 + 3 * 4 # 14 (not 20)
result2 = (2 + 3) * 4 # 20 (brackets first)
result3 = 2 ** 3 + 1 # 9 (power first)
result4 = 10 / 2 + 3 * 2 # 11.0
print(result1,result2, result3, result4)


x = int(input("Enter number of apples you want to buy: "))
totalcost = x*5
print(totalcost)


print(5 > 3 and 10 < 8)
print( (2**8) - (100 // 3) + (55 % 7))
print(256-33+6)

s = "Python"
print(len(s)) # 6 characters
print(s[0]) # P (indexing starts at 0)
print(s[-1]) # n (negative index from end)
print(s[2:5]) # tho (slicing: index 2,3,4)
print(s[:3]) # Pyt (from start to 2)
print(s[3:]) # hon (from 3 to end)
print(s[::-1]) #nohtyP (reverse!)

msg = " Hello, India! "
print(msg.upper()) # " HELLO, INDIA! "
print(msg.lower()) # "hello, india! "
print(msg.center(20))
print(msg.strip()) # "Hello, India!" (removes spaces)
print(msg.replace("India", "World")) # " Hello, World! "
print(msg.count("l")) # 3
print(msg.find("India")) # 9 (index where it starts)
print(msg.startswith(" Hello")) #True
print(msg.split())

first = "Harish"
last = "Mittal"
full = first + " " + last
print(full) # Harish Mittal
line ="-" * 30
print(line) # ------------------------------ (30 dashes)

name = "Kiran"
marks = 95
subj = "Maths"
print(f"{name} has got {marks} in the subject {subj}")
print(f"Student name : {name}")
print(f"{name} has got {marks * 2} which is double the marks {name} got last year")
print(f"pi = {3.14159:.2f}")

sentence = "I love Python programming"
words = sentence.split()
reverse = words[::-1]
print(words) #['I', 'love', 'Python', 'programming']
print(reverse)
words2 = sentence.split(",")
print(words2) #['I love Python programming']
words3 = sentence.split("o")
print(words3) #['I l', 've Pyth', 'n pr', 'gramming']
print(len(words))

joined = " ".join(words)
print(joined)
joined2 = "-".join(words2)
print(joined2)
Joined3 = "o".join(words3)
print(Joined3)

sentence1 = "I love Python programming"
s="python"
print(s.split())
print(s.count("o"))

word4 = "programming"
print(word4.count("a"))
print(word4.count("i"))
print(word4.count("o"))
print(word4.count("u"))
print(word4.count("e"))

len = int(input("length of rectangle = "))
width = int(input("breadth of rectangle = "))
print(f"Area of rectangle is {len * width} square meters")

word5 = input("Enter a word: ")
reverse = word5[::-1]
print(f"Word {word5} is a Palindrome, this is {word5 == reverse}")

fruits = ["apple", "banana", "cherry", "mango", "grapes"]
print (fruits[1])
fruits.reverse()
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(1, "Guava")
print(fruits)
print(fruits.pop())
fruits.pop()
print(fruits)


marks = [85,92,78,95,88]
print(max(marks))
print(min(marks))
print(sum(marks))
print(sorted(marks))

matrix = [[1,3,5,7,8], ["hari", "pari", "dari", "bari", "nari"]]
print(matrix)
print(matrix[0])
print(matrix[1][2])

"""

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*3)
print(3 in a)

c=a.copy()
print(c)

secret = 42
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else: print("Correct! Well done!")

for i in range(1, 20):
    print(f"current value of i is {i}")
    if i == 7: break
print(f"value of {i} has reached breakpoint")


for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end="") # :3 = width of 3
print() # newline after each row # Output: # 1 2 3 4 5 # 2 4 6 8 10 # 3 6 9 12 15 ...etc.

x, y, z = (10, 20, 30)
print(x, y, z)

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print(days)