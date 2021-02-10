
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import networkx as nx

N = 7 #num de pontos que existirão para as formigas iniciarem
NUM_ANTS = 1 #num que multiplicará a qtd de nós para obter as formigas iniciarem 1*X Formigas

def solve_tsp(G, ants, N, num_max_iterations=100, evaporation_rate=0.7):
    # do iterations for tsp
    path_dict = {}
    for iters in range(num_max_iterations):
        path_dict = {}
        for ant in ants:
            ant.reset(list(G.nodes)[0])
        for i in range(0, N):
            # since there are N cities, each ant will take exactly N iterations
            # to complete it's tour
            for ant in ants:
                ant.choose_next(G, N)

        # Each ant should've completed it's tour by now, else we don't care
        # Evaporate some pheromone
        for edge in G.edges():
            G.edges()[edge]['pheromone'] = (1-evaporation_rate) * \
                G.edges()[edge]['pheromone']

        # Add new pheromone
        for ant in ants:
            p = ant.get_path()
            if p in path_dict:
                path_dict[p] += 1
            else:
                path_dict[p] = 0
            ant.update_pheromone(G)
    
    return path_dict

class Ant(object):
    def __init__(self, start_points, PH=100, eps=0.1):
        # Places the ant at any of the given starting points randomly
        self.path = []
        self.path_length = 0
        # this is the pheromone that this ant will deposit over the length of its path
        self.PHEROMONE = PH
        #k = randint(0, start_points)
        self.path.append(start_points)  # this ant starts at initial node
        self.eps = eps 		# epsilon value to help discriminate between choosing randomly

    def reset(self, start_point):
        self.path = []
        #k = np.random.randint(0, num_start_points)
        self.path.append(start_point)
        self.path_length = 0

    def completed_tour(self, N):
        if len(self.path) == N:
            return True
        return False

    def choose_next(self, graph, N):    
        last_visited = self.path[-1]
        to_consider = []
        for neigbour in graph.neighbors(last_visited):
            if neigbour not in self.path:
                cost = graph.edges()[last_visited, neigbour]['pheromone']
                to_consider.append((cost, neigbour))

        if to_consider:
            to_eps = np.random.uniform(0, 1)
            if to_eps < self.eps:
                # Choose randomly
                k = np.random.randint(0, len(to_consider))
                self.path.append(to_consider[k][1])
            else:
                to_consider.sort()
                self.path.append(to_consider[0][1])
        elif not self.completed_tour(N):
            # am stuck since all current neibours are visited
            # move out randomly
            x = list(graph.neighbors(last_visited))
            if len(x) == 0:
                #print('Bad Luck')
                return
            t = np.random.randint(0, len(x))
            self.path.append(x[t])
        else:
            self.path.append(self.path[0])

        # update path length
        if last_visited != self.path[-1]:
            try:
                self.path_length = self.path_length + \
                    graph.edges()[(last_visited, self.path[-1])]['weight']
            except:
                pass
        else:
            # The code
            print('Shucks, Not an issue. But for better results try a more dense graph.')
            self.path_length += 0

    def update_pheromone(self, graph):
        for i in range(1, len(self.path)):
            u = self.path[i-1]
            v = self.path[i]
            try:
                graph.edges()[
                    (u, v)]['pheromone'] += self.PHEROMONE / self.path_length
            except Exception as e:
                print(u, v)

    def get_path(self):
        x = ""
        for i in self.path:
            x += i + ", "

        return x

def createGraph(listaNos):
    # Essa listaNos vem la do arquivo Runner.py aonde consegui importar o ACOSymple para pode usar a metaeuristica
    # com o grafo que ja foi gerado a partir da leitura do arquivo desejado
    graph = nx.DiGraph()  # Digrafo = Grafo Orientado

    print("Lista de Nos",listaNos)

    for no in (listaNos):  # criar grafo para usar na metaheuristica
        graph.add_node(no.getTipoLinha()) # adiciona um no ao novo grafo
        for pai in no.getPais():
            try:
                graph.add_node(pai.getTipoLinha())
                graph.add_edge(pai.getTipoLinha(), no.getTipoLinha())
            except (AttributeError):
                print("Ninguem", AttributeError)

    #nx.draw(graph, with_labels=True) #construe o grafo visualmente
    #plt.show() #exibe o grafo
    for i in range(1,10):
        main(num=1,evaporation_rate=1.0, graph_type=graph,num_iters=100, show=False, save=False)

