graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F', 'G'},
    'D': {'H', 'I'},
    'E': {'J', 'K'},
    'F': {'L', 'M'},
    'G': {'N', 'O'},
    'H': {},  # Leaf nodes (terminal)
    'I': {},
    'J': {},
    'K': {},
    'L': {},
    'M': {},
    'N': {},
    'O': {}
}

# Separate terminal values dictionary
terminal_values = {
    'H': 3,
    'I': 5,
    'J': 6,
    'K': 9,
    'L': 1,
    'M': 2,
    'N': 0,
    'O': -1
}

def alpha_beta_pruning(node, graph, max_func, alpha, beta):
    # If it's a terminal node, return its value from terminal_values
    if not graph[node]:  
        return terminal_values[node]
    
    if max_func:
        max_value = float('-inf')  # Initialize maximum value
        for child in graph[node]:
            value = alpha_beta_pruning(child, graph, False, alpha, beta)
            max_value = max(max_value, value)  # Maximize value
            alpha = max(alpha, value)  # Update alpha
            if beta <= alpha:  # Prune remaining branches
                break
        return max_value
    else:
        min_value = float('inf')  # Initialize minimum value
        for child in graph[node]:
            value = alpha_beta_pruning(child, graph, True, alpha, beta)
            min_value = min(min_value, value)  # Minimize value
            beta = min(beta, value)  # Update beta
            if beta <= alpha:  # Prune remaining branches
                break
        return min_value

# Initialize alpha and beta
alpha = float('-inf')
beta = float('inf')

# Run Alpha-Beta Pruning
result = alpha_beta_pruning('A', graph, True, alpha, beta)
print("The optimal value is:", result)
