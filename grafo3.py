# a implementacao desse grafo se dará por lista de adjacencias
# TESTANDO COM FORÇA BRUTA

class Vertice:
    def __init__(self, n):
        self.nome = n
        self.partida = False
        self.vizinhos = list()

    def adiciona_vizinho(self, v, peso, direcionado):
        if v not in self.vizinhos:
            self.vizinhos.append((Aresta(v, peso, direcionado)))

class Aresta:
    def __init__(self, v, p, direcionado):
        self.destino = v
        self.peso = p
        self.direcionado = direcionado
        self.visitado = False
        self.quantidade_visitas = 0
        #considerar colocar a origem tambem

class Caminho:
    def __init__(self, percurso):
        self.arestas_percorridas = list()
        self.percurso = percurso
        self.custo = 0


class Grafo:
    vertices = {}
    caminhos = list()
    caminhosPossiveis = 0
    caminho = ""
    custo = 0

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
    def todas_arestas_visitadas(self):
        #iterando todos os vertices
        for dd in self.vertices.values():
            #print(dd.vizinhos)
            #checando cada aresta de um vertice
            for j in dd.vizinhos:
                #print(j.visitado)
                # se a aresta nao foi ainda visitada
                if not j.visitado:
                    #print("aresta nao foi visitada")
                    # se a aresta for direcionada ....
                    if j.direcionado:
                        # retorna falso para visitar
                        return False
                        break
                    # se a aresta nao for direcionada...
                    else:
                        # e se o outro lado ainda nao foi visitado...
                        if not self.aresta_visitada(j.destino, dd.nome):
                            #print ("nao visitou nenhum dos lados")
                            # retorna falso para visitar
                            return False
                            break
        return True

    #se todas as arestas foram visitadas e eu estou no ponto de partida...
    def terminou(self, v):
        return (self.todas_arestas_visitadas() and self.vertices[v].partida)


    # esse metodo da o start ao percurso
    def encontra_caminho(self, v):
        self.vertices[v].partida = True
        self.percorre_grafo(v, 1)
        #self.percorre_grafo(v)


    # recebe o vertice que está e para onde vai, avançando o caminho para o proximo vertice
    def avanca_proximo(self, v, i, ncaminho):
    #def avanca_proximo(self, vizinhos, ncaminho):

        if len(self.vertices[v].vizinhos) <= 1:
            print("so tem um vizinho, avança")

            self.percorre_grafo(self.vertices[i.destino].nome)
            self.avanca_proximo(v, i, ncaminho)
        else:
            print("tem mais de um vizinho, vamos checar qual aresta é melhor")
            self.caminhosPossiveis += len(self.vertices[v].vizinhos)
            self.avanca_proximo(v, melhor_aresta(self.vertices[v].vizinhos), ncaminho)
            ncaminho += 1
        # marcando a aresta como visitada
            self.marca_aresta_visitada(v,i.destino)
            # somando o custo para o proximo destino
            self.custo = self.custo + i.peso

            #print(ncaminho)

            self.caminhos[ncaminho-1].arestas_percorridas.append(self.get_aresta(v,i.destino))

            #print(len(self.caminhos[ncaminho - 1].arestas_percorridas))
            # self.caminhos[ncaminho-1].percurso = self.caminhos[ncaminho-1].percurso + i.destino
            # vamos agora avançar de fato
            #self.percorre_grafo(self.vertices[i.destino].nome)

            self.percorre_grafo(self.vertices[i.destino].nome, ncaminho)

    # aqui eu percorro o grafo e verifico qual vai ser a melhor aresta para seguir
    #def percorre_grafo(self,v):
    def percorre_grafo(self, v, ncaminho):
        # estou recebendo uma lista de arestas e vamos checar qual é a melhor para prosseguir
        def melhor_aresta(lista_aresta):
            # armazenando o primeiro valor da lista
            melhor = lista_aresta[0]
            for n in range(len(lista_aresta)):

                # se o melhor atual for visitado e o comparado nao, ja atribui
                if melhor.visitado and not lista_aresta[n].visitado:
                    if lista_aresta[n].direcionado:
                        melhor = lista_aresta[n]
                    else:
                        # caso de aresta nao direcionada
                        if (not self.aresta_visitada(lista_aresta[n].destino, v)):
                            melhor = lista_aresta[n]

                # se ambos nao tiverem sido visitados, compara o de menor peso
                elif not melhor.visitado and not lista_aresta[n].visitado:
                    if lista_aresta[n].peso < melhor.peso:
                        melhor = lista_aresta[n]
                # se ambos ja foram visitados
                else:
                    # verifico qual teve menor quantidade de visitas ...
                    if lista_aresta[n].quantidade_visitas < melhor.quantidade_visitas:
                        melhor = lista_aresta[n]
            #print(f'{melhor.destino} é o melhor vertice para prosseguir')
            return melhor

        print(f'estou no vertice {v} e caminho {ncaminho}')

        if len(self.caminhos) == 0:
            print("primeiro caminho")
            self.caminhos.append(Caminho(v))
        else:
           # if len(self.caminhos) < ncaminho:
                print("novo caminho")

               # print(self.caminhos[ncaminho-2].percurso)

                self.caminhos.append(Caminho(self.caminhos[ncaminho-2].percurso + v ))
           # else:
           #     self.caminhos[ncaminho-1].percurso = self.caminhos[ncaminho-1].percurso + v

        self.caminho = self.caminho + v
        #print(f'estou no vertice {v}')
        # enquanto nao tiver chego de volta ao ponto inicial e nao tiver percorrido tudo, vai continuar...

        if not self.terminou(v):
            #print('entrou aqui?')
            #iterando cada vertice vizinho ao vertice atual
            for i in self.vertices[v].vizinhos:
                #print(len(self.vertices[v].vizinhos))
                # se tiver so um vizinho, avança pro proximo
                if len(self.vertices[v].vizinhos) <= 1:
                    print("so tem um vizinho, avança")
                    self.avanca_proximo(v, i, ncaminho)
                    break
                else:
                    print("tem mais de um vizinho, vamos checar qual aresta é melhor")
                    self.caminhosPossiveis += len(self.vertices[v].vizinhos)
                    self.avanca_proximo(v, melhor_aresta(self.vertices[v].vizinhos), ncaminho)
                    ncaminho += 1
                    #self.avanca_proximo(v, melhor_aresta(self.vertices[v].vizinhos), ncaminho )
                    #break
        # se tiver visitado todas arestas e ja estivermos no ponto inicial
        else:
            #print(f'Caminho percorrido: {self.caminho}')
            #print(self.caminhos[0].percurso)
            #print(f'caminhos gerados: {len(self.caminhos)}')
            print(len(self.caminhos))
            self.caminhos[ncaminho - 1].arestas_percorridas

            print(f'Custo total: {self.custo}')

            print(len(self.caminhos[0].arestas_percorridas))

            return True
