# Estudiante: Juan Jose Larrahondo Giron
# Codigo: 8977454

###############################

# Ejercicio 1

print()
def verificarDiagonales(mat):
    numCols = len(mat[0])
    posInicial = 0
    posFinal = numCols - 1

    for row in mat:
        if row[posInicial] != row[posFinal]:
            return False

        posInicial += 1
        posFinal -= 1

    return True


# Prueba Ejercicio 1
mat = [[11, 23, 76, 34, 11],
    [14, 30, 92, 30, 101],
    [12, 45, 58, 92, 22],
    [74, 56, 49, 56, 100],
    [99, 5, 28, 47, 99]]


print(verificarDiagonales(mat))


###############################

# Ejercicio 2

def esCapicua(lista):
    count = len(lista)
    initialPos = 0
    endPos = count - 1

    for num in lista:
        if lista[initialPos] != lista[endPos]:
            return False

        initialPos += 1
        endPos -= 1

    return True


lst1 = [42, 12, 90, 90, 12, 42]
lst2 = [42, 12, 90, 90, 12, 45]

print()
print("Prueba 1", esCapicua(lst1))
print("Prueba 2", esCapicua(lst2))


###############################

# Ejercicio 3a

def diferenciaListas(lista1, lista2):
    listaResultado = []

    for num in lista1:
        if num in lista2:
            lista2.remove(num)

        else:
            listaResultado.append(num)

    return listaResultado


listaA = [40, 10, 22, 12, 33, 33, 33]
listaB = [41, 22, 31, 15, 13, 12, 33, 19]

print()
print("Prueba 1", diferenciaListas(listaA, listaB))
print("Prueba 2", diferenciaListas(listaB, listaA))
print()


###############################

# Ejercicio 3b

def calcularNDiferenciaListas():
    n = int(input())
    listasResultados = []

    for ejecucion in range(n):
        # Primera Linea de la ejecucion
        data1 = input()
        dataSplited1 = data1.split(" ")
        num1 = int(dataSplited1[0])
        listaNStrings1 = dataSplited1[1:num1+1]

        listaNInt1 = []
        for num in listaNStrings1:
            listaNInt1.append(int(num))

        # Primera Linea de la ejecucion
        data2 = input()
        dataSplited2 = data2.split(" ")
        num2 = int(dataSplited2[0])
        listaNStrings2 = dataSplited2[1:num2+1]

        listaNInt2 = []
        for num in listaNStrings2:
            listaNInt2.append(int(num))

        listasResultados.append(
            diferenciaListas(listaNInt1, listaNInt2)
        )
    
    for lista in listasResultados:
        lstEnTexto = str(lista)
        print(lstEnTexto[1:-1])

print("Ejecución Ejercicio 3b")
calcularNDiferenciaListas()
print()


###############################

# Ejercicio 4

def mostrarPrimos(N):
    listaNums= []
    print("Números primos entre 1 y", N)

    for num in range(2, N):
        esPrimo = True
        for i in range(2, num):
            if num % i == 0:
                esPrimo = False
        
        if esPrimo == True:
            listaNums.append(num)
            print("-->" + str(num) + ",")

    print()
    print("Números entre 1 y "+str(100)+" con suma de dígitos con valor primo:")
    for num in listaNums:
        sumaDigitos = 0
        for digito in str(num):
            sumaDigitos += int(digito)

        esPrimo = True
        for i in range(2, sumaDigitos):
            if sumaDigitos % i == 0:
                esPrimo = False
        
        if esPrimo == True:
            print(str(num) + ", ", end="")


print("Prueba 1")
mostrarPrimos(100)
print()
print()
