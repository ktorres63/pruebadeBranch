# imprime 
def printMat( mat):
    
    for fila in mat:
        for elem in fila:
            print(elem, end ="\t")
        print()

#filas y columnas
filas = int(input("FILAS: "))
columnas = int(input("COLUMNAS: "))

matriz = []
#ingreso de datos

value=0
for i in range(filas): #filas
    matriz.append([])
    for j in range(columnas): #columnas
        value = value+1
        dato=int(input("ingresa el dato: "))
        matriz[i].append(dato)
       

# buscador
print ("BUSCADOR")
busq=int(input("buscar el dato: "))
for i in range(filas):
    for j in range(columnas):
        if busq==matriz[i][j]:
            print(f"{i},{j}",end=" ")
        
print()

#transpuesta
trans=[]
filT=columnas
colT=filas
for i in range(filT): #filas de trans
    trans.append([])
    for j in range(colT): # columnas de trans
        trans[i].append(matriz[j][i])
print()


print("----MATRIZ--")
printMat(matriz)

print("TRANSPUESTA")
printMat(trans)
    
