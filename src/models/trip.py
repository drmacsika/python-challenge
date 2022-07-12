from mongoengine import BooleanField, Document, ListField, StringField


class Trip(Document):
    name = StringField(max_length=255, required=True)
    destinations = ListField(StringField(max_length=255), required=True)
    business = BooleanField(default=False)
    places_to_travel = ListField(StringField(max_length=255), required=True)

    def __repr__(self):
        return "<Trip %r>" % (self.name)
