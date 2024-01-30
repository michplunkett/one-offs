"""Census Geocode functions."""
from time import sleep

import requests
from censusgeocode import CensusGeocode

from util.constants import SLEEP_TIME_ERROR


def get_client():
    """Get the Census Geocode API client."""
    return CensusGeocode()


def validate_address(client, info):
    """
    Take address information and return validation information on the submitted
    address from the Census Geocode API.

    For documentation, check this link:
    https://github.com/fitnr/censusgeocode#census-geocode.
    """
    # Make sure the necessary fields are there.
    assert len(info) == 4

    num_retries = 10
    response = None
    for _ in range(num_retries):
        try:
            response = client.address(
                street=info[0],
                city=info[1],
                state=info[2],
                zip=info[3],
                returntype="locations",
                timeout=5,
            )
            if response:
                break
        except requests.exceptions.RequestException:
            print(
                f"Pausing {SLEEP_TIME_ERROR} between Census Geocode "
                f"requests due to error."
            )
            sleep(SLEEP_TIME_ERROR)
            pass

    return response
