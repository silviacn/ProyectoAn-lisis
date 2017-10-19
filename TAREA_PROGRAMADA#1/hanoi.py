from tkinter import *
import timeit

i = 0

def Hanoi(n,Fuente,Auxiliar,Destino):
    
    if(n == 1): 

        print (Fuente,"->",Destino)
        #lbresultado = Label(master, text= str(Fuente+"->"+Destino)).place(x=130,y=320)
        

    else: 

        Hanoi(n-1,Fuente,Destino,Auxiliar) 

        print (Fuente,"->", Destino)
        #lbresultado = Label(master, text= str(Fuente+"->"+Destino)).place(x=200,y=320)

        Hanoi(n-1,Auxiliar,Fuente,Destino)
        
def antes():

    start_time = timeit.default_timer()
    
    Hanoi(int(e1.get()),"A","B","C")

    elapsed = timeit.default_timer() - start_time

    print(elapsed)

    lbresultado = Label(master, text= str(elapsed)).place(x=330,y=2)

    
   

master = Tk()
master.geometry("500x200")
Label(master, text="INGRESE LA CANTIDAD DE FICHAS").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)

Button(master, text='Show', command=antes).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
