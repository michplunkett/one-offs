import os

import googlemaps


def get_client():
    """
    Gets the GoogleMaps API client.

    :return: googlemaps.Client
    """
    key = os.getenv("GOOGLE_MAPS_API_KEY")
    return googlemaps.Client(key)


def validate_address(address_info, client):
    """"
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

    # Assert that the necessary fields are there.
    assert bool(address_info["address"])
    assert bool(address_info["address"]["regionCode"])
    assert bool(address_info["address"]["addressLines"])

    # Enable Coding Accuracy Support System
    address_info["enableUspsCass"] = True

    return client.addressvalidation(address_info)

