from .dataDis import nameOfCity
from .dataDis import flight_distances
start_city = input("Start city: ")
dest_city = input("Choose dest city : ")
index = -1
flight_distances_dict = {}
try:
    index = nameOfCity.index(dest_city)
    numberOfCities = 30
    for i in range(numberOfCities):
        city = nameOfCity[i]
        distance = flight_distances[i][nameOfCity.index(dest_city)]
        flight_distances_dict[city] = distance
except  ValueError:
    print(f"{dest_city} not found in list of cities")


