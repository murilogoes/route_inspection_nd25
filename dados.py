#grafo 1, 2, 3, 4 ....

nova_luz = {
    "arestas": [
        ('1', '2', 50, True),
        ('2', '3', 215, False),
        ('3', '4', 100, False),
        ('4', '5', 15, True),
        ('5', '6', 90, True),
        ('6', '7', 120, True),
        ('6', '9', 100, False),
        ('7', '8', 20, True),
        ('8', '1', 155, True),
        ('8', '10', 30, True),
        ('9', '10', 50, True),
        ('10', '7', 10, True),
        ('9', '11', 70, True),
        ('11', '8', 50, True),
        ('9', '12', 80, True),
        ('12', '13', 90, True),
        ('13', '6', 60, True),

    ]
}

data = {
    1: {
        "vertices": ['A', 'B', 'C', 'D', 'E'],
        "arestas": [
            ('A', 'D', 1, True), ('B', 'A', 5, True), ('B', 'C', 3, True), ('C', 'D', 8, True), ('D', 'B', 2, True),
            ('D', 'A', 3, True) #, ('B', 'E', 2, True), ('E', 'C', 4, True)
        ],
        "descricao": "grafo 100% Direcionado"
    },
    2: {
        "vertices": ['A', 'B', 'C', 'D', 'E'],
        "arestas": [
            ('A', 'D', 1, False), ('B', 'A', 5, False), ('B', 'C', 3, False), ('C', 'D', 8, False), ('D', 'B', 2, False),
            ('D', 'A', 3, False), ('B', 'E', 2, False), ('E', 'C', 4, False)
        ],
        "descricao": "grafo 100% não Direcionado"
    },
    3: {
        "vertices": ['A', 'B', 'C', 'D'],
        "arestas": [
            ('A', 'B', 3, True), ('A', 'D', 4, False), ('B', 'A', 1, True), ('B', 'C', 2, False), ('D', 'C', 2, True)
        ],
        "descricao": "grafo misto simples"
    },
    4: {
        "vertices": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        "arestas": [
            ('A', 'C', 7, True), ('B', 'A', 6, True), ('B', 'G', 5, False), ('C', 'B', 6, False), ('C', 'D', 5, False),('D', 'E', 5, True),
            ('E', 'B', 4, True), ('E', 'F', 5, False), ('F', 'G', 20, False)
        ],
        "descricao": "grafo misto mais complexo"
    }
}

