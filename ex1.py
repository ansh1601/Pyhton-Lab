lis = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 6, 'd']]

# list comprehension
flat = [i for sub in lis for i in sub]
print(flat)
