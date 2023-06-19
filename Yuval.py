from array import array
import hashlib
import zlib
import time
import matplotlib.pyplot as plt


diccionario = []
#Quiero generar 2^m/2 
#array = ["Buenos dias" , "Antonio"]
salida = zlib.crc32(b"Soy Antonio")


def FuncionResumen (n): 
    result = hashlib.md5(n.encode())
    return (result.hexdigest()) [0:9] 
                                                                                                       
def get_keys_with_value(dic, value):
    return [key for key, val in dic.items() if val == value]

def Yuval (m):

    t = pow (2,m/2)
    
    #hacer con tuplas mejor que tupla
    tupla1 = ("Buenos días,","Buenas tardes,")
    tupla2 = ("soy Antonio","soy Luis")
    tupla3 = ("Esta tarde","Esta noche")
    tupla4 = ("voy","me apetece")
    tupla5 = ("a ir","ir")
    tupla6 = ("a ganar","a jugar")
    tupla7 = ("un partido","un padel")
    tupla8 = ("por un lado","además")
    tupla9 = ("tendra","habra")
    tupla10 = ("un premio","un trofeo")
    tupla11 = ("al mejor","al peor")
    tupla12 = ("participante.","jugador.")
    tupla13 = ("Despues,","A parte")
    tupla14 = ("Llovera","Nevara")
    tupla15 = ("e iremos","y comeremos")
    tupla16 = ("a la pista de baile","en la pista de baile")
    tupla17 = ("Asi que","Por lo tanto")
    tupla18 = ("estaremos","permaneceremos")
    tupla19 = ("todos juntos","todos separados")
    tupla20 = ("cuanto antes","el mayor tiempo")
      

    listaLegitimo = []
    listaLegitimo = listaLegitimo + [tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7,tupla8,tupla9,tupla10,tupla11,tupla12,tupla13,tupla14,tupla15,tupla16,tupla17,tupla18,tupla19,tupla20]
    #listaLegitimo.extend (array01,array02,array03,array04,array05,array06,array07,array08,array09,array10,array11,array12,array13,array14,array15,array16,array17,array18,array19,array20)
    print (listaLegitimo)


    tuplasucia1 = ("Buenos noches,","Buenas,")
    tuplasucia2 = ("soy Manolo","soy Paco")
    tuplasucia3 = ("Quizas","Puede ser")
    tuplasucia4 = ("que no me conozcas","soy tu primo")
    tuplasucia5 = ("y","ahora")
    tuplasucia6 = ("vamos","nos llevan")
    tuplasucia7 = ("al parque","al rio")
    tuplasucia8 = ("a","para")
    tuplasucia9 = ("comer","tragar")
    tuplasucia10 = ("palomitas","gusanitos")
    tuplasucia11 = ("con","y")
    tuplasucia12 = ("tu tia.","tu abuelo")
    tuplasucia13 = ("Espero que","Seguro que")
    tuplasucia14 = ("te gustara","lo disfrutaras")
    tuplasucia15 = ("Despues","Seguidamente")
    tuplasucia16 = ("iremos","nos llevaran")
    tuplasucia17 = ("al cine","al teatro")
    tuplasucia18 = ("a ver","a observar")
    tuplasucia19 = ("Avatar","Detective en peligro")
    tuplasucia20 = ("te encantara","espero que te guste")
    
    
    
    
    listaIlegitimo = []
    listaIlegitimo = listaIlegitimo + [tuplasucia1,tuplasucia2,tuplasucia3,tuplasucia4,tuplasucia5,tuplasucia6,tuplasucia7,tuplasucia8,tuplasucia9,tuplasucia10,tuplasucia11,tuplasucia12,tuplasucia13,tuplasucia14,tuplasucia15,tuplasucia16,tuplasucia17,tuplasucia18,tuplasucia19,tuplasucia20]
    
    
    diccionario = {}
    
    for i in range (0,pow(2,m),1):
        if (t>i): #solo quieres generar t = 2^m/2 modificaciones
            numero_decimal = i
            binarios = [] #lista de unos y ceros 
            while numero_decimal != 0:
                # se almacena el módulo en el orden correcto
                binarios.insert(0, numero_decimal % 2)
                numero_decimal //= 2
            while (len(binarios)!= m/2):
                binarios.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash = ""
            for i2, d in enumerate (binarios):
                cadenaParaHash += listaLegitimo[i2][int(d)] 
            print (binarios)
            # print (cadenaParaHash)
            diccionario[FuncionResumen(cadenaParaHash)] = binarios #[0:10] #guardamos en el diccionario
            #print (diccionario)
        else: break
    
    for j in range (0,pow(2,m),1): #es 2^20
        if (t>j): #solamente en t intentos
            numero_decimal2 = j
            binarios2 = [] #lista de unos y ceros 
            while numero_decimal2 != 0:
                # se almacena el módulo en el orden correcto
                binarios2.insert(0, numero_decimal2 % 2)
                numero_decimal2 //= 2
            while (len(binarios2)!= m/2):
                binarios2.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash2 = ""
            for i3, d2 in enumerate (binarios2):
                cadenaParaHash2 += listaIlegitimo[i3][int(d2)] 
            #print (binarios2)
            #print (cadenaParaHash)
            
            
            if (FuncionResumen(cadenaParaHash2) in diccionario.keys()): #diccionario
                print ("---------Colisión-------------")
                print ("HASH_ILEGITIMO:", FuncionResumen(cadenaParaHash2),"BINARIOS:" ,binarios2,"CADENA:" ,cadenaParaHash2) 
                binariosConstruccion = diccionario.get(FuncionResumen(cadenaParaHash2))
                #print (binariosConstruccion)
                cadenaParaConstruirMsjLegitimo = ""
                for i4, d3 in enumerate (binariosConstruccion):
                        cadenaParaConstruirMsjLegitimo += listaLegitimo[i4][int(d3)] 
                print ("HASH_LEGITIMO:", FuncionResumen(cadenaParaConstruirMsjLegitimo), "BINARIOS:",binariosConstruccion, "CADENA", cadenaParaConstruirMsjLegitimo)
                print ("------------------------------")
                #break #si queremos una colisión solamente
        else: break
    return None
        
