def ci():
    import os
    try:
        cifile = open('.cifile.txt')
    except FileNotFoundError:
        os._exit(0)
    cifilec = cifile.read()
    cifilesh = open('cifile.sh','w')
    cifilesh.write('#!/bin/bash')
    cifilesh.write('\n')
    for i in cifilec:
        if(':' in i):
            cifilesh.write('\n')
        else:
            cifilesh.write(i)
if __name__ == "__main__":
    ci()