def bfs(graph, first_node):
    # initialize items
    queue = []
    visited = []

    # append first node to traverse to queue
    queue.append(first_node)

    while len(queue) != 0:
        curr_node = queue.pop(0)
        # print('current node:', curr_node)
        nodes = graph[curr_node]
        visited.append(curr_node)
        for node in nodes:
            if node not in visited and node not in queue:
                queue.append(node)     

    return visited  

if __name__ == '__main__':
    graph = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
        '4' : ['8'],
        '8' : []
    }

    res = bfs(graph, '5')
    print(f'traversal steps:', res)