import os

from censusgeocode import CensusGeocode

CLIENT = None


def get_client():
    """
    Gets the Census Geocode API client.

    :return: censusgeocode.client
    """

    return CensusGeocode()


def validate_address(client, info):
    """
    Takes address information and returns validation on that address from the
    Census Geocode API. For documentation, please check this link:
    https://github.com/fitnr/censusgeocode#census-geocode

    :param client: the Census Geocode API client
    :param dictionary info: A nested dictionary of strings containing
        information about a particular address

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """

    # Make sure the fields are there.
    assert len(info) == 4

    return client.address(
        street=info[0],
        city=info[1],
        state=info[2],
        zip=info[3],
        returntype="locations",
    )
