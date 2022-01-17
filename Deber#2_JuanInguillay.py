#Deber#2 - Juan Inguillay
class Ej1_video10:
    def ejercicio1(self):
        print("¿Cuál es el resultado:? 1) cadena[10]\n2) cadena[-1]\n3) cadena[0:9]\n4) cadena[:3]")
        cadena="si, profe, es cierto... yo me comi la tarea"
        resultado=cadena[10]
        print("1) ",resultado)
        resultado=cadena[-1]
        print("2) ",resultado)
        resultado=cadena[0:9]
        print("3) ",resultado)
        resultado=cadena[::3]
        print("4) ",resultado)
        print("\n¿Cómo obtener...?\n1) La cadena al revés: (aerat al imoc em oy ...otreic se ,eforp ,is)\n2) La subcadena (profe)")
        resultado=cadena[::-1]
        print("1) ",resultado)
        resultado=cadena[4:9]
        print("2) ",resultado)
resultado_video10_1=Ej1_video10()
resultado_video10_1.ejercicio1()
class Ej2_video10:
    def ejercicio2(self):
        print("""Dada la variable s="   hola, ¿cómo estás?" con 3 espacios 
        al inicio, ¿qué se obtiene en cada una de las siguientes operaciones?
        1) s[::-1] 
        2) s[len (s)] 
        3) s.count("o") 
        4) s.count("Hola") 
        5) s[-4:] 
        6) s [15:] 
        7) s.find("o")
        8) s.strip () 
        9) x=s.upper()
        x==s
        10) s[14:].upper() 
        11) len(s) %2!=0 
        12) s.replace(" ", "*") 
        13) s.replace("z", "Z")\n""")
        print("Respuesta: ")
        s="   hola, ¿cómo estás?"
        resultado=s[::-1] 
        print("1) ",resultado)
        print("2) Error")
        resultado=s.count("o") 
        print("3) ",resultado)
        resultado=s.count("Hola") 
        print("4) ",resultado)
        resultado=s[-4:] 
        print("5) ",resultado)
        resultado=s [15:] 
        print("6) ",resultado)
        resultado=s.find("o")
        print("7) ",resultado)
        resultado=s.strip () 
        print("8) ",resultado)
        x=s.upper()
        resultado=(x==s)
        print("9) ",resultado)
        resultado=s[14:].upper() 
        print("10) ",resultado)
        resultado=len(s) %2!=0 
        print("11) ",resultado)
        resultado=s.replace(" ", "*") 
        print("12) ",resultado)
        resultado=s.replace("z", "Z")
        print("13) ",resultado)
resultado_video10_2=Ej2_video10
resultado_video10_2.ejercicio2()
class Ej3_video10:
    def ejercicio3(self):
        print("""Algunas preguntas...
        1) Dada la variable X de tipo string ¿cómo se puede hallar el indice del último carácter? 
        2) Dada la variable cadena="hola" ¿qué retorna cadena.find("2") ? 
        3) ¿Qué retorna? "a" in "dátiles"
        4) ¿Qué operación retorna la posición del primer espacio en "me gusta programar"? 
        5) ¿Qué operación retorna la cantidad de espacios de la cadena "me gusta programar"? 
        6) ¿Por qué da error? cadena[0]="H"
        7) ¿Qué almacena la siguiente variable? nueva="C"+cadena[1:] 
        8) ¿Cómo reemplazar las vocales acentuadas por vocales no acentuadas en la cadena X? 
        9) ¿Qué comparación podría hacerse para averiguar si la longitud de la cadena es par? 
        10) ¿De qué forma se puede obtener la cantidad de vocales de la cadena X?\n
        Respuestas: """)
        x="programar en python"
        x=x[-1]
        print("1) ",x)
        cadena="hola"
        c=cadena.find("2")
        print("2) ",c)
        a="a" in "dátiles"
        print("3) ",a)
        r= "me gusta programar".find(" ")
        print("4) ",r)
        b= "me gusta programar".count(" ")
        print("5) ",b)
        print("6) Los string no soportan la asignación porque los string son inmutables, no podemos cambiarlos pero si podemos reemplazarlos.")
        nueva="C"+cadena[1:]
        print("7) ",nueva)
        X_="hoy es día miércoles"
        X=X_.replace("í", "i").replace("é", "e")
        print("8) ",X)
        X= len(X_)
        if X%2 ==0:
            print("9) Par")
        else:
            print("9) Imprar")
        z=X_.count("a")+X_.count("e")+X_.count("i")+X_.count("o")+X_.count("u")
        print("10) ",z)
