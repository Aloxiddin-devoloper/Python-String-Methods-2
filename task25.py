#Task25: Matndan barcha Python so‘zlarini sanang (katta-kichik farqsiz)
#Matndagi Python, PYTHON, python... kabi variantlarni ham sanang.
#input: "Python is easy. I love python and PYTHON"
#output :3

text = input("Matnni kiriting :")
word = input("So'zni kiriting :")

text_lower = text.lower()
word_lower = word.lower()

resalt = text_lower.count(word_lower)

print(resalt)