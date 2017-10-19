from tkinter import *
import timeit
import sys


# Multiplicación de N Matrices

class MultiplicadorMatrices:
    def __init__(self, master):

        #Variables Globales
        self.matrices = []
        self.tamano = 0
        self.contador = 0
        self.multiplicacion = 0
        self.master = master
        self.split = None
        self.parentesis = ""
        master.title("Multiplicacion de Matrices")
        self.master.geometry("400x600")

        #Creacion de elementos graficos del sistema incluyendo botones, entries y labels
        self.label_total = Label(master, text="Agregar numero total de matrices")
        self.label_total.pack()
        vcmd = master.register(self.validateTamano)
        self.entry_tamano = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry_tamano.pack()
        self.button_tamano = Button(master, text="Establecer Tamaño", command=self.agregartamano)
        self.button_tamano.pack()

        self.label_inicial = Label(master, text="Agregar valor 'A' de A x B de la matriz que agregar")
        self.label_inicial.pack()
        vcmd = master.register(self.validateInicial)
        self.entry_inicial = Entry(master, validate="key", validatecommand=(vcmd, '%P'), state=DISABLED)
        self.entry_inicial.pack()
        self.button_inicial = Button(master, text="Agregar Matriz", command=self.agregarmatriz, state=DISABLED)
        self.button_inicial.pack()

        self.label_final = Label(master, text="Agregar valor 'B' de A x B de la matriz final")
        self.label_final.pack()
        vcmd = master.register(self.validateFinal)
        self.entry_final = Entry(master, validate="key", validatecommand=(vcmd, '%P'), state=DISABLED)
        self.entry_final.pack()
        self.button_final = Button(master, text="Finalizar Matriz", command=self.finmatriz, state=DISABLED)
        self.button_final.pack()

        self.button_multiplicar = Button(master, text="Realizar Multiplicación", command=self.realizarmultiplicacion, state=DISABLED)
        self.button_multiplicar.pack()
        self.button_reset = Button(master, text="Empezar de nuevo", command=self.resetall)
        self.button_reset.pack()

        self.label_matrices = Label(master, text="")
        self.label_matrices.pack()
        self.label_resultado = Label(master, text="")
        self.label_resultado.pack()
        self.label_tiempo = Label(master, text="")
        self.label_tiempo.pack()
        self.label_arreglo = Label(master, text="")
        self.label_arreglo.pack()


    #validacion de total de matrices a multiplicar
    def validateTamano(self, new_text):
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
        
    #validacion de matriz agregada
    def validateInicial(self, new_text):
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
    #validacion de valor final de una matriz
    def validateFinal(self, new_text):
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

    #Se agrega la cantidad de matrices que se van a multiplicar y se asigna este valor a tamano
    def agregartamano(self):
        self.tamano = int(self.entry_tamano.get())
        self.label_resultado.config(text= "Elementos agregados: " + str(self.matrices))
        self.entry_tamano.configure(state=DISABLED)
        self.button_tamano.configure(state=DISABLED)
        self.entry_inicial.configure(state=NORMAL)
        self.button_inicial.configure(state=NORMAL)

    #agrega los valores de tamaño de cada matriz, la variable contador toma el valor del tamano actual del arreglo con las matrices
    # si el contador llega a ser igual al tamaño especificado originalmente entonces pasa a pedir el valor final
    def agregarmatriz(self):
        self.matrices.append(int(self.entry_inicial.get()))
        self.label_resultado.config(text= "Elementos agregados: " + str(self.matrices))
        self.contador = len(self.matrices)
        self.entry_inicial.delete(0, END)
        if self.contador >= self.tamano:
            self.entry_inicial.configure(state=DISABLED)
            self.button_inicial.configure(state=DISABLED)
            self.entry_final.configure(state=NORMAL)
            self.button_final.configure(state=NORMAL)

    #agrega el ultimo valor de tamaño de la ultima matriz
    def finmatriz(self):
        self.matrices.append(int(self.entry_final.get()))
        self.label_resultado.config(text= "Elementos agregados: " + str(self.matrices))
        self.entry_final.delete(0, END)
        self.entry_final.configure(state=DISABLED)
        self.button_final.configure(state=DISABLED)
        self.button_multiplicar.configure(state=NORMAL)

    #funcion que se encarga de darle reset a toda la informacion y empezar de cero una nueva multiplicacion
    def resetall(self):
        del self.matrices [:]
        self.tamano = 0
        self.contador = 0
        self.multiplicacion = 0
        self.parentesis = ""
        self.entry_inicial.delete(0, END)
        self.entry_final.delete(0, END)
        self.entry_inicial.configure(state=DISABLED)
        self.button_inicial.configure(state=DISABLED)
        self.entry_tamano.configure(state=NORMAL)
        self.entry_tamano.delete(0, END)
        self.button_tamano.configure(state=NORMAL)
        self.entry_final.configure(state=DISABLED)
        self.button_final.configure(state=DISABLED)
        self.button_multiplicar.configure(state=DISABLED)
        self.label_matrices.config(text="")
        self.label_resultado.config(text="")
        self.label_tiempo.config(text="")
        self.label_arreglo.config(text="")

    #funcion para llamar al proceso de multiplicacion, se encarga tambien de tomar cuanto tiempo se dura ejecutando
    # y finalmente muestra los resultados
    def realizarmultiplicacion(self):
        self.label_matrices.config(text= "Resultado para valores de matrices: " + str(self.matrices))
        self.button_multiplicar.configure(state=DISABLED)
        start_time = timeit.default_timer()
        self.multiplicacion = self.multiplicacionmatrices(self.matrices, len(self.matrices), self.split)
        elapsed = timeit.default_timer() - start_time
        self.label_resultado.config(text= "Numero total de multiplicaciones: " + str(self.multiplicacion))
        self.label_tiempo.config(text="Tiempo total: " + str(elapsed)+ " s")
        if self.multiplicacion < sys.maxsize:
            self.label_arreglo.config(text="Forma de multiplicar: " + self.parentesis)
        else:
            self.label_arreglo.config(text="Forma de multiplicar: No Disponible")

    #Funcion para imprimir los parentesis, los quiebres son guardados en la funcion de multiplicar matrices
    # a partir de esto genera como se multiplicaron las matrices para obtener el resultado minimo
    def imprimirparentesis(self, i, j, n, s, name, l):
        if i==j:
            l.append(str(name))
            name += 1 
            return
        l.append("(")
        self.imprimirparentesis(i,s[i][j],n,s,name, l)
        self.imprimirparentesis((s[i][j]+1), j,n, s, name, l)
        l.append(")")


    """
    Se recibe un arreglo p y un valor n
    El valor n es la longitud de p
    p contiene las matrices escritas de un formato donde la primer matriz
    es de tamaño p[0] X p [1] y luego la siguiente seria p[1] X p[2]
    y así sucesivamente hasta llegar al final del arreglo
    y tener la ultima matriz representada en p[n-2] X p[n-1]
    """
    def multiplicacionmatrices(self, p, n, s):
        # matriz donde se guardaran los resultados preliminares y resultado final
        # la fila y columna 0 no se utilizan
        m = [[0 for x in range(n)] for x in range(n)]
        s = [[0 for x in range(n)] for x in range(n)]
        # para cada ciclo en la posicion m[i][j] se guardara la cantidad minima de multiplicaciones que se pueden realizar
        # para completar la multiplicacion de matrices entre A[i] y A[j] y donde las Dimensiones de A[i] son "a x b"
        # donde "a" es el valor de p[i-1] y "b" es p[i]

        # se pone la diagonal de la matriz en 0 ya que el valor de multiplicar solo una matriz es 0
        for i in range(1, n):
            m[i][i] = 0

        # L es la cadena, inicia en 2 ya que se viendo la multiplicacion de dos matrices, luego va aumentando para ver la combinacion
        # de la multiplicacion de 3, 4, etc. hasta llegar a n
        for L in range(2, n):
            for i in range(1, n-L+1):
                j = i+L-1
                #se asigna el valor maximo posible en la casilla asi asegurar que la comparacion inicial sea menor a este numero
                m[i][j] = sys.maxsize
                for k in range(i, j):
                    #se asigna en q el total de multiplicaciones para esta combinacion
                    q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                    #si q es menor al valor en m[i][j] se guarda q en este puesto ya que es por el momento el numero menor de multiplicaciones para ese tamaño de la cadena
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k
                        
        #regresa el valor en m[1][n-1] que contiene el resultado final
        l = []
        print("i: "+ str(i) + "n-1: " + str(n-1) + "= " + str(s[i][n-1]))
        if m[1][n-1] < sys.maxsize:
            self.imprimirparentesis(1, (n-1), n, s, 1, l)
            self.parentesis = "".join(l)
            print(self.parentesis)
        return m[1][n-1]

    
                
        
        
        
            
        

        
root = Tk()
my_gui = MultiplicadorMatrices(root)
root.mainloop()











