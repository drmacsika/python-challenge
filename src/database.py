from mongoengine import connect


def connect_to_database(db_uri: str) -> None:
    """Connects to a mongo instance.

    Args:
        db_uri: target uri following the pattern:
            "mongodb://<username>:<password>@<host>:<port>/<database>"
    """
    connect(host=db_uri + "?authSource=admin")
