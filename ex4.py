def flatten(list1):
    result = []
    for el in list1:
        if isinstance(el, (list, tuple)):
            # extend() method will add specified list elements to the end of the result list
            result.extend(el)
        else:
            # and if the element is not a type of list or tuple it will append it to result list
            result.append(el)
    return result
mixed_list = [35, 53, (525, 6743), 64, 63, [743, 754, 757]]
print(flatten(mixed_list))
