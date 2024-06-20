

#Challenge 1: Dictionary of Letter Indexes**
# Define a function letter_indexes that takes a word as input
def letter_indexes(word):
    # What is the purpose of this function?
    # It creates a dictionary with the indexes of each letter in a word

    # Initialize an empty dictionary to store the letter indexes
    letter_dict = {}

    # What is this loop doing?
    # It iterates through the word using the enumerate function, which returns both the index and the value

    for i, letter in enumerate(word):
        # What is this condition checking?
        # It checks if the letter is not already in the dictionary

        if letter not in letter_dict:
            # If not, add it to the dictionary with its index as the value
            letter_dict[letter] = [i]
        else:
            # If it is already in the dictionary, append its index to the existing list of values
            letter_dict[letter].append(i)

    # What does this function return?
    # It returns the dictionary of letter indexes

    return letter_dict

# Ask the user for a word
word = input("Enter a word: ")

# What is this line doing?
# It calls the function with the user's word and prints the result

print(letter_indexes(word))


#Challenge 2: Affordable Items from Store**


# Define a function affordable_items that takes two inputs: items_purchase (a dictionary) and wallet (a string)
def affordable_items(items_purchase, wallet):
    # What is the purpose of this function?
    # It returns a list of items that can be purchased with a given wallet amount

    # Remove the $ and , characters from the wallet string and convert it to an integer
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))
    
    # What is this variable used for?
    # It stores the remaining amount of money in the wallet after purchasing items

    affordable_items = [] 
    
    # Iterate through each item in the items_purchase dictionary
    for item, price in items_purchase.items():
        # What is this loop doing?
        # It iterates through each item and its price in the items_purchase dictionary

        price_amount = int(price.replace("$", "").replace(",", ""))
        
        # What is this condition checking?
        # It checks if the price is less than or equal to the wallet amount

        if price_amount <= wallet_amount:
            # If it is, add the item to the affordable_items list and subtract its price from the wallet amount
            affordable_items.append(item)
            wallet_amount -= price_amount
    
    # What does this condition check?
    # It checks if there are any affordable items

    if not affordable_items:
        # If not, return "Nothing"
        return "Nothing"
    else:
        # Otherwise, return the sorted list of affordable items in alphabetical order
        return sorted(affordable_items)

# Define a dictionary of items with their prices
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

# Define a wallet amount
wallet = "$300"

# What does this line do?
# It calls the function with the items_purchase dictionary and wallet string and prints the result

print(affordable_items(items_purchase, wallet))  # Output: ["Bread", "Fertilizer", "Water"]

