import os

print "Processing (%s) start..." % os.getpid()
#The function of fork will return two tiwce!
pid = os.fork()
if pid == 0:
    #A child process always return 0
    print "I'm child process (%s) and my parent is (%s)." % (os.getpid(), os.getppid())
else:
    #A parent process return the pid of child
    print "I'm (%s) just created a child process (%s)." % (os.getpid(), pid)
