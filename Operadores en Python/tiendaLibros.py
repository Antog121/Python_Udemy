from xml.sax.saxutils import prepare_input_source


print("prporciona los siguientes datos del libro: ")
nombre= input("propreciona el nombre del libro: ")
id= int(input("Proporciona el id del libro"))
precio= float(input("Proporciona el precio del libro: "))
envioGratuito= (input("Indica si el envío es gratuito (True/False): "))

if envioGratuito == "True":
    envioGratuito= True
elif envioGratuito == "False":
    envioGratuito= False
else:
    envioGratuito= "valor incorrecto, debe escribir true o false"

print(f"""  # esta forma de imprimir en varias líneas es muy interesante y así solo usamos un print
    Nombre: {nombre}
    id: {id}
    precio: {precio}
    envio Gratuito?: {envioGratuito}
""")
