cyberoam-rescue
===============
Cyberoam rescue helps you to login directly into cyberoam hassle-free.  
Thanks to [Yash Mehrotra](https://github.com/yashmehrotra) for his contribution      

### Requirements:  
1. Any linux distro (tested on Ubuntu)  
2. Add the usernames, passwords to the `credentials.json` file    

### Usage:  
1. For login:  
`python .post.py login`  
2. For logout:  
`python .post.py logout`  

### Features:  
1. Automatically switches for the next username, password combination in case of unsuccessfull login with one combination.   
2. Keeps you logged in all the time by checking your login status periodically.  
3. Alerts you in case of login/logout as a notification.  

#### Additional Functionalities:  
* To open google chrome once after login, uncomment the corresponding line.  
* For best usage, add custom keyboard shortcuts for the login/logout.  

Feel free to fork and contribute
