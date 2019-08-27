#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from paramiko import SSHClient
from paramiko import AutoAddPolicy

ip = os.getenv('IPADDR')
port = 22
user = os.getenv('USER')
passwd = os.getenv('PASSWORD') 

cmd = 'pwd'

s = SSHClient()
s.set_missing_host_key_policy(AutoAddPolicy())
s.connect(ip, port, user, passwd)
stdin,stdout,stderr = s.exec_command(cmd)
print (stdout.read())
print (stderr.read())
s.close()