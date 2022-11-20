import math
import random


msg = 'rural juror'
newMsg = msg.capitalize().split()
msg2 = '''What is going 
on people'''
setObj = { 'key': 'value',
          'key2' : 'value2'}

newObj = set(setObj) 
newTup = tuple(setObj)
newList = list(setObj)

print(10//5)
print(10%3)
print(10**2)
print('')
print(math.trunc(-11.95))
print(math.floor(-11.95))
print(math.log2(16))
print(math.log10(1000000))
print('')
print(math.sin(math.radians(90)))
print('')
print(random.randrange(1, 10, 1))
print('')
print(newTup)
print(newList)
print(newObj)
print(setObj)
print('')
print(type(setObj))
print(newMsg[1].capitalize())
print(type(newMsg))
print(msg2)
print('j' in msg) 
print('j' in msg and 's' in msg)
print(type(len(msg) > len(newMsg)))
print(id(newObj))
print(setObj is not newObj)
print(walrus:='Blammo')

age = int(input('How old are you: '))

if age>=18:
    print('You can vote')
else:
    print('Straight to jail')

grade = int(input('What was your score? '))

if grade>=90 and grade<=100:
    if grade<=93:
        print('Grade: A-.')
    elif grade>93 and grade<=96:
        print('Grade: A')
    else:
        print('Grade: A+')
elif grade>=80 and grade<90:
    print('Your grade is a B.')
elif grade>=70 and grade<80:
    print('Your grade is a C.')
elif grade>=60 and grade<70:
    print('Your grade is a D.')
elif grade>100:
    print('There were only 100 points possible!')
    print('You cheated.')
else:
    if grade<30 and grade>=0:
        print('Writing your name is worth 29 points...')
    elif grade<0:
        print('This cannot be possible.')
    else:
        print('You failed. Try harder.')

# number guessing game
randNum = random.randint(1,10)
guess = int(input('Guess between 1 and 10: '))

if guess == randNum:
    print('Smash.')
elif guess >randNum:
    print('Too high.')
else:
    print('Too low.')

'''
import module_name
from module_name import something, anotherthing, andanother
bc we don't always need the entire module, we can import the specific func or var
needed, thus saving memory space and processing power
however, when importing the whole module, calling a func requires
module_name.function()
vs
from mod import something
you only need the func()

math operators:
    +
    -
    *
    /
    % - modulus, or remainder of divinding x % y
    ** - exponent
    // - trunctation or floor division, x//y returns quotient (how many times you divide y into x)

common math funcs:
    ceil(x) - returns largest integer >= x
    floor(x) - returns largest int <= x
    fabs(x) - returns absolute value of x, which can be a float, does not round or trunc
    factorial(x) - factorial of x, as in, x = 3, so 3*2*1
    fmod(x,y) - returns remainder of x/y
    log2(x) - base-2 logarithm of x
    log10(x) - base-10 logarithm of x
    pow(x,y) - x raised to the power of y
    sqrt(x) - square root
    trunc(x) - returns the truncated (nearest integer ie whole number; rounded down) value of x
    
    floor vs trunc: both round down, but trunc goes TOWARDS 0, floor goes to closest whole int going down in value
    ex above: trunc(-11.95) == -11, while floor(-11.95) == -12
can be used like in JS: module_name.function(), ie math.floor(x)
note: math is not all caps like in JS

common trig funcs in math (Note: all trig func need x in radians as param):
    sin(x) - sin of x in radians
    cos(x) - " "
    tan(x) - " "
    degrees(x) - converts angle x from radians to degrees
    radians(x) " " to radians
    
constants:
    pi - (3.14159...)
    tau - 2pi (6.28318...)
    e - euler's number (2.71828...), a constant that is the base of the natural logarithm,
        a mathematical function that is commonly used to calculate rates of growth or decay
        usually aprox = 2.718
    inf - infinity, positive
    -inf - negative infinity
    
randoms (not under math mod, under random mod):
    seed(x) - initialize the random number generator
    randrange(x, y, step) - returns a random number between the given range
    randint(x, y) - returns a random number between the given range
        both do the same if just using x and y; randrange with a step returns it with step size, and does not include endpoints
    choice(sequence) - random element from the given sequence
    shuffle(sequence) - takes a sequence and returns it in a random order
    random() - returns a random float between 0 and 1 (the same as JS MATH.Random)

Booleans or bool are True and False, capitalized unlike in JS true and false

list in py equals array in js
dictionary in py equals object in js
set in py is like an 
array but in curly bracks; or an obj without paired value
tuple in py like an
array but in paranthesis;
visually let's remember it this way:
-tuple (key1, key2)
-list [str, str]
-set {key, key2}
-dictionary {key1 : value1, key2 : value2}

== is equality, = is declaration of variable

in , not in = returns bool of whether it is part of data
and , or , not = returns bool like logical &&, ||, ! in js
is , is not = returns bool of whether memory location is same from id() method
:= is the walrus operator, combines declaration of variable and exe at same time

input(#question) always returns a string, so set the type as needed
'''

