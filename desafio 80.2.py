list = []
for c in range(0,5): # create a loop with 5 numbers
    n = int(input('Type a value: '))
    if c == 0: # put the first Value
        list.append(n)
    elif n > list[-1]: # if the new value are greater the other input value, this new value will appended to the end of the list
        list.append(n)
    else:
        pos = 0 # If the new value doesn't meet the above conditions, a new position (pos) is initialized at 0
        while pos < len(list): # While pos are smaller then len(list)
            if n <= list[pos]: # If n(number) are smaller or same than position in list
                list.insert(pos, n) # put the number in a specific position
                break # Break the While loop
            pos += 1 # Will put the numbers in other and always a new number are writing in code, will pass the numbers and reorganize the list for terminal

print('')
print('The values you entered were', ', '.join(map(str, list)))
