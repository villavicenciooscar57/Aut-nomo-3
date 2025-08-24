import turtle
import random

# Lista de palabras posibles
# Puedes agregar más palabras, pero asegúrate de que sean adecuadas para la dificultad.
palabras = ["casa", "lobo", "flor", "rayo", "arbol", "coche", "gato"]

# Elegir una palabra aleatoria de la lista
palabra_secreta = random.choice(palabras)
letras_adivinadas = []
vidas = 6  # Número de vidas para el juego
intentos_fallidos = 0 # Contador para saber qué parte del cuerpo dibujar

# Configurar la pantalla del juego
pantalla = turtle.Screen()
pantalla.title("Juego del Ahorcado")
pantalla.bgcolor("lightblue")

# Tortuga para dibujar el ahorcado
dibujo = turtle.Turtle()
dibujo.hideturtle()
dibujo.speed(5) # Aumenté la velocidad para que el dibujo sea más rápido
dibujo.width(3)

# Tortuga para mostrar texto
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.goto(-150, 200)

# Función para dibujar la base del ahorcado
def dibujar_base():
    dibujo.penup()
    dibujo.goto(-100, -150)
    dibujo.pendown()
    dibujo.forward(200)  # Base
    dibujo.backward(100)
    dibujo.left(90)
    dibujo.forward(250)  # Poste vertical
    dibujo.right(90)
    dibujo.forward(150)  # Poste horizontal
    dibujo.right(90)
    dibujo.forward(40)   # Cuerda

# Función para dibujar una parte del cuerpo según el número de intentos fallidos
def dibujar_ahorcado(intentos):
    if intentos == 1:
        # Cabeza
        dibujo.penup()
        dibujo.goto(50, 110)
        dibujo.setheading(0)
        dibujo.pendown()
        dibujo.circle(20)
    elif intentos == 2:
        # Cuerpo
        dibujo.penup()
        dibujo.goto(50, 90)
        dibujo.setheading(-90)
        dibujo.pendown()
        dibujo.forward(80)
    elif intentos == 3:
        # Brazo izquierdo
        dibujo.penup()
        dibujo.goto(50, 70)
        dibujo.setheading(135)
        dibujo.pendown()
        dibujo.forward(40)
    elif intentos == 4:
        # Brazo derecho
        dibujo.penup()
        dibujo.goto(50, 70)
        dibujo.setheading(45)
        dibujo.pendown()
        dibujo.forward(40)
    elif intentos == 5:
        # Pierna izquierda
        dibujo.penup()
        dibujo.goto(50, 10)
        dibujo.setheading(-135)
        dibujo.pendown()
        dibujo.forward(50)
    elif intentos == 6:
        # Pierna derecha
        dibujo.penup()
        dibujo.goto(50, 10)
        dibujo.setheading(-45)
        dibujo.pendown()
        dibujo.forward(50)

# Función para mostrar la palabra oculta con guiones
def mostrar_palabra():
    palabra_mostrada = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += "_ "
    texto.clear()
    texto.write("Palabra: " + palabra_mostrada.strip(), font=("Arial", 24, "bold"))

# Función principal para ejecutar el juego
def jugar():
    global vidas, intentos_fallidos
    dibujar_base()
    
    while True:
        mostrar_palabra()
        
        # Mostrar vidas restantes
        texto.goto(-150, 150)
        texto.clear()
        texto.write(f"Vidas restantes: {vidas}", font=("Arial", 18, "normal"))

        # Obtener la entrada del usuario
        intento = pantalla.textinput("Adivina una letra", "Ingresa una letra:").lower()

        # Validar la entrada del usuario
        if intento is None or len(intento) != 1 or not intento.isalpha():
            continue  # Entrada inválida, pedir de nuevo

        if intento in letras_adivinadas:
            continue  # La letra ya fue utilizada

        letras_adivinadas.append(intento)

        if intento in palabra_secreta:
            # La letra es correcta, verificar si se ganó
            if all(letra in letras_adivinadas for letra in palabra_secreta):
                mostrar_palabra()
                texto.goto(-150, 100)
                texto.write("¡Ganaste!", font=("Arial", 30, "bold"))
                break
        else:
            # La letra es incorrecta
            vidas -= 1
            intentos_fallidos += 1
            dibujar_ahorcado(intentos_fallidos)
            
            # Verificar si se perdió
            if vidas == 0:
                mostrar_palabra()
                texto.goto(-150, 100)
                texto.write(f"Perdiste. La palabra era: {palabra_secreta}", font=("Arial", 24, "bold"))
                break

# Iniciar el juego
jugar()

pantalla.mainloop()
