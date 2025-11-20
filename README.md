# 🚗 Sistema de Vehículos - POO
## 📖 Descripción del Programa
Sistema orientado a objetos que implementa vehículos utilizando los principios de POO en Python. Incluye herencia, composición, encapsulamiento y polimorfismo.

## 🎯 Características Implementadas
- **🔒 Encapsulamiento**: Atributos privados con @property y @setter
- **👑 Herencia**: Automóvil y Motocicleta heredan de Vehículo
- **🔗 Composición**: Cada vehículo contiene un objeto Motor
- **🔄 Polimorfismo**: Sobrescritura del método __str__()

 ## CAPTURAS
<img width="1364" height="767" alt="Captura de pantalla 2025-11-14 170226" src="https://github.com/user-attachments/assets/60e37892-2c74-491d-a583-16bf0ab4346e" />
<img width="1365" height="766" alt="Captura de pantalla 2025-11-14 170239" src="https://github.com/user-attachments/assets/67acad0e-3b7a-44c4-9f52-b16fad000d36" />


  
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










