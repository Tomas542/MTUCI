import random
from matplotlib import pyplot as plt
import numpy as np

results = []


def read_csv(path):  ## Чтение файла для дальнейшей обработки
    with open(path, encoding="utf-8") as file:
        text = file.read()
        for line in text.split("\n"):
            a = line.split(";")
            b = tuple(a)
            results.append(b)
        return results


(read_csv("table.csv"))
results.pop(0)  ## Удаление первого эллемента списка (названия столбцов)
# print(results)


def write_dict(massive):  # запись данных по формату словаря
    dictionary = {
        "Номер заказа": int(massive[0]),
        "Дата заказа": (massive[1]),
        "Название товара": massive[2],
        "Категория": massive[3],
        "Количество продаж": int(massive[4]),
        "Цена за штуку": int(massive[5]),
        "Общая стоимость": int(massive[6]),
    }
    return dictionary


phones = []
console = []
tv = []
laptop = []
headphones = []
photos = []
tablets = []
smarthome = []
stable = []
toothbrushes = []
speaker = []
watches = []
drones = []
monitors = []


def sort_categories(
    results,
):  ## распределение товаров по категориям и помещение их в словари
    for i in range(len(results)):
        category = results[i][3]
        if category == "Смартфоны":
            phones_dict = write_dict(results[i])
            phones.append(phones_dict)
        elif category == "Консоли":
            console_dict = write_dict(results[i])
            console.append(console_dict)
        elif category == "Телевизоры":
            tv_dict = write_dict(results[i])
            tv.append(tv_dict)
        elif category == "Ноутбуки":
            laptop_dict = write_dict(results[i])
            laptop.append(laptop_dict)
        elif category == "Наушники":
            headphones_dict = write_dict(results[i])
            headphones.append(headphones_dict)
        elif category == "Фотоаппараты":
            photos_dict = write_dict(results[i])
            photos.append(photos_dict)
        elif category == "Планшеты":
            tablets_dict = write_dict(results[i])
            tablets.append(tablets_dict)
        elif category == "Умный дом":
            smarthome_dict = write_dict(results[i])
            smarthome.append(smarthome_dict)
        elif category == "Стабилизаторы":
            stable_dict = write_dict(results[i])
            stable.append(stable_dict)
        elif category == "Электрические зубные щетки":
            toothbrushes_dict = write_dict(results[i])
            toothbrushes.append(toothbrushes_dict)
        elif category == "Портативные колонки":
            speaker_dict = write_dict(results[i])
            speaker.append(speaker_dict)
        elif category == "Умные часы":
            watches_dict = write_dict(results[i])
            watches.append(watches_dict)
        elif category == "Дроны":
            drones_dict = write_dict(results[i])
            drones.append(drones_dict)
        elif category == "Мониторы":
            monitor_dict = write_dict(results[i])
            monitors.append(monitor_dict)
        else:
            print("Нет такой категории")


sort_categories(results)
# print(phones)


def all_price_select(
    massive,
):  # общая стоимость выбранной категории из массива словарей
    total = 0
    for u in range(len(massive)):
        price = massive[u]["Общая стоимость"]
        total += price
    return total


def all_price(massive):  # общая стоимость из массива словарей
    total = 0
    for u in range(len(massive)):
        for p in range(len(massive[u])):
            price = massive[u][p]["Общая стоимость"]
            total += price
    return total


full_massive = [
    phones,
    console,
    tv,
    headphones,
    laptop,
    photos,
    tablets,
    smarthome,
    stable,
    toothbrushes,
    speaker,
    watches,
    drones,
    monitors,
]

print(f"1. Полная выручка магазина {all_price(full_massive):,.2f}".replace(",", " "))

listofsales = []


def sales(array):
    for z in range(len(array)):
        for c in range(len(array[z])):
            sale = array[z][c]["Количество продаж"]
            listofsales.append(sale)


sales(full_massive)
# print(listofsales) ## список количества продаж товаров


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        s_arr = []
        m_arr = []
        e_arr = []
        for n in arr:
            if n < q:
                s_arr.append(n)
            elif n > q:
                m_arr.append(n)
            else:
                e_arr.append(n)
        return quick_sort(s_arr) + e_arr + quick_sort(m_arr)


sorted_array = quick_sort(listofsales)  # отсортированный список количества продаж
# print(sorted_array)

list_max_sales = []  # товары, которые были проданы больше всего


def find_max_sold(array):
    max = sorted_array[-1]
    for i in range(len(array)):
        for x in range(len(array[i])):
            compare = array[i][x]["Количество продаж"]
            if compare == max:
                list_max_sales.append(
                    array[i][x]
                )  # записывает только те, которые удовлетворили условию


find_max_sold(full_massive)
# print(list_max_sales)

if len(list_max_sales) == 1:
    print(
        "2. Товар, который был продан "
        + str(list_max_sales["Количество продаж"])
        + " раз - это "
        + list_max_sales["Название товара"]
    )
else:
    answer = []
    for i in range(len(list_max_sales)):
        answer.append(list_max_sales[i]["Название товара"])
        answer.append(", ")
    answer.pop(-1)
    print(
        "2. Товары, которые были проданы "
        + str(list_max_sales[0]["Количество продаж"])
        + " раз - это "
        + "".join(answer)
    )

total_summary = []  # список товаров в котором будут все товары для дальнейшей сортировки по общей доходности


def summary_sale(array):
    for z in range(len(array)):
        for c in range(len(array[z])):
            sale = array[z][c]["Общая стоимость"]
            total_summary.append(sale)


summary_sale(full_massive)
# print(total_summary)

sorted_total_summary = quick_sort(total_summary)

max_sold_part = []


def find_max_sum(array):
    max = sorted_total_summary[-1]
    for i in range(len(array)):
        for x in range(len(array[i])):
            compare = array[i][x]["Общая стоимость"]
            if compare == max:
                max_sold_part.append(array[i][x])


find_max_sum(full_massive)
# print(max_sold_part)

print(
    "3. Наиболее продаваемый товар - "
    + max_sold_part[0]["Название товара"]
    + ", его общая стоимость продаж - "
    + str(f"{max_sold_part[0]['Общая стоимость']:,.2f}".replace(",", " "))
    + " рублей"
)

# диаграмма доли выручки каждого товара

full_price = int(all_price(full_massive))
vals = []
labels = []
for y in range(len(full_massive)):
    for f in range(len(full_massive[y])):
        part_of_full = int(full_massive[y][f]["Общая стоимость"])
        delet = (part_of_full / full_price) * 100  ## процентаж в общей сумме
        delet_round = np.around(delet, decimals=1)
        vals.append(delet_round)
        labels.append(full_massive[y][f]["Название товара"])

fig, ax = plt.subplots()
ax.pie(
    vals,
    autopct="%.1f",
    wedgeprops=dict(width=0.3),
    pctdistance=1.2,
    radius=0.6,
    explode=[0] + [0 for _ in range(len(labels) - 1)],
)
ax.legend(loc="best", bbox_to_anchor=(-0.1, 0.7, 0.25, 0.25), labels=labels)
ax.axis("equal")
plt.show()
