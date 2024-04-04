# this file has functions that get name of city, famous place in each city
def getPath(path):
    # viết hàm ở đây
    # path là mảng, yêu cầu là lần lượt in ra các thành phố mà thời gian in cách nhau khoảng lâu 30s
    print("Path")


def printFamousPlace(city):
     #viết hàm ở đây
    print("Famous place")

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
#path = ["Ha Noi", "Hai Phong", "Da Nang", "Nha Trang", "Ho Chi Minh"]
#current_city = "Da Nang"
#previous_city = goBack(path, current_city)
