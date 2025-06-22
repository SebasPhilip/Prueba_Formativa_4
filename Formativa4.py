turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"], 
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"], 
    "012": ["Julian Martinez", "Argentina", "19-09-2023"], 
    "014": ["Agustin Morales", "Argentina", "28-03-2024"], 
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"], 
    "006": ["Maria Lopez", "Mexico", "08-12-2023"], 
    "007": ["Joao Silva", "Brasil", "20-06-2024"], 
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"], 
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"], 
    "008": ["Ana Santos", "Brasil", "03-10-2023"], 
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"], 
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"], 
}
opcion=0
pais=""
valores=0
pais_dict=""

def turistas_por_pais(pais):
    while True: 
        pais=input("Ingrese el país a buscar: ").lower().strip()
        valores=turistas.values()
        turistas_pais=[]

        for valor in valores:
            if valor[1].lower().strip() == pais.lower().strip():
                turistas_pais.append(valor[0])
            
        if turistas_pais:
            print(f"Los turistas encontrados de {pais} son {turistas_pais}")
            break
        else:
            print("No se ha encontrado un turista del país señalado")

                           
                        
mes=0
valores=0
def turistas_por_mes(mes):
    while True:
        try:
            mes=int(input("Ingrese el mes de la búsqueda (1-12): "))
        except ValueError:
            print ("El mes no puede estar escrito en palabras o hay un error al escribir el número. Intente de nuevo.")
        else:
            if mes <=0 or mes >12:
                print ("El mes no puede estar dentro del valor señalado.")
            elif 1 <= mes <= 12:
                valores=turistas.values()
                meses_turistas=0
                for valor in valores:
                    fechas=valor[2]
                    diamesano= int(fechas.split("-")[1])
                    
                    if diamesano==mes:
                        meses_turistas+=1
                    porcentaje=(meses_turistas/len(valores))*100
                print(f"El porcentaje de turistas ingresados en el mes {mes} es {porcentaje}%")
            break
nombre_turista=""
def eliminar_turista():
    while True:
        nombre_turista=input("Ingrese el nombre del turista a eliminar: ").lower().strip()
        claves=turistas.keys()
        turista_eliminar=None
        for clave in claves:
            turista=turistas[clave]
            if turista[0].lower().strip()==nombre_turista.lower().strip():
                turista_eliminar=clave
                print("Coincidencia encontrada")
        if turista_eliminar!=None:
            del turistas[turista_eliminar]
            print("Borrado con éxito")
            break
        else:
            print("Sin resultados.")

while True:
    print ("*** MENU PRINCIPAL ***")
    print ("1.- Turistas por país.")
    print ("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print ("4.- Salir ")
    try:
        opcion=int(input("Ingrese la opción para continuar: --> "))
    except ValueError:
        print("La opción debe ser un número positivo.")
    else: 
        if opcion==1:
            turistas_por_pais(pais)
        elif opcion==2:
            turistas_por_mes(mes)
        elif opcion==3:
            eliminar_turista()
        elif opcion==4:
            print ("Terminando programa...Hasta luego.")
            break
        else:
            print("Elija una opción válida.")
