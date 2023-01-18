# 'in' - To check if a key is already present
d = {
    'Planet': 'Earth',
    'Continent': 'North America',
    'Country': 'USA',
}

if 'Continent' in d:
    print('Value associated with key - ' ,d['Continent'])
else:
    print('Key is not present')
    
# del instruction and clear() method
# d = {
#     'Planet': 'Earth',
#     'Continent': 'North America',
#     'Country': 'USA',
# }

# del d['Planet']
# print(d)