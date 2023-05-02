import csv
import os
from time import sleep

import geocode_verifier.api.census_geocode as cg
import geocode_verifier.api.google as gm
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
    read_directory = os.getcwd() + "/geocode_verifier/data/input/"
    write_directory = os.getcwd() + "/geocode_verifier/data/output/"

    cg_client = cg.get_client()
    gm_client = gm.get_client()

    # Get all CSVs from input directory.
    for file_name in os.listdir(read_directory):
        f = os.path.join(read_directory, file_name)

        # checking if it is a file
        output_list = []
        if os.path.isfile(f) and f.endswith(EXTENSION_CSV):
            file_dicts = read_csv_to_dict(f)
            for file_row in file_dicts:
                if file_row["address"] and file_row["zipcode"]:
                    api_dict = {
                        "regionCode": "US",
                        "addressLines": [
                            f"{float(file_row['address_number']):.0f} "
                            f"{file_row['address'].strip()}",
                            "Chicago",
                            "IL",
                            file_row["zipcode"].strip(),
                        ],
                    }

                    # TODO: If there is an error returned in cg_result, wait
                    # TODO: 60 seconds and try again.
                    cg_result = cg.validate_address(
                        cg_client, api_dict["addressLines"]
                    )
                    gm_result = gm.validate_address(gm_client, api_dict)[
                        "result"
                    ]

                    # Sleep for half a second after each request.
                    sleep(0.5)

                    output_list.append(
                        [
                            file_row["id"],
                            ", ".join(api_dict["addressLines"]),
                            # The location is confirmed down to the route
                            # or apartment level.
                            # Src: bit.ly/3ALbjE0
                            [
                                "SUB_PREMISE",
                                "PREMISE",
                                "PREMISE_PROXIMITY",
                                "ROUTE",
                            ].index(gm_result["verdict"]["geocodeGranularity"])
                            > -1,
                            len(cg_result) > 0,
                        ]
                    )

                    if len(output_list) % 20:
                        print(f"You have parsed {len(output_list)} addresses.")

                    # Add google_maps result if present
                    if output_list[-1][2]:
                        output_list[-1].append(gm_result)

                    # Add census_geocode result if present
                    if output_list[-1][3]:
                        output_list[-1].append(cg_result)

            with open(
                write_directory
                + file_name.replace(EXTENSION_CSV, ".output" + EXTENSION_CSV),
                FILE_OPEN_WRITE,
                encoding=ENCODING_STANDARD,
            ) as csv_file:
                writer = csv.writer(
                    csv_file,
                    delimiter=",",
                    quotechar='"',
                )
                writer.writerow(WRITING_DICT)
                writer.writerows(output_list)


if __name__ == "__main__":
    print("Oh, are we supposed to be validating addresses over here!?")
    main()
