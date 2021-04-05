"""
This module writes out a file "tmp/all_urls.txt" which contains all links on each county webpgage
"""

import sys
from os import path
import requests
import re
import os
from urllib import request
from os.path import isfile, join
from os import path, getcwd, listdir
from datetime import datetime

from bs4 import BeautifulSoup
import courtconfig


def get_urls(county="FORSYTH"):

    county = county.upper()
    all_urls = []
    county_url = (
        courtconfig.server + county
        #        "http://www1.aoc.state.nc.us/www/calendars/Criminal.jsp?county=" + county
        #        "http://moma"
    )
#    import ipdb; ipdb.set_trace()
    # Here we do Beatiful Soup
    county_request = requests.get(county_url)
    county_text = county_request.text
    soup = BeautifulSoup(county_text, "html.parser")

    for link in soup.find_all("a"):
        all_urls.append(link.get("href"))

    return all_urls


def clean_urls(all_url_list):
    good_urls = []

    for url in all_url_list:
        if re.findall("txt$", url):
            good_urls.append(url)

    return good_urls


def move_to_old(county):
    directory = join(getcwd(), "files", county.upper())
    list_of_files = [
        files for files in listdir(directory) if isfile(join(directory, files))
    ]

    for filename in list_of_files:
        os.rename(join(directory, filename), join(directory, "old", filename))


def generate_filename(url, county):
    directory = join(getcwd(), "files", county.upper())
    try:
        fn = re.search(
            "(/www/data/)(\w+)(/\w+/)(.+)(\d\d).(\d\d).(\d\d).(AM|PM).(.+).(CAL).txt.*",
            url,
        )

        filename = (
            fn.group(2)  # County
            + "_"
            + fn.group(7)
            + fn.group(5)
            + fn.group(6)
            + fn.group(9)
            + ".txt"
        )
        filepath = join(directory, filename)

    except AttributeError:
        """
        This happens when server files aren't in the
        correct county scheme show 18 lines above
        """
        now = datetime.now().strftime("%y%m%d%s")
        filename = county.upper() + now
        filepath = join(directory, filename + ".txt")
    return (filename, filepath)


def download_file(url):
    try:
        root_url = courtconfig.root_url
        url_r = request.urlopen(root_url + url)
        #            url_r = request.urlopen(url)
        return url_r

    except OSError:
        raise Exception(url, " : Server not reachable")


def save_urls(good_urls, county='FORSYTH'):
    assert type(good_urls) == type(["list"])
    root_url = courtconfig.root_url
    #"http://www1.aoc.state.nc.us"
    #    root_url = "http://moma"
#    root_url = courtconfig.server
    directory = join(getcwd(), "files", county.upper())

    for url in good_urls:
        print(url)
        url_r = download_file(url)

        decode_r = url_r.read().decode("utf-8")
        filename, filepath = generate_filename(url, county)
        with open(filepath, "w") as file_from_server:
            for line in decode_r:
                file_from_server.write(line)

def main(county='FORSYTH'):
    all_urls = get_urls(county)
    cleaned_urls = clean_urls(all_urls)
    move_to_old(county)
    save_urls(cleaned_urls, county)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
