template = "File: {file}.{file_type}"

file = input("Faylni kiriting :")
file_type = input("Fayl turini kiriting :")

resalt = template.format(file=file , file_type=file_type)

print(resalt)