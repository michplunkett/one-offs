import os

import googlemaps


def get_client():
    """
    Gets the GoogleMaps API client.

    :return: googlemaps.Client
    """
    key = os.getenv("GOOGLE_MAPS_API_KEY")

    # Make sure there is an API key.
    assert key != ""

    return googlemaps.Client(key)


def validate_address(client, info):
    """
    Takes address information and returns validation on that address from the
    Google Maps API. For documentation, please check this link:
    https://developers.google.com/maps/documentation/address-validation/requests-validate-address.

    :param client: the GoogleMaps API client
    :param dictionary info: A nested dictionary of strings containing
        information about a particular address

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """
    # Assert that the necessary fields are there.
    assert bool(info)
    assert bool(info["regionCode"])
    assert bool(info["addressLines"])

    return client.addressvalidation(
        info["addressLines"],
        # Enable Coding Accuracy Support System
        enableUspsCass=True,
        locality="Chicago",
        regionCode=info["regionCode"],
    )