resultado_video10_3=Ej3_video10()
resultado_video10_3.ejercicio3()
class Ej1_video12:
    def ejercicio1(self):
        N=input("Tu nombre:     ")
        print("Ahora estás en la matrix, ",N)
resultado_video12_1=Ej1_video12()
resultado_video12_1.ejercicio1()
class Ej2_video12:
    def ejercicio2(self):
        costo=float(input("Costo de la cena: $"))
        servicio=costo*0.062
        propina=costo*0.1
        print("Costo total de la comida: $",costo+servicio+propina)
resultado_video12_2=Ej2_video12()
resultado_video12_2.ejercicio2()
class Ej3_video12:
    def ejercicio3(self):
        dia=input("Día de tu nacimiento: ")
        mes= input("Mes de tu nacimiento: ")
        anio= input("Año de tu nacimiento: ")
        print(dia+"/"+mes+"/"+anio)
resultado_video12_3=Ej3_video12()
resultado_video12_3.ejercicio3()
class Ej4_video12:
    def ejercicio4(self):
        capacidad=float(input("Capacidad del tanque: "))
        kmxl=float(input("Rendimiento (km po litro): "))
        recorrido=float(input("Km totales a recorrer: "))
        kmxtanque=capacidad*kmxl
        print("Serían necesarios",recorrido/kmxtanque,"tanques.")
resultado_video12_4=Ej4_video12()
resultado_video12_4.ejercicio4()
class Ej1_video13:
     def ejercicio1(self):
        capacidadm2=4
        porcentajegradas=0.2
        porcentajeespeciales=0.3
        porcentajecomunes=0.7
        dimensiones=float(input("Dimensiones del estadio (en m2): "))
        personasengradas=int(input("Cantidad de personas que caben en las gradas: "))
        porcentajeescenario=int(input("Porcentaje que ocupa el escenario: "))
        m2gradas=dimensiones*porcentajegradas
        m2escenario=dimensiones*(porcentajeescenario/100)
        m2disponibles=dimensiones-m2gradas-m2escenario
        personastotales=(m2disponibles*4)+personasengradas
        print("Caben", personastotales, "personas")
        precioentradaespecial=float(input("Precio entrada especial: $"))
        precioentradacomun=float(input("Precio entrada común: $"))
        print("Ingreso total de ventas: $",
        (personastotales*porcentajeespeciales)*precioentradaespecial+
        (personastotales*porcentajecomunes)*precioentradacomun)
resultado_video13_1=Ej1_video13()
resultado_video13_1.ejercicio1()
class Ej1_video15:
      def ejercicio1(self):
        numero=int(input("Número: "))
        if numero<0:
                numero=numero*-1
        print("El valor absoluto es: ",numero)
resultado_video15_1=Ej1_video15()
resultado_video15_1.ejercicio1()
class Ej2_video15:
      def ejercicio2(self):
        nombre1=input("Un nombre: ")
        nombre2=input("Otro nombre: ")
        if nombre1[0]==nombre2[0] or nombre1[-1]==nombre2[-1]:
                print("Coincidencia")
        else:
                print("No hay coincidencia")
resultado_video15_2=Ej2_video15()
resultado_video15_2.ejercicio2()
class Ej3_video15:
        def ejercicio3(self):
                candidato=input("Candidato elegido: ")
                if candidato.upper()=="A":
                        print("Usted ha votado por el partido rojo")
                elif candidato.upper()=="B":
                        print("Usted ha votado por el partido azul")
                elif candidato.upper()=="C":
                        print("Usted ha votado por el partido verde")
                else:
                        print("Opción errónea")
