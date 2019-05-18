from PIL import Image
from io import BytesIO
from docx import Document
from docx.shared import Inches
from bs4 import BeautifulSoup
from http import cookiejar

import datetime
import glob
import shutil
import os
import re
import requests
import urllib

#路径变量
SOURCEPATH=""
Ops=""
INSPECTION=""
MONITOR=""
SHELVES=""

#地点变量
add = "ADDRESS"

#获取cookie
FILENAME = open("cookie.txt", 'w+')
filename = 'cookie.txt'

###
#def GetCookie():
#    url = ''
#    file=urllib.request.urlopen(url)
#    #print(file.getcode)
#    message = file.info()
#    CookieStr = str(message)
#    CookieVlue = re.findall(r'Cacti=[a-zA-Z0-9]+',CookieStr)[0]
#    print(CookieVlue,file=FILENAME)
#    print(CookieVlue)
#    url=''
#    headers = {
#        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#        'Cookie':CookieVlue,
#        'Referer': '',
#        'Host': '',
#    }
#
#    First_Page = requests.get(url,headers=headers)
#    print (First_Page.text)
#    
#GetCookie()
###



def GetCookie():
    url = 'url'
    file=urllib.request.urlopen(url)
    #print(file.getcode)
    message = file.info()
    CookieStr = str(message)
    CookieVlue = re.findall(r'Cacti=[a-zA-Z0-9]+',CookieStr)[0]
    print(CookieVlue)
    return CookieVlue

#爬取数据
document = Document()
url='url'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie':'Cacti=fdsafdsaw32342',
}


for i in (2,3,4,5,6,7,8,9,10,11,34,35,36):
    for n in (1,3,6):
        payload1 = {'action':'tree','tree_id':'2','leaf_id':'%s'%i,'page':'%d'%n}

        for m in(350,410,528,472,588,110,170,230,290,1085,1116,1142):

            #正则规则
            Regular1 = '(graph\Simage\Sphp.*local_graph_id=%d.*end=\d+)'%m
            print (Regular1)
            First_Page = requests.get(url,headers=headers,params=payload1)
            print (First_Page.url)

            #清洗数据,获取流量图URL
            plt = re.findall(Regular1,First_Page.text)
            print(plt)
            if len(plt):
                a=(plt[0])
            else:
                True
            JPG_url = ( '<URL>'+ a)
            print( '<URL>'+ a)
            JPG_url_r = JPG_url.replace(';','&')
            print(JPG_url_r)

            #获取图片二进制数据，并保存成doc
            r = requests.get(JPG_url_r,headers=headers)
            image = Image.open(BytesIO(r.content))
            image.save('image%d.bmp'%i)
    document.add_picture('image%d.bmp'%i, width=Inches(6))
document.save('FRALYCHEN.docx')

#复制巡检报告文件并标记日期
T=datetime.datetime.now()

src_file = '00' + add + 'FRALYCHEN.xls'
dst_file = "2019.{}.{}".format(T.month, T.day) + add + 'FRALYCHEN.xls'
shutil.copyfile(SOURCEPATH + src_file,INSPECTION + dst_file)

MonScfile = '00' + add + 'FRALYCHEN.docx'
MonDtfile = "2019.{}.{}".format(T.month, T.day) + add + 'FRALYCHEN.docx'
shutil.copyfile(SOURCEPATH + MonScfile,MONITOR + MonDtfile)

#删除文件
os.remove(SOURCEPATH + MonScfile)
for infile in glob.glob(os.path.join(SOURCEPATH,'*.bmp')):
    os.remove(infile)

#SVN提交
def SvnCommit():
    os.chdir(Ops)
    os.system('svn cleanup')
    r=os.popen('svn st')
    info=r.readlines()
    print(info)

    for line in info:
        line=line.strip('\n').split('       ')
        one=line[0]
        two=line[1]
        print(two)
        if one == '?':
            os.system('svn add %s' % two)
            os.system('svn commit -m %s' % two)
        elif one == '！':
            os.system('svn del %s' %two)
            os.system('svn commit -m "clear"')

SvnCommit()

