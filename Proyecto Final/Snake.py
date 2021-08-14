import turtle                   #Modulo turtle
import time                     #Modulo time
import random                   #Modulo random

posponer = 0.1                  #Hace el movimiento de nuestro programa sea mas leto.

#Marcador
score = 0                       #Inicializamos el marcador en cero.
high_score = 0                  #E inicializamos el marcador mas alto tambien en cero.

wn = turtle.Screen()            #Con el modulo turtle, abrimos una ventana y la asignamos a wn(window).
wn.title("Snake")               #Le ponemos nombre a la ventana que abrimos anteriormente
wn.bgcolor("black")             #Agregamos un fondo negro a la ventana     
wn.setup(width = 600, height = 600)     #La damos dimensiones a la ventana de 600*600. Con forma de plano cartesiano.
wn.tracer(0)                    #Le pedimos a la consola que mejores las animaciones dentro de nustra ventana.

#Cabeza Serpiente
cabeza =  turtle.Turtle()       #Creamos la variable "cabeza" como un objeto turtle.
cabeza.speed(0)                 #Solicitamos que el objeto aparezca al mismo tiempo que la ventana.
cabeza.shape("square")          #Le damos forma de cuadrado a nuestro objeto cabeza.
cabeza.color("green")           #Le otorgamos el color verde al objeto cabeza.
cabeza.penup()                  #Limpiamos el rastro que el modulo turtle deja cuando mueve un objeto.
cabeza.goto(0,0)                #Ubicamos al objeto cabeza en el centro de la ventana.
cabeza.direction = "stop"       #Hacemos que la cabeza espere de hacia donde tiene que ir por parte del teclado.

#Comida
comida =  turtle.Turtle()       #Creamos variable "comida" como un objeto turtle.
comida.speed(0)                 #Solicitamos que el objeto aparezca al mismo tiempo que la ventana.
comida.shape("circle")          #Le damos forma circular a nuestro objeto comida.
comida.color("brown")           #Le otorgamos el color cafe al objeto comida.
comida.penup()                  #Limpiamos el rastro que el modulo turtle deja cuando mueve un objeto.
comida.goto(0,100)              #Ubicamos al objeto comida en la posición (0,100) unos lugares arriba de la cabeza.

#Cuerpo Serpiente
segmentos = []                  

'''
El cuerpo de la sepiente esta dado por una lista vacia, en donde a medida que la serpiente "coma su comida" este
tendra mas valores registrados, por ende mientras más grande la serpiente, más grande la lista.
'''

#Contador
texto = turtle.Turtle()         #Creamos una variable "texto" como un objeto turtle para escribir en pantalla.
texto.speed(0)                  #Solicitamos que el texto aparezca al mismo tiempo que la ventana.
texto.color("grey")             #Le otorgamos el color gris a nuestro contador.
texto.penup()                   #Limpiamos el rastro que el modulo turtle deja cuando actualiza al objeto.
texto.hideturtle()              #Escondemos la plumilla que va a escribir el texto.
texto.goto(0,260)               #Elegimos que el texto aparezca en la parte superior, centrado.
texto.write("Score: 0         High Score: 0",          #La función write es como un print en donde se solita
 align = "center", font = ("Courier", 22, "normal"))   #que escriba los diferentes marcadores, con sus especificaciones.

#Funciones
'''
En esta parte vamos a definirle al interprete que es para nostros arriba, abajo, derecha e izquierda, para
posteriormente conectar nuestro programa a nuestro teclado.
'''
def arriba():
        cabeza.direction = "up"
def abajo():
        cabeza.direction = "down"
def derecha():
        cabeza.direction = "right"
def izquierda():
        cabeza.direction = "left"

'''
En la siguiente parte se relaciona con la linea 24 del apartado "#Cabeza Serpiente" en donde vamos a generar
el movimiento de la "cabeza de la serpiente" a partir de sustituir el valor de "stop" por el valor que recibimos
de nuestro teclado, en donde dependiendo de la dirección recibida esta se movera hacia arriba, abajo, derecha o izquierda.
'''
def mov():
        if cabeza.direction == "up":     #Entonces, si el valor es up.
                y = cabeza.ycor()        #Se solicita el valor de "y" que se modifico para almacenarlo en la variable y.
                cabeza.sety(y + 20)      #Actualizamos el valor de "y" y lo aumentamos 20 para que se sigua moviendo.         
        
        if cabeza.direction == "down":   #Entoces si el valor es down.
                y = cabeza.ycor()        #Se solicita el valor de "y" que se modifico para almacenarlo en la variable y.
                cabeza.sety(y - 20)      #Actualizamos el valor de "y" y lo disminuimos 20 para que se siga moviendo.
        
        if cabeza.direction == "right":  #Entonces si el valor es right.
                x = cabeza.xcor()        #Se solicita el valor de "x" que se modifico para almacenarlo en la variable x.
                cabeza.setx(x + 20)      #Actualizamos el valor de "x" y lo aumentamos 20 para que se sigua moviendo.
        
        if cabeza.direction == "left":   #Entonces si el valor es left.
                x = cabeza.xcor()        #Se solicita el valor de "x" que se modifico para almacenarlo en la variable x.
                cabeza.setx(x - 20)      #Actualizamos el valor de "x" y lo disminuimos 20 para que se siga moviendo.

#Teclado
wn.listen()                          #Solicitamos que la pantalla tenga una reacción inmediata a nuestro teclado.
wn.onkeypress(arriba, "Up")          #Al precionar la tecla "Up" se debe activar la función arriba.
wn.onkeypress(abajo, "Down")         #Al precionar la tecla "Down" se debe activar la función abajo.
wn.onkeypress(derecha, "Right")      #Al precionar la tecla "Right" se debe activar la función derecha.
wn.onkeypress(izquierda, "Left")     #Al precionar la tecla "Left" se debe activar la función izquierda.

