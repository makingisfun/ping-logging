# Check & log the ping
import pyping
import time

file = open(„pinglog.txt“,“a“)
file.write(„MinPing,MaxPing \n“)

r = pyping.ping(‚google.com‘)
# if ret_code == 0, the host is available
# print(r.ret_code)
maxping = r.max_rtt
minping = r.min_rtt
#print(„MinPing = “ +  minping)
#print(„MaxPing = “ +  maxping)
#print(„—————-„)
ping = minping + „,“ + maxping + „\n“
file.write(ping)