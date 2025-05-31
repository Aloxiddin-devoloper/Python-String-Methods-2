#Task23: Foydalanuvchi kiritgan matndan barcha sonlarni hisoblang
#Matnda nechta raqam borligini toping.
#input: Bugun 3 ta dars, ertaga 2 ta
#output : Raqamlar soni: 2

text = input("Matnni kiriting :")

n1 = text.count("0")
n2 = text.count("1")
n3 = text.count("2")
n4 = text.count("3")
n5 = text.count("4")
n6 = text.count("5")
n7 = text.count("6")
n8 = text.count("7")
n9 = text.count("8")
n10 = text.count("9")

soni = (n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)

print("Raqamlar soni :",soni)



