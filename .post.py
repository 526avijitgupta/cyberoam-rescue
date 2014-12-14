from urllib import urlencode
from urllib2 import urlopen
import os
import subprocess, signal
import sys
from time import sleep
from check import *

# for periodic checking of login status
SLEEP_TIME = 200

BASE_URL = "http://172.16.68.6:8090/login.xml"


user_dict = {
    'username':'password',
    'username2':'password2',
}

# Function to send login or logout request
def send_request(request_type, *arg):
    if(request_type == 'login'):
        print "Initialting login request.."
        params = urlencode({'mode':191, 'username':arg[0], 'password':arg[1]})
        
    elif(request_type == 'logout'):
        print "Initiating logout request.."
        params = urlencode({'mode':193, 'username':arg[0]})

    response = urlopen(BASE_URL, params)
    return response.read()

def notify_alert(string):
    print string
    os.system('notify-send ' + '"' + string + '"')

def logout():
    for username in user_dict:
        data = send_request('logout',username)
        if 'off' in data:
            notify_alert("Successfully logged off")
    
if __name__ == "__main__":

    login_check = False

    try:
        if "login" in sys.argv:
            for username in user_dict:
                data = send_request("login", username, user_dict[username]) 
                if "Maximum" in data:
                    print "Maximum Login Limit Reached"
                elif "exceeded" in data:
                    print "Data transfer exceeded"
                elif "into" in data:
                    notify_alert("Successfully logged in with {0} ".format(username))
                    login_check = True
                    with open(os.devnull, 'wb') as devnull:
                        # subprocess.Popen('google-chrome', stdout=devnull, stderr=subprocess.STDOUT)
                        pass
                    break
                else:
                    print "Request Failed, Please try again later"
                    login_check = False

            while login_check:
                print "waiting.."
                sleep(SLEEP_TIME)
                if not check_status(username):
                    data = send_request("login", username, user_dict[username])
                    notify_alert("Logged in again after checking status")

    except KeyboardInterrupt:
        logout()
        sys.exit()

    if "logout" in sys.argv:
        logout()
