import json
def crearInfo(*args):
    if(checkFile(args[0])==False):
        with open('data/'+args[0], "w") as write_file:
                json.dump(args[1], write_file,indent = 4)
                write_file.close()
    else:
        with open("data/"+args[0],'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data
            file_data["user"].append(args[1])
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            print('creado con exito¡')
            file.close()
            
def crearInfo3(filename, data):
    with open('data/' + filename, 'w') as file:
        json.dump(data, file, indent=4)
        
        
def crearInfo2(*args):
    if(checkFile(args[0])==False):
        with open('data/'+args[0], "w") as write_file:
                json.dump(args[1], write_file,indent = 4)
                write_file.close()
    else:
        with open("data/"+args[0],'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data
            file_data["Evento"].append(args[1])
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            print('creado con exito¡')
            file.close()
                             
def editarInfo(*args):
        with open('data/'+args[0],'w') as write_file:
             json.dump(args[1],write_file, indent=4)
             write_file.close()
                             
def delInfo(file_name,data,index):
    rta = input("¿Seguro que desea eliminar el dato? (S/N): ").upper()
    if rta == "S":
        del data['user'][index]
        with open("data/" + file_name, 'w') as file:
            json.dump(data, file, indent=4)
            file.close()
        print("El dato fue eliminado correctamente")
    elif rta == "N":
        print("Acción cancelada por el usuario")
    else:
        print("La opción es inválida. No se realizó ninguna tarea.")
    input("Presione Enter para continuar...")

def delInfo(file_name,data,index):
    rta = input("¿Seguro que desea eliminar el dato? (S/N): ").upper()
    if rta == "S":
        del data['user'][index]
        with open("data/" + file_name, 'w') as file:
            json.dump(data, file, indent=4)
            file.close()
        print("El dato fue eliminado correctamente")
    elif rta == "N":
        print("Acción cancelada por el usuario")
    else:
        print("La opción es inválida. No se realizó ninguna tarea.")
    input("Presione Enter para continuar...")
    
def delInfo2(file_name,data,index):
    rta = input("¿Seguro que desea eliminar el dato? (S/N): ").upper()
    if rta == "S":
        del data['Evento'][index]
        with open("data/" + file_name, 'w') as file:
            json.dump(data, file, indent=4)
            file.close()
        print("El dato fue eliminado correctamente")
    elif rta == "N":
        print("Acción cancelada por el usuario")
    else:
        print("La opción es inválida. No se realizó ninguna tarea.")
    input("Presione Enter para continuar...")        

def LoadInfo(fileName):
        with open('data/'+fileName, "r") as read_file:
            dicc = json.load(read_file)
            read_file.close()
        return dicc

def checkFile(filePath):
    try:
        with open('data/'+filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
