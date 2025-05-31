#Task21: To‘liq Foydalanuvchi Ma’lumotlarini Formatlash .
# Foydalanuvchi haqida: ism, familiya, yoshi, kasbi. Shu ma’lumotlar asosida jumla tuzing.
#input:"Diyorbek", "Aliyev", 23, "dasturchi"
#output:Salom, mening ismim Diyorbek Aliyev. Men 23 yoshdaman va dasturchiman.

template = "Salom, mening ismim {name} {last_name}. Men {age} yoshdaman va {profession}man"

name =input("isminggizni kiriting :")
last_name =input("Familyanggizni kiriting :")
age =int(input("yoshinggizni kiriting :"))
profession =input("kasbinggizni kiriting :")

resalt = template.format(name=name,last_name=last_name,age=age,profession=profession)

print(resalt)