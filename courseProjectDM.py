import networkx as nx 
import matplotlib.pyplot as plt


def input_graph() -> nx.DiGraph:
	graph = nx.DiGraph()
	n, m = map(int, input().split())
	for i in range(m):
		node_from, node_to, weight = map(int, input().split())
		node_to -= 1
		node_from -= 1
		graph.add_nodes_from([node_from, node_to])
		graph.add_edge(node_from, node_to, weight = weight)
	return graph


def find_path(graph: nx.DiGraph, node1, node2):
	labels = dict()
	for node in graph.nodes:
		labels[node] = node + 1
	s = node1 - 1
	v = node2 - 1
	predecessors, _ = nx.floyd_warshall_predecessor_and_distance(graph)
	shortest_path_s_v = nx.reconstruct_path(s, v, predecessors)
	edges = [(a,b) for a,b in zip(shortest_path_s_v, shortest_path_s_v[1:])]
	weights = nx.get_edge_attributes(graph, 'weight')
	smallest_weight = min(weights)
	pos = nx.circular_layout(graph)
	nx.draw(graph, pos=pos, with_labels=True, labels=labels)
	nx.draw_networkx_edges(graph, pos=pos, edgelist=edges, edge_color="r", width=1)
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)
	print("Минимальный поток из ", node1, " в ", node2, " равен: ", smallest_weight[1])
	plt.show()


def main():
	g = input_graph()
	print("Введите точку истока и стока для нахождения минимального потока: ")
	node1, node2 = map(int, input().split())
	find_path(g, node1, node2)


if __name__ == "__main__":
	main()
