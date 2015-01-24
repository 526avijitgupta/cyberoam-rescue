from urllib import urlencode
from urllib2 import urlopen
from os import system, devnull
import subprocess
import signal
from sys import argv, exit
from time import sleep
import httplib
from json import load
from check import *

# For periodic checking of login status
SLEEP_TIME = 200

BASE_URL = "http://172.16.68.6:8090/login.xml"

try:
    credentials = load(open('.credentials.json'))
    user_dict = credentials[0]
except ValueError:
    print """Error decoding the JSON file.
    [Note: Check that there is a trailing comma after every line in the
    credentials.json file, except the last one].
    """
    exit()


# Function to send login or logout request
def send_request(request_type, *arg):
    if(request_type == 'login'):
        print "Initialting login request for USERNAME: %s" % arg[0]
        params = urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif(request_type == 'logout'):
        print "Initiating logout request.."
        params = urlencode({'mode': 193, 'username': arg[0]})

    response = urlopen(BASE_URL, params)
    return response.read()


# Function to alert the user on successful login/logout
def notify_alert(string):
    print string
    system('notify-send ' + '"' + string + '"')


# Function to initiate a logout request and kill the ongoing login request
def logout():
    for username in user_dict:
        data = send_request('logout', username)
        if 'off' in data:
            notify_alert("Successfully logged off")
            system(
                """ps aux | grep python | grep '.post.py login' |
                awk '{print $2}' | xargs kill -9""")
            break


if __name__ == "__main__":

    login_check = False

    try:
        if "login" in argv:
            for username in user_dict:
                username = str(username)
                user_dict[username] = str(user_dict[username])
                data = send_request("login", username, user_dict[username])
                if "Maximum" in data:
                    print "Maximum Login Limit Reached"
                elif "exceeded" in data:
                    print "Data transfer exceeded"
                elif "could not" in data:
                    print "Incorrect username or password"
                elif "into" in data:
                    notify_alert(
                        "Successfully logged in with {0} ".format(username))
                    login_check = True
                    launch_chrome = True
                    try:
                        ps = subprocess.Popen(
                            ('ps', 'aux'), stdout=subprocess.PIPE)
                        output = subprocess.check_output(
                            ('pgrep', 'chrome'), stdin=ps.stdout)
                        output = output.split("\n")
                        if (len(output) > 1):
                            launch_chrome = False
                    except subprocess.CalledProcessError:
                        pass
                    except Exception as e:
                        print e

                    """Uncomment this piece of code to
                    automatically launch google chrome after login:
                    [Note: google-chrome will be launched only if
                    it is not already open, and not otherwise]"""

                    if credentials[1]['google-chrome'] == 'yes':
                       print "Launching chrome.."
                       with open(devnull, 'wb') as devnull:
                          subprocess.Popen(
                          'google-chrome', stdout=devnull,
                          stderr=subprocess.STDOUT)

                    print "Press Ctrl + C to logout"
                    break
                else:
                    print "Request Failed, Please try again later"
                    login_check = False

            while login_check:
                sleep(SLEEP_TIME)
                if not check_status(username):
                    data = send_request("login", username, user_dict[username])

    except KeyboardInterrupt:
        logout()
        sys.exit()
    except httplib.BadStatusLine:
        notify_alert(
            "Bad Connection. Please check your connection and try again.")
        sys.exit()
    except Exception as e:
        print e

    if "logout" in argv:
        logout()
