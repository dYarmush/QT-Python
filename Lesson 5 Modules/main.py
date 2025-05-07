# option 1 for improt
import add_module as am

print(am.add(5,10))

# option 2 - get specific function
from add_module import add

#option 3 - get all functions from module
# same as 1 but dont need to use the name
from add_module import *

#__name__ # prints the name of the fle, if it is the file being run it will be "__main__" 
# otherwise it is the name of the file
