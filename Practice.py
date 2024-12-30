var = 1
var1 = 2
var_one = 3
var4= 4
var_1 = 1
var_11 = 2
var_ONE = 3
Name= "Yasir"
Age= 24
City= "Srinagar"
'''In Python, constants are typically represented using uppercase letters to distinguish them from regular variables.
 Here’s how you can define constants for the value of pi and the gravitational constant"""
Define constants'''  # ''' is used to write multi line comments
PI = 3.14159  # Approximate value of pi
GRAVITATIONAL_CONSTANT = 9.8  # Value in m/s² for Earth's gravity

# Use the constants in calculations
circle_radius = 5
circle_area = PI * (circle_radius ** 2)

print(f"The area of a circle with radius {circle_radius} is {circle_area}")
print(f"The gravitational constant on Earth is {GRAVITATIONAL_CONSTANT} m/s²") # this one is new,f before the string:Marks it as an f-string.{GRAVITATIONAL_CONSTANT}:Inserts the value of the variable GRAVITATIONAL_CONSTANT into the string.
# Correct usage of % formatting
GRAVITATIONAL_CONSTANT = 9.8
print("The gravitational constant on Earth is %f m/s²" % GRAVITATIONAL_CONSTANT) # This one i learned already
var10, var22 , var33 = 100, 200 , 300          #ways to write many variables in one line
pRint = 1
print(pRint)
JUT= "if"
print (JUT)
input('press the enter key to print var1'); print(var10) # here ; is used to write 2 line code in one line
input('Enter your name to print var11'); print(var_11)
input1=input('Enter your name to continue')
print("Welcome ",input1)         # Learned Today

# simple Python program to calculate the square of a number entered by the user:
# Taking user input and converting it to a float
input1 = float(input("Enter a number: "))

# Squaring the input
square = input1 ** 2

# Printing the result
print(f"The Square of {input1} is {square}")





