=====================
Courtdates Webscraper
=====================

This program searches for courtdates in North Carolina counties and downloads the text-files. The configuration file is courtconfig.py. You may list your counties there. Then start the program with ``python scheduler.py``.

Steps to install:

Create and activate a virtual environment:
``python3 -m virtualenv venv``
``source venv/bin/activate``

Download beatiful soup and requests:
``python -m pip install beautifulsoup4``
``python -m pip install requests``

Edit the config-file like

.. code-block::Python

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


