import os

import censusgeocode as cg


def validate_address(address_info):
    """
    Takes address information and returns validation on that address from the
    Census Geocode API. For documentation, please check this link:
    https://github.com/fitnr/censusgeocode#census-geocode

    :param dictionary address_info: A nested dictionary of strings containing
        information about a particular address

    :returns The ValidationResult for the query.
    :rtype googlemaps.ValidationResult
    """

    # Make sure the fields are there.
    assert bool(address_info["address"])
    assert bool(address_info["city"])
    assert bool(address_info["state"])
    assert bool(address_info["zipcode"])

    return cg.address(
        address_info["address"],
        city=address_info["city"],
        state=address_info["state"],
        zip=address_info["zipcode"],
    )
