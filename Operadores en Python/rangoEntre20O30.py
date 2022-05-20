edad= int(input("introduce tu edad: "))

veintes= edad>=20 and edad<30
print(veintes)
treintas= edad>=30 and edad<40
print(treintas)

if veintes or treintas: # cualquiera de los valores que sea verdadero me va a dar verdadero
   # print("dentro de rango 20's o 30's")
    if veintes:
        print("detro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
    else:
        print("fuera de rango")
else:
    print("dentro de rango 20's o 30's")
25