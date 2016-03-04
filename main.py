print "Hello there"
import sys,random,time

for i in range(random.randint(0,5)):
    print "outputting",i,random.randint(0,2000)
    time.sleep(0.2)
outtype = random.randint(0,10)
print outtype
if outtype == 1:
    sys.exit(201)
elif outtype == 2:
    sys.exit(202)
elif outtype == 3:
    print hi
