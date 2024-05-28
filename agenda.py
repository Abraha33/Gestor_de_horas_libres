import crud
import crudE as ce
import core
import os
agenda=[]
dircontacto={"data":[]}
direvento={"data1":[]}
isMenuActivate=True

if __name__ == "__main__":
    print("****************************************") 
    print("*¡Bienvenidos a Gestor de horas libres!*")
    print("****************************************")
    os.system("pause")
    os.system('cls')
    while isMenuActivate==True:
        print("****************************************") 
        print("*             Menu Principal           *")
        print("****************************************")
        if(core.checkFile('contacto.json')):
            dircontacto=core.LoadInfo('contacto.json')
            
        else:
            core.crearInfo('contacto.json',dircontacto)
        if (core.checkFile('Eventos.json')):
            direvento=core.LoadInfo('Eventos.json') 
        else:
            core.crearInfo2('Evento.json',direvento)
            #Login para entrar al Inicio
        isLogin=True
        while isLogin==True:
            
            print("****************************************") 
            print("*                Login                 *")
            print("****************************************")
            data = core.LoadInfo("contacto.json")  # Load the data from the file
            attempts = 0
            isAttemp=True
            while isAttemp==True:
                username = input('Usuario: ')
                password = input('Contraseña: ')
                attempts += 1
                user_found = False
                for user in data["user"]:
                    if user["username"] == username and user["password"] == password:
                        personal_data=user['personal_data']['0']
                        nombre=personal_data['nombre']
                        perfil=user['perfil']
                        print(f'¡Bienvenido{perfil}: {nombre}!')
                        isAttemp=False
                        user_found=True
                        break
                
                if user_found:
                    isLogin=False
                    
                    break
                else:
                    if attempts < 3:
                        print(f"Usuario o contraseña incorrectos\nTienes {3 - attempts} oportunidades restantes")
                    elif attempts==3:
                        print("Has alcanzado el máximo de intentos")
                        rta = input("¿Te quieres registrar (S/N): ").upper()
                        if rta == "S":
                            # Lógica para agregar un nuevo usuario
                            crud.AddDataDicc()
                            print("Registro exitoso. Puedes iniciar sesión ahora.")
                            isAttemp = False
                            isLogin = True
                            attempts = 0
                        else:   
                            isLogin = False
                            continue_prompt = input("¿Quieres continuar? (S/N): ").upper()
                            if continue_prompt == "S":
                                attempts = 0
                                isLogin = True
                            else:
                                print("¡Hasta luego!")
                                isInitActivate = False
                                isMenuActivate = False
                                break   

        #Inicio de usuario 
        isInitActivate=True
        while isInitActivate==True:
            print("****************************************") 
            print("*                Inicio                *")
            print("****************************************")
            print("1.Perfil\n2.Eventos")
            option=int(input("Tu: "))
            isProfileActivate=False
            isEventActivate=False
            if option==1:
                isProfileActivate=True
            elif option==2:
                isEventActivate=True
                
                    
            while isProfileActivate==True:
                print("***************************************")
                print("*                Perfil               *")
                print("***************************************")
                if user['perfil']=="Estudiante":    
                    print("1.Actualizar datos personales\n2.Ver Perfil\n3.Eliminar\n4.Actualizar horas libres")
                    option=int(input("Tu: "))
                    if option==1:
                        crud.BuscarData(dircontacto,username) #Actualizar datos
                    elif option==2:
                        crud.VerData(dircontacto,username) #Ver perfil
                    elif option==3:
                        crud.EliminarUsuario(dircontacto,username) #Eliminar usuario
                        dircontacto=core.LoadInfo('contacto.json')
                    elif option==4:
                        ce.AddHours(direvento,dircontacto,username)
                    else:
                        print('Vuelve a intentarlo')
                elif user['perfil']=="Profesor":
                    print("1.Actualizar datos personales\n2.Ver Perfil\n3.Eliminar")
                    option=int(input("Tu: "))
                    if option==1:
                        crud.BuscarData(dircontacto,username) #Actualizar datos
                    elif option==2:
                        crud.VerData(dircontacto,username) #Ver perfil
                    elif option==3:
                        crud.EliminarUsuario(dircontacto,username) #Eliminar usuario
                        dircontacto=core.LoadInfo('contacto.json')
                    else:
                        print('Vuelve a intentarlo')
                rta = input("¿Deseas salir del Perfil? (S/N): ").upper()
                if rta == "S":
                    isProfileActivate = False
                    print("¡Hasta luego!")
                    break
                elif rta=="N":
                    isProfileActivate=True
                    
            while isEventActivate==True:
                print("***************************************")
                print("*                Eventos              *")
                print("***************************************")
                if user['perfil']=="Estudiante":
                    print("1.Eventos disponibles\n2.Inscritos\n3.Darse de baja")
                    option=int(input("Tu: "))
                    if option==1:
                        ce.register_events(username)
                    elif option==2:
                        crud.showRegisterEvent(dircontacto,username)
                    elif option==3:
                        crud.DarseBaja(direvento,dircontacto,username)
                    else:
                        print('Vuelve a intentarlo')
                
                elif user['perfil']=="Profesor":
                    print("1.Crear Evento\n2.Ver\n3.Autorizar\n4.Eliminar")
                    option=int(input("Tu: "))
                    if option==1:
                        ce.createEvent(username)
                    elif option==2:
                        ce.SeeEvents(direvento,username)
                    elif option==3:
                        ce.CheckAsist(direvento,username)
                    elif option==4:
                        ce.DeleteEvent(direvento,username)
                        direvento=core.LoadInfo('Eventos.json')
                    else:
                        print('Vuelve a intentarlo')
                rta = input("¿Deseas salir del Eventos? (S/N): ").upper()
                if rta == "S":
                    isEventActivate = False
                    print("¡Hasta luego!")
                    break
                elif rta=="N":
                    isEventActivate=True
            rta = input("¿Deseas salir del Inicio? (S/N): ").upper()
            if rta == "S":
                isInitActivate=False
                print("¡Hasta luego!")
                break
            elif rta=="N":
                isInitActivate=True
                isMenuActivate=True
        rta = input("¿Deseas cerrar Menú? (S/N): ").upper()
        if rta == "S":
            isMenuActivate=False
            print("¡Adios!")
            break
        elif rta=="N":
            isMenuActivate=True



                