#Yuval(40)  
#print (FuncionResumen("Buenas,soy PacoPuede sersoy tu primoahoranos llevanal rioatragargusanitoscontu tia.Espero quelo disfrutarasDespuesiremosal cinea observarDetective en peligrote encantara"))
#print (FuncionResumen("Buenas tardes,soy AntonioEsta nochevoyira ganarun partidopor un ladotendraun trofeoal peorparticipante.A parteNevarae iremosa la pista de baileAsi queestaremostodos separadoscuanto antes"))

def ColisionesYuval (m):
    t = pow (2,m/2)
    
   
    tupla1 = ("Buenos días,","Buenas tardes,")
    tupla2 = ("soy Antonio","soy Luis")
    tupla3 = ("Esta tarde","Esta noche")
    tupla4 = ("voy","me apetece")
    tupla5 = ("a ir","ir")
    tupla6 = ("a ganar","a jugar")
    tupla7 = ("un partido","un padel")
    tupla8 = ("por un lado","además")
    tupla9 = ("tendra","habra")
    tupla10 = ("un premio","un trofeo")
    tupla11 = ("al mejor","al peor")
    tupla12 = ("participante.","jugador.")
    tupla13 = ("Despues,","A parte")
    tupla14 = ("Llovera","Nevara")
    tupla15 = ("e iremos","y comeremos")
    tupla16 = ("a la pista de baile","en la pista de baile")
    tupla17 = ("Asi que","Por lo tanto")
    tupla18 = ("estaremos","permaneceremos")
    tupla19 = ("todos juntos","todos separados")
    tupla20 = ("cuanto antes","el mayor tiempo")
    tupla21 = ("avion","pez")
    tupla22 = ("luz antes","amor")
    tupla23 = ("lapiz","a")
    tupla24 = ("mando","e")
    tupla25 = ("os","hola")
    tupla26 = ("er","qwerty")
    tupla27 = ("asd","iuh")
    tupla28 = ("lol","ecv")
    tupla29 = ("cxc","w")
    tupla30 = ("crts","wwo")
      

    listaLegitimo = []
    listaLegitimo = listaLegitimo + [tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7,tupla8,tupla9,tupla10,tupla11,tupla12,tupla13,tupla14,tupla15,tupla16,tupla17,tupla18,tupla19,tupla20,tupla21,tupla22,tupla23,tupla24,tupla25,tupla26,tupla27,tupla28,tupla29,tupla30]
    
    print (listaLegitimo)


    tuplasucia1 = ("Buenos noches,","Buenas,")
    tuplasucia2 = ("soy Manolo","soy Paco")
    tuplasucia3 = ("Quizas","Puede ser")
    tuplasucia4 = ("que no me conozcas","soy tu primo")
    tuplasucia5 = ("y","ahora")
    tuplasucia6 = ("vamos","nos llevan")
    tuplasucia7 = ("al parque","al rio")
    tuplasucia8 = ("a","para")
    tuplasucia9 = ("comer","tragar")
    tuplasucia10 = ("palomitas","gusanitos")
    tuplasucia11 = ("con","y")
    tuplasucia12 = ("tu tia.","tu abuelo")
    tuplasucia13 = ("Espero que","Seguro que")
    tuplasucia14 = ("te gustara","lo disfrutaras")
    tuplasucia15 = ("Despues","Seguidamente")
    tuplasucia16 = ("iremos","nos llevaran")
    tuplasucia17 = ("al cine","al teatro")
    tuplasucia18 = ("a ver","a observar")
    tuplasucia19 = ("Avatar","Detective en peligro")
    tuplasucia20 = ("te encantara","espero que te guste")
    tuplasucia21 = ("asd","esyu")
    tuplasucia22 = ("ter","vne")
    tuplasucia23 = ("hbva","edsf")
    tuplasucia24 = ("asntander","marca")
    tuplasucia25 = ("si","as")
    tuplasucia26 = ("six","tecla")
    tuplasucia27 = ("sometimes","que te guste")
    tuplasucia28 = ("lucero","c guste")
    tuplasucia29 = ("libro","evc")
    tuplasucia30 = ("pen drive","easde")
    
    listaIlegitimo = []
    listaIlegitimo = listaIlegitimo + [tuplasucia1,tuplasucia2,tuplasucia3,tuplasucia4,tuplasucia5,tuplasucia6,tuplasucia7,tuplasucia8,tuplasucia9,tuplasucia10,tuplasucia11,tuplasucia12,tuplasucia13,tuplasucia14,tuplasucia15,tuplasucia16,tuplasucia17,tuplasucia18,tuplasucia19,tuplasucia20,tuplasucia21,tuplasucia22,tuplasucia23,tuplasucia24,tuplasucia25,tuplasucia26,tuplasucia27,tuplasucia28,tuplasucia29,tuplasucia30]
    
    
    diccionario = {}
    inicio = fin = tiempoTotal = 0 #solo quiero que busque el tiempo que tarda en buscarlo, ignoro en construir la tabla
    ValoresX = []
    ValoresTiempoY = []
    contColisiones = 0

    for i in range (0,pow(2,m),1):
        if (t>i): #solo quieres generar t = 2^m/2 modificaciones
            numero_decimal = i
            binarios = [] #lista de unos y ceros 
            while numero_decimal != 0:
                # se almacena el módulo en el orden correcto
                binarios.insert(0, numero_decimal % 2)
                numero_decimal //= 2
            while (len(binarios)!= m/2):
                binarios.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash = ""
            for i2, d in enumerate (binarios):
                cadenaParaHash += listaLegitimo[i2][int(d)] 
            print (binarios)
            # print (cadenaParaHash)
            diccionario[FuncionResumen(cadenaParaHash)] = binarios #[0:10] #guardamos en el diccionario
            #print (diccionario)
        else: break
    
    for j in range (0,pow(2,m),1): #es 2^20
        inicio = time.perf_counter()
        if (t>j): #solamente en t intentos
            numero_decimal2 = j
            binarios2 = [] #lista de unos y ceros 
            while numero_decimal2 != 0:
                # se almacena el módulo en el orden correcto
                binarios2.insert(0, numero_decimal2 % 2)
                numero_decimal2 //= 2
            while (len(binarios2)!= m/2):
                binarios2.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash2 = ""
            for i3, d2 in enumerate (binarios2):
                cadenaParaHash2 += listaIlegitimo[i3][int(d2)] 
            #print (binarios2)
            #print (cadenaParaHash)
            
            
            if (FuncionResumen(cadenaParaHash2) in diccionario.keys()): #diccionario
                contColisiones += 1
                ValoresX.append (FuncionResumen(cadenaParaHash2))
                fin = time.perf_counter()
                tiempoTotal = fin - inicio
                ValoresTiempoY.append(tiempoTotal)
                print ("---------Colisión-------------")
                print ("HASH_ILEGITIMO:", FuncionResumen(cadenaParaHash2),"BINARIOS:" ,binarios2,"CADENA:" ,cadenaParaHash2) 
                binariosConstruccion = diccionario.get(FuncionResumen(cadenaParaHash2))
                #print (binariosConstruccion)
                cadenaParaConstruirMsjLegitimo = ""
                for i4, d3 in enumerate (binariosConstruccion):
                        cadenaParaConstruirMsjLegitimo += listaLegitimo[i4][int(d3)] 
                print ("HASH_LEGITIMO:", FuncionResumen(cadenaParaConstruirMsjLegitimo), "BINARIOS:",binariosConstruccion, "CADENA", cadenaParaConstruirMsjLegitimo)
                print ("------------------------------")
                #break #si queremos una colisión solamente
        else: 
            print ("Número de colisiones:",contColisiones)
            plt.plot(ValoresX, ValoresTiempoY, "xr") #para poner cruces para saber dónde van los puntos
            plt.ylabel('segundos')
            plt.xlabel('hash')
            plt.plot (ValoresX,ValoresTiempoY)
            plt.show() 
            break
    return None

