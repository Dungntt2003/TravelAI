from Astar import Graph
from dataDis import road_distances
from model import start_city
from model import dest_city




graph1 = Graph(road_distances)
path = graph1.a_star_algorithm(start_city, dest_city)
