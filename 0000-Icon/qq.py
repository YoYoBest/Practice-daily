# coding=gbk

from PIL import Image, ImageDraw, ImageFont

# print(ImageFont.__file__)

#����ͼƬ����
headImage = Image.open('D:/Python projects/Exercise-01/header.jpg')  #��ͼƬ

#��ȡͼƬ����Ŀ��
w,h = headImage.size

#�����������
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',int(h/4))  #���Ҳ������壬����س��򻹻���Windows fonts /Ŀ¼�в���


# #ͼƬ��ģʽ
# ImageFont.mode
#
# #ͼƬ�ĸ�ʽ
# ImageFont.format


#����Բ��
#ImageDrawģ��ΪImage�����ṩ�򵥵�2Dͼ�Ρ�������ʹ�ø�ģ����������ͼ��ע�ͻ���������ͼ���Լ���ʱ����ͼ���Թ�Webʹ�á�
#ImageDraw.Draw.pieslice()��Բ����ͬ
ImageDraw.Draw(headImage).pieslice([(w/3*2,0),(w,h/3)],0,360,fill='red')
#ImageDraw.Draw.text()�ڸ���λ�û����ַ�����
ImageDraw.Draw(headImage).text((w*0.76,h*0.02),'3',font = font, fill = 'white')

#չʾ���ƽ��(ʹ��ϵͳĬ�ϵ�ͼƬ�����)
headImage.show()

#������ƽ��
headImage.save('D:/Python projects/Exercise-01/wode.jpg')

