# coding=gbk

from PIL import Image, ImageDraw, ImageFont

# print(ImageFont.__file__)

#创建图片对象
headImage = Image.open('D:/Python projects/Exercise-01/header.jpg')  #打开图片

#获取图片对象的宽高
w,h = headImage.size

#创建字体对象
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',int(h/4))  #若找不到字体，则加载程序还会在Windows fonts /目录中查找


# #图片的模式
# ImageFont.mode
#
# #图片的格式
# ImageFont.format


#绘制圆形
#ImageDraw模块为Image对象提供简单的2D图形。您可以使用该模块来创建新图像，注释或修饰现有图像，以及即时生成图形以供Web使用。
#ImageDraw.Draw.pieslice()与圆弧相同
ImageDraw.Draw(headImage).pieslice([(w/3*2,0),(w,h/3)],0,360,fill='red')
#ImageDraw.Draw.text()在给定位置绘制字符串。
ImageDraw.Draw(headImage).text((w*0.76,h*0.02),'3',font = font, fill = 'white')

#展示绘制结果(使用系统默认的图片浏览器)
headImage.show()

#保存绘制结果
headImage.save('D:/Python projects/Exercise-01/wode.jpg')

