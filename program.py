def min_max(list):

    result = []
    if len(list) == 0:
        return None
    min = list[0]
    max = list[0]
    for element in list:
        if element > max:
            max = element
        if element < min:
            min = element

    result.append(min)
    result.append(max)
    return result

print(min_max([6, 8, 78, 2]))
#ok
