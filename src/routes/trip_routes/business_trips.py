from src.models import Trip
from src.utils import get_most_frequent


def business_trips() -> dict:
    """
    Get all business trips information

    Returns: An object displaying the penguins with most trips,
    A list of most visited places
    The total business trips
    """
    trips = Trip.objects()
    penguins_with_most_trip = get_most_frequent(trips, "trips")
    most_visited_places = get_most_frequent(trips, "destinations")
    total_business_trips = len([i for i in trips if i.business == True])

    return {
        "penguins_with_most_trips": penguins_with_most_trip,
        "most_visited_places": most_visited_places,
        "total_business_trips": total_business_trips,
    }, 201
