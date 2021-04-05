import attorney_search
import sys
import itertools
from datetime import datetime
import courtconfig
from os.path import join

def frame():
    lu = datetime.now()
    last_update = "{:%Y-%m-%d %H:%M}".format(lu)
    frame = (
        '<html> <head> <meta charset="utf-8"> \
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> \
            <meta name="description" content=""> \
            <meta name="author" content="Philip"> \
            <title>Pony World Courtdates</title>  \
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"> \
            <link rel="stylesheet" href="cover.css"> </head> <body> <p>\
            Last update: '
        + str(last_update)
        + "UTC</p>"
    )

    return frame

def name_to_searchpattern(name):
    return courtconfig.name_list[name]

def body(name):
    sp = name_to_searchpattern(name)
    body = ""
    for county in courtconfig.county_list:
        print("Search for: " + name + sp + " in " + county)
        body = ( body
                + "<h2>"
                + county
                + "</h2>"
                + attorney_search.main(sp, county)
                )
    return body

def write_html(name):
    
    footer = "\n </body>\n</html>"
    s = frame() + body(name) + footer
    index = open(join("html", name + ".html"), "a")
    index.write(s)
    index.close()


def main():

    for page in courtconfig.name_list:
        write_html(page)
    print("writing output to file")

if __name__ == "__main__":
    sys.exit(main())
