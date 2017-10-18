"""
PROBLEMA A RESOLVER : Calcular el vuelto con monedas y su tiempo de ejecución.

Descripción: El siguiente programa calcula el vuelto con monedas según
             el monto que ingrese el usuario, haciendo un desgloce de
             la cantidad de cada tipo de moneda.


"""


from tkinter import *

import sys

from tkinter import messagebox

import timeit


def main():

    #Valida que sea un monto válido
    def validarMonto():
        if (txtCantidad.get() == "") or (txtCantidad.get().isalpha()) or (int(txtCantidad.get())<0):
            messagebox.showwarning('Atención', 'Debe ingresar un número entero positivo.')
        else:
            mostrarResultado()
            
    #Imprime en pantalla el vuelto y el tiempo de ejecución
    def mostrarResultado():
        lblResultado = Label(ventana, text= 'El vuelto es: ').place(x=20,y=160)
        
        start_time = timeit.default_timer()
        
        Resultado = Label(ventana, text= str(calcularVuelto())).place(x=120,y=140)

        elapsed = timeit.default_timer() - start_time
        
        lblResultado = Label(ventana, text= 'Duración: ' + str(elapsed)).place(x=20,y=330)

    #Calcula la cantidad de monedas según su valor
    def calcularVuelto():
        importe = int(txtCantidad.get())
        resultados = []
         
        # importes de los billetes y monedas con su tipo en singular
        tipos = (
            (500,"moneda"),
            (100,"moneda"),
            (50,"moneda"),
            (25,"moneda"),
            (20,"moneda"),
            (10,"moneda"),
            (5,"moneda")
        )
         
        for tipo in tipos:
            valor=tipo[0]
            descripcion=tipo[1]
            # funcion para mostrar la s del plural si es necesario
            s=lambda valor,text: valor > 1 and text+"s" or text

            if importe/valor>0:
                resultados.append(str("%d %s de %d" % ((importe / valor), s((importe / valor),descripcion), valor)))
                # cogemos el resto de la division
                importe = importe % valor

        resul = ""                
        for i in resultados:
            resul = resul + "\n" +  i

        return resul
                
    #Centra la pantalla
    def centrar(ventana):
        ventana.update_idletasks()
        w=ventana.winfo_width()
        h=ventana.winfo_height()
        extraW=ventana.winfo_screenwidth()-w
        extraH=ventana.winfo_screenheight()-h
        ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))

    #Reinicia la aplicación
    def resetAll():
        ventana.destroy()
        main()

    ventana = Tk()
    ventana.title("Vuelto Con Monedas")
    ventana.geometry("600x400")
    centrar(ventana)

    lblInstruccion = Label(ventana, text= "  Digite el monto a calcular:")
    lblInstruccion.pack()
    lblInstruccion.place(x=20,y=10)    

    txtElemento = Entry(ventana)
    txtCantidad = Entry(ventana)
    txtCantidad.pack(fill = X, padx=30, pady=50, ipadx=5, ipady=5)

    btnAceptar = Button(ventana, text = "Aceptar", command = validarMonto)
    btnAceptar.pack()
    btnAceptar.place(x=60, y=100)

    btnReset = Button(ventana, text = "RESET ALL", command = resetAll)
    btnReset.pack()
    btnReset.place(x=450, y=100)

    
main()
