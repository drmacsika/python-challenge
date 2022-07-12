from src.models import Example


def count_calls() -> dict:
    """Count the number of calls for this specific route. To count the calls
    a new Example document is created in the DB.

    Returns: dict with number of calls for this specific route
    """
    Example().save()
    called_times = Example.objects.count()
    return {"number_of_calls": called_times}
