#!/usr/bin/python3


import sys
import re

from os.path import isfile, join
from os import getcwd, listdir
#import group_dataset


def main(name="hester", county="forsyth"):

    name = name.upper()
    county = county.upper()

    s = ""
    directory = join(getcwd(), "files", county)
    list_of_files = [
        files for files in listdir(directory) if isfile(join(directory, files))
    ]

    # Only consider the input county
    list_for_county = sorted([f for f in list_of_files if re.match(county, f)])
    # Sort by date
#    import ipdb; ipdb.set_trace()
    for sub_page in list_for_county:
        group_county_date_room = re.match("(\w+)_(\d\d)(\d\d)(\d\d)(\w+).txt", sub_page)
#
#        #        county = group_county_date_room.group(1)
        date = group_county_date_room.group(3) + "/" + group_county_date_room.group(4)
        room = group_county_date_room.group(5)
#        group_dataset.main(date, room, sub_page)
        with open(join(directory, sub_page), "r") as sp:

            matches = re.findall("\n.+" + re.escape(name) + ".+\n.+\n.+\n", sp.read())
            # recheck if None or empty or [] or whatever
            if matches is not None:
                for entry in matches:

                    s = s + "<p>" + date + "\t" + room + "\t" + entry + "</p>\n"

    s = s + "\n  </body>\n</html>"
    return(s)
    #return ()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
