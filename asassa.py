import PIL
from PIL import Image,ImageDraw,ImageFont
im = Image.open("C:\\Users\\dell\\Desktop\\abc.jpg")
draw=ImageDraw.Draw(im)
font1=ImageFont.truetype("arial.ttf",50)
Point=(100,100)
String="abc"
draw.text(Point,String,"white",font=font1)
im.show()
"""(im.format)
print(im.mode)
print(im.size)
print(im.height)
print(im.info)
im.save("sumit.jpg")
img=Image.open("C:\\Users\\dell\\Desktop\\abcd.jpeg")
img.show()"""
