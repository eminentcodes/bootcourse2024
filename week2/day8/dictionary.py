# my_info dic name 
# 'name' key value
# gilbert is the  value
my_info = {
    'name' :"gilbert",
    'age' :29

}
print(my_info['name']) 


my_dic ={
"distant" : 100,
'distination': 'douala',
'amount' : 10000 

}

print(my_dic ['amount'],my_dic['distination'])



# ACCESSSING TWO DICT
# {"my_dic" :{
# "weight" : 100,
# 'name': 'caesar',
# 'amount' : 3000

# },

# my_dic ={
# "dish" : 100,
# 'distination': 'douala',
# 'amount' : 2000 

# }
# }

# access the key value 'history'
sample_dic = {
    'class':{
        'student':{"name":"mike","marks":{
            'physics':70,'history':80
        }}
    }
}

print(sample_dic['class']['student']['marks']['history'])

# modifying an entry in a dict?
sample_dic ['class']['student']['marks'],



# deleting an entery in dict

sample_di = {
  "name" : 'john',
'money' : 1000,
'city' : 'new york'
 }