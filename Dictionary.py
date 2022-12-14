#1: Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# res_dict = set(zip(keys, values))
# print(res_dict)


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# mydict = dict()
# for i in range(len(keys)):
#     mydict.update({keys[i]:values[i]})
# print(mydict)    

#2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# mydict = dict1.copy()
# mydict.update(dict2)
# print(mydict)

#3 5: Create a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
# # keys to extract
# keys = ["name", "salary"]

# # new dict
# res = dict()

# for k in keys:
#     # add current key with its va;ue from sample_dict
#     res.update({k: sample_dict[k]})
# print(res)        
