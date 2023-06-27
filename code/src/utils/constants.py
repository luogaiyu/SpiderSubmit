# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime
import configparser
env = os.environ.get('APP_ENV','dev')

# 加载对应环境的配置文件
config = configparser.ConfigParser()
config.read(f'config/{env}.ini')

OUTPUT_DIR = config['DEFAULT']['OUTPUT_DIR']

today = datetime.today()
OUTPUT_DIR = OUTPUT_DIR + str(today.year) +"_" + str(today.month) +"_" + str(today.day) + "_" +str(today.hour)  +  "\\"
HEADERS = {
            "Authority": "www.midjourney.com",
            "Method": "GET",
            "Path": "/showcase/recent/",
            "Scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6",
            "Cache-Control": "max-age=0",
            "Cookie": "_ga=GA1.1.955629140.1683864020; cf_clearance=7PkkA_wQ9cjtBQ1kFYk8lRcZ.rnmUCqRkm6.FKSj0jg-1683876813-0-250; __stripe_mid=1b584c86-31c7-459f-9e1c-457387dc547dd5f105; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.midjourney.com; __Host-next-auth.csrf-token=e724ad07371e605057eeac18348f271d28505af83ba829c3aa1feabed97a87e0%7Cdb9fb7ac87ef7d61f171a5517e226275f91bf401b705a48df40772a3c4f288f9; imageSize=medium; imageLayout_2=hover; getImageAspect=2; fullWidth=false; showHoverIcons=true; _ga_Q0DQ5L7K0D=GS1.1.1685442707.18.0.1685442707.0.0.0; _dd_s=rum=0&expire=1685443607590",
            "Sec-Ch-Ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }

# 登录使用的cookie,大号疏浅
LOGIN_COOKIES_shuqian = [{'domain': '.xiaohongshu.com', 'expiry': 1687439201, 'httpOnly': True, 'name': 'customerBeakerSessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'dd47dd58415f53bf2189c973d54af93c8809a323gAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAVgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2SLDOKRqf1gJAAAAYXV0aFRva2VucQNYQQAAADdmZDYwY2YwNzY0MDQ5ZWM5YjYyZGQ5Zjc0YzE1ZTMxLTlmZWE5MmE4NjY0YjQ2NWJhNjkwZWY1MWM0YmJjMDZjcQRYAwAAAF9pZHEFWCAAAABiMjRhYjU5YzA5NWM0MDM3OTQzOTVlMjY3YmRkZWRhZnEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZIsM4pGp/WAYAAAB1c2VySWRxCFgYAAAANWQ4OTUyMTQwMDAwMDAwMDAxMDA2ZjVhcQlYAwAAAHNpZHEKWBgAAAA2NDhiMGNlMjY0MDAwMDAwMDAwMDAwMDRxC3Uu'}]

# 登录使用的cookie，小熊猫号
LOGIN_COOKIES_little_pandas = [
    {'domain': '.xiaohongshu.com', 'expiry': 1718423460, 'httpOnly': False, 'name': 'galaxy.creator.beaker.session.id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1686887451149029307728'},
    {'domain': '.xiaohongshu.com', 'expiry': 1718423460, 'httpOnly': True, 'name': 'access-token-creator.xiaohongshu.com', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'customer.ares.AT-81f9a484ef4f4a71ab3d99de0b86e3ba-71ef358708fa4d38ab87c022340e7e70'},
    {'domain': '.xiaohongshu.com', 'expiry': 1718423450, 'httpOnly': True, 'name': 'x-user-id-creator.xiaohongshu.com', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '604d7d7e00000000010087a8'},
    {'domain': '.xiaohongshu.com', 'expiry': 1718423450, 'httpOnly': False, 'name': 'galaxy_creator_session_id', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'dJQkycNjthz5JzmTW272IWMzXmdgxERuNxwm'},
    {'domain': '.xiaohongshu.com', 'expiry': 1687492251, 'httpOnly': True, 'name': 'customerClientId', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '414630736960747'},
    {'domain': '.xiaohongshu.com', 'expiry': 1687492251, 'httpOnly': True, 'name': 'customerBeakerSessionId', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '51372280a6eeaa9360385e09406733570e9279ddgAJ9cQAoWBAAAABjdXN0b21lclVzZXJUeXBlcQFLAVgOAAAAX2NyZWF0aW9uX3RpbWVxAkdB2SL3BlPXClgJAAAAYXV0aFRva2VucQNYQQAAADk5ODI3OWJlMjE0NTRmYjBhYTFhMDA3YjhiM2Y4NTg4LWY3MDZhZjE0NGYyNTQ5Zjg4NjcwYjBlMjU5OWYxY2Y3cQRYAwAAAF9pZHEFWCAAAABiYTFjNDFiMTJkMjc0NTQ3ODU4OGE0ZmUxNjk3MTJmZnEGWA4AAABfYWNjZXNzZWRfdGltZXEHR0HZIvcGU9cKWAYAAAB1c2VySWRxCFgYAAAANjA0ZDdkN2UwMDAwMDAwMDAxMDA4N2E4cQlYAwAAAHNpZHEKWBgAAAA2NDhiZGMxOTY0MDAwMDAwMDAwMDAwMDJxC3Uu'},
]
