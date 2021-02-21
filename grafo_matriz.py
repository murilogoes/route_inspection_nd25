class GrafoMatriz:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        # estou pensando em grafos direcionados simples
        self.grafo[u-1][v-1] = peso  #trocar = por += se for grafo múltiplo

       # self.grafo[v-1][u-1] = peso (caso o grafo não seja direcionado)

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


