first_name = 'Aleksei'
second_name = 'Birjukov'

full_name = first_name + ' ' + second_name

print('\n'+full_name+'\n'+full_name)

names = ['Jasha','Bochmak','Pidaras']
print(names[0], names[1], names[2])

for name in names:
    print(name.title() + ', that was a great trick!' + '\n')

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

players = ['Alex','Nigga','Bochmak','Mudak','Pidar']
print(players[-2:])
for player in players[:3]:
    print(player.title()+'\n')

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
#dimensions[0] = 250
print(dimensions[0])
print(dimensions[1])

cars = ['audi','bmw','mercedes','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Idi nahui!')

banned_users = ['Andrei', 'Dima', 'Masha-Huyasha']
user = 'Bochmak'
if user not in banned_users:
    print(user.title() + ', ty vsjo taki poluchish bo ebalu')

requested_toppings = []

available_toppings = ['mushrooms', 'olives', 'green papers',
                      'peperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + " in our menu.")

alien_0 = {'color':'green'}
print(alien_0['color'])

alien_0 = {'color':'green', 'points': 5}
new_points = alien_0['points']
print('You have just earned ' + str(new_points) + ' points')

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

user_0 = {
    'username': 'Dimeon',
    'first': 'Aleksei',
    'last': 'Birjukov'
}
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

def greet_user(anyonename):
    print('Hello, ' + anyonename.title() + '!')

greet_user('Pidaras')

