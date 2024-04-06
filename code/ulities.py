# this file has functions that get name of city, famous place in each city
import time


def getPath(path):
    if not path:
        print("Path is empty.")
        return
    
    print("Path:")
    for city in path:
        print(city)
        time.sleep(30)  # Pause for 30 seconds between printing each city

def printFamousPlace(city_name):
    from dataFamousPlace import famousPlace

    for city in famousPlace:
        if city['name'] == city_name:
            print(f"Famous places in {city['name']}:\n")
            for spot in city['tourist_spots']:
                print(f"Tourist spot: {spot['name']}")
                print(f"Address: {spot['address']}")
                print(f"Description: {spot['description']}")
                print('----------------------------------------------------------------')
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

#test

# printFamousPlace
# current_city = input("Current city: ")
# printFamousPlace(current_city)

# goBack
#path = ["Ha Noi", "Hai Phong", "Da Nang", "Nha Trang", "Ho Chi Minh"]
#current_city = "Da Nang"
#previous_city = goBack(path, current_city)
#getPath(path)
