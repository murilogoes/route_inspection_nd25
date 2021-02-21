from grafo_lista import GrafoLista
from grafo_matriz import GrafoMatriz
from grafo2 import Grafo, Vertice


g = Grafo()
g.adiciona_vertice(Vertice('A'))
g.adiciona_vertice(Vertice('B'))
g.adiciona_vertice(Vertice('C'))
g.adiciona_vertice(Vertice('D'))
g.adiciona_vertice(Vertice('E'))

g.adiciona_aresta('A', 'D', 1)
g.adiciona_aresta('B', 'A', 5)
g.adiciona_aresta('B', 'C', 3)
g.adiciona_aresta('C', 'D', 8)
g.adiciona_aresta('D', 'B', 2)
g.adiciona_aresta('D', 'A', 3)
g.adiciona_aresta('B','E',2)
g.adiciona_aresta('E','C',4)

# g.adiciona_vertice(Vertice('A'))
# g.adiciona_vertice(Vertice('B'))
# g.adiciona_vertice(Vertice('C'))
# g.adiciona_vertice(Vertice('D'))
#
# g.adiciona_aresta('A', 'B', 3)
# g.adiciona_aresta('A', 'D', 4)
# g.adiciona_aresta('B', 'A', 1)
# g.adiciona_aresta('B', 'C', 2)
# g.adiciona_aresta('C', 'B', 2)
# g.adiciona_aresta('D', 'A', 4)
# g.adiciona_aresta('D', 'C', 2)


g.imprime_grafo()
#print("começando........ E")
g.encontra_caminho('D')



# for i in range(ord('A'), ord('K')):
#     g.adiciona_vertice(Vertice(chr(i)))
#
# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
# for edge in edges:
#     print(f'{edge[:1]}  {edge[1:]}')
#     g.adiciona_aresta(edge[:1], edge[1:], 3)


