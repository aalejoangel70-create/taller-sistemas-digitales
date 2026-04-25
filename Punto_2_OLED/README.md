# 🎮 Punto 2 — Juego Sencillo en Pantalla OLED con Arduino

## 🎬 Video de demostración

> 📹 **[Ver video del funcionamiento](https://youtube.com/shorts/u5heSupkzH0)**

---

## 📌 Descripción

Desarrollo de un juego sencillo usando **Arduino UNO** y una pantalla **OLED 0.96" (128x64, I2C)**. El objetivo fue programar una experiencia interactiva visual directamente en el microcontrolador, sin necesidad de una computadora durante la ejecución.

La pantalla OLED se comunica con el Arduino mediante el protocolo **I2C**, usando solo 2 cables de datos (SDA y SCL), lo que simplifica el cableado y libera pines digitales para otros usos.

---

## ⚙️ ¿Cómo funciona?

```
Arduino UNO
     ↓  (Protocolo I2C — pines A4 y A5)
Pantalla OLED 128x64
     ↓
Renderiza gráficos del juego en tiempo real
```

1. El Arduino ejecuta la lógica del juego en el `loop()`
2. Dibuja los elementos (personaje, obstáculos, puntaje) en un buffer de memoria
3. Envía ese buffer a la pantalla OLED con `display.display()`
4. El ciclo se repite actualizando la pantalla varios frames por segundo

---

## 🔌 Conexión del Hardware

### Componentes necesarios

| Componente | Cantidad |
|-----------|---------|
| Arduino UNO | 1 |
| Pantalla OLED 0.96" I2C (SSD1306) | 1 |
| Pulsador | 1 |
| Cables jumper | varios |
| Protoboard | 1 |

### Tabla de conexiones

| Pin OLED | Pin Arduino UNO |
|----------|----------------|
| VCC | 5V |
| GND | GND |
| SCL | A5 |
| SDA | A4 |
| Pulsador | Pin 2 + GND |

> 🔗 Referencia del circuito: [Tutorial OLED con Arduino](https://solectroshop.com/es/content/47-tutorial-de-la-pantalla-oled-con-arduino-uno-)

---

## 📦 Librerías necesarias

Instalar desde **Arduino IDE → Tools → Manage Libraries**:

| Librería | Para qué sirve |
|----------|---------------|
| `Adafruit SSD1306` | Controlar la pantalla OLED |
| `Adafruit GFX Library` | Dibujar formas, texto y gráficos |
| `Wire` | Comunicación I2C (incluida por defecto) |

---

## 💻 Código Arduino

```cpp
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

int posX = 10;
int posY = 50;
int obstaculoX = 128;
int puntaje = 0;
bool saltando = false;
int velocidadSalto = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("Error: OLED no encontrado");
    while (true);
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(20, 25);
  display.println("Presiona boton!");
  display.display();
  delay(2000);
}

void loop() {
  display.clearDisplay();
  display.drawLine(0, 60, 128, 60, WHITE);

  if (digitalRead(2) == LOW && !saltando) {
    saltando = true;
    velocidadSalto = -8;
  }
  if (saltando) {
    posY += velocidadSalto;
    velocidadSalto += 2;
    if (posY >= 50) { posY = 50; saltando = false; }
  }

  obstaculoX -= 3;
  if (obstaculoX < 0) { obstaculoX = 128; puntaje++; }

  display.fillRect(posX, posY, 8, 10, WHITE);
  display.fillRect(obstaculoX, 50, 6, 10, WHITE);

  display.setCursor(90, 0);
  display.print("Pts:"); display.print(puntaje);

  if (obstaculoX < posX + 8 && obstaculoX + 6 > posX && posY + 10 > 50) {
    display.clearDisplay();
    display.setTextSize(2);
    display.setCursor(25, 20); display.println("GAME");
    display.setCursor(35, 42); display.println("OVER");
    display.display();
    delay(3000);
    puntaje = 0; obstaculoX = 128; posY = 50;
  }

  display.display();
  delay(50);
}
```

---

## ▶️ Instrucciones de uso

1. Instalar las librerías desde el Library Manager de Arduino IDE
2. Conectar la OLED al Arduino según la tabla
3. Conectar un pulsador entre el **pin 2** y **GND**
4. Cargar el código en el Arduino
5. El juego inicia automáticamente

### Controles
| Acción | Control |
|--------|---------|
| Saltar | Presionar el pulsador (pin 2) |

---

## 🧠 Conceptos aplicados

- Protocolo de comunicación **I2C**
- Uso de librerías externas en Arduino
- Renderizado de gráficos en pantalla OLED
- Lógica de juego: física básica, colisiones y puntaje

---

*Punto 2 — Taller Sistemas Digitales 2026*
