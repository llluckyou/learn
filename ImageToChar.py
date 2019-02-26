import numpy as np
from PIL import Image

if __name__ == "__main__":
    image_file = 'dx.jpg'
    height = 100

    img = Image.open(image_file)
    img_width, img_height = img.size
    width = 2 * height * img_width // img_height

    img = img.resize((width, height), Image.ANTIALIAS)   # 按照计算的宽高进行resize

    pixels = np.array(img.convert("L"))                  # 将图片转化为灰度图

    chars = "MNHQ$OC?7>!:-;. "                           # 用来绘图的符号集

    step = 256 / len(chars)                              # 根据像素值划分区段

    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[int (pixels[i][j] // step)]
        result += "\n"

    with open("text.txt", mode="w") as f:
        f.write(result)
