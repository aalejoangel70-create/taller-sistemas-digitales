# taller-sistemas-digitales
Taller — Sistemas Digitales con Arduino laboratorio 2 
> Taller práctico de sistemas embebidos usando Arduino UNO, sensores, pantallas OLED y comunicación serial con Python.
---
 Contenido del Taller
Punto	Título	Video	Estado
Punto 1	 ChatBot Básico con LEDs	—	 
Punto 2	 Juego en Pantalla OLED	 Ver	 
Punto 3	 Detector de Colores CNY70	 Ver	 
---
 Estructura del Repositorio
```
taller-sistemas-digitales/
│
├── README.md
│
├── Punto_1_ChatBot/
│   ├── README.md
│   ├── sketch_arduino.ino       ← Código Arduino (control LED por serial)
│   ├── app_visual.py            ← Chatbot con interfaz gráfica (tkinter)
│   ├── voz_arduino.py           ← Chatbot con voz y sonido
│   └── imagenes/
│       ├── simulacion_tinkercad.png
│       ├── esquematico.png
│       ├── prueba_ejecucion.png
│       ├── circuito_fisico.png
│       └── ejecucion_pc.png
│
├── Punto_2_OLED/
│   ├── README.md
│   └── imagenes/
│
└── Punto_3_CNY70/
    ├── README.md
    └── imagenes/
```
---
🛠️ Herramientas Utilizadas
Herramienta	Uso
Arduino IDE 2.3.8	Programación del microcontrolador
Tinkercad	Simulación de circuitos
Python 3	Chatbot (tkinter, pyttsx3, winsound)
Arduino UNO	Microcontrolador principal
OLED SSD1306	Pantalla para el juego
Sensor CNY70	Detección de superficies
---
Cómo ejecutar el Punto 1
```bash
# Instalar dependencias
pip install pyttsx3

# Cargar sketch_arduino.ino en el Arduino UNO

# Ejecutar interfaz gráfica
python app_visual.py

# O versión consola con sonido
python voz_arduino.py
```
---
 Videos de evidencia
Punto 2 — Juego OLED: https://youtube.com/shorts/u5heSupkzH0
Punto 3 — Detector CNY70: https://youtube.com/shorts/OUkCB5Y51H4
---
