def nod(a, b):
    big = a if a > b else b
    less = a if a < b else b
    while big != less:
        if big > less:
            big -= less
        else:
            less -= big
    return big


res = nod(279, 354)
print("Наибольший общий делитель:", res)
