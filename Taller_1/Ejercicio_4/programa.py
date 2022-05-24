
a= int(input("Ingrese un número: "))
a1 = a
n = 0
# Processing

while a > 0:
    b = a % 10
    n = n * 10 + b
    a = a // 10

if a1 == n:
    c= print(a1, "Es capícua")
else:
    c= print(a1, " No es capícua")







