# Shortest Path Routing Python Challenge

## Algorithm Used

The challenge centered primarily on finding the shortest route between two destinations.

To get the shortest route between two destinations, we need to use a greedy algorithm that can be used to find the shortest path between two positive nodes on a graph whose edges have positive weights.

For this challenge I decided to use the Djikstra's Algorithm for finding the shortest paths.

Not only because Djikstra's Algorithm is popularly considered to be the best in handling tasks revolving around finding the shortest path, there are peculiar requirements between the challenge's instruction and the core properties of Djikstra's algorithm.

Here are my reasons for choosing this algorithm based on the instructions from this challenge:

- The starting point is always Munich. There is no cost to travel to the current city (Ex. Munich to Munich the travel time is 0).

When traversing nodes on a graph, the cost of traversing the same node is usually 0. This statement holds true for Djikstra's algorithm.

- The travel time is given in hours, and it's always integer.

Djikstra's Algorithm is intended to be used with positive weighted edges. This is because the weights have to be added to find the shortest path.

When a node is marked as "visited", the current path taken to get to that node is marked as the shortest path to reach that node. The presence of negative weights can alter this if the total weight can be decremented after this step has occurred.

In this challenge, we are told that the weighted edge in in hours. Since hours in time are the weighted edges for the challenge, it is safe to consider that we cannot have a negative weighted edge.

- The time from `place A` to `place B` and `place B` to `place A` is the same.

This is not specific to Djikstra's algorithm rather a property of a type of graph. What this instruction essentially depict is that the graph is undirected meaning that the weighted edge is the same if we traverse from node A to B or from B to A.

## Decisions Made

Rather than run the algorithm from the starting point "Munich" to whatever the last item on the list will be, I decided to run the algorithm specifically between two nodes at a time.

This is because last instruction:

_The destinations order is important! Is totally fine (and sometimes expected) to visit some places before they being the target destination, it doesn't exclude them for the destination list. (Ex: for given destinations: `Munchen` -> `Kinganru` -> `SantaTiesrie` the places to travel can be: `Munchen` -> **SantaTiesrie** -> `Kinganru` -> `SantaTiesrie`)_

requires that we do not lose the order in which the penguins can travel.

If I should run the algorithm from "Munich" to the last destination on the list, there is a chance that it will not have one or more of the preceding destinations in the route.

## Code Additions

- src/models/**trip.py:** A model file named trip containing a single mongo db ODM model Named Trip. This model defines four fields: name, destinations, business, places_to_travel

- src/routes/**trip_routes/calculate.py** and src/routes/**trip_routes/business_trips.py:** This route contains the required method function definition required to perform the action specified in the project's instruction.

- src/routes/add_routes.py: I added two new endpoints to the project for the above requirement. The /calculate endpoint only allows POST method and the /business-trips endpoint only allows GET method.

- src/**utils/route_algo.py:** This files contains some special utility function required in the project including the function for the Djikstra's algorithm, formatting, and other project house keeping tasks.

# Packages Added

Dev Requirements

- black: the black package was used to format the codes to maintain consistency in code style across the python files in the project.
- requests: the requests package is used to test the example response in example.py
- marshmallow: Marshmallow is a python package that is used for data serialization and validation. I used it in the project to generate automatic validations for the expected data in the POST request. This is more efficient than writing my own validator as it not only checks for the presence of data, it checks for the types as well as the types within types e.g validating List(str).

# How to run

A base API with a DB connection already exist at `docker-compose.yml`. You just need to make changes on the python files.

To run, execute the following command:
`docker-compose rm -f; docker-compose -f docker-compose.yml up --build --force-recreate`
(It will clean up existing containers and force to be recreated)

To test your API you can check `http://127.0.0.1:8001/` on your browser.

To run the example, run the script: `example.py` (`requests` lib is necessary)

## How to test

Install dependencies:

1. Create a virtual env and activate it: `python3 -m venv env; source env/bin/activate`
2. Install dependencies: `pip install -r requirements.txt -r dev-requirements.txt`
3. Run tests: `pytest test/`
