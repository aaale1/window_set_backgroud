# window_set_backgroud
一个突发奇想，想要实时将bing的网页背景设置为电脑屏幕背景的自动程序

bing-wallpaper.py文件里面包含三个部分，一个是爬虫，从cn.bing爬取背景，在其中设置了try except语句，因为得到了链接不规范，有的是前面多了"https"，有的是自带"s.cn.bing,net\"，目前也只发现这两种不规范的格式；之后代码会根据网址爬取图片并保存在本地；最后是更改系统配置自动更改壁纸。所以只要运行一下，代码就会更改电脑的壁纸，很方便。
在代码中，为了方便debug，加入了logging库，会自动保存当次运行时图片的网址、更改系统配置时的状态。如下是一次示例：具体在后面会解释。

2023-05-16 16:03:09,428 - INFO - Downloading image from  https://www.bing.com/th?id=OHR.AmericanWetlands_ZH-CN7534567518_1920x1080.webp&qlt=50

2023-05-16 16:03:09,725 - INFO - 0

2023-05-16 16:03:09,726 - INFO - 1459

最后，这个代码是可行的，我手动以及cmd中运行能完美的更改壁纸，注意，其中的文件路径均是相对路径，只有log.txt为绝对路径。

ok，经过多次的失败实践，这个计划算是已经结束了。
刚开始的想法是用actions去自动运行代码，但在debug完运行之后，恍然发现，这是在服务器上自动运行的，代码完全无法直接为本地更换壁纸。后来想去更改window的计划程序，实现每天第一次开机自动运行代码，但是通过计划程序时，依旧在更改电脑壁纸时出现了问题，就像上面的示例一样，显示0则表示更改壁纸失败，1459是错误代码，反复更改过计划程序的各种选项，但还是失败了，原因未知。

所以，现在可行的方法大概是手动运行代码，或者在代码中加入休眠1天的语句，在命令行中运行。当然，后面的方法我也没试过。

有任何问题欢迎一起讨论，或者如果大佬有时间在指导计划程序失败的原因就更好了！
