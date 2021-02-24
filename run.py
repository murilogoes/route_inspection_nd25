from grafo4 import Grafo, Vertice

import time
import dados

g = Grafo()

#numero_grafo = int(input('Digite o número do grafo:'))
numero_grafo = 3

for i in dados.data[numero_grafo]["vertices"]:
    #print(i)
    g.adiciona_vertice(Vertice(i))

for i in dados.data[numero_grafo]["arestas"]:
    g.adiciona_aresta(i[0], i[1], i[2], i[3])

#g.imprime_grafo()

inicio = time.time()
#g.encontra_caminho(input('digite o ponto de partida: ').upper())
g.encontra_caminho('D')
fim = time.time()
#
print('duracao: %f' % (fim - inicio))
