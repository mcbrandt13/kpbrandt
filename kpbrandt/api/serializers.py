from rest_framework import serializers


def state_validator(state_abbrev):
    """
    Validate the state field value.
    :param state_abbrev: The value of the state field, i.e. 'CA', 'ca'.
    """
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if state_abbrev.upper() not in states:
        raise serializers.ValidationError("{0} is not a valid US state. "
                                          "Please provide a valid state "
                                          "abbreviation.".format(state_abbrev))


class ApiWeatherSerializer(serializers.Serializer):
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True, validators=[state_validator])


class SimpleMsgSerializer(serializers.Serializer):
    msg = serializers.CharField()


class ApiWeatherResponseSerializer(serializers.Serializer):
    Location = serializers.CharField()
    Conditions = serializers.CharField()
    Temperature = serializers.CharField()
    Forecast = serializers.CharField()


class GenericSerializer(serializers.Serializer):
    """
    A generic serializer that serializes a single field dynamically. Used for
    error responses to match DRF's validation error responses.
    """

    def __init__(self, *args, **kwargs):
        field = kwargs.pop('field')
        super(GenericSerializer, self).__init__(*args, **kwargs)
        self.fields[field] = serializers.ListField()
