from graph_reader import read_graph
from a_star import a_star_search

def main():
    file_path = 'cities.txt'
    graph, heuristics = read_graph(file_path)
    
    start = input("Start node: ").strip().capitalize()
    goal = input("Destination: ").strip().capitalize()
    
    if start not in graph and goal not in graph:
        print("Invalid start and destination node.")
        return
    elif start not in graph:
        print("Invalid start node.")
        return
    elif goal not in graph:
        print("Invalid destination node.")
        return
    
    path, total_distance = a_star_search(graph, heuristics, start, goal)
    
    
    if path:
        if None in path:
            print("NO PATH FOUND")
        else:
            print(f"Path: {' -> '.join(path)}")
            print(f"Total distance: {total_distance} km")
    else:
        print("NO PATH FOUND")


if __name__ == "__main__":
    main()