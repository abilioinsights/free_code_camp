# Graph structure where each node is connected to others with specific distances
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start_node, target_node=''):
    # List of all nodes that haven't been visited yet
    unvisited_nodes = list(graph)
    
    # Dictionary to track the shortest distance to each node, start_node has distance 0
    shortest_distances = {node: 0 if node == start_node else float('inf') for node in graph}
    
    # Dictionary to track the path taken to reach each node
    paths_taken = {node: [] for node in graph}
    
    # Start the path from the start_node
    paths_taken[start_node].append(start_node)
    
    # Loop until all nodes have been visited
    while unvisited_nodes:
        # Select the unvisited node with the smallest known distance
        current_node = min(unvisited_nodes, key=shortest_distances.get)
        
        # Explore the neighbors of the current node
        for neighbor, edge_distance in graph[current_node]:
            # Calculate the potential new path distance
            new_distance = edge_distance + shortest_distances[current_node]
            
            # If the new distance is shorter, update the distance and path
            if new_distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = new_distance
                
                # Ensure paths are updated correctly
                if paths_taken[neighbor] and paths_taken[neighbor][-1] == neighbor:
                    paths_taken[neighbor] = paths_taken[current_node][:]
                else:
                    paths_taken[neighbor].extend(paths_taken[current_node])
                
                # Add the neighbor node to the path
                paths_taken[neighbor].append(neighbor)
        
        # Remove the current node from unvisited list
        unvisited_nodes.remove(current_node)
    
    # Choose which target to print: either the specific target_node or all nodes
    nodes_to_print = [target_node] if target_node else graph
    
    # Print the shortest distance and path for each node
    for node in nodes_to_print:
        if node == start_node:
            continue
        print(f'\n{start_node} -> {node} distance: {shortest_distances[node]}')
        print(f'Path: {" -> ".join(paths_taken[node])}')
    
    return shortest_distances, paths_taken

shortest_path(my_graph, 'A', 'F')
