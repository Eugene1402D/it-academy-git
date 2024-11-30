def create_data_check(num):
    lang_dict = {}
    set_all_languages = set()
    for i in range(num):
        languages = []
        m = int(input(f"Введите количество языков для {i + 1}-го школьника: "))
        for j in range(m):
            students_languages = input(f"Введите {j + 1} язык {i + 1} школьника: ")
            languages.append(students_languages)
            set_all_languages.add(students_languages)
        lang_dict[i + 1] = languages

    return lang_dict, set_all_languages


def choice_student(other_list, number):
    return other_list.get(number)


def print_info(choice, value):
    info = f"Школьник {choice} знает следующие языки:\n"
    for k in value:
        info += f"{k}\n"
    return info


n = int(input("Введите количество опрашиваемых школьников: "))
check_list, all_languages = create_data_check(n)

rating = int(input("Список языков какого ученика дополнительно вывести на печать: "))
lang_list = choice_student(check_list, rating)

print("Количество языков, которые знают все школьники:", len(all_languages))
for lang in all_languages:
    print(lang)

result = print_info(rating, lang_list)
print(result)
