import core as cr
import os
import locale
from datetime import datetime, timedelta

def createEvent(username):
    os.system('cls')
    print("****************************************")
    print("*¡            Crear Evento            !*")
    print("****************************************")
    isEventItem = True
    while isEventItem:
        isAddEvent = True
        while isAddEvent:   
            os.system("pause")
            os.system('cls')
            Id = int(input("Id: "))
            name = input("Titulo: ")
            date_time, date_time4 = CreateDate()  # Creando fecha
            dateout = date_time - timedelta(days=3)
            content = input("Descripcion: ")
            place = input("Lugar: ")   
            valid_for = int(input('¿Cuantas horas libres valen? '))
            today = datetime.now()  # Fecha actual
            available = today < dateout  # Evento disponible si no pasa de 3 días hábiles
            lista_eventos = {
                "Id": Id,
                "Creado": username,
                "Titulo": name,
                "Desde": date_time.strftime("%A, %d %B %Y %H:%M"),
                "Hasta": date_time4.strftime("%A, %d %B %Y %H:%M"),
                "lugar": place,
                "Descripcion": content,
                "Horas libres": valid_for,
                "Disponible": available
                #"inscritos":aa
            }
            cr.crearInfo2("Eventos.json", lista_eventos)
            rta = input('Desea crear otro evento más (S o N)? ')
            isAddEvent = rta.upper() == "S"
        rta = input("Desea salir (S o N)? ")
        isEventItem = rta.upper() != "S"

def CreateDate():
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    print('*     Fecha    *')
    day = int(input('Dia: '))
    month = int(input('Mes: '))
    year = int(input('Año: '))
    print('*      Desde     *')
    hour = int(input('Hora: '))
    minute = int(input('Minuto: '))
    print('*      Hasta     *')
    hour2 = int(input('Hora: '))
    minute2 = int(input('Minuto: '))
    date_time = datetime(year, month, day, hour, minute)
    date_time_end = datetime(year, month, day, hour2, minute2)
    return date_time, date_time_end


def register_events(data,username):
    data=cr.LoadInfo('Eventos.json')
    eventos=data['Evento']
    indice=1
    print("-----------------------------------------------------------------------------------------------------")
    print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(10)}|\t{'Titulo Evento'.ljust(25)}|\t{'Desde'.ljust(20)}|\t{'Hasta'.ljust(20)}|\t{'Lugar'.ljust(15)}|\t{'Descripcion'.ljust(25)}|\t{'Horas libres'.ljust(10)}|\t{'Disponible'.ljust(10)}".expandtabs())
    print("-----------------------------------------------------------------------------------------------------")
    for item in eventos:
        if item['Disponible']==True:
            print(f"{str(indice).ljust(5)}|\t{str(eventos['Id']).ljust(10)}|\t{eventos['Titulo Evento'].ljust(25)}|\t{eventos['Desde'].ljust(20)}|\t{eventos['Hasta'].ljust(20)}|\t{eventos['lugar'].ljust(15)}|\t{eventos['Descripcion'].ljust(25)}|\t{eventos['Horas libres'].ljust(10)}".expandtabs())
            indice=indice+1
    items=int(input("escriba el numero a guardar "))
    selected=eventos[items-1]
    print(f'Usted eligió {selected}')
    v=input("presione enter para continuar...")
    user_data=cr.LoadInfo('contacto.json')
    for user in user_data['user']:
        if user['username']==username:
            user['Rendimiento']["1"].update(selected)
    cr.crearInfo('contacto.json',user_data)
    """while v==True:
        rta=input('Dese otro un evento S o N')
        if rta.upper()=='S':
            v=True
        elif rta.upper()=='N':
            v=False
        else:
            print('Por favor, responde con S o N.')
            continue
        if not events:
            print('No hay eventos disponibles')
        else:
            op=int(input('Ingrese una opción: '))
            #Validando que entrada no este fuera de rango
            if 0<op<len(events):
                select_event=events[op-1]
                print(f"Has seleccionado: {select_event['name']}-{select_event['date']}-{select_event['type']}")
            else:
                print('Por favor, ingresa una opción válida. ')"""
                
        
            
        



