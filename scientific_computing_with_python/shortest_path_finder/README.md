# Dijkstra's Algorithm / Algoritmo de Dijkstra

This Python script implements Dijkstra's algorithm to find the shortest path between two nodes in a graph with non-negative edge weights.

Este script Python implementa o algoritmo de Dijkstra para encontrar o caminho mais curto entre dois nós em um grafo com pesos de aresta não negativos.

## Features / Funcionalidades
- Finds the shortest path between two nodes. / Encontra o caminho mais curto entre dois nós.
- Handles graphs with non-negative edge weights. / Lida com grafos com pesos de aresta não negativos.
- Prints the shortest distance and path for each node. / Imprime a distância e o caminho mais curtos para cada nó.

## How to Use / Como Usar
Define your graph as a dictionary where each key is a node and the value is a list of tuples representing the connected nodes and their edge weights. Then, call the `shortest_path` function with the start node and optionally the target node.

Defina seu grafo como um dicionário onde cada chave é um nó e o valor é uma lista de tuplas representando os nós conectados e seus pesos de aresta. Em seguida, chame a função `shortest_path` com o nó de início e, opcionalmente, o nó de destino.

### Example / Exemplo
```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

shortest_path(my_graph, 'A', 'F')
```

## Requirements / Requisitos
Python 3.x

## How to Contribute / Como Contribuir
- Fork the repository. / Faça um fork do repositório.
- Create a branch for your feature: git checkout -b minha-feature. / Crie uma branch para sua feature.
- Commit your changes: git commit -m 'Adicionei uma nova feature'. / Commit suas mudanças.
- Push to the branch: git push origin minha-feature. / Push para a branch.
- Open a pull request and describe your changes. / Abra um pull request e descreva suas mudanças.

## License / Licença
This project is licensed under the MIT License. See the LICENSE file for details.

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
