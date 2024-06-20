print("hello world\n"*4)

#ex three write code to calculate the result of 
## 2 : Some Math
#Instructions
#1)Write code that calculates the result of:
#(99^3)*8 (meaning 99 to the power of 3, times 8)
power = 99#3
final = power * 8
print(final)
#xercise 3 : What Is The Output ?
#Instructions
#>>> 5 < 3
#>>> 3 == 3
#>>> 3 == "3"
#>>> "3" > 3
#>>> "Hello" == "hello"
p = 5 > 3
print(p)
5 < 3
g = 3 == 3 
print(g)
#o= 3 == "3"



#k = "3" > 3
#print(k)

l = "hello" == 'HELLO'
print(l)
#🌟 # 4 : Your Computer Brand
#2)Using the computer_brand variable print a sentence that states the following:
#"I have a <computer_brand> computer".

computter_brand = 'Sony'
print('i have a {} computer'.format(computter_brand))

#🌟 # 5 : Your Information
#Instructions
#1)Create a variable called name, and set it’s value to your name.
#2)Create a variable called age, and set it’s value to your age.
#3)Create a variable called shoe_size, and set it’s value to your shoe size.
#4)Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
#5)Have your code print the info message.
#6)Run your code

name = 'eminentcode'
age = 27
shoe_size = 41
info = ' i cant go a day without music'

print(name)
print(shoe_size)
print(info)
#🌟 # 6 : A & B
#Instructions
#1)Create two variables, a and b.
#2)Each variable value should be a number.
#3)If a is bigger then b, have your code print Hello World.

a = 98
b = 76
if a > b:
    print('hello world')
else:
    print('what a world')
      
## 7 : Odd Or Even
#Instructions
#1)Write code that asks the user for a number 
# and determines whether this number is odd or even.

my_number = int(input('input number:\n'))
if (my_number % 2 )== 0 :
     print('this is an even number')
else :
    print("this is an odd number")

    
    #ex 8
name = input('write your name here.. ')
confirm_name = input('confirm ur name ')
if name ==confirm_name:
    print('welcome mr {}'.format(name))

else:
    print("unknown user")

#ex 9
hieght = int(input('input hieght\n'))
if hieght > 145:
    print('you are tall enough to ride')
else:
    print("u  need to grow some more rides")