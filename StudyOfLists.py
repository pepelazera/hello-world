fruits = ["apple", "banana", "orange", "mango", "greap"]

first_fruit = fruits[0] # apple
third_fruit = fruits[2] #orange
print(first_fruit)
print(third_fruit)

fruits.append("pineapple")
fifth_fruit = fruits[5] # pineapple
print(fifth_fruit)

fruits.insert(1, "blueberry")
second_fruit = fruits[1] # blueberry
print(second_fruit)

fruits.extend(["melon", "watermelon"])
seventh_fruit = fruits[7]
eighth_fruit = fruits[8]
print(seventh_fruit)
print(eighth_fruit)

converted_list = list("Python") #['P', 'Y', 'T', 'H', 'O', 'N']
print(converted_list)

sequenced_list = list(range(1, 11)) # Create a list from 1 a 10
