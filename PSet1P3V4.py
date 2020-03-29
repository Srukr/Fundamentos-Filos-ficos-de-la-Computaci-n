#Regresa el substring en orden alfabético más largo encontrado en el string proporcionado.
cadenaAnalizada = input("Dame el string a analizar:\n")

caracterAnterior = ""
cadenaActual = ""
cadenaMasLarga = ""

for caracter in cadenaAnalizada:
    if caracterAnterior <= caracter:
        cadenaActual += caracter
        if len(cadenaActual) > len(cadenaMasLarga):
            cadenaMasLarga = cadenaActual
    else:
        cadenaActual = caracter
    caracterAnterior = caracter
    
print("La subcadena en orden alfabético más larga es: " + cadenaMasLarga)
