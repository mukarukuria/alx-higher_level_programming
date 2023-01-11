#!/ubsr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    unique = set()
    for i, el in enumerate(my_list):
        unique.add(el)

    return sum(unique)
