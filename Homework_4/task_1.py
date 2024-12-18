def created_dict(start, stop, power):
    result = {k: k**power for k in range(start, stop + 1)}
    return result


my_dict = created_dict(1, 20, 3)
print("my_dict:", my_dict)
