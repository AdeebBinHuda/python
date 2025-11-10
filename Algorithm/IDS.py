# iterative deepening search
def dls(graph, node, target, limit,visited=None):
    if visited is None:
        visited = set()
        if node == target:
            print(node, end=' ')
            return True
        if limit <=0:
            return False
        visited.add(node)
        print(node,end=' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dls(graph, neighbour, target, limit-1, visited):
                    return True
                return False


def ids(graph,start,target,max_depth):
    for depth in range(max_depth):
        print(f"Depth Level: {depth}")
        if dls(graph,start,target, depth): #depth limited search
            print("target found")
            return
        print("target not found in this depth")



graph ={
     'A': ['B','C'],
     'B':['D','E'],
     'C':['F'],
     'D':[],
     'E':['F'],
     'F':[]
}

ids(graph,'A','F', 3)  # Example call to the ids function with max depth 3