=====================
Courtdates Webscraper
=====================

This program searches for courtdates in North Carolina counties and downloads the text-files. The configuration file is courtconfig.py. You may list your counties there. Then start the program with ``python scheduler.py``.

Install requirements
====================

Create and activate a virtual environment:

``python3 -m virtualenv venv``

``source venv/bin/activate``

Download beatiful soup and requests:

``python -m pip install beautifulsoup4``

``python -m pip install requests``


Configuration file
==================

The configuration file is courtconfig.py. It contains the server, which is being queried, the counties, which are being downloaded, and the names which should get queried and an html output generated. 

Edit the config-file courtconfig.py to something like the following

.. code-block:: Python

    """
    Add your names and county list here
    """
    server = "http://www1.aoc.state.nc.us/www/calendars/Criminal.jsp?county="
    root_url = "http://www1.aoc.state.nc.us"
    name_list = {
    #html_name: search_pattern
        "index": "mcclane",
        "test": "doe,j",
    }
    county_list = [
        "forsyth",
        "davidson",
        "polk",
    ]


scheduler
=========

The scheduler consists of 3 tasks:

1. source the config file
2. download the text files for each county in the config file.
3. generate an html output for each name-pair in the config file

