import sys
import os
try:
    get = sys.argv[1]
    if get ==' restart':
        pass
    #    os.system('./cmd/restart.sh')
except IndexError:
    print('index not found')

