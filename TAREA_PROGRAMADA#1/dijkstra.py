from tkinter import *
import timeit

def dijkstra(grafo, a, z):
    
    #Determina cual es el camino mas cortoentre 'a' y 'z' los cuales a,z son llamados nodos,
    # Grafo = quien contiene por asi decir los caminos.
    
    inf = 0#Infinito
    for letra in grafo:
        for v,w in grafo[letra]:
            inf += w
            
    # Inicializacion de estructuras auxiliares:
    #  L: diccionario vertice -> etiqueta
    #  S: conjunto de vertices con etiquetas temporales
    #  A: vertice -> vertice previo (en camino longitud minima)
    
    L = dict([(letra, inf) for letra in grafo]) #crear un grafo {}
    L[a] = 0
    S = set([letra for letra in grafo]) #crear un grafo {}
    A = {}
    
    # Funcion auxiliar, dado un vertice retorna su etiqueta
    # se utiliza para encontrar el vertice the etiqueta minima
    
    def regresar_minimo(v):
        
        return L[v]
    
    # Iteracion principal del algoritmo de Dijkstra
    while z in S:
        letra = min(S, key=regresar_minimo)#min es el minimo
        S.discard(letra)
        for v, w in grafo[letra]:
            if v in S:
                if L[letra] + w < L[v]:
                    L[v] = L[letra] + w
                    A[v] = letra
                    
    # Reconstruccion del camino de longitud minima
    P = []
    u = z
    while letra != a:
        P.append(letra)
        #print(P)
        letra = A[letra]
        #print(letra)
    P.append(e1.get())
    P.reverse()

    return P
                    
#recorda simpre ir de izquierda a derecha
grafo = {'a' : [('e',14),('c',9),('b',7)],
         'b':[('c',10),('d',15)],
         'c':[('e',2),('d',11)],
         'd':[('f',6)],
         'e':[('f',9),('g',9)],
         'f':[('c',3)],
         'g':[('e',1)],}


grafo2 = {'a':[('c',5),('b',3),('d',2),('h',10)],
         'b':[('a',3),('c',5),('d',8),('e',6),('g',6),('h',6)],
         'c':[('a',5),('b',5),('e',1),('f',7),('g',9)],
         'd':[('a',2),('b',6),('e',12),('h',14)],
         'e':[('c',1),('b',4),('d',12),('g',15)],
         'f':[('c',7),('h',9)],
         'g':[('b',4),('c',9),('e',15),('h',3)],
         'h':[('a',10),('b',6),('d',14),('f',9),('g',3)]}

G = {'s':{('u',10), ('x',5)},
     'u':{('v',1), ('x',2)},
     'v':{('y',4)},
     'x':{('u',3),('v',9),('y',2)},
     'y':{('s',7),('v',6)}}


def main():
    
    start_time = timeit.default_timer()
    p =  dijkstra(grafo, e1.get(), e2.get())
    lbresultado = Label(master, text= str("LA RUTA MAS CORTA ES: ")).place(x=250,y=2)
    lbresultado = Label(master, text= str(p)).place(x=390,y=2)

    elapsed = timeit.default_timer() - start_time
    
    #print(elapsed)
    lbresultado = Label(master, text= str("DURACION: ")).place(x=250,y=30)
    lbresultado = Label(master, text= str(elapsed)).place(x=390,y=30)


def main2():
    start_time = timeit.default_timer()
    p = dijkstra(grafo2, e1.get(), e2.get())
    lbresultado = Label(master, text=str("LA RUTA MAS CORTA ES: ")).place(x=250, y=2)
    lbresultado = Label(master, text=str(p)).place(x=390, y=2)

    elapsed = timeit.default_timer() - start_time

    # print(elapsed)
    lbresultado = Label(master, text=str("DURACION: ")).place(x=250, y=30)
    lbresultado = Label(master, text=str(elapsed)).place(x=390, y=30)

def main2():
    start_time = timeit.default_timer()
    p = dijkstra(G, e1.get(), e2.get())
    lbresultado = Label(master, text=str("LA RUTA MAS CORTA ES: ")).place(x=250, y=2)
    lbresultado = Label(master, text=str(p)).place(x=390, y=2)

    elapsed = timeit.default_timer() - start_time

    # print(elapsed)
    lbresultado = Label(master, text=str("DURACION: ")).place(x=250, y=30)
    lbresultado = Label(master, text=str(elapsed)).place(x=390, y=30)


master = Tk()
master.geometry("600x300")

Label(master, text="inicio").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)


Label(master, text="llegada").grid(row=1)

e2 = Entry(master)

e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)

Button(master, text='GRAPHO #1', command=main).grid(row=3, column=1, sticky=W, pady=4)

Button(master, text='GRAPHO #2', command=main2).grid(row=3, column=2, sticky=W, pady=4)

Button(master, text='GRAPHO #3', command=main2).grid(row=3, column=4, sticky=W, pady=4)

mainloop()

