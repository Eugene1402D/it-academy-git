def assign_and_print(a, b, c):
    result = f"a = {a}\nb = {b}\nc = {c}"
    return result


my_list = ["a", 2, "python"]
result = assign_and_print(*my_list)
print(result)
print()

new_tuple = ((1, 2, 3),)
print("Длинна кортежа:", len(new_tuple))
for i in new_tuple[0]:
    print(i)
