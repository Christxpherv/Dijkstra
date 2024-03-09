# import the Dijkstra algorithm
from PathTime import Dijkstra

class SchedulePathFinder:
  
  def __init__(self, graph, dijkstra):
      self.graph = graph
      self.dijkstra = dijkstra

  def find_shortest_path_for_schedule(self, schedule):
      # initialize the total time and path
      totalTime = 0
      path = []

      # work in progress
      return None