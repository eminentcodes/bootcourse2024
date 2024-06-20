# Challenge 1: Multiples


def print_multiples(number, length):
    multiples = []
    multiple = number
    while len(multiples) < length:
        multiples.append(multiple)
        multiple += number
    print(multiples)

number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
print_multiples(number, length)
# Challenge 2: Remove Consecutive Duplicates


def remove_consecutive_duplicates(word):
    new_word = ""
    for w in word:
        if len(new_word) == 0 or w != new_word[-1]:
            new_word += w
    return new_word

word = input("Enter a word: ")
print(remove_consecutive_duplicates(word))
