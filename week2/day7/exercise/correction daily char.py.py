number = int(input("ENTER A NUMBER")) #to take ur number 
length = int(input('enter the lenght of ur list')) #the index [from 0 _] to print ur multiple
multiple = number 

my_list = [] #empty list to take input in =>int(input("ENTER A NUMBER"))
while len(my_list) < length: #here its force that lent can be less than the list so its force therefore therefore the process stops
    my_list.append(multiple) # number entered by the user
    multiple += number#add the number 
print(my_list)
    
# print(len([3,5]))

word = input("enter your word") #take ur word
list = [] #list to  take ur input
result = ""  #to take ur string

for i in word:
    
    if i not in result:#if  character not in result  then add to  output else dont add if its exist
        result += i 
print(result)
