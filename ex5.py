dict1 = {'a': 1, 'b': 2, 'c': None, 'd': 'z', 'e': None}

# conditional dictionary comprehension
dict= {k: v for (k, v) in dict1.items() if v is not None}
print(dict)
