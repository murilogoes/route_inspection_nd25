from grafo4 import Grafo, Vertice
import sys
import time
import dados


#print(sys.getrecursionlimit())
#sys.setrecursionlimit(15000)

g = Grafo()

for i in range(13):
    # print(str(i+1))
    g.adiciona_vertice(Vertice(str(i+1)))

for i in dados.nova_luz["arestas"]:
    g.adiciona_aresta(i[0], i[1], i[2], i[3])

#numero_grafo = int(input('Digite o número do grafo:'))
numero_grafo = 3

# for i in dados.data[numero_grafo]["vertices"]:
#     #print(i)
#     g.adiciona_vertice(Vertice(i))
#
# for i in dados.data[numero_grafo]["arestas"]:
#     g.adiciona_aresta(i[0], i[1], i[2], i[3])
#
#g.imprime_grafo()
#
# inicio = time.time()
# #g.encontra_caminho(input('digite o ponto de partida: ').upper())
g.encontra_caminho('1')


# fim = time.time()
# #
# print('duracao: %f' % (fim - inicio))
