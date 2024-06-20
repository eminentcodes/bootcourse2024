# cinemax 
# under age 3 ticket is free
# bewwen 3 and 20 ticket is $ DOLLARS
# OVER THE AGE OF 12 TICKET IS $15 DOLLARS

# a = 10
# b = 15
# c = "free"
# print('WELCOME TO CINEMAX THEATRE')

# family = {'rick':42 ,'beth':13,'morty' :5,'summer':8 }
# for i in family:
# i = 0
#     if family[i] < 3:
#         print(f'{i} your entry  is {c}')
#     elif  3>= family[i]  <= 15:
#         print(f'{i} your entry  is ${a}')
#     elif  15> family[i] >= 40:
#         print(f'{i} your entry  is ${b}')
#     elif  family[i] > 15:
#         print(f'{i} your entry  is ${b}')



# Define the prices for different age groups
a = 10  # Price for ages 3-15
b = 15  # Price for ages 16 and above
c = "free"  # Free admission for ages under 3


# Define a dictionary of family members and their ages

family = {'rick':42 ,'beth':13,'morty' :5,'summer':8 }
# Print the ticket prices for each family member individually
for person,age in  family.items():
    # Check if the person's age is under 3, print "free" ENTRY
    if age < 3:
        print(f'{person} your entry  is {c}')
# check the person beween age 3 to 15 years
    elif age <= 15:
        print(f'\t {person} your entry  is $  {a}') #the age here will pay 10 dolarzelse: age >= 40:
    else:
        print(f'\t{person} your entry  is ${b}') #the age here will pay 15 dolarz
# if none of the ages are found ,
#  This shows that this person has to pay 
    
    # total of all expediture
    spending = a+a+a+b
    print(f'\tthe  total spending is for d  family  is ${spending}')


# ask ser to input names and andeaches insttead of the given varaible ake user for the names and add them into 
# a family list which ius empty

family = []

while True:
    name = input("Enter the name of a family member: ")
    if name == "":
        print(name)

print('__________________________________________')
