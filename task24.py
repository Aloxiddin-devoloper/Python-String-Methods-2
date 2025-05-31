#Parol kuchliligini tekshirish .Parol quyidagilarga ega bo‘lishi kerak:
#Kamida 1 ta harf 1 ta raqam bo'ishi kerak
#input : parol123  :      123456
#output: true       :      false 

password = input("Parolni kiriting :")

faqat_raqam = password.isalpha()
faqat_harf = password.isdigit()

resalt = not faqat_raqam and not faqat_harf
print(resalt)