resultado_video15_3=Ej3_video15()
resultado_video15_3.ejercicio3()
class Ej4_video15:
        def ejercicio4(self):
                letra=input("Letra: ")
                if len(letra)!=1:
                        print("Debe ser solo una letra")
                else:
                        if letra.lower() in "aeiou":
                                print("Es vocal")
resultado_video15_4=Ej4_video15()
resultado_video15_4.ejercicio4()
class Ej5_video15:
        def ejercicio5(self):
                anio=int(input("Año: "))
                if anio%4 != 0:
                        print("No es bisiesto.")
                else:
                        if anio%100 != 0 or anio%400 == 0:
                                print("Es bisiesto")
                        else:
                                print("No es bisiesto")
resultado_video15_5=Ej5_video15()
resultado_video15_5.ejercicio5()
class Ej1_video16:
        def ejercicio1(self):
                fecha=input("Fecha (formato 'día, DD/MM'): ")
                fecha=fecha.lower()
                diasemana=fecha[0:fecha.find(',')]
                dianro=int(fecha[fecha.find(',')+2:fecha.find('/')])
                mesnro=int(fecha[fecha.find('/')+1:])
                if dianro>31 or mesnro>12:
                        print("Fecha incorrecta")
                else:
                        if diasemana in "lunes,martes,miércoles":
                                respuesta=input("¿Se tomaron exámenes? S/N: ")
                                if respuesta.lower()=="s":
                                        aprobados=int(input("Cantidad de aprobados: "))
                                        reprobados=int(input("Cantidad de reprobados: "))
                                        print("Porcentaje de aprobados:", (aprobados*100)/(aprobados+reprobados), "%")
                        elif diasemana=="jueves":
                                asistencia=int(input("Porcentaje de asistencia: "))
                                if asistencia>50:
                                        print("Asistió la mayoría")
                                else:
                                        print("No asistió la mayoría")
                        elif diasemana=="viernes":
                                if dianro==1 and (mesnro==1 or mesnro==7):
                                        print("Nuevo ciclo")
                                        alumnos=int(input("Cantidad de alumnos: "))
                                        arancel=float(input("Arancel: $"))
                                        print("Ingreso total: $", alumnos*arancel)
                        else:
                                print("Fecha incorrecta")
                print("Fin del programa")
resultado_video16_1=Ej1_video16()
resultado_video16_1.ejercicio1()
class Ej1_video18:
        def ejercicio1(self):
                total=0
                for i in range(101):
                        if i%3 == 0:
                                total=total+i
                print("Sumatoria de los múltiplos de 3:", total)
resultado_video18_1=Ej1_video18()
resultado_video18_1.ejercicio1()
class Ej2_video18:
        def ejercicio2(self):
                numero=int(input("Número:"))
                f=1
                if numero!=0:
                        for i in range(1,numero+1):
                                f=f*i
                print("Factorial:", f)
resultado_video18_2=Ej2_video18()
resultado_video18_2.ejercicio2()
class Ej3_video18:
        def ejercicio3(self):
                n1=0
                n2=1
                print(n1)
                print(n2)
                for i in range(8):
                        n3=n1+n2
                        print(n3)
                        n1=n2
                        n2=n3
resultado_video18_3=Ej3_video18()
resultado_video18_3.ejercicio3()
class Ej4_video18:
        def ejercicio4(self):
                sumaPositivos=0
                cantidadPositivos=0
                sumaNegativos=0
                for i in range(6):
                        nro=int(input("Número: "))
                        if nro>0:
                                sumaPositivos=sumaPositivos+nro
                                cantidadPositivos=cantidadPositivos+1
                        else:
                                sumaNegativos=sumaNegativos+nro
                print("Sumatoria de los negativos: ", sumaNegativos)
                if cantidadPositivos!=0:
                        print("Promedio de los positivos: ",sumaPositivos/cantidadPositivos)
                else:
                        print("No se ingresaron números positivos")
