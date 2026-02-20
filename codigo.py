import threading
import time
import random

islas_disponibles = ["Tenerife", "Gran Canaria", "Lanzarote", "La Palma", "El Hierro", "La Gomera", "Fuerteventura"]
plataformas = {isla: threading.Semaphore(1) for isla in islas_disponibles}

buffer_molecular = ""

class Viajero(threading.Thread):
    def __init__(self, nombre, isla_origen, isla_destino, acento, modo_seguro=True):
        super().__init__()
        self.nombre = nombre
        self.origen = isla_origen
        self.destino = isla_destino
        self.acento = acento
        self.modo_seguro = modo_seguro

    def run(self):
        if self.modo_seguro:
            self.teletransporte_seguro()
        else:
            self.teletransporte_con_fallos()

    def teletransporte_seguro(self):
        print(f"[ESPERA] {self.nombre} ({self.acento}) esperando plataforma en {self.destino}...")
        
        with plataformas[self.destino]:
            print(f"[INICIO] {self.nombre} se desmaterializa en {self.origen}...")
            time.sleep(random.uniform(0.5, 1.5)) 
            print(f"[EXITO] {self.nombre} ha llegado a {self.destino} sin mutaciones.")

    def teletransporte_con_fallos(self):
        global buffer_molecular
        print(f"[PELIGRO] {self.nombre} entrando en plataforma {self.destino} SIN PERMISO!")
        
        mitad_nombre = self.nombre[:len(self.nombre)//2]
        buffer_molecular += f"{mitad_nombre}-{self.acento}-"
        
        time.sleep(random.uniform(0.1, 0.5))
        print(f"[MUTACIÓN] {self.nombre} se ha mezclado en el flujo de datos.")


def ejecutar_simulacion(segura=True):
    global buffer_molecular
    buffer_molecular = ""
    
    viajeros_datos = [
        ("Aday", "Tenerife", "Gran Canaria", "Tinerfeño"),
        ("Yeray", "Lanzarote", "Gran Canaria", "Conejero"),
        ("Paco", "Murcia", "Gran Canaria", "Murciano (Acho)")
    ]

    hilos = []
    
    print(f"\n INICIANDO SISTEMA (Modo Seguro: {segura})")
    
    for nom, ori, dest, ace in viajeros_datos:
        v = Viajero(nom, ori, dest, ace, modo_seguro=segura)
        hilos.append(v)
        v.start()

    for h in hilos:
        h.join()

    if not segura:
        print("\nRESULTADO DEL DESASTRE MOLECULAR")
        print(f"Sujeto resultante en la plataforma: {buffer_molecular}")
        if "Murciano" in buffer_molecular:
            print("ALERTA: Se ha detectado trazas de 'pijo' y 'acho' en el ADN canario. Sistema bloqueado.")

if __name__ == "__main__":
    ejecutar_simulacion(segura=True)
    
    time.sleep(2)
    
    ejecutar_simulacion(segura=False)