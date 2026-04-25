
# taller-sistemas-digitales
Taller — Sistemas Digitales con Arduino laboratorio 2 

#  Punto 1 — ChatBot Básico: Iluminación y Monitoreo de Temperatura

##  Descripción

Sistema que utiliza Arduino UNO para el control de LEDs mediante un chatbot conversacional simple. El chatbot corre en Python en la computadora y se comunica con el Arduino vía comunicación serial.

---

##  ¿Cómo funciona?

El usuario escribe comandos como encender o apagar, Python los envía al Arduino por puerto serial y el Arduino enciende o apaga el LED en el pin 13.

- El chatbot se ejecuta en la computadora y se comunica con Arduino vía serial
- Cuando el usuario envía encender o apagar se controlan los LEDs
- La interfaz visual muestra un círculo amarillo (encendido) o gris (apagado)

---

![Simulacion Tinkercad](simulacion_tinkercad.png)
![Esquematico](esquematico.png)
![Circuito fisico](circuito_fisico.png)
![Ejecucion PC](ejecucion_pc.png)
![Prueba Arduino](prueba_ejecucion.png)

---

##  Componentes

| Componente | Cantidad |
|-----------|---------|
| Arduino UNO | 1 |
| LED | 1 |
| Resistencia 220Ω | 1 |
| Protoboard | 1 |
| Cables | varios |

### Conexión
- LED positivo → Pin 13 del Arduino (con resistencia 220Ω)
- LED negativo → GND

