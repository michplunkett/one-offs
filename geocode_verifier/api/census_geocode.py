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
    assert len(info) == 4

    return cg.address(
        info[0], city=info[1], state=info[2], zip=info[3], returntype="location"
    )
