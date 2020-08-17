#21366181
Graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def bfs(graph, start):
    queue = [start]
    visited = [start]

    while queue:
        node = queue.pop(0)

        for node in graph[node]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
    return visited


def bfs_recursion(graph, node, visited, queue):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue:
        node = queue.pop(0)
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
        bfs_recursion(graph, node, visited, queue)
    return visited


def dfs(graph, start):
    stack = [start]
    visited = [start]

    while stack:
        node = stack[-1]
        remove_node = True

        for Next in graph[node]:
            if Next not in visited:
                stack.append(Next)
                visited.append(Next)
                remove_node = False
                break

        if remove_node:
            stack.pop()
    return visited


def dfs_recursion(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for Next in graph[node]:
            dfs_recursion(graph, Next, visited)
    return visited

if __name__ == '__main__':
    
    live = True
    while(live):

        choice = int(input("Choose\n\n1.bfs\n2.dfs\n3.bfs_recurssion\n4.dfs_recursion\n5.Exit\n"))
        if choice == 1:
            print(bfs(Graph, 'A'))
        elif choice == 2:
            print(dfs(Graph, 'A'))
        elif choice == 3:
            print(bfs_recursion(Graph, 'A', [], []))
        elif choice == 4:
            print(dfs_recursion(Graph, 'A', []))
        elif choice == 5:
            live = False