# Python challenge

# Introduction

Our penguins love to travel. There are two specific situations when they travel most:

- to see new places on vacations
- to visit clients

In order to help them, we are developing a platform to minimize the travel time, so they can spend more time in the final destination.

Your job here, as backend developer, is to extend our basic API adding two routes:

1. A route to find all places that must be visited in order to have a minimum travel time for a given input. (route: `/calculate`).
   Notes:

   - The starting point is always Munich.
   - There is no cost to travel to the current city (Ex. Munich to Munich the travel time is 0).
   - The travel time is given in hours, and it's always integer.
   - The time from `place A` to `place B` and `place B` to `place A` is the same.
   - Just consider one way trip: ignore the return time to Munich.
   - The destinations order is important! Is totally fine (and sometimes expected) to visit some places before they being the target destination, it doesn't exclude them for the destination list. (Ex: for given destinations: `Munchen` -> `Kinganru` -> `SantaTiesrie` the places to travel can be: `Munchen` -> **SantaTiesrie** -> `Kinganru` -> `SantaTiesrie`)

2. A route to get all consulted business trips information, so we can think in new strategies to help our employees. (route `/business-trips`)

# Routes documentation

### `/calculate`: only allows POST and expects a JSON as input.

### Payload:

- `name`: str. Penguin name.
- `destinations`: List[str]. List of destinations.
- `business`: bool. Indicates if it is a business trip. `true` for "business" trip, `false` for "casual" trip.
- `distances`: List[str]. List with distances between places.

Returns:

- `places_to_travel`: List[str]. List with all places to visit.

Example:

`POST`:

```json
{
  "name": "Alanto",
  "destinations": ["Kinganru", "Facenianorth", "SantaTiesrie"],
  "business": true,
  "distances": [
    "Munich - Munich: 0",
    "Munich - Kinganru: 3",
    "Munich - Facenianorth: 7",
    "Munich - SantaTiesrie: 4",
    "Munich - Mitling: 1",
    "Kinganru - Facenianorth: 2",
    "Kinganru - SantaTiesrie: 1",
    "Kinganru - Mitling: 1",
    "Facenianorth - SantaTiesrie: 5",
    "Facenianorth - Mitling:  3",
    "SantaTiesrie - Mitling: 2"
  ]
}
```

`Returns`:

```json
{
  "places_to_travel": [
    "Munich",
    "Mitling",
    "Kinganru",
    "Facenianorth",
    "Kinganru",
    "SantaTiesrie"
  ]
}
```

For this example the distances are:

- Munich to Munich: 0 hour
- Munich to Kinganru: 3 hours
- Munich to Facenianorth: 7 hours
- Munich to SantaTiesrie: 4 hours
- Munich to Mitling: 1 hour
- Kinganru to Facenianorth: 2 hours
- Kinganru to SantaTiesrie: 1 hour
- Kinganru to Mitling: 1 hour
- Facenianorth to SantaTiesrie: 5 hours
- Facenianorth to Mitling: 3 hours
- SantaTiesrie to Mitling: 2 hours

### `/business-trips`: only allows GET and expects a JSON as result.

### Expected result:

- `penguins_with_most_trips`: List[str]. Penguins with most business trips. If more than one penguin have the same number of trips, all must be on the list.
- `most_visited_places`: List[str]. Places that most appear as destinations (places between destinations don't count!). If more than one place appear on the list, all of them must be returned.
- `total_business_trips`: int. Number of business trips.

Example:
If the given example for `calculate` run 3 times, the business route should returns:

`Returns`:

```json
{
  "penguins_with_most_trips": ["Alanto"],
  "most_visited_places": ["Kinganru", "Facenianorth", "SantaTiesrie"],
  "total_business_trips": 3
}
```

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

# Deliverables

- A README file explaining any modifications, decisions and algorithms used.
- This entire folder as zip file.

# Technologies

- Feel free to use any 3rd-party library, just remember to justify the decision.
- The code must be compatible with python3.8
- The API must run using Flask (already set on the base source code)
- The database must be MongoDB (already set on the base source code)

Note: to test the docker-compose will be invoked, so guarantee it works.

Happy coding!
