## Flask Template

This is a template for [Flask](https://www.palletsprojects.com/p/flask/) applications!

I wrote this so I could have a quick and ready template to stand up an api to hit with other projects.

### How to use
After cloning this repository, you need to install the dependencies in the `requirements.txt` file. I highly suggest using a virtual environment to isolate the dependencies from other projects you may have. (Read more about virtual environments in python [here](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments), I personally use `virtualenv`)

Once you have the dependencies installed, all you have to do is run `python Boot.py` and then you should have a development server running, you are now ready to hack away at the code!

**Note:** To run a non-development server, I use [Gunicorn](http://gunicorn.org/). It is listed as a dependency so if you want you can run `gunicorn Boot:app` to run the application with Gunicorn.
