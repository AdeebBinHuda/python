import heapq
def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set,(0 + h[start],0,start,[start])) # (f_score, g_score, node, path)
    visited = set()

    while open_set:
        f,g,node, path = heapq.heappop(open_set)

        if node == goal:
            return path
        
        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph.get(node,[]):
            if neighbor not in visited:
                new_g = g+  cost
                new_f = new_g + h[neighbor]
                heapq.heappush(open_set,(new_f,new_g,neighbor, path+[neighbor]))
    return None

graph= {
    'A':[('B',1),('C',4)],
    'B':[('D',2),('E',5)],
     'C':[('F',1)],
     'D':[],
     'E':[('F',1)],
     'F':[]
}

heuristic ={
    'A':7,
    'B':6,
    'C':2,
    'D':1,
    'E':1,
    'F':0
}

result = a_star(graph, 'A','F',heuristic)
print("path fouund by A* search:",result)