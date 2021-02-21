# implementation of an undirected graph using Adjacency Lists
class Vertice:
    def __init__(self, n):
        self.nome = n
        self.partida = False
        self.ultimovisitado = False
        self.visitado = False
        self.vizinhos = list()

    def adiciona_vizinho(self, v, peso):
        if v not in self.vizinhos:
            #self.vizinhos.append((Aresta(v, peso)))
            self.vizinhos.append((v, peso))
            self.vizinhos.sort()

class Aresta:
    def __init__(self, v, p):
        self.vertice = v
        self.peso = p
        self.visitado = False

class Grafo:
    vertices = {}

    def adiciona_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True
        else:
            return False

    def adiciona_aresta(self, u, v, peso):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].adiciona_vizinho(v, peso)
            # self.vertices[v].adiciona_vizinho(u, peso)
            return True
        else:
            return False

    def imprime_grafo(self):
        # for dd in self.vertices.values():
        #     print(dd.vizinhos)
        #     for j in dd.vizinhos:
        #         print(j.peso)
        for key in sorted(list(self.vertices.keys())):
           print(key + str(self.vertices[key].vizinhos))

    def vertice_ultimo_visitado(self, v):
        return self.vertices[v].ultimovisitado

    def vertice_visitado(self, v):
        return self.vertices[v].visitado

    def vertice_partida(self, v):
        return self.vertices[v].partida

    def encontra_caminho(self, v):
        self.vertices[v].partida = True
        self.vertices[v].visitado = True
        # self.percorre_grafo(v)
        self.percorre_grafov2(v)

    def avanca_proximo(self, v, i):
        self.vertices[i[0]].visitado = True
        #print(self.vertices[i[0][1]])
        self.marca_ultimo(v)
        self.percorre_grafov2(self.vertices[i[0]].nome)
        # self.percorre_grafo(self.vertices[i[0]].nome)

    def marca_ultimo(self, v):
        for i in self.vertices:
            self.vertices[i].ultimovisitado = False
        self.vertices[v].ultimovisitado = True

    def tudo_visitado(self):
        for i in self.vertices:
            if not self.vertices[i].visitado:
                return False
        return True

    def terminou(self, v):
        return (self.tudo_visitado() and self.vertices[v].partida)

    def percorre_grafov2(self, v):

        def menor_aresta(lista_aresta):
            menor = lista_aresta[0]
            for n in range(len(lista_aresta)):
                if lista_aresta[n][1] < menor[1]:
                    menor = lista_aresta[n]
            return menor

        def maior_aresta(lista_aresta):
            maior = lista_aresta[0]
            for n in range(len(lista_aresta)):
                if lista_aresta[n][1] > maior[1]:
                    maior = lista_aresta[n]
            return maior

        if not self.terminou(v):
            print(f'Estou no vertice {v}')
            for i in self.vertices[v].vizinhos:
                print(i)
                print(f'{v} -> {i[0]}')
                if len(self.vertices[v].vizinhos) <= 1:
                    print(i)
                    self.avanca_proximo(v, i)
                    break
                else:
                    qtd_vizinhos = len(self.vertices[v].vizinhos)
                    nao_visitados = []
                    visitados = []
                    for n in range(qtd_vizinhos):
                        #print(f'{self.vertices[v].vizinhos[n][0]} visitado? {self.vertice_visitado(self.vertices[v].vizinhos[n][0])}')
                        if not self.vertice_visitado(self.vertices[v].vizinhos[n][0]):
                            nao_visitados.append(self.vertices[v].vizinhos[n])
                        else:
                            if not self.vertice_ultimo_visitado(self.vertices[v].vizinhos[n][0]):
                                visitados.append(self.vertices[v].vizinhos[n])
                    #print(f'nao visitados {len(nao_visitados)}')
                    if len(nao_visitados) >= 1:
                        self.avanca_proximo(v, menor_aresta(nao_visitados))
                        break
                    else:
                        self.avanca_proximo(v, maior_aresta(visitados))
                        break
        else:
            print("fim de jogo")
            return True

    # def percorre_grafo(self, v):
    #     # print(self.terminou(v))
    #     if not self.terminou(v):
    #         print(f'Estou no vertice {v}')
    #         # self.vertices[v].ultimovisitado = False
    #         for i in self.vertices[v].vizinhos:
    #             print(i)
    #             print(f'{v} -> {i[0]}')
    #             if self.vertice_visitado(i[0]):
    #                 print(f'{i[0]} ja foi visitado')
    #                 if len(self.vertices[v].vizinhos) == 1:
    #                     self.avanca_proximo(v, i)
    #                     break
    #                 else:
    #                     if self.tudo_visitado():
    #                         self.avanca_proximo(v, i)
    #                         break
    #                     else:
    #                         if not self.vertices[i[0]].ultimovisitado:
    #                             print("nao foi ultimo a ser visitado")
    #                             self.avanca_proximo(v, i)
    #                         else:
    #                             continue
    #             else:
    #                 self.avanca_proximo(v, i)
    #                 break
    #             # if not self.vertices[i[0]].ultimovisitado:
    #             #     print("nao foi ultimo a ser visitado")
    #             #     self.avanca_proximo(v,i)
    #     else:
    #         print("cabo porra")
    #         return True
