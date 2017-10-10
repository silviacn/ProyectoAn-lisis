import random
from tkinter import *
import timeit

class Knapsack:    
    def __init__(self, master):
        try:
            self.xrange
        except:
            self.xrange = range
        self.lista = (
            ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
            ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
            ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
            ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
            ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
            ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
            ("socks", 4, 50), ("book", 30, 10),
            )
        self.items  = []
        self.bagged = []
        self.master = master
        master.title("Problema de la mochila")
        self.master.geometry("500x500")

        self.secret_number = random.randint(1, 100)
        self.max = None
        self.name = None
        self.benefit = None
        self.weight = None
        self.num_guesses = 0

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
        
        vcmd = master.register(self.validateBenefit) # we have to wrap the command
        self.entry_benefit = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.message = "Elija el peso del objeto: "
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label_weight = Label(master, textvariable=self.label_text)
        
        vcmd = master.register(self.validateWeight) # we have to wrap the command
        self.entry_weight = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.create_button = Button(master, text="Crear objeto", command=self.createlist)
        self.start_button = Button(master, text="Resolver mochila", command=self.results, state=DISABLED)
        self.new_button = Button(master, text="Nueva mochila", command=self.resetnew)
    
        self.label_result = Label(master, text="RESULTADO...")
        self.label_final = Label(master, text="")
        self.label_time = Label(master, text="")
        
        self.label_max.grid(row=0, column=5, columnspan=2, sticky=W+E)
        self.entry_max.grid(row=1, column=5, columnspan=2, sticky=W+E)        
        self.label_name.grid(row=3, column=5, columnspan=2, sticky=W+E)
        self.entry_name.grid(row=4, column=5, columnspan=2, sticky=W+E)
        self.label_benefit.grid(row=6, column=5, columnspan=2, sticky=W+E)
        self.entry_benefit.grid(row=7, column=5, columnspan=2, sticky=W+E)
        self.label_weight.grid(row=9, column=5, columnspan=2, sticky=W+E)
        self.entry_weight.grid(row=10, column=5, columnspan=2, sticky=W+E)
        self.create_button.grid(row=14, column=5)
        self.start_button.grid(row=14, column=7)
        self.new_button.grid(row=14, column=8)
        self.label_result.grid(row=16, column=5)
        self.label_final.grid(row=19, column=5)
        self.label_time.grid(row=20, column=5)
        
    def validateMax(self, new_text):
        if not new_text: # the field is being cleared
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
        
    def validateBenefit(self, new_text):
        if not new_text: # the field is being cleared
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

    def validateWeight(self, new_text):
        if not new_text: # the field is being cleared
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
        
    def createlist(self):
        self.name = self.entry_name.get()
        self.items.append((self.name, self.benefit, self.weight))        
        self.reset()

    def totalvalue(self, comb):
        ' Totalise a particular combination of items'
        totwt = totval = 0
        for item, wt, val in comb:
            totwt  += wt
            totval += val
        return (totval, -totwt) if totwt <= 400 else (0, 0)
     
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
        result = []
        w = self.max
        for j in range(len(self.items), 0, -1):
            was_added = table[j][w] != table[j-1][w]
     
            if was_added:
                item, wt, val = self.items[j-1]
                result.append(self.items[j-1])
                w -= wt            
        return result

    def results(self):
        self.create_button.configure(state=DISABLED)
        self.start_button.configure(state=DISABLED)
        
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
