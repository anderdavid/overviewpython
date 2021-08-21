print("hola mundo")
print("Esto es un repaso de python")

# soy un comentario
""" print("otro mas") """

# variables
texto = "Repaso de Python"
nombre = "Anderson David Rodriguez Narvaez"
altura = "173cm"
year = "2021"

print(nombre)

# concatenar
print(f"{texto} -{nombre} - {altura} -{str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

""" # Entrada de datos
sitioWeb = input("¿Cual es tu pagina web?")
print(f"tu sitio web es: {sitioWeb}") """

""" # algoritmo ver si eres alto

altura = int(input("ingrese su altura"))

if altura >= 180:
    print("eres una persona alta")
else:
    print("eres una persona baja") """

# Funciones


def mostrarAltura(altura):
    resultado = ""
    if altura >= 180:
        resultado = "eres alto"
    else:
        resultado = "eres bajito"

    return resultado


""" altura = int(input("ingrese su altura: "))
print(mostrarAltura(altura)) """


personas = ["David", "Paco", "Pepe"]
print(personas)

for persona in personas:
    print("- " + persona)
