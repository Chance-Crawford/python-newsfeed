# Interestingly, you can import any variables or functions defined by 
# Python modules into other modules. 

# The ability to import every variable or function in a module contrasts with Node.js, 
# which requires you to explicitly declare the properties you want to expose. Such as module.export = {...}
# python does not require that.

# Thus, the bp object and the three 
# route functions are all available for importing. We only care about bp, 
# though, because the other functions are already attached to it—thanks 
# to the @bp.route() decorator.

# Let's review what's happening here. First, the .home syntax directs the program 
# to find the module named home in the current directory. Next, we want to 
# import the bp object, but we rename it home as part of the import process, 
# for practicality's sake.
from .home import bp as home

from .dashboard import bp as dashboard