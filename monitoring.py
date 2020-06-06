import psutil
import socket
import os


def send_alert(message):
    print(message)
user=os.getlogin()
#print(user)
disk = 'D:\\'
disk_threshold = 80
cpu_threshold = 80
mem_threshold = 500000000
d=psutil.disk_usage(disk)
p = psutil.cpu_percent(interval=3)
m =psutil.virtual_memory().available 
localhost =socket.gethostbyname('localhost')
if d.percent > disk_threshold:
    send_alert('Disk space ('+str(d.percent) +') has exceded ' + str(disk_threshold) +"%'")
    generate_mail_error('automation@example.com', user + '@examples.com', 'Error - Available disk space is less than 20%', 'Please check your system and resolve the issue as soon as possible.')

if p > cpu_threshold:
    send_alert('CPU usuage (' + str(p) +') has exceded ' + str(cpu_threshold) +"%'")
     generate_mail_error('automation@example.com', user + '@examples.com', 'Error - CPU usage is over 80%', 'Please check your system and resolve the issue as soon as possible.')

if m < mem_threshold:
      send_alert('Available memory (' + str(m) +') is less than' + str(mem_threshold) +"%'")
      generate_mail_error('automation@example.com', user + '@examples.com', 'Error - Available memory is less than 500MB', 'Please check your system and resolve the issue as soon as possible.')
if localhost != '127.0.0.1':
    send_alert('Localhost IP cannot me resolved')
    generate_mail_error('automation@example.com', user + '@examples.com', 'Error - localhost cannot be resolved to 127.0.0.1', 'Please check your system and resolve the issue as soon as possible.')









