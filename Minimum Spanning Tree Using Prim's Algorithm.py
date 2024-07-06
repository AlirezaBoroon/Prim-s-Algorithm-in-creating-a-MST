import networkx as nx
import matplotlib.pyplot as plt
import time
import random

def prim_algorithm(adj_matrix):
    num_nodes = len(adj_matrix)
    selected_nodes = [False] * num_nodes # in the first stage, all nodes are not selected yet.
    selected_nodes[0] = True # starting from the node 0 as a selected node.
    mst_edges = [] # the goal list.

    for _ in range(num_nodes - 1):
        min_weight = float('inf') # set and reset the min value to +inf.
        u, v = -1, -1 # for having the target nodes later (after some calculations).
        for i in range(num_nodes): # for trying to find nodes in the selected nodes list.
            if selected_nodes[i]== True:
                for j in range(num_nodes): # for checking neighbors of the selected nodes.
                    if not selected_nodes[j] and adj_matrix[i][j] > 0 and adj_matrix[i][j] < min_weight:
                            min_weight = adj_matrix[i][j]
                            u, v = i, j
        # making node the member of selected (visited) nodes list:
        selected_nodes[v] = True
        mst_edges.append((u, v, min_weight))

    return mst_edges

def visualize_graph(G, pos, mst_edges):
    # Interactive mode is one, so the windows of the figures will updata and also close automatically.
    plt.ion()
    mst_G = nx.Graph()
    for u, v, weight in mst_edges:
        mst_G.add_edge(u, v, weight=weight)
        ###
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        #### the sizes should be fitted with already plotted plots. (but the above plot should be written later and with width= 2)
        nx.draw(mst_G, pos, with_labels=True, edge_color='r', width=2, node_color='lightblue', node_size=500, font_size=10)
        mst_labels= nx.get_edge_attributes(mst_G, 'weight')
        nx.draw_networkx_edge_labels(mst_G, pos, edge_labels= mst_labels)
        ###
        plt.show()
        plt.pause(3)
        plt.close()
    plt.ioff()

    plt.title("Minimum Spanning Tree using Prim's Algorithm")
    nx.draw(mst_G, pos, with_labels=True, edge_color='r', width=2, node_color='lightgreen', node_size=500, font_size=10)
    mst_labels= nx.get_edge_attributes(mst_G, 'weight')
    nx.draw_networkx_edge_labels(mst_G, pos, edge_labels= mst_labels)

    manager = plt.get_current_fig_manager()
    # Maximize the figure window to fullscreen
    manager.window.showMaximized()
    plt.show()
    
# Menue:
print("""Welcome to the Prim's Algorithm Program.\nPrim's Algorithm is a greedy method used to find the Minimum Spanning Tree (MST) of a connected, undirected graph. It works by:
    1. Starting from an arbitrary vertex and adding it to the MST.
    2. Repeatedly adding the smallest edge that connects a vertex in the MST to a vertex outside the MST.
    3. Using a priority queue to efficiently select the minimum weight edge at each step.
This algorithm is efficient for dense graphs and ensures the MST has the minimum possible total edge weight.Please determine that you want to calculate the Algorithm on your own graph or just on a random one?:""")
print("1: My own Graph / 2: Random Graph")
while True:
    choice= input()
    if choice== '1':
        print("Ok, please enter the number of nodes:")
        while True:
            number_of_nodes= input()
            if number_of_nodes.isdigit():
                number_of_nodes= int(number_of_nodes)
                break
            else:
                print("Please enter a valid number.")
                continue
        print("Now you enter the weights of the edges of your graph.\n(weights should be >0 and 0 means there isn't an edge between the two nodes.)")
        adj_matrix= []
        for i in range(0, number_of_nodes):
            adj_matrix.append([])
            for j in range(0, number_of_nodes):
                if i> j:
                    # entered before.
                    adj_matrix[i].append(adj_matrix[j][i])
                elif j== i:
                    adj_matrix[i].append(0)
                else:
                    adj_matrix[i].append(int(input(f"[{i+ 1}][{j+ 1}]:")))
        break
    elif choice== '2':
        print("Ok, please enter the number of nodes:")
        while True:
            number_of_nodes= input()
            if number_of_nodes.isdigit():
                number_of_nodes= int(number_of_nodes)
                break
            else:
                print("Please enter a valid number.")
                continue
        adj_matrix= []
        for i in range(0, number_of_nodes):
            adj_matrix.append([])
            for j in range(0, number_of_nodes):
                if i> j:
                    # entered before.
                    adj_matrix[i].append(adj_matrix[j][i])
                elif j== i:
                    adj_matrix[i].append(0)
                else:
                    num= random.randint(0, 10)
                    if num% 3== 0:
                        # zero weight is chosen in relateion of 1/3 +(a little fraction) from all other possible edge weights. it can also be done by a statistics distribution.
                        edge_weight= 0
                    else:
                        edge_weight= random.randint(1, 40) # the bounds are based on your preferences.
                    adj_matrix[i].append(edge_weight)
        time.sleep(1)
        print("A random Graph has been chosen!")
        break
    else:
        print("Please choose from the menue.")
        continue
# Showing the main Graph:
print("The Graph is:")
G = nx.Graph()
for i in range(number_of_nodes):
    for j in range(number_of_nodes):
        if adj_matrix[i][j] > 0:
            G.add_edge(i, j, weight=adj_matrix[i][j])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
# Example usage
# adj_matrix = np.array([
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]
# ])

print(6*'*')
print("The Prim's Algorithm runs...")
mst_edges = prim_algorithm(adj_matrix)
visualize_graph(G, pos, mst_edges)
print(6* '*')

print("(Edges log):")
for u, v, weight in mst_edges:
    print(f"Edge ({u}, {v}) with Weight: {weight}")

print("(Adjacency matrix log):")
for i in adj_matrix:
    print(i)
input()