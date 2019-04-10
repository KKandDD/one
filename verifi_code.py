import tesserocr
from PIL import Image

image = Image.open('code.jpg')
# 参数L，即可将图片转化为灰度图像
image = image.convert('L')
# 二值化阈值设置为127
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)