# 🔴 Punto 3 — Detector de Colores con Sensor CNY70

## 🎬 Video de demostración

> 📹 **[Ver video del funcionamiento](https://youtube.com/shorts/OUkCB5Y51H4)**

---

## 📌 Descripción

Desarrollo de un detector de superficies claras y oscuras usando el sensor óptico reflexivo **CNY70** y **Arduino UNO**. El sistema detecta el color/reflectividad de una superficie al emitir luz infrarroja y medir la cantidad de luz reflejada.

Cuando una superficie **clara (blanca)** está cerca → refleja mucha luz → el fototransistor conduce más  
Cuando una superficie **oscura (negra)** está cerca → absorbe la luz → el fototransistor conduce menos

---

## ⚙️ ¿Cómo funciona el CNY70?

```
   CNY70
┌──────────────┐
│  LED IR  →→→ │──── emite luz infrarroja
│  Fototrans.  │──── recibe luz reflejada
└──────────────┘
        ↓
   Señal analógica
        ↓
   Arduino A0
        ↓
   Clasifica: CLARO / OSCURO
```

El **CNY70** es un sensor óptico de reflexión compuesto por:
- Un **emisor infrarrojo** (LED IR) con resistencia de 180Ω
- Un **fototransistor receptor** con resistencia de 10kΩ en configuración divisor de voltaje

---

## 🔌 Conexión del Hardware

### Componentes necesarios

| Componente | Cantidad | Valor |
|-----------|---------|-------|
| Arduino UNO | 1 | — |
| Sensor CNY70 | 1 | — |
| Resistencia emisor | 1 | 180Ω |
| Resistencia receptor | 1 | 10kΩ |
| LED indicador | 1 | rojo/verde |
| Resistencia LED | 1 | 220Ω |
| Protoboard | 1 | — |
| Cables jumper | varios | — |

### Tabla de conexiones

| Pin CNY70 | Conexión |
|-----------|----------|
| Ánodo LED IR (pin 1) | 5V a través de resistencia 180Ω |
| Cátodo LED IR (pin 2) | GND |
| Colector fototrans. (pin 3) | 5V |
| Emisor fototrans. (pin 4) | Pin A0 del Arduino + resistencia 10kΩ a GND |

> 🔗 Referencia: [Tutorial CNY70 - Talos Electronics](https://www.taloselectronics.com/blogs/tutoriales/sensor-optico-de-reflexion-cny70)

---

## 💻 Código Arduino

```cpp
int sensorPin = A0;
int ledPin = 13;
int valorSensor = 0;
int umbral = 500; // Ajustar según calibración

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  Serial.println("=== Detector CNY70 iniciado ===");
  Serial.println("Acercar superficie al sensor...");
}

void loop() {
  valorSensor = analogRead(sensorPin);

  Serial.print("Valor leído: ");
  Serial.print(valorSensor);
  Serial.print("  →  ");

  if (valorSensor < umbral) {
    Serial.println("SUPERFICIE CLARA (blanco/claro)");
    digitalWrite(ledPin, HIGH); // LED encendido = superficie clara
  } else {
    Serial.println("SUPERFICIE OSCURA (negro/oscuro)");
    digitalWrite(ledPin, LOW);  // LED apagado = superficie oscura
  }

  delay(300);
}
```

---

## ▶️ Instrucciones de uso

1. Armar el circuito según la tabla de conexiones
2. Cargar el código en el Arduino desde Arduino IDE
3. Abrir el **Serial Monitor** a **9600 baud**
4. Acercar distintas superficies al sensor (a ~5mm de distancia)
5. Observar la clasificación en el monitor serial

### Calibración
Si la detección no es precisa, ajustar el valor `umbral` en el código:
- Si detecta mal superficies claras → **bajar** el umbral
- Si detecta mal superficies oscuras → **subir** el umbral

---

## 🧠 Conceptos aplicados

- Sensor óptico de reflexión infrarroja **CNY70**
- Lectura de señal **analógica** con `analogRead()`
- Divisor de voltaje con fototransistor
- Umbralización para clasificación binaria (claro/oscuro)
- Comunicación por **puerto serial** para monitoreo

---

## 📊 Valores de referencia (típicos)

| Superficie | Valor analógico (0-1023) |
|------------|--------------------------|
| Blanco / muy claro | 0 – 400 |
| Gris / tono medio | 400 – 600 |
| Negro / muy oscuro | 600 – 1023 |

> ⚠️ Los valores exactos dependen de la distancia al sensor y la luz ambiental. Siempre calibrar en el entorno real de uso.

---

*Punto 3 — Taller Sistemas Digitales 2026*
