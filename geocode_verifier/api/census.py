import os

import census


def create_client():
    """
    Gets the census API client.

    :return: census.Census the Census API client.
    """
    key = os.getenv("CENSUS_API_KEY")
    return census.Census(key)