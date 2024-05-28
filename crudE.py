import core as cr
import os
import locale
from datetime import datetime, timedelta

def createEvent(username):
    dicc={}
    dicInsc={}
    dicAsis={}
    os.system('cls')
    print("****************************************")
    print("*¡            Crear Evento            !*")
    print("****************************************")
    isEventItem = True
    while isEventItem:
        isAddEvent = True
        while isAddEvent:
            value=0   
            os.system("pause")
            os.system('cls')
            Id = int(input("Id: "))
            name = input("Titulo: ")
            
            # Extrayendo fecha inicio y fecha final
            date_time, date_time4 = CreateDate()  
            dateout = date_time - timedelta(days=3)
            
            content = input("Descripcion: ")
            place = input("Lugar: ")   
            valid_for = int(input('¿Cuantas horas libres valen? '))
            
            today = datetime.now()  
            # Evento disponible si no pasa de 3 días hábiles
            available = today < dateout  
            
            dicInsc.update({value:{}})
            dicAsis.update({value:{}})
            dicc["Inscritos"]=dicInsc
            dicc["Asistencia"]=dicAsis
            lista_eventos = {
                "Id": Id,
                "Creado": username,
                "Titulo": name,
                "Desde": date_time.strftime("%A, %d %B %Y %H:%M"),
                "Hasta": date_time4.strftime("%A, %d %B %Y %H:%M"),
                "lugar": place,
                "Descripcion": content,
                "Horas libres": valid_for,
                "Disponible": available,
                "Inscritos":dicInsc,
                "Asistencia":dicAsis
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

def register_events(username):
    os.system('cls')
    v = True
    while v:
        user_data = cr.LoadInfo('contacto.json')  # Extrae archivo de usuarios
        for user in user_data['user']:
            if user['username'] == username:
                if "eventos_inscritos" not in user:
                    user["eventos_inscritos"] = {"0": {}}
                eventos_inscritos = user["eventos_inscritos"]["0"]
                index = max(map(int, eventos_inscritos.keys()), default=0) + 1

                while True:
                    eventos_data = cr.LoadInfo('Eventos.json')
                    eventos = eventos_data['Evento']
                    personal_data=user["personal_data"]["0"]
                    print("-----------------------------------------------------------------------------------------------------")
                    print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(10)}|\t{'Titulo Evento'.ljust(25)}|\t{'Desde'.ljust(20)}|\t{'Hasta'.ljust(20)}|\t{'Lugar'.ljust(15)}|\t{'Descripcion'.ljust(25)}|\t{'Horas libres'.ljust(10)}|\t{'Disponible'.ljust(10)}".expandtabs())
                    print("-----------------------------------------------------------------------------------------------------")
                    
                    indice = 1
                    for item in eventos:
                        if item['Disponible']==True:       
                            print(f"{str(indice).ljust(5)}|\t{str(item['Id']).ljust(10)}|\t{item['Titulo'].ljust(25)}|\t{item['Desde'].ljust(20)}|\t{item['Hasta'].ljust(20)}|\t{item['lugar'].ljust(15)}|\t{item['Descripcion'].ljust(25)}|\t{str(item['Horas_libres']).ljust(10)}".expandtabs())
                            indice += 1
                    
                    items = int(input("Escriba el número del evento a guardar: "))
                    
                    # Evento seleccionado
                    select_event = eventos[items - 1]  
                    
                    op = int(input(f'Usted eligió {select_event["Titulo"]}\n1. Guardar\n2. Elegir de nuevo\nIngrese su opción: '))
                    
                    if op == 1:
                        # Extraer los campos
                        evento_reducido = {
                            "id_evento": select_event["Id"],
                            "nombre_evento": select_event["Titulo"],
                            "fecha_inicio": select_event["Desde"],
                            "fecha_fin": select_event["Hasta"],
                            "horas_libres": select_event["Horas_libres"]
                        }
                        datos_reducidos={
                            "codigo":personal_data["codigo"],
                            "nombre":personal_data["nombre"],
                        }

                        user['eventos_inscritos']['0'][str(index)] = evento_reducido
                        for evento in eventos_data['Evento']:
                            if evento['Id'] == select_event['Id']:
                                if "Inscritos" not in evento:
                                    evento["Inscritos"] = {"0": {}}
                                inscritos = evento["Inscritos"]["0"]
                                inscritos_index = max(map(int, inscritos.keys()), default=0) + 1
                                inscritos[str(inscritos_index)] = datos_reducidos
                                break
                        # Guardar los datos actualizados en contacto.json
                        cr.crearInfo3('contacto.json', user_data)
                        cr.crearInfo3("Eventos.json",eventos_data)
                        break
                    elif op == 2:
                        continue
                    else:
                        print("Opción no válida")
                        continue

        rta = input('¿Desea inscribirse en otro evento? (S/N): ').upper()
        if rta == 'N':
            v = False
            
