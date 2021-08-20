from PIL import Image,ImageDraw,ImageFont

createImage = Image.open('D:/Python projects/Practice-daily-01-icon/header.jpg')

w,h = createImage.size

createFont = ImageFont.truetype('C:/Windows/Fonts/Arial')

drawImage = ImageDraw.Draw

ImageDraw.Draw(createImage).pieslice([(w/3*2,0),(w,h/3)],0,360,fill='red')
ImageDraw.Draw(createImage).text('(w*0.76,h*0.02)','3',font=createFont,fill='write')

createImage.show()

createImage.save('D:/Python projects/Practice daily-01-icon/header_copy.jpg')