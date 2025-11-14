"""
SISTEMA DE VEHÍCULOS - POO
Herencia, Composición y Encapsulamiento
"""

class Motor:
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor
    
    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self, valor):
        self._potencia = valor
    
    def encender_motor(self):
        return f"Motor {self.tipo} encendido - {self.potencia}HP"
    
    def detener_motor(self):
        return f"Motor {self.tipo} detenido"
    
    def __str__(self):
        return f"Motor {self.tipo} de {self.potencia}HP"


class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._encendido = False
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, valor):
        self._marca = valor
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, valor):
        self._anio = valor
    
    def encender(self):
        self._encendido = True
        return f"{self.marca} {self.modelo} encendido"
    
    def apagar(self):
        self._encendido = False
        return f"{self.marca} {self.modelo} apagado"
    
    def estado(self):
        return "Encendido" if self._encendido else "Apagado"
    
    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo} ({self.anio}) - Estado: {self.estado()}"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_puertas, motor):
        super().__init__(marca, modelo, anio)
        self._numero_puertas = numero_puertas
        self.motor = motor  # Composición
    
    @property
    def numero_puertas(self):
        return self._numero_puertas
    
    @numero_puertas.setter
    def numero_puertas(self, valor):
        self._numero_puertas = valor
    
    def abrir_maletero(self):
        return f"Maletero del {self.marca} {self.modelo} abierto"
    
    def tocar_claxon(self):
        return "¡Beep! ¡Beep!"
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nTipo: Automóvil - Puertas: {self.numero_puertas}\nMotor: {self.motor}"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindraje, motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self.motor = motor  # Composición
    
    @property
    def cilindraje(self):
        return self._cilindraje
    
    @cilindraje.setter
    def cilindraje(self, valor):
        self._cilindraje = valor
    
    def hacer_caballito(self):
        return f"¡{self.marca} {self.modelo} haciendo caballito!"
    
    def usar_patada_arranque(self):
        return "Usando patada de arranque..."
    
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nTipo: Motocicleta - Cilindraje: {self.cilindraje}cc\nMotor: {self.motor}"


# PROGRAMA PRINCIPAL
def main():
    print("🚗 SISTEMA DE VEHÍCULOS 🏍️")
    print("=" * 40)
    
    # Crear motores
    motor_v8 = Motor("V8", 450)
    motor_4cil = Motor("4 Cilindros", 180)
    motor_moto1 = Motor("2 Tiempos", 125)
    motor_moto2 = Motor("4 Tiempos", 600)
    
    # Crear vehículos
    carro1 = Automovil("Toyota", "Corolla", 2023, 4, motor_4cil)
    carro2 = Automovil("Ford", "Mustang", 2024, 2, motor_v8)
    
    moto1 = Motocicleta("Yamaha", "MT-07", 2023, 700, motor_moto1)
    moto2 = Motocicleta("Honda", "CBR", 2024, 600, motor_moto2)
    
    print("📦 VEHÍCULOS CREADOS:")
    print(carro1)
    print("-" * 30)
    print(carro2)
    print("-" * 30)
    print(moto1)
    print("-" * 30)
    print(moto2)
    print()
    
    print("🎬 PROBANDO MÉTODOS:")
    print("=" * 30)
    
    # Probar métodos de carros
    print("CARROS:")
    print(carro1.encender())
    print(carro1.motor.encender_motor())
    print(carro1.tocar_claxon())
    print(carro1.abrir_maletero())
    print(carro1.apagar())
    print()
    
    # Probar métodos de motos
    print("MOTOS:")
    print(moto2.encender())
    print(moto2.motor.encender_motor())
    print(moto2.usar_patada_arranque())
    print(moto2.hacer_caballito())
    print(moto2.apagar())

# Ejecutar el programa
if __name__ == "__main__":
    main()