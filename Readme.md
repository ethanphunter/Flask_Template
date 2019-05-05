## Flask Template [![Build Status](https://travis-ci.com/ethanphunter/Flask_Template.svg?branch=master)](https://travis-ci.com/ethanphunter/Flask_Template)

This is a template for [Flask](https://www.palletsprojects.com/p/flask/) applications!

I wrote this so I could have a quick and ready template to stand up an api to hit with other projects.

### How to Run
After cloning this repository, you need to install the dependencies in the `requirements.txt` file. I highly suggest using a virtual environment to isolate the dependencies from other projects you may have. (Read more about virtual environments in python [here](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments), I personally use `virtualenv`)

Once you have the dependencies installed, all you have to do is run `python Boot.py` and then you should have a development server running, you are now ready to hack away at the code!

**Note:** To run a non-development server, I use [Gunicorn](http://gunicorn.org/). It is listed as a dependency so if you want you can run `gunicorn Boot:app` to run the application with Gunicorn.

### How to Use
I like to use [Postman](https://www.getpostman.com/) to interact with the application during development. You can use `curl` or probably any other http client you can think of but Postman is just my personal preference. Included in this repository is a `Flask_Template.postman_collection.json` file, which is a collection of Postman requests that you can import into Postman for your own use with this application. I plan on adding the example endpoint documentation soon!
