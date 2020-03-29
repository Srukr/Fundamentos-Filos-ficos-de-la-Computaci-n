#Cuenta el número de vocales en el texto que es proporcionado
def analizar(texto):
    cuenta = 0
    for x in texto:
        if(x == "a" or x == "e" or x == "i" or x == "o" or x == "u"):
            cuenta += 1
    return str(cuenta)

string = input("Dame el texto que quieres analizar:\n")
print("El numero de vocales contenidas en el texto es " + analizar(string))


