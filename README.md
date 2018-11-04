# Automatic LinkedIn Liker
A script developed for a pilot proof of concept.

### Requirements for installation
- [x] Git
- [x] Python (Version 3)
- [x] Pip

### Installation steps
1. Clone the repository and move to the created folder.

    Execute in the terminal: 

   `$ git clone https://github.com/germmand/automatic-linkedin-liker.git && cd ./automatic-linkedin-liker`

2. Create virtual environment. 

    As a suggestion, you could use [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/).
    Follow the steps on that link to create it and activate it.
    
3. Once you're done with that, you need to install the requirements. To do that, run the following in the terminal:

    `$ pip install -r requirements.txt`
    
4. The script works out of the box upon the chrome driver. You can get it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   Make sure to locate it in a place where your PATH can find it (e.g. `/usr/bin/`)

5. Finally, open `main.py` and set the credentials (i.e. `EMAIL` and `PASSWORD`) and the `PROFILE_NAME` to evaluate latest posts from.

And that's it! Now you can run the script as:

- `$ python main.py`

The browser should pop up and automatically go to the person's profile and like his/her latest post.
