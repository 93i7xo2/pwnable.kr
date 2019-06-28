import subprocess
import os
import socket
import sys

s1 = [ "a" for i in range(0,100)]
s1[0]="./input"
s1[ord('A')] = ""
s1[ord('B')] = "\x20\x0a\x0d"
s1[ord('C')] = "8787"

r1,w1 = os.pipe()
r2,w2 = os.pipe()

new_env = os.environ.copy()
new_env["\xde\xad\xbe\xef"]="\xca\xfe\xba\xbe";

p = subprocess.Popen(s1,stdin= r1, stderr=r2,env=new_env)

w1 = os.fdopen(w1, 'w')
w1.write("\x00\x0a\x00\xff")
w1.close()

w2 = os.fdopen(w2, 'w')
w2.write("\x00\x0a\x02\xff")
w2.close()
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print "Socket successfully created"
except socket.error as err: 
    print "socket creation failed with error %s" %(err) 
  
# default port for socket 
port = 8787
  
try: 
    host_ip = socket.gethostbyname('localhost') 
except socket.gaierror: 
    print "there was an error resolving the host"
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 
s.send("\xde\xad\xbe\xef")
s.close()
