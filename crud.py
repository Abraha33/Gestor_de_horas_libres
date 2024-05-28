import core as cr
import os
import time

def HorasCarrera():
    data=cr.LoadInfo('carreras.json')
    carrera=data['carrera']
    indice=1
    print("-------------------------------------------")
    print(f"{'Item'.ljust(10)}|\t{'carrera'.ljust(10)}|\t{'horas_libres_minimas'.ljust(10)}|\t{'semestres'.ljust(10)}".expandtabs())
    print("-------------------------------------------")
    for item in carrera:
        print(f"{str(indice).ljust(5)}|\t{item['carrera'].ljust(30)}|\t{str(item['horas_libres_minimas']).ljust(15)})|\t{str(item['semestre']).ljust(10)})".expandtabs())
        indice=indice+1
    items=int(input("escriba el numero a guardar "))
    selected=carrera[items-1]
    print(f'Usted eligió {selected}')
    v=input("presione enter para continuar...")
    carrera=selected['carrera']
    horas_libres_minimas=selected['horas_libres_minimas']
    semestre=selected['semestre']
    
    return carrera,horas_libres_minimas,semestre

def AddDataDicc():
    dicc = {}
    dicPersonalData = {}
    dicProgress={}
    dicEvent={}
    os.system('cls')
    print("****************************************")
    print("*¡        Creando Usuario             !*")
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
        isAddPersonalData = True
        while isAddPersonalData == True:
            #Usuario Estudiante
            if ocupacion=="Estudiante":
                valor=0
                nombre = input("Nombre del usuario:    ")
                email = input("Email del usuario:      ")
                codigo = int(input("Código:                "))
                telefono = int(input("Telefono:             "))
                carrera,horas_libres_minimas,semestre=HorasCarrera()
                HLR= 0 #Horas Libres Registradas
                PromedioS= round(horas_libres_minimas/semestre,None)
                PromedioM=round(PromedioS/6,None)
                PromedioA=round(PromedioS*2,None)
                Faltantes=semestre-HLR
                dicPersonalData.update({valor:{"nombre":nombre,"email":email,"codigo":codigo,"telefono":telefono,"carrera":carrera,"horas_libres_minimas":horas_libres_minimas}})
                dicProgress.update({valor:{"Horas_libres":HLR,"Faltantes":Faltantes,"Promedio_Mensual":PromedioM,"Promedio_Semestral":PromedioS,"Promedio_Anual":PromedioA,}})
                dicEvent.update({valor:{}})
                dicc["personal_data"] = dicPersonalData
                dicc["eventos_incritos"]=dicEvent
                contacto = {
                        "username": username,
                        "password": password,
                        "perfil":ocupacion,
                        "personal_data": dicPersonalData,
                        "rendimiento":dicProgress,
                        "eventos_incritos":dicEvent        
                }
                #Usuario Profesor
            elif ocupacion=="Profesor":
                valor=0
                nombre=input("Nombre de usuario           ")
                codigo=int(input("código:                 "))  
                carrera,horas_libres_minimas,semestre=HorasCarrera()   
                email=input("Correo:                   ")
            
                dicPersonalData.update({valor:{"nombre":nombre,"email":email,"codigo":codigo,"carrera":carrera}})
                dicc["personal_data"] = dicPersonalData
                contacto = {
                        "username": username,
                        "password": password,
                        "perfil":ocupacion,
                        "personal_data": dicPersonalData,      
                }
        
            cr.crearInfo("contacto.json", contacto)
            break
            os.system("pause")
            os.system('cls')
        rta = input('Desea crear otro usuario más S o N')
        if rta.upper() == "S":
            isAddPersonalData = True
        elif rta.upper() == "N":
            isAddPersonalData = False
        rta = input("Desea salir S o N")
        if rta.upper() == "S":
            isDataItem = False
        elif rta.upper() == "N":
            isDataItem = True    
                    
def RecargarData(diccionario):
    cr.RefrescarData("contacto.json",diccionario)
    
