template = "{a}+{b}={natija}"

a = float(input())
b = float(input())

natija = a+b
resalt = template.format(a=a,b=b,natija=natija)

print(resalt)