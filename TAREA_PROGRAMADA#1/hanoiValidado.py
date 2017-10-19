from tkinter import *
import timeit
from tkinter import messagebox

i = 0

def Hanoi(n,Fuente,Auxiliar,Destino):
    
    if(n == 1): 

        print (Fuente,"->",Destino)
   
    else: 

        Hanoi(n-1,Fuente,Destino,Auxiliar) 

        print (Fuente,"->", Destino)

        Hanoi(n-1,Auxiliar,Fuente,Destino)


#Centra la pantalla
def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
        
def antes():

    if (e1.get() == "") or (e1.get().isalpha()) or (int(e1.get())<0):
        messagebox.showwarning('Atención', 'Debe ingresar un número entero positivo.')
    else:
        if (int(e1.get())>=20):

            messagebox.showinfo('Información', 'El valor ingresado puede provocar que la máquina aumente la temperatura del procesador considerablemente.')
        
        start_time = timeit.default_timer()
        
        Hanoi(int(e1.get()),"A","B","C")

        elapsed = timeit.default_timer() - start_time

        print(elapsed)

        lbresultado = Label(master, text= str(elapsed)).place(x=330,y=2)

    
   

master = Tk()
master.geometry("500x200")
master.title("Torres de Hanoi")
Label(master, text="Ingrese la cantidad de fichas: ").grid(row=0)
centrar(master)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Show', command=antes).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
