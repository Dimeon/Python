import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

huiname = 'numbers.json'
with open(huiname) as f_obj:
    hujambers = json.load(f_obj)
    print(hujambers)