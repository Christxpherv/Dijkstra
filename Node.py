# defines nodes which represent locations on campus while providing a method for connecting adjacent nodes to each other using their distance and time apart
class Node:
  # initialize method that requires the location's name
  def __init__(self, name):
    self.name = name
    # dictionary of adjacent nodes (locations located nearby)
    self.adjacents = {}

  # add an adjacent node to the current node that specifies their distance and time apart from each other
  def addAdjacent(self, node, distance, time):
    self.adjacents[node] = (distance, time)
