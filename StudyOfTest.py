from Studies.StudyOfDIct import quant

sequence = list(range(1, 11))
print(sequence)

print()

foods = ["haburguer", "pizza", "fetuccine", "sushi"]
first_foods = foods[0:3] # 0, (3-1) [0, 2]

last_foods = foods[-2:]

print(first_foods)
print(last_foods)

print()
numbers2 = [10, 20, 30, 40, 50]
print(numbers2)

numbers2[2] = 25
print(numbers2)

print()
numbers2[1:3] = [77, 165]
print(numbers2)

print()
intNumbers = [1, 2, 3]
print(intNumbers)

intNumbers.append(4)
print(intNumbers)

intNumbers.insert(0, -1)
intNumbers.insert(1, 0)
print(intNumbers)

intNumbers.extend([5, 6, 7])
print(intNumbers)

new_intNumbers = intNumbers + [8, 9, 10]
print(new_intNumbers)

new_intNumbers.pop(5)
print(new_intNumbers)

print()
test_remove = [1, 2, 3, 4, 5, 6, 5]
test_remove.remove(5)
print(test_remove)

test_pop = [1, 2, 3, 4, 5, 6, 5]
test_pop.pop()
print(test_pop)

print()
del test_pop[1:3]
print(test_pop)

print()
random_numbers = [5, 7, 8, 2, 1]
print(random_numbers)

ordered_numbers = sorted(random_numbers)
print(ordered_numbers)

ordered_numbers.reverse()
print(ordered_numbers)

print()

new_list = [1, 1, 2, 2, 2, 3, 3, 3, 3]
quant_new_list = new_list.count(2), new_list.count(3)
print(quant_new_list)

print()
position = new_list.index(1)
print(position)

size = len(new_list)
print(size)