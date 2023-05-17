import ctypes
import requests
from lxml import etree
import logging
import subprocess

logging.basicConfig(level=logging.INFO, filename='log.txt', filemode='a',format='%(asctime)s - %(levelname)s - %(message)s')

# 获取bing的网页背景图片的链接
url = "https://cn.bing.com"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35"}
rs = requests.get(url=url, headers=headers)
html = etree.HTML(rs.content)
try:
    img_url = "https://www.bing.com" + html.xpath('//link[@id="preloadBg"]/@href')[0]  # 获取第一个括号内的内容
    img_url = img_url.replace("s.cn.bing.net", "")
    img_rs = requests.get(url=img_url)
except:
    img_url = "https://www.bing.com" + html.xpath('//link[@id="preloadBg"]/@href')[0][6:]  # 获取第一个括号内的内容
    img_url = img_url.replace("s.cn.bing.net", "")
    img_rs = requests.get(url=img_url)

logging.info('Downloading image from  ' + img_url)

# 下载图片到本地
img_path = "E:\\bing-wallpaper-pictures\\bing_wallpaper.jpg"  # 你可以修改图片的保存路径
with open(img_path, "wb") as f:
    f.write(img_rs.content)

# 更改壁纸
SPI_SETDESKWALLPAPER = 20 # 系统参数，表示设置壁纸
SPIF_UPDATEINIFILE = 1 # 系统参数，表示更新配置文件
result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINIFILE)
error_code = ctypes.GetLastError()



logging.info(result)
logging.info(error_code)
