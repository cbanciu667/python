###
# base example
import subprocess

def myrun(cmd):
    """from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
    """
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print line,
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)

###
# example with filters output
import subprocess
proc = subprocess.Popen(['python','fake_utility.py'],stdout=subprocess.PIPE)
while True:
  line = proc.stdout.readline()
  if line != '':
    #the real code does filtering here
    print "test:", line.rstrip()
  else:
    break
