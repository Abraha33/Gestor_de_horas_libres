import core as cr
import os
import time

def HorasCarrera(data):
    dicc={}
    cr.LoadInfo('carreras.json')
    indice=1
    print("-------------------------------------------")
    print(f"{'Item'.ljust(5)}|\t{'nombre'.ljust(5)}|\t{'email'.ljust(5)}|\t{'codigo'.ljust(5)}|\t{'telefono'.ljust(5)}|\t{'carrera'}.ljust(5)".expandtabs())
    print("-------------------------------------------")
    for item in data ['carrera']:
        print(f"{str(indice).ljust(5)}|\t{item['nombre'].ljust(30)}|\t{item['email'].ljust(20)})".expandtabs())
        indice=indice+1
    v=input("presione enter para continuar...")
    items=int(input("escriba el numero de contacto a eliminar "))
    
        
        

def AddDataDicc():
    dicc = {}
    dicData = {}
    os.system('cls')
    print("****************************************")
    print("*¡                Menu               !*")
    print("****************************************")
    isDataItem = True
    while isDataItem == True:
        username = input("Usuario:              ")
        password = input("Contraseña:           ")
        v=int(input('Estudiante[1]\nProfesor[2]'))
        if v==1:
            v='Estudiante'
            ocupacion=v
        elif v==2:
            v='Profesor'
            ocupacion=v
        os.system("pause")
        os.system('cls')
        isAddData = True
        while isAddData == True:
            #Usuario Estudiante
            if ocupacion=="Estudiante":
                valor = len(dicData)
                nombre = input("Nombre del usuario:    ")
                email = input("Email del usuario:      ")
                codigo = int(input("Código:                "))
                telefono = int(input("Telefono:             "))
                carrera=input("Carrera:                ")
                
                dicData.update({valor:{"nombre":nombre,"email":email,"codigo":codigo,"telefono":telefono,"carrera":carrera}})
                rta = input('Desea crear otro usuario más S o N')
                if rta.upper() == "S":
                    isAddData = True
                elif rta.upper() == "N":
                    isAddData = False
            #Usuario Profesor
            elif ocupacion=="Profesor":
                valor=len(dicData)
                nombre=input("Nombre de usuario           ")
                codigo=int(input("código:                 "))  
                carrera=input("Facultad:                   ")    
                email=input("Correo:                   ")
            #///función para eventos   
                #Eventos: 
                dicData.update({valor:{"nombre":nombre,"email":email,"codigo":codigo,"carrera":carrera}})
                rta = input('Desea crear otro usuario más S o N')
                if rta.upper() == "S":
                    isAddData = True
                elif rta.upper() == "N":
                    isAddData = False
            os.system("pause")
        os.system('cls')
        dicc["personal_data"] = dicData
        contacto = {
                "username": username,
                "password": password,
                "perfil":ocupacion,
                "personal_data": dicData
        }
        cr.crearInfo("contacto.json", contacto)
        #Checklist
        rta = input("Desea salir S o N")
        if rta.upper() == "S":
            isDataItem = False
        elif rta.upper() == "N":
            isDataItem = True                
                
def RecargarData(diccionario):
    cr.RefrescarData("contacto.json",diccionario)
    
def VerData(data):
    os.system('cls')
    for item in data['data']:
        print(f"{item['nombre']}|\t{item['email']}|\t{item['codigo']}".expandtabs())
    v=input("Presione enter para continuar....")

def BuscarData(data,username):
    os.system('cls')
    for user in data['user']:
        if user['username']==username:    
            if user['perfil'] == "Estudiante":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Email'.ljust(25)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Carrera'.ljust(20)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{personal_data['email'].ljust(25)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['carrera'].ljust(15)}".expandtabs())        

            elif user['perfil'] == "Profesor":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ")  
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Facultad'.ljust(20)}|\t{'Email'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['facultad'].ljust(20)}|\t{personal_data['email'].ljust(25)}".expandtabs())
                                       
    items=1
    selected_user=data['user'][items-1]
    personal_data=selected_user['personal_data']['0']
    for key, valor in personal_data.items():
        print(f'{key}:{valor}')
        modif=input(f'Desea modificar {key} S o N: ')
        if(modif.upper()=='S'):
            personal_data [key]=input(f'Ingrese un nuevo {key} : ')
    cr.editarInfo('contacto.json',data)
    v=input('presione enter para continuar')

def BorrarData(data):
    os.system('cls')
    indice=1
    print("-------------------------------------------")
    print(f"{'Item'.ljust(5)}|\t{'nombre'.ljust(5)}|\t{'email'.ljust(5)}|\t{'codigo'.ljust(5)}|\t{'telefono'.ljust(5)}|\t{'carrera'}.ljust(5)".expandtabs())
    print("-------------------------------------------")
    for item in data ['data']:
        print(f"{str(indice).ljust(5)}|\t{item['nombre'].ljust(30)}|\t{item['email'].ljust(20)})".expandtabs())
        indice=indice+1
    v=input("presione enter para continuar...")
    items=int(input("escriba el numero de contacto a eliminar "))
    cr.delInfo('contacto.json',data)
    
    
    
def EliminarUsuario(data,username):
    os.system('cls')
    for i, user in enumerate (data['user']):
        if user['username']==username:    #Determina posición de usuario
            if user['perfil'] == "Estudiante":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Email'.ljust(25)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Carrera'}.ljust(15)".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{personal_data['email'].ljust(25)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['carrera'].ljust(20)}".expandtabs())        

            elif user['perfil'] == "Profesor":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ")  
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Facultad'.ljust(20)}|\t{'Email'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['facultad'].ljust(20)}|\t{personal_data['email'].ljust(25)}".expandtabs())
    
    
            cr.delInfo('contacto.json',data,i) #Elimina usuario en posición determinada
    v=input("presione enter para continuar...")                   
    
"""def register_events(file_path):
    print('Estos son los eventos disponibles: ')
    with open(file_path, 'r',encoding='utf8') as file:
        lines = file.readlines()
    events = []
    for line in lines:
        event_data = line.strip().split(',')
        if len(event_data) >= 4:
            event = {
                'name': event_data[0],
                'date': event_data[1],
                'time': event_data[2],
                'type': event_data[3]
            }
            events.append(event)
            print(f"{len(events)}.{event['name']}-{event['date']}-{event['type']}")
        else:
            pass
    return events
events=register_events('Events.txt')
v=True
while v==True:
    rta=input('Dese elegir un evento S o N')
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
    
        
    





    
    
