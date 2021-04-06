"""
courtdates main program
"""

from os import path, getcwd, makedirs
import get_url_list
import generate_html
import courtconfig
from datetime import datetime

#Add your names (search patterns into the following line
name_list = courtconfig.name_list
county_list = courtconfig.county_list
start_time = datetime.now()

# IF NO FILE DIRECTORY EXIST, THEN CREATE THEM
# directory = getcwd() + "/files"
# print(path.exists(path.join(directory, "old")))
# print(path.join(directory, "old"))
# print(directory)
# if not path.exists(directory):
#    makedirs(directory)
#
#    if not path.exists(path.join(directory, "old")):
#        makedirs(path.join(directory, "old"))


# Writes all urls on the root page of the NC Courtpage to "tmp/all_urls.txt"
for county in county_list:
    print(county, " is being processed. Files are downloaded.")
    get_url_list.main(county)

# Generate html files for attorneys and counties
generate_html.main()

end_time = datetime.now()
print("Start:", start_time)
print("Ende:", end_time)
print("Job done")

quit()
