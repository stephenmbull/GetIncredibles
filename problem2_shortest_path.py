#!/usr/bin/python

from __future__ import print_function  # bring the print function from Python 3 into Python 2.6+
import csv

def shortest_path_shortcut(fname):
  """
  Knowing what the data looks like and its pre-sorted order, we only need to
  find the route with the longest distance and just start from the next route,
  thereby never travelling the longest section (and thus finding the shortest 
  path by default).
  """
  print("Shortest path shortcut.")
  city_routes = []

  with open(fname, 'r') as fp:
    reader = csv.reader(fp, delimiter=' ')

    longest_distance = 0
    longest_route = -1
    for row in reader:
      distance = int(row[4])
      city_routes.append([str(row[0]).strip(), str(row[2]).strip(), distance])
      if distance > longest_distance:
        longest_distance = distance
        longest_route = len(city_routes)-1

  print("  Longest route:",city_routes[longest_route][0],"to",city_routes[longest_route][1],longest_distance)
  print("  Start at",city_routes[longest_route][1],"to avoid the longest distance!\n")
  start_idx = 0
  end_idx = longest_route
  for i in range(len(city_routes)):
    if (city_routes[longest_route][1] == city_routes[i][0]):
      start_idx = i
      break
  #print("Starting route:",city_routes[start_idx],"\n")

  return city_routes, start_idx, end_idx


def shortest_path(city_routes):
  """
  Finds shortest distance and path between all cities and outputs results to 
  terminal.

  Quick and dirty solution cycles through all possible paths (operates in O(n)
  access time) to find the shortest, and assumes the incoming (file) list is not
  already sorted. This can certainly be made more efficient for longer, more 
  complicated routes!
  """
  print("Searching for shortest path.")
  shortest_path = {'route': [], 'distance': -1}
  num_paths = len(city_routes)

  i = 0
  for j, route in enumerate(city_routes):
    distance = 0

    n = 0
    visit_count = 0
    this_path = []

    # Loop through to find next start route and sum route distances
    while True:
      n += 1
      if (n==len(city_routes)):
        n = 0

      if (city_routes[i]['end'] == city_routes[n]['start']):
        visit_count += 1
        if (visit_count==len(city_routes)):
          break;  # all routes have been visited for the i'th start route

        if (visit_count==1):
          this_path.append(city_routes[n]['start'])
          #print("\nStarting from:",city_routes[n]['start'])
        this_path.append(city_routes[n]['end'])

        i += 1
        if (i==len(city_routes)):
          i = 0

        distance += city_routes[n]['distance']

    #print(" ",this_path,"distance:",distance)
    if (shortest_path['distance']==-1 or distance<shortest_path['distance']):
      shortest_path['route'] = this_path
      shortest_path['distance'] = distance

  print("\nShortest path is",shortest_path['route'][0],"->",shortest_path['route'][1],"->",shortest_path['route'][2],"->",shortest_path['route'][3],"=",shortest_path['distance'])


def read_cities(fname):
  """
  Reads file of city routes and distances.

  @return:  a list of city routes and distances.
  """
  print("Reading city routes file.")
  city_routes = []

  with open(fname, 'r') as fp:
    reader = csv.reader(fp, delimiter=' ')

    for row in reader:
      city_routes.append({'start': str(row[0]).strip(), 'end': str(row[2]).strip(), 'distance': int(row[4])})

  return city_routes


# ------------------------------------------------------------------------------


if __name__ == '__main__':
  import argparse, sys, traceback
  
  try:
    # Check args first before calling main()
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile_cities', default='./q2.txt')
    args = parser.parse_args()

    #shortest_path_shortcut(args.infile_cities)
    shortest_path(read_cities(args.infile_cities))

  except:
    print('Exception traceback:', traceback.format_exc())
    sys.exit(-1)
