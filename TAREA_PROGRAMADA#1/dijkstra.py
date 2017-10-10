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



def main():
    
    start_time = timeit.default_timer()
    p =  dijkstra(grafo, e1.get(), e2.get())
    lbresultado = Label(master, text= str("LA RUTA MAS CORTA ES: ")).place(x=250,y=2)
    lbresultado = Label(master, text= str(p)).place(x=390,y=2)

    elapsed = timeit.default_timer() - start_time
    
    #print(elapsed)
    lbresultado = Label(master, text= str("DURACION: ")).place(x=250,y=30)
    lbresultado = Label(master, text= str(elapsed)).place(x=390,y=30)
    


master = Tk()
master.geometry("600x300")

Label(master, text="inicio").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)


Label(master, text="llegada").grid(row=1)

e2 = Entry(master)

e2.grid(row=1, column=1)


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)

Button(master, text='Show', command=main).grid(row=3, column=1, sticky=W, pady=4)

mainloop()


#def main():
    
#    p =  dijkstra(grafo, 'c', 'd')
#    print (' nodos con distancia mas corta hasta dicho punto: ', p)
    
#if __name__ == '__main__':
#    main()
