import os

import googlemaps


def _get_client():
    """
    Gets the GoogleMaps API client.

    :return: googlemaps.Client
    """
    key = os.getenv("GOOGLE_MAPS_API_KEY")

    # Make sure there is an API key.
    assert key != ""

    return googlemaps.Client(key)


def validate_address(info):
    """
    Takes address information and returns validation on that address from the
    Google Maps API. For documentation, please check this link:
    https://developers.google.com/maps/documentation/address-validation/requests-validate-address

    :param dictionary info: A nested dictionary of strings containing
        information about a particular address

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """

    client = _get_client()

    # Assert that the necessary fields are there.
    assert bool(info["address"])
    assert bool(info["address"]["regionCode"])
    assert bool(info["address"]["addressLines"])

    # Enable Coding Accuracy Support System
    info["enableUspsCass"] = True

    return client.addressvalidation()