#ColisionesYuval (36)  

def YuvalTiempoColision (m):
    inicio = final = 0
    inicio = time.perf_counter()
    t = pow (2,m/2)
    
    #hacer con tuplas mejor que tupla
    tupla1 = ("Buenos días,","Buenas tardes,")
    tupla2 = ("soy Antonio","soy Luis")
    tupla3 = ("Esta tarde","Esta noche")
    tupla4 = ("voy","me apetece")
    tupla5 = ("a ir","ir")
    tupla6 = ("a ganar","a jugar")
    tupla7 = ("un partido","un padel")
    tupla8 = ("por un lado","además")
    tupla9 = ("tendra","habra")
    tupla10 = ("un premio","un trofeo")
    tupla11 = ("al mejor","al peor")
    tupla12 = ("participante.","jugador.")
    tupla13 = ("Despues,","A parte")
    tupla14 = ("Llovera","Nevara")
    tupla15 = ("e iremos","y comeremos")
    tupla16 = ("a la pista de baile","en la pista de baile")
    tupla17 = ("Asi que","Por lo tanto")
    tupla18 = ("estaremos","permaneceremos")
    tupla19 = ("todos juntos","todos separados")
    tupla20 = ("cuanto antes","el mayor tiempo")
      

    listaLegitimo = []
    listaLegitimo = listaLegitimo + [tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7,tupla8,tupla9,tupla10,tupla11,tupla12,tupla13,tupla14,tupla15,tupla16,tupla17,tupla18,tupla19,tupla20]
    #listaLegitimo.extend (array01,array02,array03,array04,array05,array06,array07,array08,array09,array10,array11,array12,array13,array14,array15,array16,array17,array18,array19,array20)
    print (listaLegitimo)


    tuplasucia1 = ("Buenos noches,","Buenas,")
    tuplasucia2 = ("soy Manolo","soy Paco")
    tuplasucia3 = ("Quizas","Puede ser")
    tuplasucia4 = ("que no me conozcas","soy tu primo")
    tuplasucia5 = ("y","ahora")
    tuplasucia6 = ("vamos","nos llevan")
    tuplasucia7 = ("al parque","al rio")
    tuplasucia8 = ("a","para")
    tuplasucia9 = ("comer","tragar")
    tuplasucia10 = ("palomitas","gusanitos")
    tuplasucia11 = ("con","y")
    tuplasucia12 = ("tu tia.","tu abuelo")
    tuplasucia13 = ("Espero que","Seguro que")
    tuplasucia14 = ("te gustara","lo disfrutaras")
    tuplasucia15 = ("Despues","Seguidamente")
    tuplasucia16 = ("iremos","nos llevaran")
    tuplasucia17 = ("al cine","al teatro")
    tuplasucia18 = ("a ver","a observar")
    tuplasucia19 = ("Avatar","Detective en peligro")
    tuplasucia20 = ("te encantara","espero que te guste")
    
    
    
    
    listaIlegitimo = []
    listaIlegitimo = listaIlegitimo + [tuplasucia1,tuplasucia2,tuplasucia3,tuplasucia4,tuplasucia5,tuplasucia6,tuplasucia7,tuplasucia8,tuplasucia9,tuplasucia10,tuplasucia11,tuplasucia12,tuplasucia13,tuplasucia14,tuplasucia15,tuplasucia16,tuplasucia17,tuplasucia18,tuplasucia19,tuplasucia20]
    
    
    diccionario = {}
    
    for i in range (0,pow(2,m),1):
        if (t>i): #solo quieres generar t = 2^m/2 modificaciones
            numero_decimal = i
            binarios = [] #lista de unos y ceros 
            while numero_decimal != 0:
                # se almacena el módulo en el orden correcto
                binarios.insert(0, numero_decimal % 2)
                numero_decimal //= 2
            while (len(binarios)!= m/2):
                binarios.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash = ""
            for i2, d in enumerate (binarios):
                cadenaParaHash += listaLegitimo[i2][int(d)] 
            print (binarios)
            # print (cadenaParaHash)
            diccionario[FuncionResumen(cadenaParaHash)] = binarios #[0:10] #guardamos en el diccionario
            #print (diccionario)
        else: break
    
    for j in range (0,pow(2,m),1): #es 2^20
        if (t>j): #solamente en t intentos
            numero_decimal2 = j
            binarios2 = [] #lista de unos y ceros 
            while numero_decimal2 != 0:
                # se almacena el módulo en el orden correcto
                binarios2.insert(0, numero_decimal2 % 2)
                numero_decimal2 //= 2
            while (len(binarios2)!= m/2):
                binarios2.insert (0,0) #insertar ceros en la posición cero, para que se rellene de ceros
            
            cadenaParaHash2 = ""
            for i3, d2 in enumerate (binarios2):
                cadenaParaHash2 += listaIlegitimo[i3][int(d2)] 
            #print (binarios2)
            #print (cadenaParaHash)
            
            
            if (FuncionResumen(cadenaParaHash2) in diccionario.keys()): #diccionario
                print ("---------Colisión-------------")
                print ("HASH_ILEGITIMO:", FuncionResumen(cadenaParaHash2),"BINARIOS:" ,binarios2,"CADENA:" ,cadenaParaHash2) 
                binariosConstruccion = diccionario.get(FuncionResumen(cadenaParaHash2))
                #print (binariosConstruccion)
                cadenaParaConstruirMsjLegitimo = ""
                for i4, d3 in enumerate (binariosConstruccion):
                        cadenaParaConstruirMsjLegitimo += listaLegitimo[i4][int(d3)] 
                print ("HASH_LEGITIMO:", FuncionResumen(cadenaParaConstruirMsjLegitimo), "BINARIOS:",binariosConstruccion, "CADENA", cadenaParaConstruirMsjLegitimo)
                print ("------------------------------")
                final = time.perf_counter()
                print ("El tiempo total es: " , final - inicio ,"segundos", (final - inicio)/60 ,"minutos")
                break #si queremos una colisión solamente
        else: break
    return None
        
YuvalTiempoColision(40) 