def convert_to_int(roman: str) -> int:
    dict_of_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_value = 0

    for char in reversed(roman):
        value = dict_of_val[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result


roman_num = "MCMXCIV"
print(convert_to_int(roman_num))
