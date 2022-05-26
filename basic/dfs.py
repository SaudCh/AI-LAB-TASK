graph = {
            0: [1, 2, 3, 4],
            1: [0, 5],
            2: [0, 5],
            3: [0, 6],
            4: [0, 6],
            5: [1, 2, 7],
            6: [3, 4, 7],
            7: [5, 6],
}
def dfs(graph, start,toSearch):  
    # keep track of all visited nodes  []
    explored = []  # []
    # keep track of nodes to be checked
    queue = [start]   # [0,6]  [4]
    print(queue)   #[4]
    # keep looping until there are nodes still to be checked[0,6]
    while queue:
        print("queue : ", queue)
        # pop Top node (first node) from stack
        node = queue.pop(0) # 0
#        print(node)
#        node = queue.pop(0)
#        print('node being explored: ',node)
        print("explored : ", explored)
        if node not in explored: #[4]
            # add node to list of checked nodes
            explored.append(node) #[4,0]
            neighbours = graph[node]  #[1,2,3,4]
            # add reversed neighbours of node to stack so they could pop in actual order.
            #neighbours.reverse() #[6,0]
            for neighbour in neighbours:
                queue.append(neighbour)  
    return explored
toSearch = 3
print(dfs(graph, 4,3))
# EXPECTED OUTPUT : [0, 1, 5, 2, 7, 6, 3, 4]
