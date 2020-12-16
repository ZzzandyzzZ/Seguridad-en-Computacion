import operator

def preprocesar(texto):
    texto=texto.upper()
    reemplazos=(
        ("Á","A"),
        ("É","E"),
        ("Í","I"),
        ("Ó","O"),
        ("Ú","U"),
        ("Ñ","N")
    )
    for a,b in reemplazos:
        texto=texto.replace(a,b)
    texto="".join(filter(lambda texto:(texto.isalpha() or texto==" "), texto))
    return texto
def enCesar(entrada,salida,k,spaces=False):
    texto = open(entrada, "r")
    texto=texto.read()
    result=""
    texto=preprocesar(texto)
    for i in texto:
        if(spaces and i==" "):
            result+=i
            continue
        val=ord(i)+k
        result+=chr(val) if val<=ord('Z') else chr(val-ord('Z')+ord('A')-1)
    salida = open(salida,"w")
    salida.write(result)
    return result
def deCesar(texto,k,spaces=False):
    result=""
    texto=preprocesar(texto)
    for i in texto:
        if(spaces and i==" "):
            result+=i
            continue
        val=ord(i)-k
        result+=chr(val) if val>=ord('A') else chr(ord('Z')+val-ord('A')+1)
    return result
def crip_diccionario(entrada,salida,spaces=False):
    diccionario = open("diccionario.txt", "r")
    diccionario = diccionario.read().split(" ")
    cifer = open(entrada, "r")
    cifer=cifer.read()
    answer=0
    resultado=""
    for i in range(1,26):
        analisis = deCesar(cifer,i,spaces)
        total = 0
        for j in diccionario:
            total+=analisis.find(j)
        if(total>answer):
            answer=total
            resultado=analisis
            k=i
    print("EL MAYOR NUMERO DE COINCIDENCIAS FUE: {}".format(total))
    print("EL VALOR DE K CORRESPONDIENTE ES {}".format(k))
    resultado+="\n FACTOR K = {}".format(k)
    salida = open(salida,"w")
    salida.write(resultado)

def get_frecuencias(file="texto",n=1):
    frecuencias={}
    for i in range(1,n+1):
        name="{}.txt".format(file) if(n==1) else "{}{}.txt".format(file,i)
        texto = open(name, "r")
        texto=texto.read()
        texto=preprocesar(texto)
        for i in texto:
            if(i==" "):continue
            if(i not in frecuencias):
                frecuencias[i]=0
            else:
                frecuencias[i]+=1
    frecuencias = dict(sorted(frecuencias.items(), key=operator.itemgetter(1), reverse=True))
    return frecuencias

def crip_frecuencias(entrada,salida,spaces=False):
    cifer = open(entrada, "r")
    cifer=cifer.read()
    tabla_frecuencias=get_frecuencias(n=3)
    print("FRECUENCIAS GENERALES\n")
    print(tabla_frecuencias)
    cifer_frecuencias=get_frecuencias(file="cifer")
    print("FRECUENCIAS DEL TEXTO CIFRADO\n")
    print(cifer_frecuencias)
    a=list(tabla_frecuencias.keys())
    b=list(cifer_frecuencias.keys())
    print(ord(a[0]),ord(b[0]))
    k=abs(ord(a[0])-ord(b[0]))
    print(k)
    resultado=deCesar(cifer,k,True)
    resultado+="\n FACTOR K = {}".format(k)
    salida = open(salida,"w")
    salida.write(resultado)


for i in range(1,26):
    answer = enCesar("in.txt","out.txt",i)
    str = "K = {:2}, encriptado = {}, desencriptado = {}".format(i,answer,deCesar(answer,i))
    print(str)
 

"""
entrada = open("diccionario.txt", "r")
entrada = entrada.read().replace("  "," ")
entrada = entrada.replace("\n","")
salida = open("diccionario.txt","w")
salida.write(entrada)
"""
enCesar("txt_plano.txt","cifer.txt",5,True)
crip_diccionario("cifer.txt","resultado_dic.txt",True)

crip_frecuencias("cifer.txt","crip_Frecuencias.txt",True)