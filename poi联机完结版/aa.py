from PIL import Image

img_src = Image.open('./img/map1/PD.gif')
img_src = img_src.convert('RGBA')
src_strlist = img_src.load()
for x in range(1, 500):
    color = src_strlist[x, 700]
    print(color)
