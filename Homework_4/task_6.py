def clear_text(text):
    return "".join([char if char.isalnum() else " " for char in text])


def create_list(new_text):
    new_list = []
    first_list = new_text.split()
    for word in first_list:
        if word not in new_list:
            new_list.append(word)
    return new_list


def count_diff_word(lst):
    res = len(lst)
    return res


my_text = (
    "Во входе! занст. Слас идх пдолсь\n"
    "(реьхв идх оарзны!? омли лчом\n"
    "токи Опрелс зичны омли, слодер вэст."
)

clear_text = clear_text(my_text)

my_list = create_list(clear_text)

result = count_diff_word(my_list)
print("Количество различных слов в тексте:", result)
