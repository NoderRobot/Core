import subprocess
p=subprocess.Popen('travis login --com',stdin=subprocess.PIPE)
a=p.stdin.write('yes')