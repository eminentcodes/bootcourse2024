# variable increment
# here we will add a number by +1

my =  7
my += 1
# it means the value of my will be 8

# this syntax can be used in any operator 

print("\nmy new number is ",my)
# string formating
# string formating helps us to print onr or two types of variables at once
# using th f-string also called formated string literal f- ther (f) containing strings  and curly brackets
# and xpressions which carry values

name = 'eminentcodes'
age = 30

print('hello {}.you are {} old'.format(name,age))
print(f'hello { name} you are {age} old')
birthday = 23
birthmonth = '5'
birthyr = 2001


print('i was born the {}/{}/{}'.format(birthday,birthmonth,birthyr))
 
#  numeric operation
# we can use variables to perform all types operations
# if used alongside th {input} FUNCTION be carefull and remember that
# input always gives u a string return as a result u need to cast ur string into an interger
# if u wish to p[erform a a mathematicaL operation,perform it with ;

# number = input ("multipy me by 3")
# number * 3 
# output : will be error
# so
numbers = int(input('multiply me by 3'))
result = numbers*3
print(result)
# output 12 which is correct

# conditionals in python 
# conditions are expressions that compare two elements in pythons
# python support the following condions 

# ==
# >
# <
# =>
# <=
# if statement
# the keyword to create a condtion is the if (statement)
# followed by else
# elif comes at times before else if its a nested loop 
# example\
a = 6
r = 9
if a < r:
    print('\n a is greater than r')
else:
    print('\nr is greater than a')


#     the elif it catches anything that is not cot in the if statment
# if a previouse conditions do not hold , we now depend on the elif (statement)

# example

mark = int(input('enter your mark!!'))
if mark < 8:
    print('ypu are very weak')
elif mark > 8 and mark < 12:
 print('\n you are weak ')
elif 15 >= mark and mark < 20:
    print('\nyou are average')
else:
   print('PLEASE ENTER A VALID MARK')


   #THE AND $ OR STATMENTS
#    ----------------------- READ ON


# the and statement is used to check if two conditions are true
#IN KEYWORD 



   
   