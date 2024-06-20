

#Exercise 1: Favorite Numbers#


my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(6)  # Note: Sets do not have an add method, use the update method instead
my_fav_numbers.update([6, 7])
my_fav_numbers.remove(5)
friend_fav_numbers = {8, 9, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


#Exercise 2: Tuple#


# Given a tuple which value is integers, is it possible to add more integers to the tuple?
# No, tuples are immutable in Python, which means you cannot add or remove elements from a tuple once it's created.


#Exercise 3: List#


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list
basket.remove("Banana")
# Remove “Blueberries” from the list
basket.remove("Blueberries")
# Add “Kiwi” to the end of the list
basket.append("Kiwi")
# Add “Apples” to the beginning of the list
basket.insert(0, "Apples")
# Count how many apples are in the basket
print(basket.count("Apples"))
# Empty the basket
basket.clear()
print(basket)


#Exercise 4: Floats#

# Recap – What is a float? What is the difference between an integer and a float?
# A float is a number with a decimal part, whereas an integer is a whole number.

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5
numbers = [round(i) for i in range(1.5, 6, 0.5)]

print(numbers)

# Can you think of another way to generate a sequence of floats?
# Yes, you can use a list comprehension with a formula to generate the sequence.


#Exercise 5: For Loop# 


# Use a for loop to print all numbers from 1 to 20, inclusive.
for i in range(1, 21):
    print(i)

# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


#Exercise 6: While Loop#


# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = "John"
while True:
    user_name = input("Enter your name: ")
    if user_name.lower() == name.lower():
        break
    else:
        print("Try again!")


#Exercise 7: Favorite Fruits#


# Ask the user to input their favorite fruit(s) (one or several fruits).
favorite_fruits = input("Enter your favorite fruit(s), separated by space: ").split()
print(favorite_fruits)

# Store the favorite fruit(s) in a list.
fruit_list = favorite_fruits

# Ask the user to input a name of any fruit.
fruit_choice = input("Enter a fruit: ")

# Check if the user's input is in the favorite fruits list.
if fruit_choice.lower() in [fruit.lower() for fruit in fruit_list]:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")


#Exercise 8: Who Ordered A Pizza ?#


# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
toppings = []
while True:
    topping = input("Enter your pizza topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)

# As they enter each topping, print a message saying you’ll add that topping to their pizza.
for topping in toppings:
    print(f"Adding {topping} to your pizza!")

# Upon exiting the loop print all the toppings on the pizza pie and what the total price is.
total_price = len(toppings) * (2.5 + 10)
print(f"Your pizza will have {', '.join(toppings)}")
print(f"The total price is ${total_price:.2f}")


#Exercise 9: Cinemax#


# Ask a family the age of each person who wants a ticket.
family_members = []
while True:
    age = input("Enter age of family member (or 'quit' to stop): ")
    if age.lower() == 'quit':
        break
    family_members.append(int(age))

# Store the total cost of all the family's tickets and print it out.
total_cost = sum([10 if age < 12 else 15 for age in family_members])
print(f"The total cost of all tickets is ${total_cost:.2f}")

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
teenagers = []
while True:
    age = input("Enter age of teenager (or 'quit' to stop): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 16 or age > 21:
        print(f"{age} is not allowed to watch this movie. Removing them from the list.")
        continue
    teenagers.append(age)

print(f"Final list of teenagers: {', '.join(map(str, teenagers))}")


#Exercise 10: Sandwich Orders#


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” from sandwich_orders.
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print(sandwich_orders)

finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)

# After all the sandwiches have been made, print a message listing each sandwich that was made.
for i in range(len(finished_sandwiches)):
    print(f"I made your {finished_sandwiches[i]}")
 