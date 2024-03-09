# import required classes
from Graph import Graph
from PathFinder import SchedulePathFinder
from PathTime import Dijkstra

# create a function to create a display for the information (path, time, and total time)
def display_path_and_time(schedule_path, total_time, schedule_number):
  print(f"{schedule_number}:")
  for start, end, time in schedule_path:
    print(f"From {start} to {end}: {time} min")
  print(f"Total walking time: {total_time} min")
  print("-" * 30)

# create a graph of buildings and their distances
memphisCampus = Graph()
