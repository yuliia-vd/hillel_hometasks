import os

dict1 = {}
for root, dirs, files in os.walk('.'):
    for one_file in files:
        if os.path.exists(one_file):
            dict1[one_file] = os.path.getsize(one_file)
print(dict1)

sorted_dict = {}
sorted_keys = sorted(dict1, key=dict1.get)
# print(sorted_keys)
largest_files = sorted_keys[-10:]
# print(largest_files)

for item in largest_files:
    sorted_dict[item] = dict1[item]
print(sorted_dict)

