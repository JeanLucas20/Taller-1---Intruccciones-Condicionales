


a= int(input("Ingrese un número: "))
n= 2
b= 0

# Processing

while n<a:
    if a%n == 0:
        b= 1
        c= print ("No es un número primo.")
    n = n + 1

if b == 0:
    c= print ("Si es un número primo.")

