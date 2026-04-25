import tkinter as tk
import pyttsx3

voz = pyttsx3.init()

def hablar(texto):
    print(":", texto)
    voz.say(texto)
    voz.runAndWait()

estado_led = False

def encender():
    global estado_led
    estado_led = True
    canvas.itemconfig(foco, fill="yellow")
    hablar("LED encendido")

def apagar():
    global estado_led
    estado_led = False
    canvas.itemconfig(foco, fill="gray")
    hablar("LED apagado")

def comando():
    texto = entrada.get().lower()
    
    if "encender" in texto:
        encender()
    elif "apagar" in texto:
        apagar()
    elif "salir" in texto:
        hablar("Cerrando sistema")
        ventana.destroy()
    else:
        hablar("No entendí")

ventana = tk.Tk()
ventana.title("Sistema Inteligente")
ventana.geometry("300x400")

canvas = tk.Canvas(ventana, width=200, height=200)
canvas.pack()

foco = canvas.create_oval(50, 50, 150, 150, fill="gray")

entrada = tk.Entry(ventana)
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Enviar", command=comando)
boton.pack()

btn_on = tk.Button(ventana, text="Encender", command=encender)
btn_on.pack(pady=5)

btn_off = tk.Button(ventana, text="Apagar", command=apagar)
btn_off.pack(pady=5)

hablar("Sistema visual iniciado")

ventana.mainloop()
