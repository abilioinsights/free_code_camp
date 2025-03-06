def initialize_shortest_distances(graph, start_node):
    """Inicializa as distâncias mais curtas para cada nó."""
    return {node: 0 if node == start_node else float('inf') for node in graph}

def initialize_paths_taken(graph, start_node):
    """Inicializa os caminhos percorridos para cada nó."""
    paths_taken = {node: [] for node in graph}
    paths_taken[start_node].append(start_node)
    return paths_taken

def shortest_path(graph, start_node, target_node=''):
    """Encontra o caminho mais curto entre dois nós usando o algoritmo de Dijkstra."""
    # Input validation
    if start_node not in graph or (target_node and target_node not in graph):
        raise ValueError("Nó de início ou destino não encontrado no grafo.")

    # Initialize distances and paths
    unvisited_nodes = list(graph)
    shortest_distances = initialize_shortest_distances(graph, start_node)
    paths_taken = initialize_paths_taken(graph, start_node)

    # Loop until all nodes have been visited
    while unvisited_nodes:
        # Selects the unvisited node with the shortest known distance
        current_node = min(unvisited_nodes, key=shortest_distances.get)
        
        # Explore the neighbors of the current node
        for neighbor, edge_distance in graph[current_node]:
            # Calculates the new potential distance
            new_distance = edge_distance + shortest_distances[current_node]
            
            # If the new distance is smaller, update the distance and path
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                
                # Updates the path taken
                if paths_taken[neighbor] and paths_taken[neighbor][-1] == neighbor:
                    paths_taken[neighbor] = paths_taken[current_node][:]
                else:
                    paths_taken[neighbor].extend(paths_taken[current_node])
                
                # Adds neighboring node to path
                paths_taken[neighbor].append(neighbor)
        
        # Remove current node from unvisited list
        unvisited_nodes.remove(current_node)
    
    # Choose which nodes to print: the specific target node or all nodes
    nodes_to_print = [target_node] if target_node else graph
    
    # Print the shortest distance and path to each node
    for node in nodes_to_print:
        if node == start_node:
            continue
        print(f'\n{start_node} -> {node} distance: {shortest_distances[node]}')
        print(f'Path: {" -> ".join(paths_taken[node])}')
    
    return shortest_distances, paths_taken

# Graph structure where each node is connected to others with specific distances
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Example usage
shortest_path(my_graph, 'A', 'F')