resultado_video18_4=Ej4_video18()
resultado_video18_4.ejercicio4()
class Ej1_video19:
        def ejercicio1(self):
                alfabeto="abcdefghijklmnñopqrstuvwxyz"
                corrimiento=int(input("Corrimiento: "))
                for i in range(5):
                        mensaje=input("Mensaje a encriptar: ")
                        encriptado=""
                        for caracter in mensaje:
                                if caracter.lower() in alfabeto:
                                        indice=alfabeto.find(caracter.lower())
                                        indice=(indice+corrimiento)%27
                                        encriptado+=alfabeto[indice]
                                else:
                                        encriptado+=caracter
                        print("*** Mensaje encriptado: ", encriptado)
resultado_video19_1=Ej1_video19()
resultado_video19_1.ejercicio1()
class Ej1_video21:
        def ejercicio1(self):
                total=0
                monto=float(input("Monto de una venta: $"))
                while monto!=0:
                        if monto<0:
                                print("Monto no válido.")
                        else:
                                total+=monto
                        monto=float(input("Monto de una venta: $"))
                if total>1000:
                        total-=total*0.1
                        print("Monto total a pagar: $", total)
resultado_video21_1=Ej1_video21()
resultado_video21_1.ejercicio1()
class Ej2_video21:
        def ejercicio2(self):
                numero=int(input("numero: "))
                totalPares=0
                totalImpares=0
                while numero!=0:
                        pares=0
                        impares=0
                        while numero!=0:   
                                ultimodigito=numero%10
                                if ultimodigito%2==0:
                                        pares+=1
                                        totalPares+=1
                                else:
                                        impares+=1
                                        totalImpares+=1
                                numero=numero//10
                        print("El número ingresado tiene ",pares," digitos pares y ",impares," digitos impares")
                        numero=int(input("Otro número: "))
                print("Total de dígitos pares:", totalPares)
                print("Total de dígitos impares:", totalImpares)
resultado_video21_2=Ej2_video21()
resultado_video21_2.ejercicio2()
class Ej3_video21:
        def ejercicio3(self):
                lineas=0
                digitos="0123456789"
                cantidadDigitos=0
                cadena=input("Cadena: ")
                while cadena!="*":
                        for caracter in cadena:
                                if caracter in digitos:
                                        cantidadDigitos+=1
                        if cadena=="/":
                                lineas+=1
                                print("Aparecen ", cantidadDigitos, " dígitos en la línea")
                                cantidadDigitos=0
                        cadena=input("Cadena: ")
                print("Se leyeron ",lineas," líneas completas")
resultado_video21_3=Ej3_video21()
resultado_video21_3.ejercicio3()
class Ej1_video22:
        def ejercicio1(sefl):
                frase=input("Frase: ").strip()
                cantidad=0
                len_p_mas_larga=0
                while len(frase) != 0:
                        cantidad=cantidad+1
                        i=frase.find(" ")
                        if i != -1:
                                palabra=frase[0:i]
                                while i < len(frase) and frase[i] == " ":
                                        i=i+1
                                frase=frase[i:]
                        else:
                                palabra=frase
                                frase=""
                        if len(palabra) > len_p_mas_larga:
                                len_p_mas_larga=len(palabra)
                                p_mas_larga=palabra
                if cantidad > 0:
                        print("Palabra más larga:", p_mas_larga)
                print("Cantidad de palabras:", cantidad)
resultado_video22_1=Ej1_video22()
resultado_video22_1.ejercicio1()
class Ej1_video24:
        def ejercicio1(self):
                cantidad=0
                n=int(input("Número: "))
                while n!=0:
                        primo=True
                        for i in range(2,n):
                                if n%i==0:
                                        primo=False
                                        break
                        if primo:
                                cantidad+=1
                        n=int(input("Número: "))
                print("primos: ", cantidad)
resultado_video24_1=Ej1_video24()
resultado_video24_1.ejercicio1()
class Ej2_video24:
        def ejercicio2(self):
                anioInicio=int(input("Año inicial:"))
                anioFin=int(input("Año final:"))
                for anio in range(anioInicio, anioFin+1):
                        if not anio%10==0:
                                continue
                        if not anio%4==0:
                                continue
                        if anio%100!=0 or anio%400==0:
                                print(anio)