def VerData(data,username):
    os.system('cls')
    for user in data['user']:
        if user['username']==username:    
            if user['perfil'] == "Estudiante":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                            {user['perfil']}:Datos personales                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Email'.ljust(25)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Carrera'.ljust(20)}|\t{'Horas libres mínimas'.ljust(15)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{personal_data['email'].ljust(25)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['carrera'].ljust(15)}|\t{str(personal_data['horas_libres_minimas']).ljust(15)}".expandtabs())        
                rendimiento=user['rendimiento']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                            {user['perfil']}:Rendimiento                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Horas_libres'.ljust(15)}|\t{'Faltantes'.ljust(25)}|\t{'Promedio Mensual'.ljust(25)}|\t{'Promedio Semestral'.ljust(25)}|\t{'Promedio Anual'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{str(rendimiento['Horas_libres']).ljust(15)}|\t{str(rendimiento['Faltantes']).ljust(25)}|\t{str(rendimiento['Promedio_Mensual']).ljust(25)}|\t{str(rendimiento['Promedio_Semestral']).ljust(25)}|\t{str(rendimiento['Promedio_Anual']).ljust(25)}".expandtabs())        
                
            elif user['perfil'] == "Profesor":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ")  
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Código'.ljust(10)}|\t{'Carrera'.ljust(20)}|\t{'Email'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['carrera']).ljust(15)}|\t{personal_data['email'].ljust(25)}".expandtabs())                                   
                v=input("Presione enter para continuar....")


def BuscarData(data, username):
    os.system('cls')
    for user in data['user']:
        if user['username'] == username:
            if user['perfil'] == "Estudiante":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Email'.ljust(25)}|\t{'Código'.ljust(10)}|\t{'Teléfono'.ljust(15)}|\t{'Carrera'.ljust(20)}|\t{'Horas_libres_minimas'.ljust(20)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{personal_data['email'].ljust(25)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['telefono']).ljust(15)}|\t{personal_data['carrera'].ljust(15)}|\t{personal_data['horas_libres_minimas']}".expandtabs())        
                
                for key, valor in personal_data.items():
                    if key == "horas_libres_minimas":
                        break
                    else:
                        print(f'{key}: {valor}')
                        modif = input(f'Desea modificar {key}? (S o N): ')
                        if modif.upper() == 'S':
                            if key == "carrera":
                                carrera, horas_libres_minimas, semestre = HorasCarrera()
                                personal_data[key] = carrera
                                personal_data["horas_libres_minimas"] = horas_libres_minimas 
                            else:
                                personal_data[key] = input(f'Ingrese un nuevo {key}: ')
                    
            elif user['perfil'] == "Profesor":
                personal_data = user['personal_data']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                                             {user['perfil']}                                       ")  
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Código'.ljust(10)}|\t{'Carrera'.ljust(20)}|\t{'Email'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['carrera']).ljust(15)}|\t{personal_data['email'].ljust(25)}".expandtabs())                                   

                for key, valor in personal_data.items():
                    if key == "horas_libres_minimas":
                        break
                    else:
                        print(f'{key}: {valor}')
                        modif = input(f'Desea modificar {key}? (S o N): ')
                        if modif.upper() == 'S':
                            if key == "carrera":
                                carrera, horas_libres_minimas, semestre = HorasCarrera()
                                personal_data[key] = carrera
                            else:
                                personal_data[key] = input(f'Ingrese un nuevo {key}: ')
            break
        
    cr.editarInfo('contacto.json', data)
    

def DarseBaja(event_data, data, username):
    os.system('cls')
    
    # Buscar al usuario
    user_index = None
    usuario = None
    for i, user in enumerate(data['user']):
        if user['username'] == username:
            user_index = i
            usuario = user
            break
    
    if not usuario:
        print("Usuario no encontrado")
        return
    
    if "eventos_inscritos" in usuario and "0" in usuario['eventos_inscritos']:
        eventos_inscritos = usuario['eventos_inscritos']['0']
        
        print("-----------------------------------------------------------------------------------------------------")
        print(f"                            {usuario['perfil']}: Eventos inscritos                                       ")
        print("-----------------------------------------------------------------------------------------------------")
        print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(15)}|\t{'nombre_evento'.ljust(25)}|\t{'Fecha Inicio'.ljust(10)}|\t{'Fecha Final'.ljust(15)}|\t{'Horas Libres'.ljust(20)}".expandtabs())
        print("-----------------------------------------------------------------------------------------------------")
        
        # Mostrar eventos inscritos
        for indice, (key, evento) in enumerate(eventos_inscritos.items(), start=1):
            print(f"{str(indice).ljust(5)}|\t{str(evento['id_evento']).ljust(15)}|\t{evento['nombre_evento'].ljust(25)}|\t{str(evento['fecha_inicio']).ljust(10)}|\t{str(evento['fecha_fin']).ljust(15)}|\t{str(evento['horas_libres']).ljust(15)}".expandtabs())
        
        # Seleccionar el evento del que se quiere dar de baja
        try:
            items = int(input("Escriba el número al que desea darse de baja: "))
            selected_key = list(eventos_inscritos.keys())[items - 1]
            selected_event = eventos_inscritos[selected_key]
        except (IndexError, ValueError):
            print("Selección inválida. Asegúrese de ingresar un número válido.")
            return
        
        eventos_reducido = {
            "id_evento": selected_event['id_evento'],
            "nombre_evento": selected_event['nombre_evento']
        }
        print(f'Usted eligió: {eventos_reducido}')
        
        # Eliminar evento de eventos_inscritos del usuario en contacto.json
        del usuario['eventos_inscritos']['0'][selected_key]
        cr.editarInfo('contacto.json', data)
        
        # Eliminar usuario de la lista de inscritos en Eventos.json
        for evento in event_data['Evento']:
            if evento['Id'] == eventos_reducido['id_evento']:
                if "Inscritos" in evento and "0" in evento["Inscritos"]:
                    inscritos = evento["Inscritos"]["0"]
                    for key, value in list(inscritos.items()):
                        if value.get('nombre') == username:
                            del inscritos[key]
                            break
                break

        cr.editarInfo('Eventos.json', event_data)
        print("Baja realizada con éxito")
    else:
        print("No hay eventos inscritos")

    
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
                print(f"{'Item'.ljust(5)}|\t{'Nombre'.ljust(15)}|\t{'Código'.ljust(10)}|\t{'Carrera'.ljust(20)}|\t{'Email'.ljust(25)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{str(1).ljust(5)}|\t{personal_data['nombre'].ljust(15)}|\t{str(personal_data['codigo']).ljust(10)}|\t{str(personal_data['carrera']).ljust(15)}|\t{personal_data['email'].ljust(25)}".expandtabs())                                   

            cr.delInfo('contacto.json',data,i) #Elimina usuario en posición determinada
                       
