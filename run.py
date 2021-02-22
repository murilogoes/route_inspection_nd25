from grafo_lista import GrafoLista
from grafo_matriz import GrafoMatriz
from grafo2 import Grafo, Vertice


g = Grafo()

# grafo 100% direcionado
# g.adiciona_vertice(Vertice('A'))
# g.adiciona_vertice(Vertice('B'))
# g.adiciona_vertice(Vertice('C'))
# g.adiciona_vertice(Vertice('D'))
# g.adiciona_vertice(Vertice('E'))
#
# g.adiciona_aresta('A', 'D', 1, True)
# g.adiciona_aresta('B', 'A', 5, True)
# g.adiciona_aresta('B', 'C', 3, True)
# g.adiciona_aresta('C', 'D', 8, True)
# g.adiciona_aresta('D', 'B', 2, True)
# g.adiciona_aresta('D', 'A', 3, True)
# g.adiciona_aresta('B','E',2, True)
# g.adiciona_aresta('E','C',4, True)


#grafo misto
g.adiciona_vertice(Vertice('A'))
g.adiciona_vertice(Vertice('B'))
g.adiciona_vertice(Vertice('C'))
g.adiciona_vertice(Vertice('D'))

g.adiciona_aresta('A', 'B', 3, True)
g.adiciona_aresta('A', 'D', 4, False)
g.adiciona_aresta('B', 'A', 1, True)
g.adiciona_aresta('B', 'C', 2, False)
g.adiciona_aresta('D', 'C', 2, True)

#grafo misto 2
# g.adiciona_vertice(Vertice('A'))
# g.adiciona_vertice(Vertice('B'))
# g.adiciona_vertice(Vertice('C'))
# g.adiciona_vertice(Vertice('D'))
# g.adiciona_vertice(Vertice('E'))
# g.adiciona_vertice(Vertice('F'))
# g.adiciona_vertice(Vertice('G'))
# #
# g.adiciona_aresta('A', 'C', 7, True)
# g.adiciona_aresta('B', 'A', 6, True)
# g.adiciona_aresta('B', 'G', 5, False)
# g.adiciona_aresta('C', 'B', 6, False)
# g.adiciona_aresta('C', 'D', 5, False)
# g.adiciona_aresta('D', 'E', 5, True)
# g.adiciona_aresta('E', 'B', 4, True)
# g.adiciona_aresta('E', 'F', 5, False)
# g.adiciona_aresta('F', 'G', 20, False)

#g.imprime_grafo()
#print("começando........ E")
g.encontra_caminho('A')


# for i in range(ord('A'), ord('K')):
#     g.adiciona_vertice(Vertice(chr(i)))
#
# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
# for edge in edges:
#     print(f'{edge[:1]}  {edge[1:]}')
#     g.adiciona_aresta(edge[:1], edge[1:], 3)


