# -*- coding: cp1252 -*-
import Tkinter 
import tkMessageBox
from Tkinter import *
import sys

import timeit

INF = 999999999

def main():

    def printSolution(distGraph):

        string = "inf"

        nodes =distGraph.keys()

        resultado = []
        resultado.append("        ")
        for n in nodes:

            resultado.append("        "+(n),)

        resultado.append("\n\n")

        

        for i in nodes:

            resultado.append("        "+(i),)

            for j in nodes:

                if distGraph[i][j] == INF:

                    resultado.append("        "+(string)),

                else:

                    resultado.append("        "+str((distGraph[i][j]),))

            resultado.append("\n\n")
            

        matrizResultado = " "

        for i in range(len(resultado)):
            
            matrizResultado += str(resultado[i])

        return matrizResultado            

    def floydWarshall(graph):

        nodes = graph.keys()

        distance = {}

        for n in nodes:

            distance[n] = {}

            for k in nodes:

                distance[n][k] = graph[n][k]

        for k in nodes:

            for i in nodes:

                for j in nodes:

                    if distance[i][k] + distance[k][j] < distance[i][j]:

                        distance[i][j] = distance[i][k]+distance[k][j]

        return printSolution(distance)

    if __name__ == '__main__':

        graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},

                 'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},

                 'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},

                 'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},

                 'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}

                 }

        """
                10
           (0)------->(3)
            |         /|\
          5 |          |
            |          | 1
           \|/         |
           (1)------->(2)
                3           """

        graph1 = {'A':{'A':0,'B':5,'C':INF,'D':10},

                 'B':{'A':INF,'B':0,'C':3,'D':INF},

                 'C':{'A':INF,'B':INF,'C':0,'D':1},

                 'D':{'A':INF,'B':INF,'C':INF,'D':0}

                 }


        
        """
                _(B)
                 /\ \   
                /    \
               /      \
              /        \
             /         _\/       
           (A)<---------(D)
             \           /
             _\/       \/_
              (C)---->(E)

        """
        
        graph2 = {'A':{'A':0,'B':5,'C':1,'D':INF,'E':INF},

                 'B':{'A':INF,'B':0,'C':INF,'D':3,'E':INF},

                 'C':{'A':INF,'B':INF,'C':0,'D':INF,'E':3},

                 'D':{'A':6,'B':INF,'C':INF,'D':0,'E':4},

                 'E':{'A':INF,'B':4,'C':INF,'D':0,'E':INF}

                 }
        



    def grafo1():
        start_time = timeit.default_timer()    
        
        lbresultado1 = Label(ventana, text= str("MATRIZ: ")).place(x=50,y=200)
        lbresultado1 = Label(ventana, text= floydWarshall(graph)).place(x=170,y=200)

        elapsed = timeit.default_timer() - start_time
        
        lbresultado2 = Label(ventana, text= str("DURACION: ")).place(x=50,y=480)
        lbresultado2 = Label(ventana, text= str(elapsed)).place(x=170,y=480)

        btnGrafo1.config(state = DISABLED)
        btnGrafo2.config(state = DISABLED)
        btnGrafo3.config(state = DISABLED)

    def grafo2():
        
        start_time = timeit.default_timer()    
        
        lbresultado1 = Label(ventana, text= str("MATRIZ: ")).place(x=50,y=200)
        lbresultado1 = Label(ventana, text= floydWarshall(graph1)).place(x=170,y=200)

        elapsed = timeit.default_timer() - start_time
        
        lbresultado2 = Label(ventana, text= str("DURACION: ")).place(x=50,y=480)
        lbresultado2 = Label(ventana, text= str(elapsed)).place(x=170,y=480)

        btnGrafo1.config(state = DISABLED)
        btnGrafo2.config(state = DISABLED)
        btnGrafo3.config(state = DISABLED)

    def grafo3():

        start_time = timeit.default_timer()    
        
        lbresultado1 = Label(ventana, text= str("MATRIZ: ")).place(x=50,y=200)
        lbresultado1 = Label(ventana, text= floydWarshall(graph2)).place(x=170,y=200)

        elapsed = timeit.default_timer() - start_time
        
        lbresultado2 = Label(ventana, text= str("DURACION: ")).place(x=50,y=480)
        lbresultado2 = Label(ventana, text= str(elapsed)).place(x=170,y=480)

        btnGrafo1.config(state = DISABLED)
        btnGrafo2.config(state = DISABLED)
        btnGrafo3.config(state = DISABLED)



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
    ventana.title("Algoritmo de Floyd-Warshall")
    
    ventana.geometry("700x550")
    
    centrar(ventana)

    lblInstruccion = Label(ventana, text= "  Seleccione el grafo que quiere mostrar:")
    lblInstruccion.pack()
    lblInstruccion.place(x=50,y=50)

    btnGrafo1 = Button(ventana, text = "Grafo#1", command = grafo1)
    btnGrafo1.pack()
    btnGrafo1.place(x=60, y=100)

    btnGrafo2 = Button(ventana, text = "Grafo#2", command = grafo2)
    btnGrafo2.pack()
    btnGrafo2.place(x=160, y=100)

    btnGrafo3 = Button(ventana, text = "Grafo#3", command = grafo3)
    btnGrafo3.pack()
    btnGrafo3.place(x=260, y=100)

    btnReset = Button(ventana, text = "RESET ALL", command = resetAll)
    btnReset.pack()
    btnReset.place(x=450, y=100)

    ventana.mainloop()

    
main()
