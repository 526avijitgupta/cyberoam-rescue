cyberoam-rescue
===============
Cyberoam rescue helps you to login directly into cyberoam hassle-free.  
Thanks to [Yash Mehrotra](https://github.com/yashmehrotra) for his contribution.        

### Screenshots:  
![Login](https://github.com/526avijitgupta/cyberoam-rescue/blob/master/screenshots/login.png "Login")  
![Logout](https://github.com/526avijitgupta/cyberoam-rescue/blob/master/screenshots/logout.png "Logout")  

### Requirements:  
1. Any linux distro (tested on Ubuntu and Elementary OS).    
2. Add the usernames, passwords to the `.credentials.json` file. You can have as many usernames as you want, just make sure only correct combinations are there to prevent time wastage.      

### Usage:  
1. For login: `python .post.py login`  
2. For logout: `python .post.py logout`  

Note: You may set the value of `"web-browser"` in `.credentials.json` file (default:`"2"`), according to this:
* `"1"` - Launch **firefox** immediately after successful login.
* `"2"` - Launch **google-chrome** immediately after successful login. (default)
* `"0"` - Do not launch any browser.

### Features:  
1. Automatically switches for the next username, password combination in case of unsuccessfull login with one combination.   
2. Keeps you logged in all the time by checking your login status periodically.  
3. Alerts you in case of successful login/logout through notify-send.  

#### Additional Functionalities:  
* For best usage, add custom keyboard shortcuts for the login/logout.  

Feel free to fork and contribute