def CheckAsist(data, username):
    os.system('cls')
    eventos = data['Evento']

    # Imprimir lista de eventos
    print("-----------------------------------------------------------------------------------------------------")
    print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(10)}|\t{'Titulo'.ljust(25)}|\t{'Lugar'.ljust(15)}".expandtabs())
    print("-----------------------------------------------------------------------------------------------------")
    indice=1
    for item in eventos:
        print(f"{str(indice).ljust(5)}|\t{str(item['Id']).ljust(10)}|\t{item['Titulo'].ljust(25)}|\t{item['lugar'].ljust(15)}".expandtabs())
        indice=indice+1
    # Solicitar al usuario que elija un evento
    items= int(input("Escriba el número del evento para ver la lista de inscritos: "))
    selected_event = eventos[items-1]

    # Imprimir los detalles de los inscritos en el evento seleccionado
    print(f"\nDetalles del evento seleccionado:")
    print(f"Id: {selected_event['Id']}")
    print(f"Titulo: {selected_event['Titulo']}")
    print(f"Lugar: {selected_event['lugar']}")
    print(f"Descripcion: {selected_event['Descripcion']}")
    print(f"Horas libres: {selected_event['Horas_libres']}")
    print(f"Disponible: {selected_event['Disponible']}")
    print("-----------------------------------------------------------------------------------------------------")
    
    if "Inscritos" in selected_event and "0" in selected_event["Inscritos"]:
        asistencia = selected_event["Inscritos"]["0"]
        print("Lista de inscritos:")
        print("-----------------------------------------------------------------------------------------------------")
        print(f"{'Item'.ljust(5)}|\t{'Codigo'.ljust(10)}|\t{'Nombre'.ljust(25)}".expandtabs())
        print("-----------------------------------------------------------------------------------------------------")
        for key, valor in asistencia.items():
            print(f"{key}:{valor}")
            modif=input(f'El estudiante {valor} asistió al evento? S/N:')
            if modif.upper() == "S":
                asistencia[key] = {"codigo": valor["codigo"], "nombre": valor["nombre"], "asistio": True}
            elif modif.upper() == "N":
                asistencia[key] = {"codigo": valor["codigo"], "nombre": valor["nombre"], "asistio": False}

        selected_event["Asistencia"]["0"] = asistencia
        cr.editarInfo("Eventos.json",data)
        print("Actualizado con exito")
    else:
        print("No hay inscritos en este evento.")

    input('Presione enter para continuar')

def AddHours(event_data,data,username):
    #Se btiene horas libres recientes de usuario
    for user in data['user']:
        if user['username']==username:
            rendimiento=user['rendimiento']['0']
            Horas_libres=int(rendimiento.get("Horas_libres",0))
    #Se buscan eventos a los que asistió usuario
    eventos_asistidos=[]
    for evento in event_data['Evento']:
        if "Asistencia" in evento and "0" in evento["Asistencia"]:
            for key, asistencia in evento["Asistencia"]["0"].items():
                if asistencia.get('codigo') == user['personal_data']['0']['codigo'] and asistencia.get('asistio'):
                    eventos_asistidos.append(evento)
    #Se suman todas las horas
    total_horas=sum(int(evento['Horas_libres']) for evento in eventos_asistidos)
    rendimiento['Horas_libres']=Horas_libres+total_horas
    cr.editarInfo("contacto.json",data)
    cr.editarInfo("Eventos.json",event_data)
    print("Se agregado con exito")
    
def SeeEvents(data,username):
    for user in data['Evento']:
        if user['Creado']==username:
            print("-----------------------------------------------------------------------------------------------------")
            print(f"                            {user['perfil']}:Eventos inscritos                                       ") 
            print("-----------------------------------------------------------------------------------------------------")
            print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(15)}|\t{'nombre_evento'.ljust(25)}|\t{'Fecha Inicio'.ljust(10)}|\t{'Fecha Final'.ljust(15)}|\t{'Horas Libres'.ljust(20)}".expandtabs())
            print("-----------------------------------------------------------------------------------------------------")
            print(f"{str(1).ljust(5)}|\t{str(user['id_evento']).ljust(15)}|\t{user['nombre_evento'].ljust(25)}|\t{str(user['fecha_inicio']).ljust(10)}|\t{str(user['fecha_fin']).ljust(15)}|\t{str(user['horas_libres']).ljust(15)}".expandtabs())        
        else:
            print("No hay eventos inscritos con este usuario")
            break

def DeleteEvent(data,username):
    #Usuario solo puede eliminar eventos creados por él mismo
    for i, event in enumerate(data['Evento']):
        if event['Creado']==username:
            print("-----------------------------------------------------------------------------------------------------")
            print(f"                            {username}:Eventos inscritos                                       ") 
            print("-----------------------------------------------------------------------------------------------------")
            print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(15)}|\t{'Titulo'.ljust(25)}|\t{'Fecha Inicio'.ljust(10)}|\t{'Fecha Final'.ljust(15)}|\t{'Lugar'.ljust(20)}|\t{'Horas_libres'.ljust(15)}".expandtabs())
            print("-----------------------------------------------------------------------------------------------------")
            indice=1
            for item in event['Creado']:
                print(f"{str(indice).ljust(5)}|\t{str(item['Id']).ljust(15)}|\t{item['Titulo'].ljust(25)}|\t{item['Desde'].ljust(10)}|\t{item['Hasta'].ljust(15)}|\t{item['lugar'].ljust(15)}|\t{str(item['Horas_libres']).ljust(15)}".expandtabs())        
                indice=indice+1
            items=int(input("Ingrese el numero de evento a eliminar:"))
            selected_event=data['Evento'][items-1]
            evento_reducido={
                "Id":selected_event['Id'],
                "Titulo":selected_event["Titulo"],
                "Fecha":selected_event["Desde"]
            }
            print(f'Usted eligio el evento: {evento_reducido}')
            cr.delInfo2('Eventos.json',data,i)
            break
        else:
            print("No hay eventos inscritos con este usuario")
            break
        

    
    
    
    
