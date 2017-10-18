"""

Problema a resolver : Ordenar una lista de N elementos con los algortimos de ordenamiento QuickSort y HeapSort,
                      y calcular los tiempos de ejecución con cada uno de ellos.


Descripción: El siguiente programa ordena una lista del tamaño que indique el usuario
             y calcula su tiempo de ejecución con una interfaz gráfica intuitiva.


"""



contador = 1

from tkinter import *

import sys

from tkinter import messagebox

import timeit


def main():
    
    #Valida si el tamaño de la lista es correcto
    def ingresarLista():

        if (txtCantidad.get() == "") or (txtCantidad.get().isalpha()) or (int(txtCantidad.get())<0):
            messagebox.showwarning('Atención', 'Debe ingresar un número entero positivo.')
        else:            
            global contador
            etiqueta2 = Label(ventana, text= "Ingrese el valor #"+str(contador)).place(x=20,y=170)
            txtElemento.pack(fill = X, padx=30, pady=70, ipadx=5, ipady=5)
            btnIngresar.place(x=60, y=250)
            btnResultado1.pack()
            btnResultado1.place(x=250, y=250)
            btnResultado2.pack()
            btnResultado2.place(x=450, y=250)
            btnAceptar.config(state = DISABLED)
            btnResultado1.config(state = DISABLED)
            btnResultado2.config(state = DISABLED)
            txtCantidad.config(state = DISABLED)
        
    #Ingresa cada elemento a la lista        
    def ingresarElemento():

        if (txtElemento.get() == "") or (txtElemento.get().isalpha()):
            messagebox.showwarning('Atención', 'Debe ingresar un número entero positivo.')
        else:

            cantidadElementos = int(txtCantidad.get())

            listaElementos1.append(int(txtElemento.get()))

            listaElementos2.append(int(txtElemento.get()))

            btnResultado1.config(state = NORMAL)

            btnResultado2.config(state = NORMAL)            

            txtElemento.delete(0, END)
            
            if (contador == int(txtCantidad.get())):
                btnIngresar.config(state = DISABLED)
                txtElemento.config(state = DISABLED)
            contar()

    #Aumenta el contador global            
    def contar():
        global contador
        contador += 1
        print(str(contador))
        
        
    def darResultadoQuickSort():
        lblResultado1 = Label(ventana, text= 'Resultado Quicksort: ').place(x=20,y=340)
        
        start_time = timeit.default_timer()
        
        lblArregloOrdenado1 = Label(ventana, text= str(quicksort(listaElementos1))).place(x=20,y=400)

        elapsed = timeit.default_timer() - start_time
        
        lblResultado1 = Label(ventana, text= 'Duración: ' + str(elapsed)).place(x=20,y=370)
        

    def darResultadoHeapSort():
        lblResultado2 = Label(ventana, text= 'Resultado Heapsort: ').place(x=20,y=470)
        
        start_time = timeit.default_timer()
        
        lblArregloOrdenado2 = Label(ventana, text= str(heapsort(listaElementos2))).place(x=20,y=530)

        elapsed = timeit.default_timer() - start_time

        lblResultado2 = Label(ventana, text= 'Duración: ' + str(elapsed)).place(x=20,y=500)

        
    #QUICKSORT        
    def quicksort(arr):
        high = []
        low = []
        pivot_list = []

        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            for i in arr:
                if i < pivot:
                    low.append(i)
                elif i > pivot:
                    high.append(i)
                else:
                    pivot_list.append(i)
            high = quicksort(high)
            low = quicksort(low)

        return low + pivot_list + high

    #HEAPSORT
    def heapsort(A):
        def heapify(A):
            start = (len(A) - 2) / 2
            while start >= 0:
                siftDown(A, start, len(A) - 1)
                start -= 1

        def siftDown(A, start, end):
            root = int(start)
            while root * 2 + 1 <= end:
                child = root * 2 + 1
                if child + 1 <= end and A[child] < A[child + 1]:
                    child += 1
                if child <= end and A[root] < A[child]:
                    A[root], A[child] = A[child], A[root]
                    root = child
                else:
                    return

        heapify(A)
        end = len(A) - 1
        while end > 0:
            A[end], A[0] = A[0], A[end]
            siftDown(A, 0, end - 1)
            end -= 1

        return A

    #Reinicia la aplicación
    def resetAll():
        ventana.destroy()
        main()
        global contador
        contador = 1
        
    #Centra la pantalla
    def centrar(ventana):
        ventana.update_idletasks()
        w=ventana.winfo_width()
        h=ventana.winfo_height()
        extraW=ventana.winfo_screenwidth()-w
        extraH=ventana.winfo_screenheight()-h
        ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))

    
    #Comienza a ingresar los elementos de la lista
    def start():
        ingresarElemento();


    #Creación de la interfaz 
    listaElementos1 = []
    listaElementos2 = []
    ventana = Tk()
    ventana.title("Algortimo QuickSort Y HeapSort")
    ventana.geometry("600x600")
    centrar(ventana)
    
    cantidadElementos = 0

    lblInstruccion = Label(ventana, text= "  Digite la cantidad de elementos a ordenar:")
    lblInstruccion.pack()
    lblInstruccion.place(x=20,y=10)
    btnIngresar = Button(ventana, text = "Ingresar", command = start)
    btnIngresar.pack()
    btnIngresar.place(x=60, y=49)

    txtElemento = Entry(ventana)
    txtCantidad = Entry(ventana)
    txtCantidad.pack(fill = X, padx=30, pady=50, ipadx=5, ipady=5)
    
    btnAceptar = Button(ventana, text = "Aceptar", command = ingresarLista)
    btnAceptar.pack()
    btnAceptar.place(x=60, y=100)

    btnReset = Button(ventana, text = "RESET ALL", command = resetAll)
    btnReset.pack()
    btnReset.place(x=450, y=100)

    btnResultado1 = Button(ventana, text = "R/ QuickSort", command = darResultadoQuickSort)
    btnResultado2 = Button(ventana, text = "R/ HeapSort", command = darResultadoHeapSort)

    ventana.mainloop()
    
main()
