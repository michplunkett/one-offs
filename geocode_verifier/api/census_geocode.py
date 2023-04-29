import os

import censusgeocode as cg


def validate_address(info):
    """
    Takes address information and returns validation on that address from the
    Census Geocode API. For documentation, please check this link:
    https://github.com/fitnr/censusgeocode#census-geocode

    :param dictionary info: A nested dictionary of strings containing
        information about a particular address

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """

    # Make sure the fields are there.
    assert bool(info["address"])
    assert bool(info["city"])
    assert bool(info["state"])
    assert bool(info["zipcode"])

    return cg.address(
        info["address"],
        city=info["city"],
        state=info["state"],
        zip=info["zipcode"],
    )
