import os

import googlemaps


def get_client():
    """
    Gets the GoogleMaps API client.

    :return: googlemaps.Client
    """
    key = os.getenv("GOOGLE_MAPS_API_KEY")
    return googlemaps.Client(key)
