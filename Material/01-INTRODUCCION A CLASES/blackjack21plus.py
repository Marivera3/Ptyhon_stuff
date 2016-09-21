""" Se han efectuado las siguientes mejoras al programa blackjack:
    (1) definición de atributos generales de la clases Carta y Mazo
    (2) integración de la función mostrar_mano dentro de clase Jugador
    (3) impresión inicial del maso para ver si hay errores """
import random
class Carta:
    """ Atributos de instancias: pinta, valor
        Atributo de la Clase: mono_10 """
    mono_10 = ['K','Q','J']
    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor   

    def __str__(self):
        return str(self.valor) + self.pinta

    def get_valor(self):
        if self.valor in self.mono_10: # 'K' 'Q'  'J'
            return 10
        elif self.valor == "A":  # puede valer 1 u 11
            return 1             # lo dejámos en 1 por ahora
        else:
            return self.valor        

class Mazo:
    """ Atributos de instancias: mazo
        Método de inicio: generar_mazo
        Atributos de la Clase: nombre_pintas, valor_nombres, valor_pintas """
    pintas = ['♥', '♦','♠','♣']
    valor_nombres = ['A','J','Q','K']
    valor_nums = range(2,11)
    def __init__(self):
        self.mazo = []
        self.generar_mazo()

    def __str__(self):
        m = ""
        for c in self.mazo:
            m += str(c) + " "
        return m

    def generar_mazo(self):
        for p in self.pintas:
            for i in self.valor_nums:
                carta = Carta(p,i)
                self.mazo.append(carta)
                
            for i in self.valor_nombres:
                self.mazo.append(Carta(p,i))
        random.shuffle(self.mazo)

    def dar_carta(self, jugador, num):
        for i in range(num):
            jugador.recibir_carta(self.mazo.pop())
           
class Jugador:
    " Atributos: nombre, mano """
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def __str__(self):
        m = ""
        for c in self.mano:
            m += str(c) + " "
        m += "-> " + str(self.contar_mano())
        return m

    def contar_mano(self):   # calcular los puntos en la "mano"
        conteo = 0; ases = 0
        for carta in self.mano:
            conteo += carta.get_valor() # aquí consideramos los Ases como 1
            if carta.valor == 'A': 
                ases += 1          # contamos los Ases
        while ases > 0 and conteo <= 11:
            conteo += 10     # porque un As vale 1 u 11
            ases -= 1
        return conteo
    
    def mostrar_mano(self,una=False):
        # print()
        print(self.nombre, end=" ")
        if una: print(self.mano[0])  # cuando solo se muestra una carta
        else: print(self)   # muestra todas las cartas
    
# Comienza Prog Ppal

# Función para jugar
def jugar():
    una = True
    print("Comencemos el juego")
    j1 = Jugador('jugador')
    pc = Jugador('Casino')
    # Generar mazo
    mazo = Mazo()
    # Imprimo el mazo solo para ver si no tengo errores
    # Cuando entregue la Tarea, eliminaré esta instrucción
    print(mazo)
    print()
    # Repartir 2 cartas a cada jugador
    mazo.dar_carta(j1,2)
    mazo.dar_carta(pc,2)
    pc.mostrar_mano(una)
    j1.mostrar_mano()
    # Gana jugador si tiene 21 en dos cartas
    if(j1.contar_mano() == 21):
        print("Blackjack! Gana", j1.nombre)
        return
    
    # Si jugador no tiene 21, pide cartas en un ciclo
    while(j1.contar_mano() < 21):
        opcion = int(input("1: Pedir carta\n2: Plantarse\n"))
        if(opcion == 1):
            mazo.dar_carta(j1,1)
        if(opcion == 2):
            break    # sale del ciclo
        pc.mostrar_mano(una)
        j1.mostrar_mano()
    print()
    # Ahora juega el Casino
    pc.mostrar_mano()
    j1.mostrar_mano()
    while(pc.contar_mano() < j1.contar_mano() <= 21):
        input("Casino saca otra carta (presiona Return)")
        mazo.dar_carta(pc,1)
        pc.mostrar_mano()
        j1.mostrar_mano()
    print()
    # Ganador
    if(j1.contar_mano() < pc.contar_mano() <= 21 
        or j1.contar_mano() > 21):
        print("Gana", pc.nombre)
    elif(j1.contar_mano() == pc.contar_mano()):
        print("Empate")
    else:
        print("Gana", j1.nombre)

# Programa principal que invoca a la función jugar()
jugar()
