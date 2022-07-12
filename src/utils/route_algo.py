from collections import defaultdict
from typing import List


class CityRoute:
    def __init__(self):
        """
        self.routes is a dict of all possible next routes
        e.g. {'Munich': ['Kinganru', 'Facenianorth', 'SantaTiesrie', 'Mitling'], ...}

        self.hours has all the hours between two cities,
        with the two cities in a tuple, as the key
        e.g. {('Munich', 'Kinganru'): 3, ('Munich', 'Facenianorth'): 7, ...}
        """
        self.routes = defaultdict(list)
        self.hours = {}

    def add_route(self, from_city, to_city, hour):
        # The hours between cities are bi-directional
        self.routes[from_city].append(to_city)
        self.routes[to_city].append(from_city)
        self.hours[(from_city, to_city)] = hour
        self.hours[(to_city, from_city)] = hour


def get_shortest_route(city_route: CityRoute, initial: str, last: str) -> List[str]:
    """
    Using djikstra's algorithm,
    get the shortest route as a dict of nodes
    whose value is a tuple of (previous node, hour)
    """
    shortest_routes = {initial: (None, 0)}
    current_city = initial
    visited = set()

    while current_city != last:
        visited.add(current_city)
        destinations = city_route.routes[current_city]
        hour_to_current_city = shortest_routes[current_city][1]

        for next_city in destinations:
            hour = city_route.hours[(current_city, next_city)] + hour_to_current_city
            if next_city not in shortest_routes:
                shortest_routes[next_city] = (current_city, hour)
            else:
                current_shortest_hour = shortest_routes[next_city][1]
                if current_shortest_hour > hour:
                    shortest_routes[next_city] = (current_city, hour)

        next_destinations = {
            city: shortest_routes[city]
            for city in shortest_routes
            if city not in visited
        }
        if not next_destinations:
            return "Route cannot be processed!"

        # next city is the destination with the lowest hour
        current_city = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest routes
    travelled_routes = []
    while current_city is not None:
        travelled_routes.append(current_city)
        next_city = shortest_routes[current_city][0]
        current_city = next_city

    # Reverse travelled_routes
    travelled_routes = travelled_routes[::-1]
    return travelled_routes


def get_city_pair_and_distance(route: str) -> tuple:
    """
    Get the city pair from the list of routes.
    """
    hour = int(route.split(":")[1].strip())
    cities = route.split(":")[0].strip().split("-")
    return (cities[0].strip(), cities[1].strip(), hour)


def get_routes_from_list(list_of_routes: List[str]) -> List[str]:
    """
    Get the routes from the list of routes.
    """
    distinct_city = set()
    routes = set()

    for route in list_of_routes:
        distinct_city.add(route.split(":")[0].strip().split("-")[0].strip())

    for city in distinct_city:
        routes.add((city, city, 0))

    for route in list_of_routes:
        routes.add(get_city_pair_and_distance(route))

    return list(routes)


def get_places_to_travel(destinations: List[str], city_route: CityRoute) -> List[str]:
    """
    Gets the shortest route from destinations
    """
    places_to_travel, calculated_routes = [], []

    for destination in range(len(destinations) - 1):
        if destination == 0:
            calculated_routes.append(
                get_shortest_route(city_route, "Munich", destinations[destination])
            )
            calculated_routes.append(
                get_shortest_route(
                    city_route, destinations[destination], destinations[destination + 1]
                )
            )
        else:
            calculated_routes.append(
                get_shortest_route(
                    city_route, destinations[destination], destinations[destination + 1]
                )
            )

    for calculated_route in range(len(calculated_routes)):
        if calculated_route == 0:
            places_to_travel = [route for route in calculated_routes[calculated_route]]
        else:
            calculated_routes[calculated_route].pop(0)
            for route in calculated_routes[calculated_route]:
                places_to_travel.append(route)

    return places_to_travel


def get_most_frequent(items: list, type_of_items: str) -> List[str]:
    """
    Get the most frequent destinations or trips.
    """
    store = {}

    if type_of_items == "trips":
        for item in items:
            if item["name"] in store:
                store[item["name"]] = store[item["name"]] + 1
            else:
                store[item["name"]] = 1

    elif type_of_items == "destinations":
        frequent_destinations = [d for item in items for d in item["destinations"]]

        for frequent_destination in frequent_destinations:
            if frequent_destination in store:
                store[frequent_destination] = store[frequent_destination] + 1
            else:
                store[frequent_destination] = 1
    else:
        print("Error: type_of_items must be 'trips' or 'destinations'")

    return [
        max_item
        for max_item in store
        if store[max_item] == max(set(i for i in store.values()))
    ]
