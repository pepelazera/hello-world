coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)

numbers_of_tuple = (1, 2, 3, 4, 5)
first, *mid, last = numbers_of_tuple
last = 5
print(numbers_of_tuple)
print(first, mid, last)

a, b = 10, 20
a, b = b, a
print(a, b)

amount = numbers_of_tuple.count(2) # The same as count on lists
print(amount)

position = numbers_of_tuple.index(4)
print(position) # Return the position of number 4 in the tuple. So, this is tha same as index on lists

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated = tuple1 + tuple2
print(concatenated)

repeated = tuple1 * 2
print(repeated)

tuple_with_list = (1, 2, [3, 4]) # Although tuples are immutables, they can have mutable objects (like lists)
print(tuple_with_list) # (1, 2, [3, 4])

tuple_with_list[2].append(5)
print(tuple_with_list)

print()
def get_user_data():
    return "Pedro", 25, "pepelazera@gmail.com" # We can use tuples like this

name, age, email = get_user_data()
print(f"{name}, {age}, {email}")

