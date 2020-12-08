import psycopg2
from conexion_bd import conexion

def insertar_bd(n):
    try:
        with conexion.cursor() as cursor:
            if n == 1:
                dato = input("Ingresar cantidad de casos positivos por dia: ")
                query = "INSERT INTO casos_de_covid (covid_recuperados, covid_positivos, covid_fallecidos) VALUES (%s, %s, %s);"
                cursor.execute(query,("0",dato,"0"))
                conexion.commit()
                cursor.close()
            elif n == 2:
                dato = input("Ingresar cantidad de recuperados por dia: ")
                covid_limite = covid_en_hospital()
                if int(dato) <= covid_limite:
                    query = "INSERT INTO casos_de_covid (covid_recuperados, covid_positivos, covid_fallecidos) VALUES (%s, %s, %s);"
                    cursor.execute(query,(dato,"0","0"))
                    conexion.commit()
                    print("Dato insertado correctamente en la base de datos. . .")
                    cursor.close()
                else:
                    print("ERROR: Supera el limite de personas en hospital -> ", covid_limite)
            elif n == 3:
                dato = input("Ingresar cantidad de fallecidos por dia: ")
                covid_limite = covid_en_hospital()
                if int(dato) <= covid_limite:
                    query = "INSERT INTO casos_de_covid (covid_recuperados, covid_positivos, covid_fallecidos) VALUES (%s, %s, %s);"
                    cursor.execute(query,("0","0",dato))
                    conexion.commit()
                    print("Dato insertado correctamente en la base de datos. . .")
                    cursor.close()
                else:
                     print("ERROR: Supera el limite de personas en hospital -> ", covid_limite)
            else:
                print("Ninguna opción es válida")
    except psycopg2.Error as e:
        print("Error al insertar dato a la base de datos: ",e)
    finally:
        conexion.close()

def consultar_bd(n):
    try:
        with conexion.cursor() as cursor:
            if n == 4:
                query2 = "SELECT SUM (covid_positivos) FROM casos_de_covid"
                cursor.execute(query2) 
                row = cursor.fetchone()
                print("Total de Casos Positivos: ",row[0])
                cursor.close()
            elif n == 5:
                query2 = "SELECT SUM (covid_recuperados) FROM casos_de_covid"
                cursor.execute(query2)
                row = cursor.fetchone()
                print("Total de Recuperados: ",row[0])
            elif n == 6:
                query2 = "SELECT SUM (covid_fallecidos) FROM casos_de_covid"
                cursor.execute(query2)
                row = cursor.fetchone()
                print("Total de Fallecidos: ",row[0])
                cursor.close()
            elif n == 7:
                covid_limite = covid_en_hospital()
                print("Cantidad de personas en Hospital: ",covid_limite)
            else:
                print("Ninguna opción es válida")
    except psycopg2.Error as e:
        print("Error al consultar dato en la base de datos: ",e)
    finally:
        conexion.close()

def covid_en_hospital():
    print("Verificando cantidad de personas en hospital . . .")
    try:
        with conexion.cursor() as cursor:
            #CONSULTA
            query = "SELECT SUM(covid_recuperados + covid_fallecidos), SUM(covid_positivos) FROM casos_de_covid"
            cursor.execute(query)
            row = cursor.fetchone()
            covid_sum_no_hospital = int(row[0])
            covid_acumulado = int(row[1])

            #CALCULO 
            covid_limite = covid_acumulado - covid_sum_no_hospital

            return covid_limite
    except psycopg2.Error as e:
        print("Error al consultar dato en la base de datos: ",e)