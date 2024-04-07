"""
traverse a graph by depth
for each node in a graph, add its neighbors to a queue
then traverse the nodes in the queue
until the to_search element is found
"""
def bfs(graph, first_node):
    pass

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