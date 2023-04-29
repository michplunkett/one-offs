import csv
import os

import geocode_verifier.api.census_geocode as cg
import geocode_verifier.api.google as g
from util.constants import ENCODING_STANDARD, EXTENSION_CSV, FILE_OPEN_WRITE
from util.files import read_csv_to_dict

WRITING_DICT = [
    "id",
    "original_address",
    "googlemaps_verification",
    "census_verification",
    "googlemaps_json",
    "census_json",
]


def main():
    # Get all CSVs from input directory.
    directory = os.getcwd() + "/geocode_verifier/data/input/"
    for name in os.listdir(directory):
        f = os.path.join(directory, name)

        # checking if it is a file
        if os.path.isfile(f) and f.endswith(EXTENSION_CSV):
            file_dicts = read_csv_to_dict(f)
            for v in file_dicts:
                print(v["id"])
                if v["address"] and v["zipcode"]:
                    api_dict = {
                        "address": {
                            "regionCode": "US",
                            "addressLines": [
                                v["address"],
                                "Chicago",
                                "IL",
                                v["zipcode"],
                            ],
                        }
                    }

                    v["cg"] = cg.validate_address(api_dict["address"])
                    v["g"] = g.validate_address(api_dict)
                    print(v["cg"])
                    print(v["g"])

                with open(
                    directory + name + EXTENSION_CSV,
                    FILE_OPEN_WRITE,
                    encoding=ENCODING_STANDARD,
                ) as csv_file:
                    writer = csv.writer(csv_file, delimiter=",", quotechar='"')
                    writer.writerow(WRITING_DICT)
                    for v in file_dict.values():
                        writer.writerow(
                            [
                                v["id"],
                                api_dict["address"]["addressLines"],
                                "",
                                "",
                                "",
                                "",
                            ]
                        )


if __name__ == "__main__":
    print("Oh, are we supposed to be validating addresses over here!?")
    main()
