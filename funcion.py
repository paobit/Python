

from datetime import datetime

from functools import reduce

class establecimiento:
        
    def cursar(self):
        if establecimiento== "cocina":
            print("Curso abierto")
        elif establecimiento == "idioma":
            print("Curso abierto")
        elif establecimiento == "arte":
            print("Curso abierto")
        elif establecimiento =="tecnología":
            print("Curso abierto")
        elif establecimiento=="manualidades":
            print("Curso abierto")
        else:
            print("No hay está disponible")

  

    
def ordenar(curso):
    curso = ['tecnologia', 'cocina', 'idioma', 'arte', 'manualidades' ]
    curso.sort()
    print(curso)
    curso.sort(key = str.lower)
    print(curso)

class inscripcion:
    def __init__(self, nro, fecha):
                self.__nro = nro
                self.__fecha = fecha   
    
    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        self.__fecha = fecha

    def getNro(self):
        return self.__nro

    def setNro(self, nro):
        self.__nro = nro

    nro = property(getNro, setNro)
    fecha = property(getFecha, setFecha)


f1 = inscripcion(1, datetime(2019, 1, 1))
f2 = inscripcion(8, datetime(2019, 1, 5))
f3 = inscripcion(9, datetime(2019, 1, 2))
f4 = inscripcion(2, datetime(2019, 1, 9))

lista_fechas = [f1,f2,f3,f4]

fecha_ordenada_nro = sorted(lista_fechas, key=lambda objeto: objeto.nro)
print("Ordenamiento por nro:")
for s in fecha_ordenada_nro:
    print(s.nro, s.fecha)

fecha_ordenada_fecha = sorted(lista_fechas, key=lambda objeto: objeto.fecha)
print("Ordenamiento por fecha:")
for s in fecha_ordenada_fecha:
    print(s.nro, s.fecha)

class matriculacion:
        
    def matricular(self):
        if self.alumno <=30:
            self.alumno += 1
            print("Matricular", self.alumno, "se puede")
        else:
            print("No quedan más vacantes")

    

class total_curso:

    def abonar(self):
        if self.__alu_regular == 100:
            print("abona", self.__alu_regular, "total")
        elif matriculacion == 80:
            print("abona", self._alu_regular, "80%")
        elif matriculacion== 50:
            print("abona", self._alu_regular, "50%")
        else:
            print("No es alumno regular")
    
    def sumar(abonar):
        return matriculacion
    l = [matriculacion]
    suma = reduce(sumar, l)   
    print("Suma: ", suma)

    def sumar(abonar):
        return establecimiento
    l = [establecimiento]
    suma = reduce(sumar, l)   

    print("Suma: ", suma)

    

datetime()
reduce()
establecimiento.sumar()  


    
    


