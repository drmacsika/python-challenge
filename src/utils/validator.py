from marshmallow import Schema, ValidationError, fields


class TripSchema(Schema):
    name = fields.String(required=True)
    destinations = fields.List(fields.String(), required=True)
    business = fields.Boolean(required=True)
    distances = fields.List(fields.String(), required=True)
