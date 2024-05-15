import core as cr
import os
import datetime
datetime
def createEvent():
    dicc={}
    dicEvent={}
    os.system('cls')
    print("****************************************")
    print("*¡            Crear Evento            !*")
    print("****************************************")
    isEventItem = True
    while isEventItem == True:
        os.system("pause")
        os.system('cls')
        Id=int(input("Id               :"))
        #// Funcion crear id con numero aleatorio no repetido par id
        
        name=input("Titulo             :")
        date_time=input("Fecha\nEjemplo Ene 03 2024 14:20:")
        date_time=datetime.datetime.strptime(date_time, '%b %d %Y %H:%M')
        #//formato fecha_tiempo no lo cambia el tipo Dec 03 2024 15:36
        content=input("descripcion     :")
        place=input("Lugar             :")   
        valid_for=int(input('Valido por:'))
        #//Corregir formato para solicitar informacion
        os.system("pause")
        os.system('cls')
        lista_eventos = {
                "Id": Id,
                "Titulo Evento": name,
                "Descripción":content,
                "Cuando": date_time,
                f"Valido por{valid_for} horas libres":valid_for
        }
        cr.crearInfo("Eventos.json",lista_eventos)
        #Checklist
        rta = input("Desea salir S o N")
        if rta.upper() == "S":
            isEventItem = False
        elif rta.upper() == "N":
            isEventItem = True                
  