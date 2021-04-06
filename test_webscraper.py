import pytest
import requests
import get_url_list
import courtconfig


@pytest.fixture
def good_urls():
    return ["/DAVIDSON_210223DC09.txt"]


@pytest.fixture
def test_url():
    return "/DAVIDSON_210223DC09.txt"

@pytest.fixture
def prod_url():
    return "/www/data/TRANSYLVANIA/calendar/DISTRICT.CRIMINAL_DISTRICT_COURT_.04.01.21.PM.0001.CAL.txt"


# class TestWebscraper(unittest.TestCase):
def test_config_file_names():
    """
    Test that config names is not empty
    """
    assert courtconfig.name_list


def test_config_file_counties():
    """
    Test that config county is not empty
    """
    assert courtconfig.county_list


def test_connectivity():
    """
    Test that server can be reached
    """
    county_url = (
        #       "http://www1.aoc.state.nc.us/www/calendars/Criminal.jsp?county=" + county
               "http://www1.aoc.state.nc.us" 
        #"http://moma"
    )

    county_request = requests.get(county_url)
    assert county_request.status_code == 200


def test_clean_urls():
    test_input = ["DAVIDSON.txt2", "DAVIDSON.txt", "DAVIDSON.html"]
    expected_output = [
        "DAVIDSON.txt",
    ]

    assert get_url_list.clean_urls(test_input) == expected_output


def test_move_to_old(county="FORSYTH"):

    assert True


def test_save_urls(good_urls):
    pass


def test_name_to_searchpattern():
    target = __import__("generate_html")
    assert target.name_to_searchpattern("index") == ":hester"


def test_generate_filename():

    target = __import__('get_url_list')
    test_input = "/www/data/TRANSYLVANIA/calendar/DISTRICT.CRIMINAL_DISTRICT_COURT_.04.01.21.PM.0001.CAL.txt"
    expected_output = "TRANSYLVANIA_2104010001.txt"
    real_output, filepath = get_url_list.generate_filename(test_input,  'TRANSYLVANIA')
    assert real_output == expected_output

def download_file_test_server(test_url):
    """
    Test Case for downloading a file from
    a) the test server
    """
    target = __import__('get_url_list')
    filename, filepath = target.generate_filename(test_url)
    target.download_file(test_url)
    assert isfile(filepath)

def download_file_prod_server(prod_url):
    """
    Test Case for downloading a file from
    b) from production
    """

    target = __import__(get_url_list)
    filepath = target.generate_filename(prod_url)
    target.download_file(prod_url)
    assert isfile(filepath)



# if __name__ == "__main__":
#    unittest.main()
#    test_connectivity()
