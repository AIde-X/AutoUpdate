import os
hostname = "reg.exam.dtu.ac.in" #example
response = os.system("ping -c 4000 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'
