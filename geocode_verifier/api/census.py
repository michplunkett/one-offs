import os

import census


def get_client():
    """
    Gets the census API client.

    :return: census.Census the Census API client.
    """
    key = os.getenv("CENSUS_API_KEY")
    return census.Census(key)


def validate_address(address_info, client):
    """
    Takes address information and returns validation on that address from the
    Google Maps API. For documentation, please check this link:
    https://developers.google.com/maps/documentation/address-validation/requests-validate-address

    :param dictionary address_info: A nested dictionary of strings containing
        information about a particular address
    :param googlemaps.Client client: The client that will be used to make the
        API call.

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """
