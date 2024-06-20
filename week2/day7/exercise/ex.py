#iterate through 1 to 100 using ranch function function
for fizzbuzz in range(101):
    # Check if the current number is divisible by both 3 and 5 (i.e., divisible by 15)
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        # If divisible by both 3 and 5, print "fizzbuzz" and continue to the next iteration
        print("fizzbuzz")
        
    # Check if the current number is divisible only by 3
    elif fizzbuzz % 3 == 0:
        # If divisible only by 3, print "fizz" and continue to the next iteration
        print("fizz")
        
    # Check if the current number is divisible only by 5
    elif fizzbuzz % 5 == 0:
        # If divisible only by 5, print "buzz" and continue to the next iteration
        print("buzz")
        
    # If the number is neither divisible by 3 nor 5, print the number itself
    print(fizzbuzz) 

# ex2

user_input = input("Enter a string of 10 characters: ")

if len(user_input) > 10:
    print("Too long!")
elif len(user_input) < 10:
    print("Too short!")
else:
    print("Just right!")

    
    # ex 4
    s = "HELLO WORLD"
for i in range(len(s)):
    print("".join(s[:i+1]))

# ex5
    import random

words = ["hello", "world"]
random.shuffle(words)

print(" ".join(words))


