from array import array
import hashlib
import random
import string
import sys
import time
import matplotlib.pyplot as plt


def get_keys_with_value(dic, value):
    return [key for key, val in dic.items() if val == value]

def FuncionResumen (n): 
    result = hashlib.md5(n.encode())
    return (result.hexdigest()) [0:10] 


def FuncionRecodificante(n,tam): #LA ENTRADA SEA IGUAL QUE LA SALIDA (T)
    texto = ""
    while (len(texto) < tam):
        for i in n:  #de esta forma el hash tiene que ser igual a la constante de la contraseña, por eso devolvemos el texto a la altura del while
            constanteASumar = "2"
            sum = hex(int(i.swapcase(), 16) + int(constanteASumar, 16))
            nDecimal = int(sum, base=16)
            nDecimal += 97 
            texto += chr(nDecimal)
    return texto 


def arcoiris(tam,nEntradas):
    diccionario = {}
    #Crear nEntradas contraseñas 
    contEntradas = 0
    while (contEntradas <= nEntradas):
        contador = 1
        password = (''.join(random.choice(string.ascii_lowercase) for _ in range(tam)))
        password1 = password   
        # for j in range (1,tam-1,1):
        #     password1 = FuncionRecodificante (FuncionResumen(password1),tam) #paso h -> r->

        while (contador<tam - 1): #número que quieres que se repita el proceso para obtener
            password1 = FuncionRecodificante (FuncionResumen(password1),tam) #paso h -> r->
            contador += 1
        
        hashAlmacenar = FuncionResumen(password1)
        if hashAlmacenar not in diccionario:
            diccionario [hashAlmacenar] = password #la última solo hay que aplicar al hash
            contEntradas +=1
    print ('--------------DICCIONARIO--------------')       
    print (diccionario)
    print ('--------------DICCIONARIO--------------')  
   

#arcoiris (5,10)

def arcoirisCompleto(tam,nEntradas):
    diccionario = {}
    #Crear nEntradas contraseñas 
    contEntradas = 0
    while (contEntradas <= nEntradas):
        contador = 1
        password = (''.join(random.choice(string.ascii_lowercase) for _ in range(tam)))
        password1 = password   
        # for j in range (1,tam-1,1):
        #     password1 = FuncionRecodificante (FuncionResumen(password1),tam) #paso h -> r->

        while (contador<tam - 1): #número que quieres que se repita el proceso para obtener
            password1 = FuncionRecodificante (FuncionResumen(password1),tam) #paso h -> r->
            contador += 1
        
        hashAlmacenar = FuncionResumen(password1)
        if hashAlmacenar not in diccionario:
            diccionario [hashAlmacenar] = password #la última solo hay que aplicar al hash
            contEntradas +=1
    print ('--------------DICCIONARIO--------------')       
    print (diccionario)
    print ('--------------DICCIONARIO--------------') 

    contraseñaABuscar = 'antoni' #mismos caracteres que t-1
    hashContraseñaABuscar = FuncionResumen (contraseñaABuscar)
    #hashBusqueda = hashContraseñaABuscar
    for z in range (1, tam, 1):
        if hashContraseñaABuscar in diccionario.keys():
            print ("Encontrado en la fila--> HASH:", hashContraseñaABuscar, "PASSWORD:", diccionario.get(hashContraseñaABuscar), "PasswordInicial:" ,contraseñaABuscar,"hashinicial:", FuncionResumen (contraseñaABuscar))
            break
        hashContraseñaABuscar = FuncionResumen(FuncionRecodificante(hashContraseñaABuscar,tam)) #busca en la última columna y si no está va a hacer Resumen y Recodificar
            
    if (z == tam-1): #NO LO VA A ENCONTRAR
        sys.exit() #return None

        
    pwd = diccionario[hashContraseñaABuscar] #para buscarla, como ya sabemos la fila
    contadorWhile = 0 #se puede dar el caso que el final de la fila tengan el mismo hash y esa no tenga el hash a buscar, por eso hay que encontrar el bucle
    while (FuncionResumen(pwd) != hashContraseñaABuscar):
        if (contadorWhile == tam):
            return False
        pwd = FuncionRecodificante(FuncionResumen(pwd),tam)
        contadorWhile +=1
    return pwd


