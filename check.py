from urllib2 import urlopen
from bs4 import BeautifulSoup

CHECK_URL = "http://172.16.68.6:8090/live?"


# Function to check login status
def check_status(username):
    url = CHECK_URL + "mode=192&username=" + str(username)
    read = urlopen(url).read()
    bs = BeautifulSoup(read)
    xml_resp = bs.html.body
    if ("exceeded" not in xml_resp or
        "same IP" not in xml_resp or
        "login again" not in xml_resp):
        return True
    else:
        return False
