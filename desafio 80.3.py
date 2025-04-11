import bisect
list = []

for v in range(0,5):
    n = int(input('Type a number: '))
    bisect.insort(list, n)
    print(f'Numbers {n} included in position {list.index(n)}')
print(f'The numbers typed is {list}')  