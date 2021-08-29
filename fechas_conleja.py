def fechas(ocasion, sentimiento):

    respuesta = input("Esa fecha fue " + ocasion)
    respuesta_2 = input("Y tú que es lo que más recuerdas de ese día?: ")
    print(sentimiento)


menu = """

Estos son los recuerdos de Luleja plasmados en código:

1- Martes 24 de Agosto 2021
2- Sabado 24 de Julio 2021
3- 


Escoge una fecha: """

opcion = int(input(menu))

if opcion == 1:
    fechas("Nuestro viaje a Guatavita y una de las mejores expereciencias", "Cada momento a tu lado fue relmente especial incluso nuestra resolución de conflictos jaja")
elif opcion == 2:
    fechas("Celebración de nuestro segundo aniversario", "Uno de los momentos más importantes en mi vida, lograr una relacion tan fuerte a tu lado")
elif opcion == 3:
    pass
else:
    fechas("Tienes que seleccionar un número de la lista Guevota")


