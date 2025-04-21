# Convertir números romanos a decimales

Romanos = {
    'I': 1,
    'V': 5,
    'X': 10
}

def romanoAdecimal(romano): 
    decimal = 0
    for i in range(len(romano)):
        if i > 0 and Romanos[romano[i]] > Romanos[romano[i - 1]]:
            decimal += Romanos[romano[i]] - 2 * Romanos[romano[i - 1]] 
        else:
            decimal += Romanos[romano[i]] 
    return decimal

# Bloque principal
romano = input("Introduce un número romano: ").upper()  # .upper() por si lo escriben en minúsculas
decimal = romanoAdecimal(romano)
print(f"El número romano {romano} es igual a {decimal} en decimal.")
