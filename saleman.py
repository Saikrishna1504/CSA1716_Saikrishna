import itertools

def tsp(cities):
    return min(itertools.permutations(cities), key=lambda path: sum(abs(path[i] - path[i+1]) for i in range(len(path)-1)))

# Example usage:
cities = (0, 1, 2, 3)  # Example cities
best_path = tsp(cities)
print("Best Path:", best_path) epxlain 
