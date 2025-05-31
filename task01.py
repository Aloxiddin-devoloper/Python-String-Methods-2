template = "Salom , mening ismim  {name} va yoshim {age}."

name = input("Isminggizni kiriting :")
age = input("Yoshinggizni kiriting :")

message = template.format(name=name, age=age)

print(message)