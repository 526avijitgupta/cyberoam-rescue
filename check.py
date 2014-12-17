from urllib2 import urlopen

CHECK_URL = "http://172.16.68.6:8090/live?"


# Function to check login status
def check_status(username):
    url = CHECK_URL + "mode=192&username=" + str(username)
    read = urlopen(url).read()
    if "<ack>ack</ack>" in read:
        return True
    else:
        return False
