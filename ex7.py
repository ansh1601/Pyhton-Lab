def dict_union(dict1, dict2):
    return dict2.update(dict1)


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 4, 'd': 'e'}

print(dict_union(d1, d2))
print(d2)
