import os
from . import main

try: 
    os.mkdir(os.sep.join(['.','plugin','data','OlivaGithub']))
except FileExistsError: 
    pass
