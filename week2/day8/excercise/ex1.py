# CONVERTING TWO LIST INTO A DICT
keys= ['TEN','TWENTY','THIRTY']

values = [10,20,30]
key_zip = zip(keys,values)

my_dict = dict(key_zip)
print(my_dict)