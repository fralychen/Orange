from PIL import Image
from io import BytesIO
from docx import Document
from docx.shared import Inches
from bs4 import BeautifulSoup
from http import cookiejar

import os
import re
import requests
import urllib

FILENAME = open("cookie.txt", 'w+')
filename = 'cookie.txt'

def GetCookie():
    url = ''
    file=urllib.request.urlopen(url)
    #print(file.getcode)
    message = file.info()
    CookieStr = str(message)
    CookieVlue = re.findall(r'Cacti=[a-zA-Z0-9]+',CookieStr)[0]
    print(CookieVlue,file=FILENAME)
    print(CookieVlue)
    url=''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Cookie':CookieVlue,
        'Referer': '',
        'Host': '',
    }

    First_Page = requests.get(url,headers=headers)
    print (First_Page.text)

GetCookie()
