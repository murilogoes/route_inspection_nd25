import secrets
# a implementacao desse grafo se dará por lista de adjacencias
# TESTANDO COM FORÇA BRUTA

class Vertice:
    def __init__(self, n):
        self.nome = n
        self.partida = False
        self.vizinhos = list()

    def adiciona_vizinho(self, v, peso, direcionado):
        if v not in self.vizinhos:
            self.vizinhos.append((Aresta(v, peso, direcionado, secrets.token_hex(nbytes=16))))

class Aresta:
    def __init__(self, v, p, direcionado, hash):
        self.destino = v
        self.peso = p
        self.direcionado = direcionado
        self.visitado = False
        self.quantidade_visitas = 0
        self.hash = hash
        #considerar colocar a origem tambem

class Caminho:
    def __init__(self, percurso):
        self.arestas_hashes = list()
        self.arestas_percorridas = list()
        self.percurso = percurso
        self.custo = 0


class Grafo:
    vertices = {}
    caminhos = list()
    caminhosPossiveis = 0
    caminho = ""
    custo = 0
    arestas_hashes = list()

    # adiciona os vertices ao grafo (A,B,C,D....)
    def adiciona_vertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
            self.vertices[vertice.nome] = vertice
            return True
        else:
            return False

    # adiciona arestas aos vertices
    def adiciona_aresta(self, u, v, peso, direcionado):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].adiciona_vizinho(v, peso, direcionado)
            # se ele nao for direcionado, vai adicionar no outro sentido
            if not direcionado:
                self.vertices[v].adiciona_vizinho(u, peso, direcionado)
            return True
        else:
            return False

    def gera_lista_hashes(self):
        for dd in self.vertices.values():
            for j in dd.vizinhos:
                self.arestas_hashes.append(j.hash)


    #imprime o grafo como lista de adjacencias
    def imprime_grafo(self):
        for dd in self.vertices.values():
            lista = dd.nome + ":"
            for j in dd.vizinhos:
                lista = f'{lista} -> {j.destino} ({j.peso})({j.direcionado})'
            print(lista)

    # retorna qual vertice iniciou o percurso
    def vertice_partida(self, v):
        return self.vertices[v].partida

    # metodo para anotar que determinada aresta ja foi visitada
    def marca_aresta_visitada(self, v, d):
        for i in self.vertices[v].vizinhos:
            if i.destino == d:
                i.quantidade_visitas += 1
                i.visitado = True


    # metodo para me dizer se a aresta ja foi visitada
    def aresta_visitada(self, v, d):
        #print(f'{v}, {d}')
        for i in self.vertices[v].vizinhos:
            if i.destino == d:
                return i.visitado
                break

    def get_aresta(self, v, d):
        #print(f'{v}, {d}')
        for i in self.vertices[v].vizinhos:
            if i.destino == d:
                return i

    # metodo para me dizer se todas as arestas ja foram visitadas
    # aqui, quando uma aresta nao direcionada nao foi percorrida em determinado sentido, eu verifico se ja foi no outro sentido, ai marca como visitada
    # def todas_arestas_visitadas(self):
    #     #iterando todos os vertices
    #     for dd in self.vertices.values():
    #         #print(dd.vizinhos)
    #         #checando cada aresta de um vertice
    #         for j in dd.vizinhos:
    #             #print(j.visitado)
    #             # se a aresta nao foi ainda visitada
    #             if not j.visitado:
    #                 #print("aresta nao foi visitada")
    #                 # se a aresta for direcionada ....
    #                 if j.direcionado:
    #                     # retorna falso para visitar
    #                     return False
    #                     break
    #                 # se a aresta nao for direcionada...
    #                 else:
    #                     # e se o outro lado ainda nao foi visitado...
    #                     if not self.aresta_visitada(j.destino, dd.nome):
    #                         #print ("nao visitou nenhum dos lados")
    #                         # retorna falso para visitar
    #                         return False
    #                         break
    #     return True

    # #se todas as arestas foram visitadas e eu estou no ponto de partida...
    # def terminou(self, v):
    #     return (self.todas_arestas_visitadas() and self.vertices[v].partida)

    # metodo para me dizer se todas as arestas ja foram visitadas
    # aqui, quando uma aresta nao direcionada nao foi percorrida em determinado sentido, eu verifico se ja foi no outro sentido, ai marca como visitada
    def todas_arestas_visitadas(self, arestas_percorridas):
        hashes_percorridos = list()
        for i in arestas_percorridas:
            hashes_percorridos.append(i.hash)
        return set(self.arestas_hashes) == set(hashes_percorridos)

    #se todas as arestas foram visitadas e eu estou no ponto de partida...
    def terminou(self, v, arestas_percorridas):
        return (self.todas_arestas_visitadas(arestas_percorridas) and self.vertices[v].partida)


    def checa_aresta_visitada(self, aresta, arestas):
        for i in arestas:
            if i.hash == aresta.hash:
                return True
                break
        return False


    # esse metodo da o start ao percurso
    def encontra_caminho(self, v):
        self.gera_lista_hashes()
        self.vertices[v].partida = True
        print(len(self.arestas_hashes))
        self.percorre_grafo(v, 1)

        print("finalizando execucao...")
        for i in self.caminhos:
            print(i.percurso)
        #self.percorre_grafo(v)

    def avanca_proximo(self, v, i, ncaminho):
        print(ncaminho)
        print(len(self.caminhos))
        if not self.checa_aresta_visitada(i, self.caminhos[ncaminho - 1].arestas_percorridas):
            self.caminhos[ncaminho - 1].arestas_percorridas.append(self.get_aresta(v, i.destino))
            self.caminhos[ncaminho - 1].percurso += i.destino
            print(f'indo de {v} para {i.destino} caminho {ncaminho}')
            ncaminho += 1
            self.percorre_grafo(self.vertices[i.destino].nome, ncaminho)

    def percorre_grafo(self, v, ncaminho):
       # print(v)

        if len(self.caminhos) == 0:
            # print("primeiro caminho")
            self.caminhos.append(Caminho(v))
        else:
         #   print(f'{ncaminho} {len(self.caminhos)}')
            if ncaminho > len(self.caminhos):
                self.caminhos.append(Caminho(self.caminhos[ncaminho - 2].percurso + v))
            #self.caminhos.append(Caminho(self.caminhos[ncaminho - 1].percurso + v))
        #print(f'estou no vertice {v} e caminho {ncaminho}')
        if not self.terminou(v, self.caminhos[ncaminho - 1].arestas_percorridas) and ncaminho < 100:



            # if len(self.vertices[v].vizinhos) == 1:
            #     print("so tem um vizinho, avança")
            #     self.avanca_proximo(v, self.vertices[v].vizinhos[0], ncaminho)
            # else:
            for i in self.vertices[v].vizinhos:
                self.avanca_proximo(v, i, ncaminho)
                #ncaminho+=1


