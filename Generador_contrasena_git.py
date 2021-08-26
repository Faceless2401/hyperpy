import random


def generar_contrasena():
    pais = ["Colombia", "Argentina", "Peru", "Venezuela"]
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
      'U', 'V', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{',
     '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^',
      '&', '$', '#', '"']
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    caracteres = pais + simbolos + numeros

    contrasena = []

    for i in range(5):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("la nueva contraseña para ti es la siguiente: " + contrasena) 
    print("la segunda contraseña para ti rama 2 es la siguiente: " + contrasena) 

if __name__ == "__main__":
    run()