import ctypes
import requests
import re


# 获取bing的网页背景图片的链接
url = "https://cn.bing.com"
rs = requests.get(url=url)
html = rs.content.decode("utf-8")
pattern = r'<link rel="preload" href="(.*?)" as="image" id="preloadBg" />' # 定义匹配模式
match = re.search(pattern, html) # 搜索匹配结果
img_url = "https://cn.bing.com" + match.group(1) # 获取第一个括号内的内容



# 下载图片到本地
img_rs = requests.get(url=img_url)
img_path = "E:\\bing-wallpaper-pictures\\bing_wallpaper.jpg" # 你可以修改图片的保存路径
with open(img_path, "wb") as f:
    f.write(img_rs.content)

# 更改壁纸
SPI_SETDESKWALLPAPER = 20 # 系统参数，表示设置壁纸
SPIF_UPDATEINIFILE = 1 # 系统参数，表示更新配置文件
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path, SPIF_UPDATEINIFILE) # 调用系统函数更改壁纸
