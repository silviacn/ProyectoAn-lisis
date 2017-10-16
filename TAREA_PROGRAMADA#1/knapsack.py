import random
from tkinter import *
import timeit

"""
*****************************************************************************************
* Análisis de algoritmos                                                                *
*                                                                                       *
* Silvia Calderón Navarro                                                               *
*                                                                                       *
* Algoritmo de la mochila                                                               *
*                                                                                       *
*****************************************************************************************
"""

#Clase en la que se crea la ventana y se ejecuta el algoritmo
class Knapsack:    
    def __init__(self, master):

        #Variables globales        
        try:
            self.xrange
        except:
            self.xrange = range
        self.max = None
        self.name = None
        self.benefit = None
        self.weight = None
        self.num_guesses = 0
        self.items  = []
        self.bagged = []
        
        self.master = master
        master.title("Problema de la mochila")
        self.master.geometry("400x600")

        #Creación de labels
        self.message = "Elija el peso máximo de la mochila: "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label_max = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validateMax) # we have to wrap the command
        self.entry_max = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        
        self.message = "Elija el nombre del objeto: "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label_name = Label(master, textvariable=self.label_text)

        self.entry_name = Entry(master)

        self.message = "Elija el beneficio del objeto: "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label_benefit = Label(master, textvariable=self.label_text)
        
        vcmd = master.register(self.validateBenefit)
        self.entry_benefit = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.message = "Elija el peso del objeto: "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label_weight = Label(master, textvariable=self.label_text)
        
        vcmd = master.register(self.validateWeight)
        self.entry_weight = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        #Creación de botones
        self.create_button = Button(master, text="Crear objeto", command=self.createlist)
        self.start_button = Button(master, text="Resolver", command=self.results, state=DISABLED)
        self.new_button = Button(master, text="Nuevo", command=self.resetnew)

        #Creación de labels
        self.label_result = Label(master, text="RESULTADO...")
        self.label_final = Label(master, text="")
        self.label_time = Label(master, text="")

        #Posicionamiento de los elementos en la pantalla
        self.label_max.grid(row=0, column=2, columnspan=2)
        self.entry_max.grid(row=1, column=2, columnspan=2)        
        self.label_name.grid(row=3, column=2, columnspan=2)
        self.entry_name.grid(row=4, column=2, columnspan=2)
        self.label_benefit.grid(row=6, column=2, columnspan=2)
        self.entry_benefit.grid(row=7, column=2, columnspan=2)
        self.label_weight.grid(row=9, column=2, columnspan=2)
        self.entry_weight.grid(row=10, column=2, columnspan=2)
        self.create_button.grid(row=11, column=1, columnspan=2)
        self.start_button.grid(row=11, column=3, columnspan=2)
        self.new_button.grid(row=11, column=4, columnspan=2)
        self.label_result.grid(row=13, column=0)
        self.label_final.grid(row=14, column=0)
        self.label_time.grid(row=15, column=0)

    #Función para validar el peso máximo de la mochila
    def validateMax(self, new_text):
        if not new_text: 
            self.max = None
            return True

        try:
            max = int(new_text)
            if 1 <= max:
                self.max = max
                return True
            else:
                return False
        except ValueError:
            return False
        
    #Función para validar el beneficio del elemento
    def validateBenefit(self, new_text):
        if not new_text:
            self.benefit = None
            return True

        try:
            benefit = int(new_text)
            if 1 <= benefit:
                self.benefit = benefit
                return True
            else:
                return False
        except ValueError:
            return False

    #Función para validar el peso del elemento
    def validateWeight(self, new_text):
        if not new_text:
            self.weight = None
            return True

        try:
            weight = int(new_text)
            if 1 <= weight:
                self.weight = weight
                return True
            else:
                return False
        except ValueError:
            return False

    #Procedimiento que limpia los espacios al introducir un elemento
    def reset(self):
        self.entry_max.configure(state=DISABLED)
        self.entry_name.delete(0, END)
        self.entry_benefit.delete(0, END)
        self.entry_weight.delete(0, END)
        self.name = ""
        self.benefit = 0
        self.weight = 0

        self.create_button.configure(state=NORMAL)
        self.start_button.configure(state=NORMAL)

    #Procedimiento que limpia los espacios para crear una nueva mochila
    def resetnew(self):
        self.entry_max.configure(state=NORMAL)
        self.entry_max.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_benefit.delete(0, END)
        self.entry_weight.delete(0, END)
        self.name = ""
        self.max = None
        self.benefit = None
        self.weight = None
        self.items  = []
        self.label_result.config(text="RESULTADO")
        self.label_final.config(text="")
        self.label_time.config(text="")

        self.create_button.configure(state=NORMAL)
        self.start_button.configure(state=DISABLED)

    #Procedimiento que crea la lista de elementos
    def createlist(self):
        self.name = self.entry_name.get()
        self.items.append((self.name, self.weight, self.benefit))        
        self.reset()

    #Función que devuelve el valor total
    def totalvalue(self, comb):
        totwt = totval = 0
        for item, wt, val in comb:
            totwt  += wt
            totval += val
        return (totval, -totwt) if totwt <= 400 else (0, 0)

    #Función creación de la mochila
    def knapsack01_dp(self):
        table = [[0 for w in range(self.max + 1)] for j in self.xrange(len(self.items) + 1)]
     
        for j in self.xrange(1, len(self.items) + 1):
            item, wt, val = self.items[j-1]
            for w in self.xrange(1, self.max + 1):
                if wt > w:
                    table[j][w] = table[j-1][w]
                else:
                    table[j][w] = max(table[j-1][w],
                                      table[j-1][w-wt] + val)

        for row in table:
          print (' '.join(map(str,row)))

        
        result = []
        w = self.max
        
        for j in range(len(self.items), 0, -1):
            was_added = table[j][w] != table[j-1][w]     
            if was_added:
                item, wt, val = self.items[j-1]
                result.append(self.items[j-1])
                w -= wt

        return result

    #Función muestra los resultados de esa mochila
    def results(self):
        self.create_button.configure(state=DISABLED)
        self.start_button.configure(state=DISABLED)

        #Mide el tiempo de respuesta al llamar a la función de la mochila
        start_time = timeit.default_timer()
        self.bagged = self.knapsack01_dp()
        elapsed = timeit.default_timer() - start_time
        
        self.label_result.config(text="\nObjeto:".join(map(str, self.bagged)))        
        for j in range(0, len(self.bagged)):
            self.message = self.bagged[j]
            print (self.bagged[j])
       
        val, wt = self.totalvalue(self.bagged)
        print("Para un valor total de %i y un peso total de %i" % (val, -wt))
        print("Duración: %f s" % (elapsed))
        self.label_final.config(text="Para un valor total de %i y un peso total de %i" % (val, -wt))
        self.label_time.config(text="Duración: %f s" % (elapsed))
        
root = Tk()
my_gui = Knapsack(root)
root.mainloop()