🔗 [Ver simulación en Tinkercad](https://www.tinkercad.com/things/2fg1y0LspLa-chatbot-basico)

---

## Código Arduino

```cpp
String comando;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    comando = Serial.readString();
    comando.trim();

    if (comando.indexOf("encender") >= 0) {
      digitalWrite(13, HIGH);
    }

    if (comando.indexOf("apagar") >= 0) {
      digitalWrite(13, LOW);
    }
  }
}
```

---

##  Archivos Python

### `app_visual.py` — Interfaz gráfica con Tkinter
Muestra un círculo que simula el LED (gris = apagado, amarillo = encendido) con botones de control y respuesta por voz.

### `voz_arduino.py` — Versión consola con sonido
Control por texto desde la terminal con beep de frecuencia alta al encender y baja al apagar.

---

##  Instrucciones de uso

```bash
pip install pyttsx3
python app_visual.py
```

### Comandos disponibles

| Comando | Acción |
|---------|--------|
| `encender` | Enciende el LED |
| `apagar` | Apaga el LED |
| `estado` | Dice el estado actual |
| `salir` | Cierra el sistema |

---

##  Conceptos aplicados

- Comunicación **serial** entre Python y Arduino
- Interfaces gráficas con **Tkinter**
- Síntesis de voz con **pyttsx3**
- Control de pines digitales con `digitalWrite()`
- Simulación de circuitos en **Tinkercad**

---

*Punto 1 — Taller Sistemas Digitales 2026*
---
 Videos de evidencia
Punto 2 — Juego OLED: https://youtube.com/shorts/u5heSupkzH0
Para este punto se desarrolló una interfaz gráfica en Python usando Tkinter que permite controlar el sistema de iluminación de forma visual e intuitiva. La interfaz simula visualmente el estado del LED mediante un círculo que cambia de color:

-  Amarillo → LED encendido
-  Gris → LED apagado

El objetivo fue mitigar errores del sistema al tener una representación visual clara del estado actual del LED, evitando confusiones al operar solo con texto en consola.

---

##  ¿Cómo funciona?

La interfaz tiene 3 formas de interactuar:
1. Escribir el comando en el campo de texto y presionar "Enviar"
2. Presionar el botón "Encender" directamente
3. Presionar el botón "Apagar" directamente

El flujo del sistema es:

- El usuario escribe o presiona un botón
- La interfaz cambia el color del círculo de inmediato
- El sistema responde con voz usando `pyttsx3`
- La señal se envía al Arduino por puerto serial
- El LED físico enciende o apaga

---

##  Estados visuales

| Estado | Color del círculo | LED físico |
|--------|-----------------|------------|
| Encendido | 🟡 Amarillo | HIGH (pin 13) |
| Apagado | ⚫ Gris | LOW (pin 13) |

Punto 3 — Detector CNY70: https://youtube.com/shorts/OUkCB5Y51H4
##  Video de demostración

> **[Ver video del funcionamiento](https://youtube.com/shorts/OUkCB5Y51H4)**
##  Descripción

Desarrollo de un detector de superficies claras y oscuras usando el sensor óptico reflexivo CNY70 y Arduino UNO. El proyecto siguió una metodología de simulación primero, físico después:

1.  Fase 1 — Simulación en Tinkercad: se diseñó y validó el circuito virtualmente
2.  Fase 2 — Implementación física: una vez validado, se montó el circuito real con los componentes

---

##  ¿Cómo funciona el CNY70?

El sensor emite luz infrarroja y mide cuánta luz rebota de la superficie:

- Superficie blanca/clara → refleja mucha luz → valor bajo → CLARO
- Superficie negra/oscura → absorbe la luz → valor alto → OSCURO

El CNY70 tiene dos partes internas:
- Un emisor infrarrojo (LED IR) que emite luz invisible
- Un fototransistor receptor que mide la luz reflejada

---

##  Fase 1 — Simulación en Tinkercad

Antes de armar el circuito físico se simuló en Tinkercad para:
- Probar la lógica sin riesgo de dañar componentes
- Verificar las conexiones del sensor
- Validar los valores analógicos leídos
- Ajustar el umbral de detección

---

##  Fase 2 — Circuito Físico

### Componentes

| Componente | Cantidad | Valor |
|-----------|---------|-------|
| Arduino UNO | 1 | — |
| Sensor CNY70 | 1 | — |
| Resistencia emisor IR | 1 | 180Ω |
| Resistencia receptor | 1 | 10kΩ |
| LED indicador | 1 | rojo o verde |
| Resistencia LED | 1 | 220Ω |
| Protoboard | 1 | — |

### Conexiones

| Pin CNY70 | Conexión |
|-----------|----------|
| Ánodo LED IR (pin 1) | 5V con resistencia 180Ω |
| Cátodo LED IR (pin 2) | GND |
| Colector fototransistor (pin 3) | 5V |
| Emisor fototransistor (pin 4) | Pin A0 + 10kΩ a GND |
| LED indicador (+) | Pin 13 con 220Ω |
| LED indicador (-) | GND |

---

##  Código Arduino

```cpp
int sensorPin = A0;
int ledPin = 13;
int valorSensor = 0;
int umbral = 500;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  Serial.println("Detector CNY70 iniciado");
}

void loop() {
  valorSensor = analogRead(sensorPin);
  Serial.print("Valor: ");
  Serial.print(valorSensor);
  Serial.print("  →  ");

  if (valorSensor < umbral) {
    Serial.println("SUPERFICIE CLARA");
    digitalWrite(ledPin, HIGH);
  } else {
    Serial.println("SUPERFICIE OSCURA");
    digitalWrite(ledPin, LOW);
  }
  delay(300);
}
```

---

##  Valores de referencia

| Superficie | Valor (0–1023) | Resultado |
|------------|----------------|-----------|
| Blanco | 0 – 300 | CLARA |
| Gris claro | 300 – 500 | CLARA |
| Gris oscuro | 500 – 700 | OSCURA |
| Negro | 700 – 1023 | OSCURA |

##  Ventajas de la metodología simulación → físico

- Detecta errores de diseño sin riesgo de dañar componentes
- Permite ajustar el código antes del ensamblaje real
- Valida la lógica del sistema de forma segura
- Ahorra tiempo al llegar al montaje físico

---

## Conceptos aplicados

- Sensor óptico CNY70 y lectura analógica con `analogRead()`
- Divisor de voltaje con fototransistor
- Umbralización para clasificación binaria (claro/oscuro)
- Comunicación por puerto serial en tiempo real
- Metodología simular primero → implementar después
---
