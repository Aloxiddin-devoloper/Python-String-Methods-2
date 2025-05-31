template = "{product} mahsuloti narxi $ {price}"

product = input("Mahsulotni kiriting :")
price = input("Narxini kiriting :")

list = template.format(product=product , price=price )

print(list)