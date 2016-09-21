import random

class Carta:
    """ Atributos: pinta, valor """
    def __init__(self, pinta, valor):
        self.pinta = pinta
        self.valor = valor   

    def __str__(self):
        return str(self.valor) + self.pinta

    def get_valor(self):
        if (self.valor == 'K' or self.valor == 'Q' 
            or self.valor == 'J'):
            return 10
        elif self.valor == "A": # puede valer 1 u 11
            return 1            # lo dejámos en 1 por ahora 
        else:
            return self.valor        

class Mazo:
    """ Atributos: mazo
        Método de inicio: generar_mazo """
    def __init__(self):
        self.mazo = []
        self.generar_mazo()

    def generar_mazo(self):
        for p in ['♥', '♦','♠','♣']:
            for i in range (2,11):
                carta = Carta(p,i)
                self.mazo.append(carta)
            
            for i in ['A','J','Q','K']:
                self.mazo.append(Carta(p,i))
        random.shuffle(self.mazo)

    def dar_carta(self, jugador, num):
        for i in range(num):
            jugador.recibir_carta(self.mazo.pop())
           
class Jugador:
    " Atributos: nombre, mano """
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []    # la lista de cartas en la "mano"

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def __str__(self):
        m = ""
        for c in self.mano:
            m += str(c) + " "
        m += "-> " + str(self.contar_mano())
        return m

    def contar_mano(self):    # calcular los puntos en la "mano"
        conteo = 0; ases = 0
        for carta in self.mano:
            conteo += carta.get_valor()  # aquí consideramos los Ases como 1
            if carta.valor == 'A':
                ases += 1         # contamos los Ases
        while ases > 0 and conteo <= 11:
            conteo += 10     # porque un As vale 1 u 11
            ases -= 1
        return conteo
# Comienza Prog Ppal
# Función para mostrar_manos ("mano" es una lista de cartas)
def mostrar_manos(j,pc,juega_pc):
    print()
    if(juega_pc): print(pc.nombre, pc) # muestra todas las cartas del Casino
    else: print(pc.nombre, pc.mano[0]) # solo muestra una carta del Casino
    print(j.nombre, j)   # muestra todas las cartas del Jugador

# Función para jugar
def jugar():
    j1 = Jugador('Jugador')
    pc = Jugador('Casino')
    mazo = Mazo()

    mazo.dar_carta(j1,2)
    mazo.dar_carta(pc,2)
    mostrar_manos(j1,pc,False) # solo muestra una carta del Casino
    if(j1.contar_mano() == 21):
        # gana el jugador por conseguir 21 puntos con dos cartas
        print("Blackjack! Gana", j1.nombre)
        return

    # Jugador pide cartas
    while(j1.contar_mano() < 21):
        opcion = int(input("1: Pedir carta\n2: Plantarse\n"))
        if(opcion == 1):
            mazo.dar_carta(j1,1)
        if(opcion == 2):
            break   # sale del ciclo
        mostrar_manos(j1,pc,False)

    # Juega el Casino
    mostrar_manos(j1,pc,True) # muestra las dos cartas del Casino
    while(pc.contar_mano() < j1.contar_mano() <= 21):
        input("Casino saca otra carta (presiona Return)")
        mazo.dar_carta(pc,1)
        mostrar_manos(j1,pc,True) # muestra todas las cartas del Casino

    # Ganador
    if(j1.contar_mano() < pc.contar_mano() <= 21 
        or j1.contar_mano() > 21):
        # gana el Casino
        print("Gana", pc.nombre)
    elif(j1.contar_mano() == pc.contar_mano()):
        print("Empate")
    else:
        # gana el Jugador
        print("Gana", j1.nombre)

# Programa principal que invoca a la función jugar()
n = 1
cond = True
print("Juego de 21 Real, Jugador vs Casino")
while cond:
    print()
    print("¿quieres jugar la ronda "+str(n)+" ?")
    a = input("Ingresa SI o NO: ")
    if a=="SI" or a=="Si" or a=="sI" or a=="si":
        print()
        print("RONDA número "+str(n))
        jugar()
        n += 1
    else:
        cond = False
        print("CHAO")
