#Proyecto Final
import os
os.system("cls")
print("\n\t\tSemáforo COVID")
op='0'
sem=0
suma=0
pers=0
promedioT=0
datos=[]
promedio=[]
while(op!='2'):
    print("\n\t1) Ingresar datos\n\t2) Salir")
    op=input("\nElige una opción: ")
    if op=='1':
        edad=input("\n\tEdad: ")
        indi=input("\tIndicador COVID: ")
        if indi <='0.7':
            covid='Negativo' #Si el indicador es menor que 0.8 no tiene COVID
        else:
            covid='Positivo' #Si el indicador es mayor o igual a 0.8 tiene COVID
            sem=sem+1
        reg=edad+', '+indi+', '+covid+'\n' #Tener una bd.csv con edad, indicador[0-1]
        promedio.append(edad)
        datos.append(reg)  
        pers=pers+1
        print("\nDatos registrados: "+str(pers))
    elif op=='2':
        print("\n\t||Recuerda realizar tu pruba COVID en los centros de atención ciudadana||")
    else:
        print("\nOpción no válida. Vuleve a intentarlo.")

#Calcular el color del semáforo COVID
if sem<=0:
    print("\n\t||El semáforo epidemiológico está en color VERDE||")
elif sem<=30:
    print("\n\t||El semáforo epidemiológico está en color AMARILLO||")
elif sem<=70:
    print("\n\t||El semáforo epidemiológico está en color NARANJA||")
else:
    print("\n\t||El semáforo epidemiológico está en color ROJO||")

#Calcular la edad promedio de las personas con COVID
if len(promedio)==0:
    print()
else:
    for i in promedio:
        suma=suma+int(i)
    promedioT=suma/len(promedio)

print("\n"+str(datos))

print("\nEl promedio de las edades registradas es: "+str(promedioT))

#Tener una bd.csv con edad, indicador[0-1]
a=open("bd.csv",'a')
a.writelines(datos)
a.close()

a=open("bd.csv",'r')
contenido=a.read()
a.close()

print("\n"+str(contenido))
print("\n\t||GRACIAS POR UTILIZAR MI PROGRAMA||")