resultado_video24_2=Ej2_video24()
resultado_video24_2.ejercicio2()
class Ej1_video29:
        def validarDNI(dni):
                cantidad=0
                while dni!=0:
                        cantidad+=1
                        dni//=10
                return cantidad==7 or cantidad==8
resultado_video29_1=Ej1_video29()
resultado_video29_1.validarDNI(1234567)
class Ej2_video29:
        def lenUltimaPalabra(frase):
                if len(frase)==0:
                        return 0
                cantidad=0
                for i in range(len(frase)):
                        if frase[i]!=' ':
                                cantidad+=1
                        else:
                                if i<len(frase)-1 and frase[i+1]!=' ':
                                        cantidad=0
                return cantidad
resultado_video29_2=Ej2_video29()
resultado_video29_2.lenUltimaPalabra("Hola mundo")
class Ej3_video29:
        def lenUltimaPalabra(cadena):
                longitud=len(cadena)
                if longitud==0:
                        return 0
                cantidad=0
                for i in range(longitud):
                        if cadena[i]!=' ':
                                cantidad+=1
                        else:
                                if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                                        cantidad=0
                return cantidad
        def DNIvalido(dni):
                cantidad=0
                while dni!=0:
                        cantidad+=1
                        dni//=10
                return cantidad==7 or cantidad==8

        def primerosTresDigitos(numero):
                while numero >= 1000:
                        numero = numero // 10
                return numero

        def obtenerIdentificador(nombre, dni):
                nombre=nombre.strip()
                id=nombre[:nombre.find(" ")]
                id=id+str(lenUltimaPalabra(nombre))
                id=id+str(primerosTresDigitos(dni))
                return id
        #programa principal
        nombre=input("Nombre del socio: ")
        while nombre!="":
                dni=int(input("DNI del socio: "))
                while (DNIvalido(dni)):
                        print("Número inválido.")
                        dni=int(input("DNI del socio: "))
                print(obtenerIdentificador(nombre,dni))
                nombre=input("Nombre del socio: ")
resultado_video29_3=Ej3_video29()
resultado_video29_3.lenUltimaPalabra("Hola mundo")
resultado_video29_3.DNIvalido(1234567)
resultado_video29_3.primerosTresDigitos(1879)
resultado_video29_3.obtenerIdentificador("Alfredo",1234567)
class Ej1_video32:
        def sumatoria(lista):
                suma=0
                for n in lista:
                        suma+=n
                return suma
        def numerosMenores(lista, limite):
                nueva=[]
                for n in lista:
                        if n<limite:
                                nueva.append(n)
                return nueva
        def frecuencias(lista):
                nueva=[]
                for n in lista:
                        if [n, lista.count(n)] not in nueva:
                                nueva.append([n, lista.count(n)])
                return nueva
