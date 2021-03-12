from grafo4 import Grafo, Vertice
import sys
import time
import dados


#print(sys.getrecursionlimit())
sys.setrecursionlimit(15000)

g = Grafo()

#
# dataset = dados.data[1]["arestas"]
# tamanho = dados.data[1]["vertices"]
# for i in tamanho:
#     g.adiciona_vertice(Vertice(i))
#
# for i in dataset:
#     g.adiciona_aresta(i[0], i[1], i[2], i[3])

dataset = dados.nova_luz["arestas"]
for i in range(38):
    g.adiciona_vertice(Vertice(str(i+1)))
for i in dataset:
    g.adiciona_aresta(i[0], i[1], i[2], i[3])


#numero_grafo = int(input('Digite o número do grafo:'))
# numero_grafo = 2
#
# for i in dados.data[numero_grafo]["vertices"]:
#     #print(i)
#     g.adiciona_vertice(Vertice(i))
#
# for i in dados.data[numero_grafo]["arestas"]:
#     g.adiciona_aresta(i[0], i[1], i[2], i[3])
#

#g.imprime_grafo()
#
inicio = time.time()
# #g.encontra_caminho(input('digite o ponto de partida: ').upper())
g.encontra_caminho('1')


fim = time.time()
#
print('duracao: %f' % (fim - inicio))
