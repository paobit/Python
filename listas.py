lc = [0, 1, 2, 3] #Comprensión de listas
m = ["arte", "idioma", "tecnologia"] 
n1 = [s * v for s in m 
        for v in lc 
	    if v > 0]
print(n1)


def mi_generador(n, m, s):
    while(n <= m):
        yield n
        n += s

for n in mi_generador(0, 5, 1):
    print (n)

lista = list(mi_generador(0,5,1))   
print(lista)


la = [0, 1, 2, 3] #Comprensión de listas
m = ["Gonzalez", "Perez", "Lopez"] 
n2 = [s * v for s in m 
        for v in la
	    if v > 0]
print(n2)


def mi_generador(n, m, s):
    while(n <= m):
        yield n
        n += s

for n in mi_generador(0, 5, 1):
    print (n)

lista = list(mi_generador(0,5,1))   
print(lista)


