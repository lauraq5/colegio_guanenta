import tkinter as tk
from tkinter import messagebox

#---------------------------------
# Desktop app No. 6 - datos de estudiantes del colegio guanenta
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("datos de un estudainte del colegio guanenta ")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="magenta2")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=260, height=300)
frame_entrada.place(x=40, y=40)

# logo de la app
logo = PhotoImage(file="img/escudo.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=25,y=25)


#se desea calcular las notas
def calcular_notas():
    nota_1 = float(entry_nota_1.get())
    nota_2 = float(entry_nota_2.get())
    nota_3 = float(entry_nota_3.get())
    
    promedio = (nota_1 + nota_2 + nota_3 ) / 3
    
    if promedio >= 4.5:
        mensaje_nota = "excelente"
    elif promedio >= 3.0:
        mensaje_nota = "Aprobado superior"
    else:
        mensaje_nota = "Reprobado bajo"
    
    messagebox.showinfo("Resultado", f"Promedio de notas: {promedio}\n{mensaje_nota}")
    

def calcular_masa_corporal():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    
    masa_corporal = peso / (altura ** 2)
    
    if masa_corporal < 18.5:
        estado = "Bajo peso"
    elif masa_corporal < 25:
        estado = "Peso normal"
    elif masa_corporal < 30:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"
    
    messagebox.showinfo("Resultado", f"Índice de masa corporal: {masa_corporal:.2f}\nEstado: {estado}")
    

def calcular_salud():
    # Aquí puedes incluir tu propia lógica para evaluar la salud del estudiante
    # y mostrar el resultado utilizando messagebox.showinfo()
    pass


# Crear la ventana principal
root = tk.Tk()
root.title("Cálculo de notas, masa corporal y salud")

# Etiquetas y campos de entrada para las notas
label_notas = tk.Label(root, text="Notas del estudiante")
label_notas.grid(row=0, column=0, padx=10, pady=5)

label_nota_1 = tk.Label(root, text="Nota 1: COGNITIVA:")
label_nota_1.grid(row=1, column=0, padx=10, pady=5)
entry_nota_1 = tk.Entry(root)
entry_nota_1.grid(row=1, column=1, padx=10, pady=5)

label_nota_2 = tk.Label(root, text="Nota 2: ACTITUDINAL:")
label_nota_2.grid(row=2, column=0, padx=10, pady=5)
entry_nota_2 = tk.Entry(root)
entry_nota_2.grid(row=2, column=1, padx=10, pady=5)

label_nota_3 = tk.Label(root, text="Nota 3: PROCEDIMENTAL:")
label_nota_3.grid(row=3, column=0, padx=10, pady=5)
entry_nota_3 = tk.Entry(root)
entry_nota_3.grid(row=3, column=1, padx=10, pady=5)


btn_calcular_notas = tk.Button(root, text="Calcular Notas", command=calcular_notas)
btn_calcular_notas.grid(row=4, column=0, columnspan=2, padx=10, pady=5)


# Etiquetas y campos de entrada para la masa corporal
label_masa_corporal = tk.Label(root, text="Masa corporal del estudiante")
label_masa_corporal.grid(row=5, column=0, padx=10, pady=5)

label_peso = tk.Label(root, text="Peso (kg):")
label_peso.grid(row=6, column=0, padx=10, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=6, column=1, padx=10, pady=5)

label_altura = tk.Label(root, text="Altura (m):")
label_altura.grid(row=7, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=7, column=1, padx=10, pady=5)

btn_calcular_masa_corporal = tk.Button(root, text="Calcular Masa Corporal", command=calcular_masa_corporal)
btn_calcular_masa_corporal.grid(row=8, column=0, columnspan=2, padx=10, pady=5)


# Botón para calcular la salud
btn_calcular_salud = tk.Button(root, text="Calcular Salud", command=calcular_salud)
btn_calcular_salud.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()

