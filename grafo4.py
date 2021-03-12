import secrets
from copy import deepcopy
import time
import matplotlib.pyplot as plt
import time


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
        # considerar colocar a origem tambem


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

    #########################################
    # as linhas abaixo é para gerar o grafico
    elements = list()
    times = list()
    tempo = 0
    vezes = 0

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

    # gera uma lista com todos os hashes das arestas no começo do programa para facilitar a busca em tempo de execucao
    def gera_lista_hashes(self):
        for dd in self.vertices.values():
            for j in dd.vizinhos:
                self.arestas_hashes.append(j.hash)

    # imprime o grafo como lista de adjacencias
    def imprime_grafo(self):
        for dd in self.vertices.values():
            lista = dd.nome + ":"
            for j in dd.vizinhos:
                lista = f'{lista} -> {j.destino} ({j.peso})({j.direcionado})'
            print(lista)

    # metodo me retorna uma aresta passando o vertice de origem e o destino
    def get_aresta(self, v, d):
        for i in self.vertices[v].vizinhos:
            if i.destino == d:
                return i

    # metodo para me dizer se todas as arestas ja foram visitadas
    # aqui, quando uma aresta nao direcionada nao foi percorrida em determinado sentido, eu verifico se ja foi no outro sentido, ai marca como visitada
    def todas_arestas_visitadas(self, arestas_percorridas):

        # montando uma lista com os hashes das arestas percorridas
        arestas_percorridas_hashes = list()
        for i in arestas_percorridas:
            arestas_percorridas_hashes.append(i.hash)

        # montando uma lista dos hashes nao percorridos
        hashes_nao_percorridos = list()
        # for j in arestas_percorridas:
        for j in self.arestas_hashes:
            if j not in arestas_percorridas_hashes:
                hashes_nao_percorridos.append(j)

        # aqui eu vou checar se caso houver uma aresta nao visitada e ela for nao direcionada, checa se a aresta do outro lado foi visitada
        # caso a aresta inversa ja foi visitada, eu considero toda aresta visitada e removo da lista de hashes nao percorridos
        for i in self.vertices.values():
            for j in i.vizinhos:
                if not j.direcionado:
                    if j.hash in hashes_nao_percorridos:
                        # pegando as coordenadas do hash nao visitado
                        coordenadas = self.get_aresta_por_hash(j.hash)
                        # invertando as coordenadas, pegando a aresta do lado contrario
                        aresta = self.get_aresta(coordenadas[1], coordenadas[0])
                        # se a aresta do lado contrario for visitada, eu removo a nao visitada da lista
                        if aresta.hash in arestas_percorridas_hashes:
                            hashes_nao_percorridos.remove(j.hash)

        # se a lista de hash nao percorrido for igual a zero significa que ja percorreu tudo
        return len(hashes_nao_percorridos) == 0

    # metodo para pegar uma aresta passando o hash como entrada
    def get_aresta_por_hash(self, hash):
        teste = list()
        for i in self.vertices.values():
            for j in i.vizinhos:
                if j.hash == hash:
                    teste.append(i.nome)
                    teste.append(j.destino)
                    return teste

    # metodo para dizer se o percurso terminou, se todas as arestas foram visitadas e eu estou no ponto de partida...
    def terminou(self, v, arestas_percorridas):
        return (self.todas_arestas_visitadas(arestas_percorridas) and self.vertices[v].partida)

    # aqui eu passo uma aresta unica e uma lista de arestas, se essa aresta tiver na lista, significa que ja foi visitada
    def caminho_visitado(self, aresta, arestas_percorridas):
        for i in arestas_percorridas:
            if aresta.hash == i.hash:
                return True
        return False

    # aqui eu vou pegar exatamente a aresta do caminho especifico que foi rodado, em relacao a aresta do grafo original
    def get_aresta_caminho(self, aresta, arestas_percorridas):
        for i in arestas_percorridas:
            if aresta.hash == i.hash:
                return i

    # esse metodo da o start ao percurso da aplicacao
    def encontra_caminho(self, v):
        self.gera_lista_hashes()
        self.vertices[v].partida = True
        self.percorre_grafo(v, 1)

        print("finalizando execucao...")
        for i in self.caminhos:
            print(f'{i.percurso} + {i.custo}')
        print(len(self.caminhos))
        plt.xlabel('Iterações')
        plt.ylabel('Time Complexity')
        #plt.plot(elements, times, label='Força Bruta')
        plt.plot(self.elements, self.times, label='Força Bruta')
        plt.grid()
        plt.legend()
        plt.show()
        # aqui ele vai iterar os caminhos feitos, me falar o percurso e o custo de cada


    # metodo para avancar ao proximo vertice
    def avanca_proximo(self, v, i, ncaminho):

        if ncaminho > len(self.caminhos):
            #print("novo caminho")
            self.caminhos.append(deepcopy(self.caminhos[ncaminho - 2]))
            # self.caminhos[ncaminho - 1].percurso += v
            # self.caminhos[ncaminho - 1].visitado = True

        contem_aresta = False
        nova_aresta = {}

        # essa iteracao esta sendo necessaria para eu checar se estou passando pela mesma aresta
        # ao inves de adicionar uma aresta nova no caminho, eu apenas incremento a existente
        for j in self.caminhos[ncaminho - 1].arestas_percorridas:
            if j.hash == i.hash:
                contem_aresta = True
                nova_aresta = j
                break
        if contem_aresta:
            nova_aresta.quantidade_visitas += 1
        else:
            # se for uma aresta nova, eu pego ela e jogo no caminho
            nova_aresta = deepcopy(i)
            nova_aresta.quantidade_visitas += 1
            nova_aresta.visitado = True
            self.caminhos[ncaminho - 1].arestas_percorridas.append(nova_aresta)

        # independente dos dois casos acima, incrementando o percurso e o peso
        self.caminhos[ncaminho - 1].percurso += "->" + i.destino
        self.caminhos[ncaminho - 1].custo += i.peso
        #print(f'indo de {v} para {i.destino} caminho {ncaminho}')

        # chamando a funcao que vai percorrer o grafo, passando o vertice destino e a posicao do caminho
        self.percorre_grafo(self.vertices[i.destino].nome, ncaminho)

    # metodo principal que vai fazer caminhar de um vertice do outro, escolhendo a melhor aresta
    def percorre_grafo(self, v, ncaminho):

        inicio = time.time()
        # print(f'Estou no vertice {v}')

        # esse metodo vai me dizer qual vai ser a melhor aresta a ser seguida atraves do vertice que estou
        def melhor_aresta(lista_aresta, arestas_percorridas):
            # armazenando o primeiro valor da lista
            melhor = lista_aresta[0]
            alternativo = None
            for n in range(len(lista_aresta)):

                # se o melhor atual for visitado e o comparado nao, ja atribui
                if self.caminho_visitado(melhor, arestas_percorridas) and not self.caminho_visitado(lista_aresta[n],
                                                                                                    arestas_percorridas):
                    # print("melhor ja foi visitado e valor testado nao")
                    if lista_aresta[n].direcionado:
                        melhor = lista_aresta[n]
                    else:
                        # caso de aresta nao direcionada
                        aresta_inversa = self.get_aresta(lista_aresta[n].destino, v)
                        if not self.caminho_visitado(aresta_inversa, arestas_percorridas):
                            melhor = lista_aresta[n]

                # se ambos nao tiverem sido visitados, compara o de menor peso
                elif not self.caminho_visitado(melhor, arestas_percorridas) and not self.caminho_visitado(
                        lista_aresta[n], arestas_percorridas):
                    # print("nenhum dos dois foram visitados")
                    # TO MEXENDO AQUI PARA RESOLVER O PROBLEMA DE RECURSAO
                    # elif not melhor.visitado and not lista_aresta[n].visitado:
                    if lista_aresta[n].peso < melhor.peso:
                        # if lista_aresta[n].hash != melhor.hash:
                        alternativo = deepcopy(melhor)
                            #self.avanca_proximo(v, melhor, len(self.caminhos) + 1)
                        melhor = lista_aresta[n]
                    #else:
                      #  if lista_aresta[n].hash != melhor.hash:
                       #     alternativo = deepcopy(lista_aresta[n])
                            # self.avanca_proximo(v, lista_aresta[n], len(self.caminhos) + 1)
                        #print(f'indo de {v}  para {melhor.destino} caminho {ncaminho}')
                    # else:
                    #     self.avanca_proximo(v, lista_aresta[n], len(self.caminhos) + 1)
                # se ambos ja foram visitados
                # else:
                elif self.caminho_visitado(melhor, arestas_percorridas) and self.caminho_visitado(lista_aresta[n],
                                                                                                  arestas_percorridas):
                    # verifico qual teve menor quantidade de visitas ...
                    # print("ambos foram visitados")

                    if self.get_aresta_caminho(lista_aresta[n],
                                               arestas_percorridas).quantidade_visitas < self.get_aresta_caminho(melhor,
                                                                                                                 arestas_percorridas).quantidade_visitas:

                        melhor = lista_aresta[n]

                # print(f'{melhor.destino} é o melhor vertice para prosseguir')
                if alternativo:
                    self.avanca_proximo(v, alternativo, len(self.caminhos) + 1)
                    # AQUI EU POSSO COLOCAR UMA TRAVA PARA GERAR MENOS CAMINHOS
                #if alternativo and len(self.caminhos) < 1:
                #    self.avanca_proximo(v, alternativo, len(self.caminhos) + 1)


            return melhor

        ######### FIM DA FUNCAO QUE VERIFICA A MELHOR ARESTA ###########

        # se tiver no começo da aplicação, ainda não temos caminhos, então vamos criar o primeiro


        if len(self.caminhos) == 0:
            # print("primeiro caminho")
            self.caminhos.append(Caminho(v))
        # else:

        #   print(f'{ncaminho} {len(self.caminhos)}')
        # se ja tiver caminho criado, vamos checar se é um novo caminho pelo ncaminho
        # se o ncaminho for superior ao tamanho de caminhos, significa que estou querendo criar um novo caminho
        #    if ncaminho > len(self.caminhos):
        #        self.caminhos.append(deepcopy(self.caminhos[ncaminho - 2]))
        #        self.caminhos[ncaminho - 1].percurso += v
        #        self.caminhos[ncaminho - 1].visitado = True

        # se nao terminou, ou seja, se ainda nao percorreu tudo e chegou ao inicial...
        # ncaminho < 10 eu coloquei para percorrer apenas 10 caminhos

        if not self.terminou(v, self.caminhos[ncaminho - 1].arestas_percorridas):

            # se so tiver uma aresta para ir ate o vizinho do vertice atual, ja avança para o proximo
            if len(self.vertices[v].vizinhos) == 1:
                # print("so tem um vizinho, avança")
                self.avanca_proximo(v, self.vertices[v].vizinhos[0], ncaminho)
            # senao, vamos verificar qual aresta é melhor
            else:
                # print("tem mais de um vizinho, vamos ver qual vai pegar")
                self.avanca_proximo(v, melhor_aresta(self.vertices[v].vizinhos,
                                                     self.caminhos[ncaminho - 1].arestas_percorridas), ncaminho)
                # self.avanca_proximo(v, melhor_aresta(self.vertices[v].vizinhos, ncaminho))

        fim = time.time()
        #print(fim - inicio)
        self.tempo = self.tempo + (fim - inicio)
        self.elements.append(self.vezes)
        self.vezes += 1
        self.times.append(self.tempo)
        # self.elements().append(len(self.caminhos))
        #self.elements().append(len(fim - inicio))