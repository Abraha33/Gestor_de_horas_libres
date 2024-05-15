import crud
import crudE as ce
import core
import os
agenda=[]
dircontacto={"data":[]}
isMenuActivate=True

if __name__ == "__main__":
    print("****************************************") 
    print("*¡Bienvenidos a Gestor de horas libres!*")
    print("****************************************")
    os.system("pause")
    os.system('cls')
    if(core.checkFile('contacto.json')):
        dircontacto=core.LoadInfo('contacto.json')
    else:
        core.crearInfo('contacto.json',dircontacto)    
    while isMenuActivate==True:
        os.system('cls')
        print("****************************************") 
        print("*            ¡Menu Principal           *")
        print("****************************************")
        #//Mensaje de bienvenida explicando
        #//funcion aplicacion de gestor de horas libres
        os.system('cls')
        print("                  Inicio                ")
        #login de usuario y contraseña
        isLogin=True
        while isLogin==True:
            data = core.LoadInfo("contacto.json")  # Load the data from the file
            isAttemp = True
            attempts = 0
            while isAttemp==True and attempts < 3:
                username = input('Usuario: ')
                password = input('Contraseña: ')
                user_found = False
                for user in data["user"]:
                    if user["username"] == username and user["password"] == password:
                        print(f'¡Bienvenido {username}!')
                        isAttemp = False
                        isLogin = False
                        user_found = True
                        break
                
                if not user_found:
                    attempts += 1
                    if attempts < 3:
                        print(f"Usuario o contraseña incorrectos\n Tienes {3-attempts} oportunidades restantes")
                    else:
                        print("Has alcanzado el máximo de intentos")
                        rta = input("Te quieres registrar (S/N): ").upper()
                        if rta == "S":
                            crud.AddDataDicc()
                            data = core.LoadInfo('contacto.json')
                            isAttemp = False
                            isLogin = True
                        elif rta == "N":
                            rta = input("¿Quieres continuar? (S/N): ").upper()
                            if rta == "S":
                                attempts = 0
                            else:
                                isAttemp = False
                                isLogin = False
                                print("¡Hasta luego!")
                                isMenuActivate=False
                                break
                            
        #revisar diferencia de función
        """
-----------------------------------------------------------------------------------------------------------------------        
        #login de usuario y contraseña
        isLogin=True
        while isLogin==True:
            data = core.LoadInfo("contacto.json")  # Load the data from the file
            isAttemp=True
            while isAttemp==True:
                attempts = 1
                username = input('Usuario: ')
                password = input('Contraseña: ')
                for user in data["user"]:
                    if user["username"] == username and user["password"] == password:
                        print(f'¡Bienvenido {username}!')
                        isAttemp=False
                        isLogin=False
                        break
                    else:
                        attempts +=1
                        print(f"Incorrect username or password\n Tienes {4-attempts} oportunidades restantes" )
                        
                        if isAttemp==True and attempts==3:
                            print("Maximum attempts reached")
                            rta = input("Te quieres registrar S o N ")
                            if rta.upper() == "S":
                                crud.AddDataDicc()
                                dircontacto=core.LoadInfo('contacto.json')
                                isAttemp=False
                                isLogin=True
                            elif rta.upper()=="N":
                                rta=input("Quieres continuar S o N")
                                if rta.upper()=="S":
                                    attempts=0
                                elif rta.upper()=="N":
                                    isAttemp=False
                                    isLogin=False
                                    print("¡Hasta luego!")
                                isMenuActivate=False
                                break
----------------------------------------------------------------------------------------------------------------------                                
        """
        data=core.LoadInfo("contacto.json")
        #Mostrando perfiles de tipo-usuario
        for personal_data in data['user']:
            if personal_data['username']== username and personal_data["perfil"]=='Estudiante':
                personal_data=personal_data["personal_data"]["0"]
                print(f"""****************************************
*               Estudiante                 *
********************************************
Código: {personal_data['codigo']}
Nombre: {personal_data['nombre']}
Correo: {personal_data['email']}
telefono:{personal_data['telefono']}
programa:{personal_data['programa']} 
                    
                    """)
                                
            elif personal_data["perfil"]=="Profesor":
                personal_data=personal_data["personal_data"]["0"]
                print(f"""*******************************************
*                 Admin                     *
*********************************************
Codigo:   {personal_data['codigo']}
Nombre:   {personal_data['nombre']}
Facultad: {personal_data['facultad']}
Correo:   {personal_data['email']}
                """)
                print("eventos")
                ce.createEvent()
                
                

                
            
            
