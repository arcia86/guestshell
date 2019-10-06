import os

f = os.popen('mv -f /bootflash/autoconfig/aarcia/running.latest /home/guestshell/guestshell/running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/guestshell; git add running')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/guestshell; git commit -m "Latest change"')
who = f.read()
f.close
print "Result:", who
f = os.popen('cd /home/guestshell/guestshell; git push')
who = f.read()
f.close
print "Result:", who