def showRegisterEvent(data,username):
     for user in data['user']:
        if user['username']==username: 
            if "eventos_inscritos" in user and "0" in user['eventos_inscritos']:   
                eventos_inscritos = user['eventos_inscritos']['0']
                print("-----------------------------------------------------------------------------------------------------")
                print(f"                            {user['perfil']}:Eventos inscritos                                       ") 
                print("-----------------------------------------------------------------------------------------------------")
                print(f"{'Item'.ljust(5)}|\t{'Id'.ljust(15)}|\t{'nombre_evento'.ljust(25)}|\t{'Fecha Inicio'.ljust(10)}|\t{'Fecha Final'.ljust(15)}|\t{'Horas Libres'.ljust(20)}".expandtabs())
                print("-----------------------------------------------------------------------------------------------------")
                indice=1
                for key,evento in eventos_inscritos.items():   
                    print(f"{str(1).ljust(5)}|\t{str(evento['id_evento']).ljust(15)}|\t{evento['nombre_evento'].ljust(25)}|\t{str(evento['fecha_inicio']).ljust(10)}|\t{str(evento['fecha_fin']).ljust(15)}|\t{str(evento['horas_libres']).ljust(15)}".expandtabs())        
                    indice=indice+1
            else:
                print("No hay eventos inscritos")
                break
                
        
        
