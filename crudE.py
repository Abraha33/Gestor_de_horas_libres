import core as cr
import os
import locale
from datetime import datetime

def createEvent():
    dicc={}
    dicEvent={}
    os.system('cls')
    print("****************************************")
    print("*¡            Crear Evento            !*")
    print("****************************************")
    isEventItem = True
    while isEventItem == True:
        isAddEvent=True
        while isAddEvent==True:   
            os.system("pause")
            os.system('cls')
            Id=int(input("Id               :"))
            #// Funcion crear id con numero aleatorio no repetido par id
            name=input("Titulo             :")
            date_time,date_time4=CreateDate() #Creando fecha
            content=input("Descripcion     :")
            place=input("Lugar             :")   
            valid_for=int(input('¿Cuantas horas libres valen?'))
            #//Corregir formato para solicitar informacion
            os.system("pause")
            os.system('cls')
            lista_eventos = {
                    "Id": Id,
                    "Titulo Evento": name,
                    "Desde": date_time,
                    "Hasta":date_time4,
                    "lugar":place,
                    "Descripcion":content,
                    "Horas libres": valid_for
            }
            rta = input('Desea crear otro usuario más S o N')
            if rta.upper() == "S":
                isAddEvent = True
                cr.crearInfo2("Eventos.json",lista_eventos)
            elif rta.upper() == "N":
                isAddEvent = False
        cr.crearInfo2("Eventos.json",lista_eventos)
        #Checklist
        rta = input("Desea salir S o N")
        if rta.upper() == "S":
            isEventItem = False
        elif rta.upper() == "N":
            isEventItem = True
    
def CreateDate():
    locale.setlocale(locale.LC_TIME,'es_ES.UTF-8')
    print('*     Fecha    *')
    day=int(input('Dia:  '))
    month=int(input('Mes: '))
    year=int(input('Año: '))
    print('*      Desde     *')
    hour=int(input('Hora: '))
    minute=int(input('Minuto: '))
    print('*      Hasta     *')
    hour2=int(input('Hora: '))
    minute2=int(input('Minuto: '))
    date_time = datetime(year, month, day, hour, minute)
    date_time2=date_time.strftime("%A, %d %B %Y %H:%M")
    date_time3=datetime(year,month,day,hour2,minute2)
    date_time4=date_time3.strftime("%A, %d %B %Y %H:%M")
    return date_time2, date_time4
        
    
createEvent()