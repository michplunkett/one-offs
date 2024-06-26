"""Run the Geocode verification process for the files in the input directory."""

import csv
import os

import geocode_verifier.api.census_geocode as cg
import geocode_verifier.api.google_maps as gm
from util.constants import (
    ENCODING_STANDARD,
    EXTENSION_CSV,
    FILE_OPEN_MODE_WRITE,
)
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
    """Run the Geocode verification process."""
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
                # If the row does not at least have a street and zipcode,
                # it is ignored.
                if file_row["address"] and file_row["zipcode"]:
                    # The city is defaulted to Chicago if it is not present.
                    if not file_row.get("city"):
                        file_row["city"] = "Chicago"

                    # The state is defaulted to IL if it is not present.
                    if not file_row.get("state"):
                        file_row["state"] = "IL"

                    api_dict = {
                        "regionCode": "US",
                        "addressLines": [
                            f"{float(file_row['address_number']):.0f} "
                            f"{file_row['address'].strip()}",
                            file_row["city"],
                            file_row["state"],
                            file_row["zipcode"].strip(),
                        ],
                    }

                    cg_result = cg.validate_address(
                        cg_client, api_dict["addressLines"]
                    )
                    gm_result = gm.validate_address(gm_client, api_dict)[
                        "result"
                    ]

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
                            # As long as one result shows up, we count it as
                            # confirmed.
                            len(cg_result) > 0,
                        ]
                    )

                    if len(output_list) % 20 == 0:
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
                FILE_OPEN_MODE_WRITE,
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
    main()
