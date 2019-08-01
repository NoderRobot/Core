import sys
import os
try:
    get = sys.argv[1]
    if get ==' restart':
        pass
    #    os.system('./cmd/restart.sh')
    elif get == 'help':
        print("Sorry! I can't do it")
except IndexError:
    print('index not found')

