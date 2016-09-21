import random
# lom == lomitos
# comp == completos
class Meson:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.lom = 0
        self.comp = 0
        
    def libre(self):
        return  self.capacidad - self.lom - self.comp
        
    def lleno(self):
        return self.libre() <= 0
    
    def __str__(self):
        estado = "  Mesón: "+ str(self.lom)+" lomitos, "
        estado += str(self.comp)+ " completos, " 
        estado += str(self.libre())+ " libre(s)"
        return estado

class Mozo:
    def __init__(self, tipo, Max, meson):
        self.tipo = tipo
        self.Max = Max
        self.meson = meson
        self.faltan = 0

    def retiraPlatos(self):
        nPlatos = random.randint(0,self.Max)
        print()
        print("  Mozo quiere "+str(nPlatos)+" "+self.tipo,end="s  ")
        cuenta = 0
        for i in range (0,nPlatos):
            if self.tipo == "lomito" and not self.meson.lom <= 0:
                cuenta += 1
                self.meson.lom -= 1
            elif self.tipo == "completo" and not self.meson.comp <= 0:
                cuenta += 1
                self.meson.comp -= 1
        print("y retira " + str(cuenta) +" "+self.tipo+"s")
        self.faltan = nPlatos - cuenta

class Cocinero:
    def __init__(self,tipo,Max,meson):
        self.tipo = tipo
        self.Max = Max
        self.meson = meson

    def agregaPlatos(self):
        nPlatos = random.randint(0,self.Max)
        cuenta = 0
        for i in range (0,nPlatos):
            if not self.meson.lleno():
                cuenta += 1
                if self.tipo == "lomito":
                    self.meson.lom += 1
                else:   # self.tipo == "completo"
                    self.meson.comp += 1
        print("  Cocinero agrega "+str(cuenta)+" de "+str(nPlatos)+" "+self.tipo+"s")
        print(self.meson)

### programa principal ###
meson=Meson(20)                           # crea un mesón de capacidad 20 platos
cocinero1 = Cocinero("lomito",6,meson)    # crea cocinero con máx. 6 lomitos            
cocinero2 = Cocinero("completo",8,meson)  # crea cocinero con máx. 8 completos 
mozo1=Mozo("lomito",5,meson)              # crea mozo que retira máx. 5 lomitos
mozo2=Mozo("completo",4,meson)            # crea mozo que retira máx. 4 completos

t=0     # ejecuta 50 iteraciones
while t < 50:
    cocinero1.agregaPlatos()
    cocinero2.agregaPlatos()
    print("  Mesón lleno : ", meson.lleno())
    mozo1.retiraPlatos()
    print("  Faltan : ", mozo1.faltan," ",mozo1.tipo)
    mozo2.retiraPlatos()
    print("  Faltan : ", mozo2.faltan," ",mozo2.tipo)
    t = t + 1
    print()
    print ("t = "+ str(t)+"  ",meson)
# fin de la iteración
