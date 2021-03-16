#!/usr/bin/env python
import argparse
import sys

import time
import matplotlib.pyplot as plt

import chinese_postman_lib
import chinese_postman_lib.data as data
from chinese_postman_lib import eularian, network


def setup_args():
    """ Caso quiser pegar o nome do grafo como argumento. """
    parser = argparse.ArgumentParser(description='Procurar um circuito euleriano.')
    parser.add_argument('graph', nargs='?', help='Nome do grafo a ser carregado')
    args = parser.parse_args()
    return args.graph


def main():
    #declarando duas listas para gerar o grafico
    tempos = list()
    numeroArestas = list()
    edges = None

    #se quiser pegar do console, descomenta aqui
    #graph_name = setup_args()

    # grafos que serao testados colocados na mao
    graph_names = ["nova_luz2", "nova_luz"]

    for graph_name in graph_names:
        inicio = time.time()
        try:
            print('Carregando grafo: {}'.format(graph_name))
            edges = getattr(chinese_postman_lib.data, graph_name)
        except (AttributeError, TypeError):
            print('\nNome de grafo invalido. Grafos disponíveis:\n\t{}\n'.format(
                '\n\t'.join([x for x in dir(chinese_postman_lib.data)
                if not x.startswith('__')])))
            sys.exit()

        original_graph = network.Graph(edges)

        print('<{}> arestas'.format(len(original_graph)))
        if not original_graph.is_eularian:
            print('Convertendo para um caminho euleriano...')
            graph, num_dead_ends = eularian.make_eularian(original_graph)
            print('Conversão Completa')
            print('\tAdicionadas {} arestas'.format(len(graph) - len(original_graph) + num_dead_ends))
            print('\tO custo total é {}'.format(graph.total_cost))
        else:
            graph = original_graph

        print('Tentando resolver o circuito eulariano...')
        route, attempts = eularian.eularian_path(graph, start=1)
        if not route:
            print('\tDesistindo depois de <{}> tentativas.'.format(attempts))
        else:
            print('\tResolvido em <{}> tentativas'.format(attempts, route))
            print('Solução: (<{}> arestas)'.format(len(route) - 1))
            print('\t{}'.format(route))
        fim = time.time()
        tempos.append(fim - inicio)
        numeroArestas.append(len(route) - 1)
    plt.xlabel('Número de Arestas')
    plt.ylabel('Time Complexity')
    # plt.plot(elements, times, label='Força Bruta')
    plt.plot(numeroArestas, tempos, label='Número de Arestas x Tempo - Branch and Bound (Dijkstra)')
    plt.grid()
    plt.legend()
    plt.show()




if __name__ == '__main__':

    main()



