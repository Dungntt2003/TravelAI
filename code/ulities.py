# this file has functions that get name of city, famous place in each city
import time
from dataFamousPlace import famousPlace
def getPath(path):
    if not path:
        print("Path is empty.")
        return
    
    print(f"Path: {path}")
    for city in path:
        # index_current_city = path.index(city)
        print(city)
        printFamousPlace(city)
        # if index_current_city > 0:
        #     choice = input("Do you want to go to the previous city : y/n?")
        #     if choice == 'y':
        #         previous_city = goBack(path,city)
        #         print(previous_city)
        #         printFamousPlace(previous_city)
        #         time.sleep(5)
        #         print(city)
        #         printFamousPlace(city)

        

def printFamousPlace(city_name):
    for city in famousPlace:
        if city['name'] == city_name:
            print(f"Famous places in {city['name']}:\n")
            for spot in city['tourist_spots']:
                print(f"Tourist spot: {spot['name']}")
                print(f"Address: {spot['address']}")
                print(f"Description: {spot['description']}")
                print('----------------------------------------------------------------')
                time.sleep(5)
            return

    print(f"No information found about {city_name}.")


def goBack(path, city):
    if not path:
        print("There is no previous path.")
        return None

    try:
        index_current_city = path.index(city)
        if index_current_city > 0:
            previous_city = path[index_current_city - 1]
            print(f"Go back to the previous city: {previous_city}")
            return previous_city
        else:
            print("This is the first city on the path.")
            return None
    except ValueError:
        print(f"The city {city} is not found in the path.")
        return None

path = ["Ha Noi", "Hai Phong", "Da Nang", "Nha Trang", "TP Ho Chi Minh"]
getPath(path)
