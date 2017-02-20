import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

huiname = 'numbers.json'
with open(huiname) as f_obj:
    hujambers = json.load(f_obj)
    print(hujambers)

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We welcome you - " + username + "!")

filename = 'username.json'
if __name__ == '__main__':
    with open(filename) as f_obj:
        username = json.load(f_obj)
        print("Welcome back, " + username + "!")

# Программа загружает имя пользователя, если оно было сохранение ранее
# В противном случае она запрашивает имя пользователя и сохраняет его

filename = 'hujusername.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your fucking name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you, when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")