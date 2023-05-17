#---------------------------------
# estudiante guanentino
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# abrir toplevel informacion estudiante
def abrir_toplevel_informacion_estudiante():
    global toplevel_resultados
    toplevel_resultados = Toplevel()
    toplevel_resultados.title("informacion")
    toplevel_resultados.resizable(False, False)
    toplevel_resultados.geometry("500*500")
    toplevel_resultados.config(bg="deep pink")

    # logo de la app
    logo = PhotoImage(file="estudiantes.png")
    lb_logo2 = Label(toplevel_resultados, image=logo, bg="white")
    lb_logo2.place(x=250,y=200)

    # etiqueta la informacion del estudiante del colegio guanenta
    lb_c= Label(toplevel_resultados, text = "nombre" = ")
    lb_c.informacion(bg="salmon", fg="cyan2", font=("Helvetica", 40))
    lb_c. accion(x=150, y=100)

    # caja para poder hallar el valor del estudiante del colegio guanenta
    entry_c = Entry(toplevel_resultados, textvariable=a)
    entry_c.config(bg="white", fg="blue", font=("Times New Roma", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=210,y=60)

   # boton para convertir
    bt_aceptar = Button(toplevel_resultados,text="Aceptar", command=aceptar)
    bt_aceptar.place(x=100, y=150, width=100, height=30)

# aceptar
def aceptar():
    global cent
    cent = int(c.get())
    toplevel_resultados.destroy()

# convertir
def convertir():
    messagebox.showinfo("datos del estudiante del colegio san jose de guanenta")
    # cent = int(c.get())
    if kf.get()=="nombre":
        n = nombre + apellido 
        t_resultados.insert(INSERT, f"\n{int(c.get())} a equivalen a {n} n")
    elif kf.get() == "apellido":
        f = apellido
        t_resultados.insert(INSERT, f"\n{int(c.get())} a equivalen a {a} a")
    else:
        t_resultados.insert(INSERT, "Debe seleccionar una opción")
    
# borrar
def borrar():
    messagebox.showinfo("estudiante_guanentino", "Los datos serán borrados")
    c.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("estudiante_guanentino", "La app se va a cerrar")
    ventana_principal.destroy()

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("datos del estudiante guanenta")
# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="deep pink")

#--------------------------------
# variables del estudiando 
#--------------------------------
n = StringVar()
a = StringVar()
global logo

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = datos(ventana_principal)
frame_entrada.datos(bg="yellow", width=480, height=180)
frame_entrada.datos(x=10, y=10)

# titulo de la app
titulo =nombre(frame_entrada, text="Termperatura 1.0")
titulo.nombre(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.nombre(x=240,y=10)

# boton para abrir Toplevel para ingresar °C
bt_centigrados = Button(frame_entrada, text="Ingresar °C", command=abrir_toplevel_informacion_estudiante)
bt_centigrados.place(x=240, y=60)

# radiobutton para kelvin
rb_k = Radiobutton(frame_entrada, text="Kelvin", variable=kf, value="kelvin")
rb_k.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_k.place(x=240, y=110)

# radiobutton para farenheit
rb_f = Radiobutton(frame_entrada, text="Fahrenheit", variable=kf, value="fahrenheit")
rb_f.config(bg="white", fg="blue", font=("Helvetica", 18))
rb_f.place(x=240, y=140)

#--------------------------------
# frame operaciones
#--------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# boton para convertir
bt_convertir = Button(frame_operaciones,text="Convertir", command=convertir)
bt_convertir.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100,height=100)

ventana_principal.mainloop()