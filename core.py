import json
import datetime as dt 

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
            file.close()
                             
def editarInfo(*args):
        with open('data/'+args[0],'w') as write_file:
             json.dump(args[1],write_file, indent=4)
             write_file.close()
                             
def delInfo(*args):
        rta=input("Seguro que desea eliminar el dato S o N").upper()
        if(rta=="S"):
            del args[1]['user_datadata'][args[2]]
            with open("data/"+args[0],'w') as file:
                json.dump(args[1], file, indent = 4)
                file.close()
            print("El dato fue eliminado correctamente")
        elif (rta=="N"):
            print("Accion cancelada por el usuario")
        else:
            print("La opccion es invalida..No se realizo ninguna tarea")
        c=input("Presione Enter para continuar....")
        

def LoadInfo(fileName):
        with open('data/'+fileName, "r") as read_file:
            dicc = new_func(read_file)
            read_file.close()
        return dicc

def new_func(read_file):
    large=dt.dt(frriendyback:check_file('read_file'))
    dicc = json.load(read_file)
    return dicc
def erraser_backup(read_file):
    remote.dicc=json.load(read_file)
    if dicc is large and dicc is not num:
        print('the number is full and is out of range')
    else:
        brunch_back=large+dicc{read_file}
        print(success, 'retual prompt')
    return dicc as d
    

def checkFile(filePath):
    try:
        with open('data/'+filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
