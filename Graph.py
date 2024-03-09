# import the Node class to create a graph of nodes that represent locations on campus
from Node import Node

# defines a graph of nodes that represent locations on campus while providing a method for adding nodes and edges to the graph
class Graph:
  
  # initialize method that creates an empty dictionary of nodes
  def __init__(self):
      self.nodes = {} # dictionary of objects (nodes)

  # adds nodes to the current graph, one by one 
  def addNode(self, name):
      # call the Node class to create a new node object
      node = Node(name)
      # add the node to the dictionary of nodes
      self.nodes[name] = node
      return node
  
  # adds edges to the current graph, connecting two nodes together and specifying their distance and time apart from each other
  def addEdge(self, node1, node2, distance, time):
      # checks if both nodes are not included in the dictionary of nodes and adds the nodes if they are missing, else move on
      if node1 not in self.nodes:
          self.addNode(node1)
      if node2 not in self.nodes:
          self.addNode(node2)
      
      # connect the two nodes together by adding the adjacent nodes to one another
      self.nodes[node1].addAdjacent(self.nodes[node2], distance, time)
      self.nodes[node2].addAdjacent(self.nodes[node1], distance, time)

  # display the nodes and their adjacent nodes along with their distance and time apart
  def display(self):
    for node in self.nodes.values():
      print(node.name, ":", ", ".join([f"{adj.name}({dist} ft, {time} min)" for adj, (dist, time) in node.adjacents.items()]))