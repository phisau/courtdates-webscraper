#!/usr/bin/python3
import sys
import re
from os.path import isfile, join
from os import getcwd, listdir


def main(name, county):

    name = name.upper()
    county = county.upper()

    s = ""
    directory = getcwd() + "/files"
    list_of_files = [
        files for files in listdir(directory) if isfile(join(directory, files))
    ]

    # Only consider the input county
    list_for_county = sorted([f for f in list_of_files if re.match(county, f)])
    # Sort by date
    for sub_page in list_for_county:
        print(sub_page)
        group_county_date_room = re.match("(\w+)_(\d\d)(\d\d)(\d\d)(\w+).txt", sub_page)

        #        county = group_county_date_room.group(1)
        date = group_county_date_room.group(3) + "/" + group_county_date_room.group(4)
        room = group_county_date_room.group(5)
        with open("files/" + sub_page, "r") as sp:
            matches = re.findall(
                "\n.+" + re.escape(name) + ".+\n.+\n.+\n.+\n", sp.read()
            )
            # recheck if None or empty or [] or whatever
            if matches is not None:
                for entry in matches:

                    s = s + "<p>" + date + "\t" + room + "\t" + entry + "</p>\n"
            if sub_page == "FORSYTH_171201001C.txt":
                print(sp.read())
                print("HALLA")
                quit()

    s = s + "\n  </body>\n</html>"
    return s


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
