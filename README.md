# 🚗 Sistema de Vehículos - POO
## 📖 Descripción del Programa
Sistema orientado a objetos que implementa vehículos utilizando los principios de POO en Python. Incluye herencia, composición, encapsulamiento y polimorfismo.

## 🎯 Características Implementadas
- **🔒 Encapsulamiento**: Atributos privados con @property y @setter
- **👑 Herencia**: Automóvil y Motocicleta heredan de Vehículo
- **🔗 Composición**: Cada vehículo contiene un objeto Motor
- **🔄 Polimorfismo**: Sobrescritura del método __str__()
## 📊 Diagrama UML

```ascii
    ╔═══════════════════════════════╗
    ║           VEHÍCULO            ║
    ╠═══════════════════════════════╣
    ║            -marca             ║
    ║            -modelo            ║
    ║             -año              ║
    ╠═══════════════════════════════╣
    ║          +encender()          ║
    ║          +apagar()            ║
    ║          +__str__()           ║
    ╚═══════════════════════════════╝
                ║
                ║
    ╔═══════════╩═══════════╗
    ║                       ║
    ║                       ║
▼════════▼             ▼════════▼
╔══════════════╗       ╔══════════════╗
║  AUTOMÓVIL   ║       ║ MOTOCICLETA  ║
╠══════════════╣       ╠══════════════╣
║  -puertas    ║       ║ -cilindraje  ║
╠══════════════╣       ╠══════════════╣
║ +abrir_      ║       ║ +hacer_      ║
║  maletero()  ║       ║  caballito() ║
║ +tocar_      ║       ║ +usar_       ║
║  claxon()    ║       ║  patada()    ║
║ +__str__()   ║       ║ +__str__()   ║
╚══════════════╝       ╚══════════════╝
        ║                     ║
        ║                     ║
        ╚═══════════╦═════════╝
                    ║
              ╔═══════════╗
              ║   MOTOR   ║
              ╠═══════════╣
              ║   -tipo   ║
              ║ -potencia ║
              ╠═══════════╣
              ║+encender_ ║
              ║  motor()  ║
              ║+detener_  ║
              ║  motor()  ║
              ║+__str__() ║
              ╚═══════════╝









