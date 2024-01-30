"""Contains the GoogleMaps API functions."""
import os

import googlemaps


def get_client():
    """Get the GoogleMaps API client."""
    key = os.getenv("GOOGLE_MAPS_API_KEY")

    # Make sure there is an API key.
    assert key != ""

    return googlemaps.Client(key)


def validate_address(client, info):
    """
    Take address information and returns validation on that address from the
    Google Maps API.

    For documentation, please check this link:
    https://developers.google.com/maps/documentation/address-validation/requests-validate-address.
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
