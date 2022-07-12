from json import dumps, loads

from flask import jsonify, request
from marshmallow import ValidationError
from src.models import Trip
from src.utils import CityRoute, TripSchema, get_places_to_travel, get_routes_from_list


def calculate() -> dict:
    """
    Find all places that must be visited
    in order to have a minimum travel time for a given input.

    Returns: list of places to travel with the shortest path
    """
    try:
        body = TripSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 405

    distances = body["distances"]
    destinations = body["destinations"]
    routes = get_routes_from_list(distances)
    city_route = CityRoute()
    for route in routes:
        city_route.add_route(*route)

    places_to_travel = get_places_to_travel(destinations, city_route)

    calculate_trip = Trip(
        name=body["name"],
        destinations=destinations,
        business=body["business"],
        places_to_travel=places_to_travel,
    )
    calculate_trip.save()
    return {"places_to_travel": places_to_travel}, 201