#A
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#B
resultado_video32_1=Ej1_video32
print("Sumatoria de los números:", resultado_video32_1.sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#C
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#D
limite=int(input("Filtrar números menores a: "))
for n in resultado_video32_1.numerosMenores(numeros, limite):
    print(n)
#E
print("Frecuencias:")
for tupla in resultado_video32_1.frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")
class Ej2_video32:
        def agregarPasajeros(pasajeros):
                nombre=input("Nombre -x para cortar: ")
                while nombre!="x":
                        dni=int(input("DNI: "))
                        destino=input("Ciudad destino: ")
                        pasajeros.append((nombre,dni,destino))
                        nombre=input("Nombre -x para cortar: ")
                return pasajeros

        def agregarCiudades(ciudades):
                ciudad=input("Ciudad -x para cortar: ")
                while ciudad!="x":
                        pais=input("País: ")
                        ciudades.append((ciudad,pais))
                        ciudad=input("Ciudad -x para cortar: ")
                return ciudades

        def buscarCiudad(pasajeros, dni):
                for viaje in pasajeros:
                        if viaje[1]==dni:
                                return viaje[2]
                return ""
        def cantidadPasajerosCiudad(pasajeros, ciudad):
                cantidad=0
                for viaje in pasajeros:
                        if viaje[2]==ciudad:
                                cantidad+=1
                return cantidad

        def buscarPaisDestino(pasajeros, ciudades, dni):
                buscada=buscarCiudad(pasajeros, dni)
                for ciudad in ciudades:
                        if ciudad[0]==buscada:
                                return ciudad[1]
                return ""

        def cantidadPasajerosPais(pasajeros, ciudades, pais):
                cantidad=0
                for viaje in pasajeros:
                        if pais==buscarPaisDestino(pasajeros, ciudades, viaje[1]):
                                cantidad+=1
                return cantidad

#programa principal
resultado_video32_2=Ej2_video32
pasajeros=[]
ciudades=[]
while True:
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino mediante el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante DNI")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=resultado_video32_2.agregarPasajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=resultado_video32_2.agregarCiudades(ciudades)
    elif opcion==3:
        dni=int(input("DNI: "))
        print("El pasajero viaja a", resultado_video32_2.buscarCiudad(pasajeros, dni))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan", resultado_video32_2.cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        dni=int(input("DNI: "))
        print("Viaja a", resultado_video32_2.buscarPaisDestino(pasajeros, ciudades, dni))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan", resultado_video32_2.cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")  
class Ej1_video35:
        def cargarNombres(alumnos):
                nombre=input("Nombre: ")
                while nombre!="x":
                        alumnos.add(nombre)
                        nombre=input("Nombre: ")
                return alumnos
resultado_video35_1=Ej1_video35
primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=resultado_video35_1.cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=resultado_video35_1.cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
   print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
   print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
   print(nombre)
class Ej2_video35:
        def direcciones(ventas):
                 domicilios=set()
                 for venta in ventas:
                        domicilios.add(venta[3])
                 return domicilios
class Ej1_video37:
        def ejercicio1(self):
                contadores={}
                for i in range(50):
                        cadena=input("Cadena de caracteres: ")
                        for caracter in cadena:
                                if caracter not in contadores:
                                        contadores[caracter]=1
                                else:
                                        contadores[caracter]+=1
                print("Frecuencia de cada carácter")
                for caracter, cantidad in contadores.items():
                        print(caracter, ": ", cantidad)
class Ej1_video39:
        def cargarSocios(socios):
                numero=int(input("Número de socio (0 para cortar): "))
                while numero!=0:
                        nombre=input("Nombre y apellido: ")
                        fecha=input("Fecha de ingreso (DDMMAAAA): ")
                        cuota=input("¿Cuota al día? s/n: ")
                        socios[numero]=[nombre,fecha,cuota.lower()=="s"]
                        numero=int(input("Número de socio (0 para cortar): "))
                return socios

        def modificarFecha(socios, fecha_anterior, fecha_nueva):
                for datos in socios.values():
                        if datos[1]==fecha_anterior:
                                datos[1]=fecha_nueva
                return socios

        def numeroSocio(socios, nombre):
                for numero,datos in socios.items():
                        if datos[0].lower()==nombre.lower():
                                return numero
                return 0

        def formatoFecha(fecha):
                return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

        def imprimirListado(socios):
                for numero,datos in socios.items():
                        print("-Número:",numero)
                        print("-Nombre:",datos[0])
                        print("-Ingresó:", formatoFecha(datos[1]))
                        if datos[2]:
                                print("-Cuota al día")
                        else:
                                print("-En deuda")

resultado_video39=Ej1_video39
socios_activos={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos=resultado_video39.cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("***Registrar pago de cuotas")
numero=int(input("Número de socio: "))
socios_activos[numero][2]=True

print("***Modificando fecha de ingreso...")
socios_activos=resultado_video39.modificarFecha(socios_activos, "13032018", "14032018")

print("***Eliminar socio")
nombre=input("Nombre y apellido: ")
numero=resultado_video39.numeroSocio(socios_activos, nombre)
if numero in socios_activos:
        del socios_activos[numero]
resultado_video39.imprimirListado(socios_activos)