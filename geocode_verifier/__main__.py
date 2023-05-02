import csv
import os
from time import sleep

import geocode_verifier.api.census_geocode as cg
import geocode_verifier.api.google as g
from util.constants import ENCODING_STANDARD, EXTENSION_CSV, FILE_OPEN_WRITE
from util.files import read_csv_to_dict

WRITING_DICT = [
    "id",
    "original_address",
    "googlemaps_verification",
    "census_geocode_verification",
    "googlemaps_json",
    "census_geocode_json",
]


def main():
    # Get all CSVs from input directory.
    directory = os.getcwd() + "/geocode_verifier/data/input/"
    for name in os.listdir(directory):
        f = os.path.join(directory, name)

        # checking if it is a file
        output_list = []
        if os.path.isfile(f) and f.endswith(EXTENSION_CSV):
            file_dicts = read_csv_to_dict(f)
            for row in file_dicts:
                if row["address"] and row["zipcode"]:
                    api_dict = {
                        "address": {
                            "regionCode": "US",
                            "addressLines": [
                                f"{float(row['address_number']):.0f} "
                                f"{row['address'].strip()}",
                                "Chicago",
                                "IL",
                                row["zipcode"].strip(),
                            ],
                        }
                    }
                    print(api_dict)

                    cg_result = cg.validate_address(
                        api_dict["address"]["addressLines"]
                    )
                    print(cg_result)
                    gm_result = g.validate_address(api_dict)
                    print(gm_result)
                    sleep(0.5)

                    output_list.append(
                        [
                            row["id"],
                            api_dict["address"]["addressLines"].join(", "),
                            "",
                            len(cg_result) > 0,
                        ]
                    )

                    # Add google_maps result if present
                    if len(output_list[-1][2]):
                        output_list[-1][4] = gm_result

                    # Add census_geocode result if present
                    if len(output_list[-1][3]):
                        output_list[-1][5] = cg_result

                with open(
                    directory + name + EXTENSION_CSV,
                    FILE_OPEN_WRITE,
                    encoding=ENCODING_STANDARD,
                ) as csv_file:
                    writer = csv.writer(csv_file, delimiter=",", quotechar='"')
                    writer.writerow(WRITING_DICT)
                    for o_l in output_list:
                        writer.writerow(o_l)


if __name__ == "__main__":
    print("Oh, are we supposed to be validating addresses over here!?")
    main()
