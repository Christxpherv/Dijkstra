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
      
      # iterate through the unvisited nodes until all nodes are visited
      while unvisited:
          # find the unvisited node with the shortest time
          current_node_name = min(unvisited, key=lambda node: shortest_times[node])
          current_node = self.graph.nodes[current_node_name]

          # break the loop if the current node is unreachable or the end node is reached
          if shortest_times[current_node_name] == float('infinity') or current_node_name == end_name:
              break
          # iterate through the adjacent nodes of the current node
          for adjacent, (edgeDistance, edgeTime) in current_node.adjacents.items():
              # add the edge time to the shortest time of the current node
              time = shortest_times[current_node_name] + edgeTime
             
              # update the shortest time of the adjacent node if the new time is shorter
              if time < shortest_times[adjacent.name]:
                  shortest_times[adjacent.name] = time
          # remove the current node from the unvisited set
          unvisited.remove(current_node_name)
      # return the shortest time of the end node if it is reachable, else return None
      return shortest_times[end_name] if shortest_times[end_name] != float('infinity') else None
