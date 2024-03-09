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

      # iterate through the schedule to find the shortest path between each pair of buildings
      for i in range(len(schedule) - 1):
          # set the starting building to i
          startBuilding = schedule[i]
          # set the ending building to the one after the starting building
          endBuilding = schedule[i + 1]

          # find the shortest time between the starting and ending buildings using the Dijkstra algorithm
          time = self.dijkstra.shortestPath(startBuilding, endBuilding)
          if time is None:
              print(f"No path found between {startBuilding} and {endBuilding}.")
              return None
          # add the time to the total time and append the path to the list
          totalTime += time
          path.append((startBuilding, endBuilding, time))

      return path, totalTime
