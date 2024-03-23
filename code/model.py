import numpy as np

nameOfCity = ["Tay Ninh", "Vung Tau", "Ben Tre", "Phu Quoc", "TP Ho Chi Minh", "Nha Trang", "Dong Thap", "Can Tho", "Soc Trang", "Ca Mau"]

# flight distances between 10 cities
flight_distances = np.array([
    [0,150,125,125,80,352,105,154,194,259],
    [150,0,85,346,73,304,158,177,155,254],
    [125,85,0,260,71,380,78,90,83,176],
    [125,346,260,0,296,607,187,174,230,183],
    [80,73,71,296,0,321,110,145,153,243],
    [352,304,380,607,321,0,426,463,456,555],
    [105,158,78,187,110,426,0,50,104,159],
    [154,177,90,174,145,463,50,0,69,109],
    [194,155,83,230,153,456,104,69,0,100],
    [259,254,176,183,243,555,159,109,100,0]
])

# road distances between 10 cities
road_distances = np.array([
    [0,185,173,418,88,496,169,246,277,357],
    [185,0,190,476,96,384,230,261,292,379],
    [173,190,0,379,108,503,133,142,121,255],
    [418,476,379,0,477,783,226,241,276,248],
    [88,96,108,477,0,402,148,155,212,293],
    [496,384,503,783,402,0,546,553,609,691],
    [169,230,133,226,148,546,0,77,133,194],
    [246,261,142,241,155,553,77,0,84,144],
    [277,292,121,276,212,609,133,84,0,114],
    [357,379,255,248,293,691,194,144,114,0]
])
dest_city = input("Choose dest city : ")
index = -1
flight_distances_dict = {}
try:
    index = nameOfCity.index(dest_city)
    numberOfCities = 10
    for i in range(numberOfCities):
        city = nameOfCity[i]
        distance = flight_distances[i][nameOfCity.index(dest_city)]
        flight_distances_dict[city] = distance
except  ValueError:
    print(f"{dest_city} not found in list of cities")


