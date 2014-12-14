from urllib2 import urlopen
import xml.etree.ElementTree as ET

CHECK_URL = "http://172.16.68.6:8090/live?"

# Function to check login status
def check_status(username):
    print "Checking login status.."
    url = CHECK_URL + "mode=192&username=" + str(username)
    print url
    x = urlopen(url).read()
    print x
    if "<ack>ack</ack>" in x:
        print "Still logged in.."
        return True
    else:
        print "Logged out.."
        return False
