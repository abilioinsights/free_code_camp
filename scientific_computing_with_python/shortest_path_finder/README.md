# Shortest Path Finder - Dijkstra Algorithm

This Python project implements the **Dijkstra algorithm** to find the shortest path between nodes in a graph. The algorithm calculates the minimum distance from a starting node to other nodes and records the optimal path.

## Features

- Find the shortest path from a start node to a target node.
- Calculates distances for all nodes in the graph from a start node.
- Visualize the shortest path and distance for each node.

## Usage

### Graph Structure

The graph is represented as an **adjacency list**, where each node has a list of tuples. Each tuple contains the connected node and the weight of the edge between them.

Example graph:

```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}
```

## Running the Algorithm
To find the shortest path between nodes in a graph, you can use the function shortest_path().

## Function Parameters:
- graph: A dictionary representing the graph.
- start: The starting node for the path search.
- target: (Optional) A specific target node. If not provided, the distances and paths to all nodes will be shown.


```py
from dijkstra_algorithm import shortest_path

# Example usage
distances, paths = shortest_path(my_graph, 'A', 'F')
```

Example Output:
```py
A-F distance: 7
Path: A -> B -> F
```

## Returning Values
- distances: A dictionary where the keys are nodes, and the values are the shortest distances from the start node.
- paths: A dictionary where the keys are nodes, and the values are lists representing the shortest path from the start node.

## Installation
1. Clone the repository:

```py
git clone https://github.com/yourusername/shortest_path_finder.git

```

2. Navigate to the project folder:

```py
cd shortest_path_finder
```

3. Run the script:

```py
python dijkstra_algorithm.py
```

## Customization
You can modify the my_graph variable with your own graph, adjusting the nodes and edge weights as necessary.
