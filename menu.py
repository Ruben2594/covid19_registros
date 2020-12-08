from consultas_bd import insertar_bd, consultar_bd

def menu():
    menu = """Registros de Casos de COVID-19 2020
    1- Introducir casos por dia
    2- Introducir recuperados por dia
    3- Introducir fallecidos por dia
    4- Consultar total de casos acumulados
    5- Consultar total de recuperados
    6- Consultar total de fallecidos
    7- Consultar total de personas en hospital
    8- Salir
    """
    print(menu) #Imprime menu

    opcion = int(input("Selecciona una opción: ")) #entrada de data
    if opcion == 1:
        insertar_bd(1)
    elif opcion == 2:
        insertar_bd(2)
    elif opcion == 3:
        insertar_bd(3)
    elif opcion == 4:
        consultar_bd(4)
        print("Consulta finalizada. . .")
    elif opcion == 5:
        consultar_bd(5)
        print("Consulta finalizada. . .")
    elif opcion == 6:
        consultar_bd(6)
        print("Consulta finalizada. . .")
    elif opcion == 7:
        consultar_bd(7)
        print("Consulta finalizada. . .")
    else:
        print('Ninguna opción es válida')