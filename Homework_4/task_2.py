def create_cities_dict(n):
    cities = {}
    for i in range(n):
        city_info = input("Введите (через пробел) название страны и города этой страны: ").split()
        country = city_info[0]
        for city in city_info[1:]:
            cities[city] = country
    return cities


def get_country_list(m, cities_dict):
    res = []
    for i in range(m):
        city = input("Введите название города: ")
        res.append(cities_dict.get(city, "Город в списке не найден"))
    return res


def print_result(country_list):
    return country_list


n = int(input("Введите количество стран: "))
cities_dict = create_cities_dict(n)

m = int(input("Введите количество запросов: "))
country_list = get_country_list(m, cities_dict)

countries = print_result(country_list)
for country in countries:
    print(country)
