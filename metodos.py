

@classmethod
def setCurso(self, curso):
        self.__curso = curso

def setFechaLimite(self, fecha):
        self.__fecha = fecha

def setFechaLimite(self, nro):
        self.__nro = nro

def setInscripcion(self, inscripcion):
        self.__inscripcion = inscripcion

def setTotalCurso(self, total_curso):
        self._total_curso= total_curso

def setListaCurso(self, lista_cursos):
        self._lista_cursos= lista_cursos

def getListaCurso(self):
        return self.__curso
def getFechaLimite(self):
        return self.__fecha
def getNroLimite(self):
        return self.__nro
def getInscripcion(self):
        return self.__inscripcion
def getTotalCurso(self):
        return self.__total_costo
def getListaCurso(self):
        return self.__lista_cursos

establecimiento= property(setCurso,getListaCurso, getFechaLimite,setFechaLimite, getInscripcion, setInscripcion, getTotalCurso,setTotalCurso, getListaCurso, setListaCurso)


def __str__(self):
        return "{} informacion general {} cursos".format(self.curso, self.fecha_limita, self.inscripcion, self.total_cursos, self.lista_cursos)
       
class AgregarElemento(list): #Creamos una clase Agregarelemento heredando atributos de clase list
    def append(self, alumnos): #Definimos que el método append (de listas) añadirá el elemento alumno
        print ("Añadido el alumno", alumnos) #Imprimimos el resultado del método
        super().append(alumnos) #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                                  #del método append para la variable alumno
 
n2 = AgregarElemento() #Definimos la clase de nuestra lista llamada "Lista1"
n2.append ('Som') #Añadimos un elemento a la lista como lo haríamos normalmente
n2.append('Sam') #Otro elemento...
print(n2)  # Imprimimos la lista para corroborar los alumnos...

class AgregarElemento(list): #Creamos una clase Agregarelemento heredando atributos de clase list
    def append(self, curso): #Definimos que el método append (de listas) añadirá el elemento curso
        print ("Añadido el alumno", curso) #Imprimimos el resultado del método
        super().append(curso) #Incorporamos la función super SIN INDICAR LA CLASE ACTUAL, seguida
                                                    #del método append para la variable alumno

n1 = AgregarElemento() #Definimos la clase de nuestra lista llamada "Lista"
n1.append ('danzas') #Añadimos un elemento a la lista como lo haríamos normalmente
n2.append('carpinteria') #Otro elemento...
print(n2)  # Imprimimos la lista para corroborar los cursos...

n2.modificacion = "danzas" #Modifico atributo público de clase
