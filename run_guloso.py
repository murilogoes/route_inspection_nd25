from guloso import Grafo, Vertice
import matplotlib.pyplot as plt
import time
import dados

tempos = list()
arestas = list()

inicio = time.time()
g = Grafo()
dataset = dados.nova_luz2["arestas"]
for i in range(38):
    g.adiciona_vertice(Vertice(str(i+1)))
for i in dataset:
    g.adiciona_aresta(i[0], i[1], i[2], i[3])
g.encontra_caminho('1')
arestas.append(g.numero_arestas_total)
tempos.append(time.time() - inicio)

g1 = Grafo()
dataset2 = dados.nova_luz["arestas"]
for i2 in range(12):
    g1.adiciona_vertice(Vertice(str(i2+1)))
for i2 in dataset2:
    g1.adiciona_aresta(i2[0], i2[1], i2[2], i2[3])
g1.encontra_caminho('1')
arestas.append(g1.numero_arestas_total)
tempos.append(time.time() - inicio)

fim = time.time()

plt.xlabel('Iterações')
plt.ylabel('Time Complexity')
# plt.plot(elements, times, label='Força Bruta')
plt.plot(arestas, tempos, label='Força Bruta')
plt.grid()
plt.legend()
plt.show()
#
print('duracao: %f' % (fim - inicio))