def main(num=0, evaporation_rate=0.7, graph_type=None, num_iters=1000, show=True, save=True):
    print('For Experiment {}'.format(num))
    N = graph_type.number_of_nodes()

    # Initalize graph
    if not graph_type:
        G = nx.complete_graph(N)
    else:
        G = graph_type

    for edge in G.edges():
        G.edges()[edge]['weight'] = np.random.randint(5, 20) #add peso as arestas
        G.edges()[edge]['pheromone'] = 1 #add feromonio a aresta
        
    # Initialize ants
    ants = []
    for i in range(0, NUM_ANTS * N):
        ants.append(Ant(list(G.nodes)[0])) #cria formiga no ponto inicial do grafo

    pos = nx.spring_layout(G)
    # Perform ACO
    paths = solve_tsp(G, ants, N, num_max_iterations=num_iters,evaporation_rate=evaporation_rate)
    
    print(paths)
    converted = []
    for path in paths:
        p = tuple(map(lambda x: str(x.strip()), path.split(',')[:-1])) ##Error aqui
        converted.append((paths[path], p))
    converted.sort()
    top_path = converted[-1]
    print('Top Path = ', top_path[1], 'Confidence = ', top_path[0]/NUM_ANTS)

    edge_list = []
    for k in range(1, len(top_path[1])):
        edge_list.append((top_path[1][k-1], top_path[1][k]))

    for edge in G.edges():
        print(edge, G.edges()[edge]['weight'], G.edges()[edge]['pheromone'])

    labels = {}
    for node in G.nodes():
        labels[node] = node

    print(nx.to_numpy_matrix(G))
    plt.figure()

    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=edge_list, edge_color='b')
    nx.draw_networkx_labels(G, pos, labels, font_size=16)

    if show:
        plt.show()
    if save:
        plt.savefig('Figure_{}'.format(num))

    return top_path[0]


if __name__ == '__main__':
    # global NUM_ANTS, N
    expt = 0

    # Variation with number of ants:
    X = []
    Y = []
    for i in range(100, 110, 5):
        NUM_ANTS = i
        q = main(expt, show=True, save=False)
        plt.close()
        expt += 1
        X.append(i)
        Y.append(q)
    plt.figure()
    plt.plot(X, Y)
    plt.show()

    # Variation with evaporation rate:
    NUM_ANTS = 100
    X = []
    Y = []
    for i in np.linspace(0.1, 0.9, 9):
            q = main(expt, evaporation_rate=i, show=False, save=False)
            plt.close()
            expt+=1
            X.append(i)
            Y.append(q)
    plt.figure()
    plt.plot(X, Y)
    plt.show()

    # Variation with number of cities:
    X = []
    Y = []
    for i in range(5, 10):
            N = i
            q = main(expt, show=False, save=False)
            plt.close()
            expt+=1
            X.append(i)
            Y.append(q)
    plt.figure()
    plt.plot(X, Y)
    plt.show()

    # variation with sparsity
    N = 7
    X = []
    Y = []
    for i in range(N+1, N+9):
            G = nx.gnm_random_graph(N, i)
            q = main(expt, graph_type=G, show=False, save=False)
            plt.close()
            expt+=1
            X.append(i)
            Y.append(q)
    plt.figure()
    plt.plot(X, Y)
    plt.show()

    # variation with number of iterations
    N = 5
    X = []
    Y = []
    for i in range(50, 200, 15):
            q = main(expt, num_iters=i, show=False, save=False)
            plt.close()
            expt+=1
            X.append(i)
            Y.append(q)
    plt.figure()
    plt.plot(X, Y)
    plt.show()

