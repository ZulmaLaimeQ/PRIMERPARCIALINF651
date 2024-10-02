#///////////PROBLEMA1//////////////
def es_perfecto(n: int):
    suma_div = 0
    for i in range(1, n):
        if n % i == 0:
            suma_div += i
    return suma_div == n
try:
    numero = int(input("Introduce un numero entero: ")) 
    if numero > 0:
        if es_perfecto(numero):
            print(f"{numero} es un numero perfecto")
        else:
            print(f"{numero} no es un numero perfecto")
    else:
        print("Introduce un numero mayor que 0")
except ValueError:
    print("Introduce un numero entero")




#//////////PROBLEMA2///////////
leds_por_digito = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}
def contar_leds(numero: int) -> int:
    numero_str = str(numero)
    total_leds = sum(leds_por_digito[digito] for digito in numero_str)
    return total_leds
try:
    numero = int(input("Introduce un numero entero: "))
    leds = contar_leds(numero)
    print(f"El numero {numero} se puede formar con {leds} leds")
except ValueError:
    print("Introduce un numero entero")