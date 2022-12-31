def bfs(graph: list, start: int):
    queue = [start] 
    queue_i = 0 

    visited = [False] * len(graph) 

    while queue_i < len(queue):
        current = queue[queue_i] 
        print(current, end = ' ') 

        for neibour in graph[current]:
            if not visited[neibour]:
                queue.append(neibour) 
                visited[neibour] = True 

        queue_i += 1 


def dfs(graph: list, start: int):
    stack = [start] 
    
    visited = [False] * len(graph) 

    while stack:
        current = stack.pop()  
        print(current, end = ' ') 

        for neibour in graph[current]:
            if not visited[neibour]:
                stack.append(neibour) 
                visited[neibour] = True 


graph = [
    [1, 2], 
    [3], 
    [4, 1], 
    [], 
    [] 
]

print("BFS:", end = ' ') 
bfs(graph, 0) 

print("\nDFS:", end = ' ')  
dfs(graph, 0) 