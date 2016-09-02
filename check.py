from urllib2 import urlopen

CHECK_URL = "http://172.16.68.6:8090/live?"


# Function to check login status
def check_status(username):
    url = CHECK_URL + "mode=192&username=" + str(username)
    resp = urlopen(url).read().lower()
    not_logged_in_codes = ('exceeded','same ip', 'login again')
    logged_out = any([True for code in not_logged_in_codes if code in resp])
    if logged_out:
        return False
    return True
