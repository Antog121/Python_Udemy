valor = int(input("escribe el valor: "))

valorMin= 0

valorMax= 5

dentroRango= (valor >= valorMin) and (valor <= valorMax)

if dentroRango:
    print(valor, "está dentro del rango")
else:
    print(valor, "no está dentro del rango")   
