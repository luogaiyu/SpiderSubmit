import urllib.request
url = 'https://cdn.midjourney.com/77c34660-3810-4e56-9ebb-ae1569f18904/0_0_640_N.webp'
filename = 'example.html'

headers = {
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
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
data = response.read()

# 写入到文件
with open('image.jpg', 'wb') as f:
    f.write(data)

# req = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(req)
# img = response.read()
# print(img)
# # 将数据转换为PIL Image对象
# img = Image.fromarray(np.uint8(img))
#
# # 保存图片
# img.save(r'D:\Desktop\workRelated\chatgpt\pythonProject1\code\data\img\image.png')

# print(html)