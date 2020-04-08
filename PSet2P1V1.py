import math

#Suma el área y el cuadrado del perímetro del polígono regular. 
#Devuelve la suma redondeada a 4 decimales.
def polysum(n,s):
    area = (((0.25*n)*(s**2))/(math.tan(math.pi/n)))
    perimetro = n * s
    resultado = round((area + perimetro**2), 4)
    return resultado

lados = float(input("Dame el numero de lados del polígono regular:\n"))
longitudes = float(input("Dame la longitud de cada lado del polígono regular:\n"))
print(polysum(lados, longitudes))