#print ("Reconstrucción en esa fila-->", arcoirisCompleto (6,100000))
#print (FuncionResumen ("fqfqc"), FuncionResumen("tonic"))

def arcoiris100Pruebas(tam,nEntradas):
    diccionario = {}
    #Crear nEntradas contraseñas 
    contEntradas = 0
    while (contEntradas <= nEntradas):
        contador = 1
        password = (''.join(random.choice(string.ascii_lowercase) for _ in range(tam)))
        password1 = password   
  

        while (contador<tam - 1): #número que quieres que se repita el proceso para obtener
            password1 = FuncionRecodificante (FuncionResumen(password1),tam) #paso h -> r->
            contador += 1
        
        hashAlmacenar = FuncionResumen(password1)
        if hashAlmacenar not in diccionario:
            diccionario [hashAlmacenar] = password #la última solo hay que aplicar al hash
            contEntradas +=1
    print ('--------------DICCIONARIO--------------')       
    print (diccionario)
    print ('--------------DICCIONARIO--------------') 
    inicio = fin = tiempoTotal = 0 #solo quiero que busque el tiempo que tarda en buscarlo, ignoro en construir la tabla
    ValoresX = []
    ValoresTiempoY = []
    contraseñasEncontradas = []
    ValoresTiempoYBool = 0
    for i in range (0,100,1):
        contraseñaABuscar = (''.join(random.choice(string.ascii_lowercase) for _ in range(tam)))
        ValoresX.append (contraseñaABuscar)
        inicio = time.perf_counter()
        hashContraseñaABuscar = FuncionResumen (contraseñaABuscar)
        for z in range (1, tam, 1):
            if hashContraseñaABuscar in diccionario.keys():
                contraseñasEncontradas.append (contraseñaABuscar)
                print ("Encontrado en la fila--> HASH:", hashContraseñaABuscar, "PASSWORD:", diccionario.get(hashContraseñaABuscar), "PasswordInicial:" ,contraseñaABuscar,"hashinicial:", FuncionResumen (contraseñaABuscar))
                fin = time.perf_counter()
                tiempoTotal = fin - inicio
                ValoresTiempoY.append(tiempoTotal)
                ValoresTiempoYBool = 1
                break
            ValoresTiempoYBool = 0
            hashContraseñaABuscar = FuncionResumen(FuncionRecodificante(hashContraseñaABuscar,tam)) #busca en la última columna y si no está va a hacer Resumen y Recodificar
        i += 1  
        if (z == tam-1 and ValoresTiempoYBool==0):
            ValoresTiempoY.append(0)
    print (ValoresX)
    print (ValoresTiempoY)
    plt.plot(ValoresX, ValoresTiempoY, "xr") #para poner cruces para saber dónde van los puntos
    plt.ylabel('segundos')
    plt.xlabel('contraseñas')
    plt.plot (ValoresX,ValoresTiempoY)
    plt.show() 
    
    pwd = diccionario[hashContraseñaABuscar] #para buscarla, como ya sabemos la fila
    contadorWhile = 0 #se puede dar el caso que el final de la fila tengan el mismo hash y esa no tenga el hash a buscar, por eso hay que encontrar el bucle
    while (FuncionResumen(pwd) != hashContraseñaABuscar):
        if (contadorWhile == tam):
            return False
        pwd = FuncionRecodificante(FuncionResumen(pwd),tam)
        contadorWhile +=1
    return pwd #pero puede que pwd no sea la real!
    
#print (FuncionResumen ("qghglqghgl"), FuncionResumen("gboywio"))

print ("Reconstrucción en esa fila-->", arcoiris100Pruebas (10,100000000))
