def array_diff(a, b):
    new_list = a[:]
    if not a or not b:
        return new_list
    else:
        for num_2 in b:
            for num_1 in a:
                if num_2 == num_1:
                    if num_2 in new_list:
                        new_list.remove(num_2)
        return new_list