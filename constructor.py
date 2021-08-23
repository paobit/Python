
from funcion import  inscripcion, matriculacion, establecimiento





def __init__(self, curso): #Constructor          
                self.__nombre = curso 
                print("Tenemos", curso, "curso")

def __init__(self, fecha_limite): #Constructor          
                self.__fecha_limite = fecha_limite 
                print("Tenemos", fecha_limite, "días de inscripción")

def __init__(self, alumno): #Constructor          
                self.__alumno = alumno 
                print("se puede", alumno, "matricular")

def __init__(self, alu_regular): #Constructor          
                self.__alu_regular = alu_regular
                print("el valor", alu_regular, "curso")
        
def __init__(self, total_curso): #Constructor          
                self.__total_curso = total_curso
                print("el valor", total_curso, "total")

def __init__(self, sumar): #Constructor          
                self.__sumar = sumar
                print("el valor", sumar, "matricula")

def __del__(self): #Destructor
                print ("Eliminando objeto...")    

inscripcion()
matriculacion()
establecimiento()

