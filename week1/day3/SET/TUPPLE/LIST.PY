my_name = "gilbert"
hello = "hello word"
my_age = 23

my_list = [my_name,hello,my_age]
my_tupple = [my_name,my_age,hello]
print(my_list[0:3])#all the elements are printed

print(my_list[0:2]) #print first ans second element 
#to modify elements in your list 
my_list [0] = 1500
print("my new list is ",my_list)
#to remove from list 
my_list.remove(my_age)
print("ur age has been deleted",my_list)
my_list.pop(1)
print(my_list)
#dding an elements to list
my_list.append("my way ")
print("\n a new item has been added",my_list)
#adding to list together 

list1 = ["whisky","juice","wine"]
list2 = ["fufu","eru","garri"]
print(list1+list2)

list0 = [5,10 ,15,16,18,19,20]
# check if 20 is in the list 
if 20 in list0 :
    new_value = list0.index(20)
    print(new_value)
list0[new_value] = 200
print(list0)
# unpack the following into 4 variables
a_tupple = (10,3,4,7)
m,n,k,o = my_tupple
print(o)
print(n)




