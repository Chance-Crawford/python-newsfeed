# __init__.py is similar to index.js 
# In the root directory of your project, create a new directory called app. 
# In this directory, create a new file called __init__.py. That's two underscores on each side.

# Next, let's start our Flask server by running the python -m flask run command. 
# This works only if the entry point of the app uses the default name of app.

#  You just made your first Python package! In Python, a package is a directory that can contain 
# other packages or modules. Just the presence of an __init__.py file designates the directory 
# as a package, but the file can also contain logic to consolidate submodules, 
# perform startup tasks, and more.

# When Flask runs the app package, it tries to call a create_app() function. Let's define that function now. 
# Open the app/__init__.py file, then add the following code:
from flask import Flask

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')