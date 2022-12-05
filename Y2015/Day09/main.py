import itertools

from Helpers.GetInput import *

from itertools import permutations

def total_distance(route, distances):
    distance = 0
    for i in range(len(route) - 1):
        distance += distances[route[i]][route[i+1]]
    return distance

def create_distance_matrix(distances):
    # Create a list of all locations
    locations = []
    for distance in distances:
        location1, location2 = distance.split(" to ")[0], distance.split(" to ")[1].split(" = ")[0]
        if location1 not in locations:
            locations.append(location1)
        if location2 not in locations:
            locations.append(location2)

    # Create a distance matrix with the maximum possible distance value
    num_locations = len(locations)
    max_distance = num_locations * num_locations
    matrix = [[max_distance for _ in range(num_locations)] for _ in range(num_locations)]

    # Set the entries on the diagonal to zero
    for i in range(num_locations):
        matrix[i][i] = 0

    # Populate the distance matrix with the specified distance values
    for distance in distances:
        location1, location2, distance = distance.split(" to ")[0], distance.split(" to ")[1].split(" = ")[0], int(distance.split(" to ")[1].split(" = ")[1])
        i, j = locations.index(location1), locations.index(location2)
        matrix[i][j] = distance
        matrix[j][i] = distance

    for x in matrix:
        print(x)
    return matrix


def Day9():
    data = get_input_split_lines(2015, "09")
    for x in range(len(data)):
        data[x] = data[x].replace("\n", "")
    matrix = create_distance_matrix(data)
    routes = list(itertools.permutations(range(8)))

    # calculate the total distance for each route
    distances = [total_distance(route, matrix) for route in routes]

    # find the shortest routes
    print("Shortest route:", routes[distances.index(min(distances))])
    print("Distance:", min(distances))

    # print the shortest route and its distance
    print("Shortest route:", routes[distances.index(max(distances))])
    print("Distance:", max(distances))


if __name__ == "__main__":
    Day9()
