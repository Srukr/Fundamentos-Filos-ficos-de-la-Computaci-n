#Regresa el numero de veces que 'bob' aparece en el string proporcionado
texto = input("Dame la cadena de texto que quieres analizar:\n")
patron = "bob"
cuenta = 0
bandera = True
inicio = 0
while bandera:

    a = texto.find(patron, inicio)
    if a == -1:
        bandera = False
        
    else:
        cuenta += 1
        inicio = a+1
print(cuenta)
