import csv

summ = 0

with open("files/list.csv", encoding='utf-8') as file:
    s = csv.reader(file)
    print('Купить: ')

    for string in s:
        print(f"{string[0]} - {string[1]} шт. за {string[2]} руб.")
        summ += int(string[2]) * int(string[1])
    print(f"Итого: {summ}")