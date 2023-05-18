#Integer

age = 17
players = 2
teams = 5

print(f"There are {players * teams} players with {age} years old.")


#Float

distance = 0.9
price = 9.99

print(f"I'm {distance} away from the market. I'm gonna buy a notebook for the price of ${price}")


#String

name = "Brandon"
humor = "hungry"
food = "apple"

print(f"{name} is {humor}, he want to eat an {food}.")


#Boolean

running = input("Is the code running?")

if running == "yes":
    print(True)
else: print (False)

#Typecasting

#explicit
name = "Mairton" #str
age = 17 #int
height = 1.6 #float
student = True #bool

age = float(age) #int to float
print (type(age))

student = str(student) #bool to str
print (type(student))

age = bool(age) #anything that it's not 0, it's true.
print(age)

#implicit

x = 2
y = 2.0

x= x / y

print(x) #it will turn into a float, the type casting can be converted when you perform certain operations on it. 