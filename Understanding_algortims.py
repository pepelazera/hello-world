def binary_search(numbs, item):
    low = 0
    high = len(numbs) - 1

    while low <= high:
        mid = (low + high) // 2
        kick = numbs[mid]

        if kick == item:
            return mid
        if kick > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(f"Position of 3: {binary_search(my_list, 3)}")
print(f"Position of -1: {binary_search(my_list, -1)}")