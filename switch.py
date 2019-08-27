#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from paramiko import SSHClient
from paramiko import AutoAddPolicy

ip = os.getenv('IPADDR')
port = 22
user = os.getenv('USER')
passwd = os.getenv('PASSWORD') 

print(ip)
print(port)
print(passwd)
print(user)

#cmd = 'dis ip pool interface vlanif1 used                                                                                                    '
cmd = 'pwd'

s = SSHClient()
s.set_missing_host_key_policy(AutoAddPolicy())
s.connect(ip, port, user, passwd)
stdin,stdout,stderr = s.exec_command(cmd)
print (stdout.read())
print (stderr.read())
s.close()