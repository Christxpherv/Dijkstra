# implement the Dijkstra algorithm to find the shortest path between two nodes in the graph
class Dijkstra:
  # initialize method that requires a graph of nodes
  def __init__(self, graph):
      self.graph = graph
  
  # find the shortest path between two nodes in the graph using the Dijkstra algorithm
  def shortestPath(self, start_name, end_name):
      # create a dictionary of nodes with their shortest times, initially set to infinity
      shortest_times = {node: float('infinity') for node in self.graph.nodes}
      # set the shortest time of the starting node to 0
      shortest_times[start_name] = 0
      # set of unvisited nodes
      unvisited = set(self.graph.nodes.keys())

      return None
