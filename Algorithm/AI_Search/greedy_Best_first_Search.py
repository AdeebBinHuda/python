import heapq
graph = {
   'A': [('B', 1), ('C', 2)],
   'B': [('D', 3), ('E', 5)],
   'C': [('F', 4)],
   'D': [('G', 6)],
   'E': [('G', 1)],
   'F': [('G', 1)],
   'G': []
}
heuristic = {
    'A': 8,
    'B': 5,
    'C': 6,
    'D': 2,
    'E': 1,
    'F': 1,
    'G': 0
}
def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    visited = {start}
    while priority_queue:
        (h_cost, current_node, path) = heapq.heappop(priority_queue)
        if current_node == goal:
          return path
        if current_node in graph:
            for neighbor, actual_cost in graph[current_node]:
              if neighbor not in visited:
               new_h_cost = heuristic[neighbor]
               new_path = path + [neighbor]
               heapq.heappush(priority_queue, (new_h_cost, neighbor, new_path))
               visited.add(neighbor)
    return "Goal not found"
start_node = 'A'
goal_node = 'G'
result = greedy_best_first_search(graph, start_node, goal_node, heuristic)
print(f"Starting Node: **{start_node}**")
print(f"Goal Node: **{goal_node}**")
print(f"Heuristic values: {heuristic}")
print("---")
print(f"Path found by GBFS: **{result}**")