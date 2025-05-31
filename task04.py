template = "Bugun {weekdays} kuni, dars soat {time} da."

weekdays = input("Hafta kunini kiriting :")
time = input("Vaqtni kiriting :")

list = template.format(weekdays=weekdays , time=time)

print(list)