from grafo_lista import GrafoLista
from grafo_matriz import GrafoMatriz

print("Lista de Adjacencia")

g = GrafoLista(4)

#adiciona_aresta(vertice a, que vai ao b, e o peso)
g.adiciona_aresta(1, 4, 1)
g.adiciona_aresta(2, 1, 5)
g.adiciona_aresta(2, 3, 3)
g.adiciona_aresta(3, 4, 8)
g.adiciona_aresta(4, 1, 3)
g.adiciona_aresta(4, 2, 2)

g.mostra_lista()

print("Matriz de Adjacencia")
g = GrafoMatriz(4)

#adiciona_aresta(vertice a, que vai ao b, e o peso)
g.adiciona_aresta(1, 4, 1)
g.adiciona_aresta(2, 1, 5)
g.adiciona_aresta(2, 3, 3)
g.adiciona_aresta(3, 4, 8)
g.adiciona_aresta(4, 1, 3)
g.adiciona_aresta(4, 2, 2)

g.mostra_matriz()