while True:
        wn.update()

        #Colisiones bordes
        if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
                '''
                Dentro del if, hay una condición que impide que la serpiente salga del "tablero" de 600*600, de tal,
                forma que si la serpiente alcanza un valo mayor de 280 o -280 en cualquiera de los ejes, la cabeza
                perdera su "cuerpo" y se posicionara en (0,0).
                '''
                time.sleep(1)                   #Se le ordena detener al programa por un segundo.
                cabeza.goto(0,0)                #Se le ordena a la cabeza reubicarse en la posición (0,0).
                cabeza.direction = "stop"       #Obliga a la cabeza a detenerse.

                #Limpiar segmentos
                for segmento in segmentos:
                        segmento.goto(1000,1000)  #Como no se puede eliminar el cuerpo de la serpiente, simplemente los
                                                  #hace desaparecer del la ventana, enviandolos a posiciones lejanas.
                segmentos.clear()                 #Limpia los valores de la lista segmentos.

                #Resetear Marcador
                score = 0       #Se le da el valor de cero a la variable score.
                texto.clear()   #Limpia el texto
                texto.write("Score: {}          High Score: {}".format(score, high_score),
                        align = "center", font = ("Courier", 20, "normal"))
                                #Imprime nuevo texto pero conserva los valores de score y high_score, en el nuevo texto
                                #con sus diferentes especificaciones.

        #Colisiones Comida
        if cabeza.distance(comida) < 20:        #Define la distncia entre la cabeza y la comida. Comprobando si se tocan.
                x = random.randint(-280,280)    #Si es cierto, crea una coordenada x aleatorea, y la asigna a x.    
                y = random.randint(-280,280)    #Si es cierto, crea una coordenada y aleatorea, y la asigna a y.
                comida.goto(x,y)                #Generando una nueva comida en las coordendas aleatoreas xy.

                nuevo_segmento =  turtle.Turtle()       #Creamos una variable "nuevo_segmento" como un objeto turtle.
                nuevo_segmento.speed(0)                 #Solicitamos que el texto aparezca al mismo tiempo que la ventana.
                nuevo_segmento.shape("square")          #Le damos forma circular a nuestro objeto nuevo_segmento.
                nuevo_segmento.color("lightgreen")      #Le otorgamos el color verde claro al objeto nuevo segmento.
                nuevo_segmento.penup()                  #Limpiamos el rastro que el modulo turtle deja cuando actualiza al objeto.
                segmentos.append(nuevo_segmento)        #Guardamos a nuevo_segmento en la lista segmentos.

                #Aumentar Marcador
                score += 10                   #La variable score aumenta 10 cada vez que la zabeza y la comida se tocan.
                if score > high_score:        #La estructura if dice que si score se vulve mayor a high_score...     
                        high_score = score    #Otrogar los valores de score a high_score.
                
                texto.clear()   #Limpia el texto
                texto.write("Score: {}          High Score: {}".format(score, high_score),
                        align = "center", font = ("Courier", 20, "normal"))
                                #Imprime nuevo texto pero conserva los valores de score y high_score, en el nuevo texto
                                #con sus diferentes especificaciones.
        
        #Mover Cuerpo Serpiente
        totalSeg = len(segmentos)       #Asignamos a totalSeg el número de datos que hay en la lista segementos.
        for index in range(totalSeg -1, 0, -1): #Se itera entre cada uno de los segmentos.
                '''
                Lo que sucede aquí es que el ultimo elemento de mi lista siga al penultimo y así sucesivamente. Empezando
                en la posición cero, por eso se decrece uno.
                '''
                x = segmentos[index - 1].xcor() #Obtenemos la coordenada x del segmento anterior.
                y = segmentos[index - 1].ycor() #Obtenemos la coordenada y del segmento anterior.
                segmentos[index].goto(x,y)      #Hacemos que los segmento se muevan a las coordenadas xy.

        if totalSeg > 0:
                x = cabeza.xcor()       #Obtenemos la coordenada x
                y = cabeza.ycor()       #Obtenemos la coordenada y
                segmentos[0].goto(x,y)  #Se pide que el elemento se mueva donde esta la cebeza.

        mov()

        #Colisiones Cuerpo
        for segmento in segmentos:
                if segmento.distance(cabeza)<20:        #La estrcutura if define que si, cabeza y segmentos se tocan...
                        time.sleep(1)                   #Se le ordena detener al programa por un segundo.
                        cabeza.goto(0,0)                #Se le ordena a la cabeza reubicarse en la posición (0,0).
                        cabeza.direction = "stop"       #Obliga a la cabeza a detenerse.

                        #Limpiar segmentos
                        for segmento in segmentos:       #Como no se puede eliminar el cuerpo de la serpiente, simplemente
                                segmento.goto(1000,1000) #los hace desaparecer del la ventana, enviandolos a posiciones lejanas.
                        segmentos.clear()                #Limpia los valores de la lista segmentos.

                        score = 0       #Se le da el valor de cero a la variable score.
                        texto.clear()   #Limpia el texto
                        texto.write("Score: {}          High Score: {}".format(score, high_score),
                                align = "center", font = ("Courier", 20, "normal"))
                                        #Imprime nuevo texto pero conserva los valores de score y high_score, en el nuevo texto
                                        #con sus diferentes especificaciones.


        time.sleep(posponer)    #Hace el movimiento de nuestro programa sea mas leto.
