import numpy as np

def iguales(lista1, lista2):           #compara las dos listas 
    c=0
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            c=c+1
            if c==1:
                return False
    return True

def patron_usuario():
    print("Dame el número de renglones: ")
    renglones=int(input())
    print("Dame el número de columnas: ")
    columnas=int(input())
    matriz=[]
    for r in range(renglones):
        lista=[]
        for c in range(columnas):
            print ("Teclea el dato para el renglón", r, "la columna",c)
            dato=int(input())
            lista.append(dato)
        matriz.append(lista)
        
    return matriz

def mostrar_matriz(prueba):
    renglones=len(prueba[0])
    columnas=len(prueba[0])
    for r in range(renglones):
        for c in range(columnas):
            print(prueba[r][c], end = " ")
        print()

#Vectores entrenamiento
C0=[1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1]
C1=[1,-1,-1,-1,1,1,-1,1,1,1,1,-1,-1,1,1,1,-1,1,1,1,1,-1,-1,-1,1]
C2=[1,-1,-1,-1,1,1,1,-1,1,1,1,1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,1]
C3=[1,1,1,1,1,1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,1,1,1,1]
C4=[1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,1]

#matriz 25x25
W = []


for i in range(0,len(C0)):
    for j in range(0,len(C0)):
        W.append( (((C0[i])*(C0[j])) +((C1[i])*(C1[j]))+((C2[i])*(C2[j]))+((C3[i])*(C3[j]))+((C4[i])*(C4[j])))*(1/25))
        
W= np.array(W).reshape(len(C0),len(C0))    #arregla la matriz en 25x25                   
for i in range(len(C0)):
    for j in range(len(C0)):
        if i==j:
            W[i][j]=0
cont=0          #Nos sirve para contar el numero de iteraciones que va a tener

pru=patron_usuario()
mostrar_matriz(pru)
prueba=[]          #

for t in pru:
    for w in t:
        prueba.append(w)

while True:
    listprueba= []
    
    pn = np.dot(W,prueba)
    
    for i in pn:
        if i>0 or i == 0:
            listprueba.append(1)
        elif i<0 :
            listprueba.append(-1)
    
    if iguales(listprueba,C0) or iguales(prueba,C0):
        print("A")
        break
    elif iguales(listprueba,C1) or iguales(prueba,C1):
        print("E")
        break   
    elif iguales(listprueba,C2) or iguales(prueba,C2):
        print("I")
        break
    elif iguales(listprueba,C3) or iguales(prueba,C3):
        print("O")
        break
    elif iguales(listprueba,C4) or iguales(prueba,C4):
        print("U")
        break
    elif cont==100000:
        print("Sin coincidencia")
        break
    cont+=1    