"""
courtdates main program
"""

from os import path, getcwd, makedirs
import get_url_list
import generate_html
import courtconfig
from datetime import datetime

start_time = datetime.now()
# directory = getcwd() + "/files"
#
#
# print(path.exists(path.join(directory, "old")))
# print(path.join(directory, "old"))
# print(directory)
# if not path.exists(directory):
#    makedirs(directory)
#
#    if not path.exists(path.join(directory, "old")):
#        makedirs(path.join(directory, "old"))
#
# Add your names (search patterns into the following line
#name_list = courtconfig.name_list
county_list = courtconfig.county_list

# This module calls the Forsyth county homepage
# and finds all links

# Open file and empty it.
# thefile = open("tmp/all_urls.txt", "w")
# print("", file=thefile)
# thefile.close()
#
# thefile = open("tmp/good_urls.txt", "w")
# print("", file=thefile)
# thefile.close()


# Writes all urls on the root page of the NC Courtpage to "tmp/all_urls.txt"
#for county in county_list:
#    print(county)
#    get_url_list.main(county)

# Run for attorneys and counties
# for name in name_list:
#    generate_html.main(name=name, county=county_list)
generate_html.main()

end_time = datetime.now()
print("Start:", start_time)
print("Ende:", end_time)
print("Job done")

quit()
