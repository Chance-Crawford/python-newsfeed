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
# app.routes will find the __init__.py file in the routes package (directory) we created. 
# We are then importing an object containing the home routes from there, as well as the dashboard
# and other routes by separating thjem with a comma.
# the app.routes name here can also just be written as .routes, it is up to preference
from app.routes import home, dashboard

def create_app(test_config=None):
    # set up app config
    # The app should serve any static resources from the root directory 
    # and not from the default /static directory.
    app = Flask(__name__, static_url_path='/')
    # Trailing slashes are optional (meaning that /dashboard and /dashboard/ load the same route).
    app.url_map.strict_slashes = False
    # The app should use the key called 'super_secret_key' when creating server-side sessions.
    app.config.from_mapping(
        SECRET_KEY="super_secret_key"
    )

    #We add an inner function, called hello(), that returns a string. However, in the 
    # preceding line, the decorator @app.route('/hello') turns the hello() function 
    # into a route. The function's return becomes the route's response.
    @app.route('/hello')
    def hello():
        return 'hello world'

    # register the imported home routes into the app server
    app.register_blueprint(home)
    # register the imported dashboard routes into the app server
    app.register_blueprint(dashboard)

    return app

