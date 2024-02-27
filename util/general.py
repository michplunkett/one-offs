"""
Stores non-specific domain functions that are used in multiple files.
"""

def list_to_parsed_set(unparsed_list: [str], delimiter: str = "/"):
    unparsed_list.sort()
    parsed_set = set()
    for element in unparsed_list:
        if delimiter in element:
            for p in element.split(delimiter):
                fmt_element = p.strip().lower()
                if p:
                    parsed_set.add(fmt_element)
        else:
            fmt_element = element.strip().lower()
            parsed_set.add(fmt_element)

    # Remove any empty values from set
    if "" in parsed_set:
        parsed_set.remove("")
    return parsed_set
