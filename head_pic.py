# coding:utf-8
import hashlib
# 导入图像相关模块
from PIL import Image, ImageDraw

# 根据字符串生成5*5的0，1矩阵
def to_hash_array(str_):
    row=5   # 行数
    col=5   # 列数
    hash_str = hashlib.md5(str_).hexdigest()
    binary_str = bin(int(hash_str,16))[2:][:60:4]
    
    # 创建二维列表
    arr = [[0] * col for i in range(row)]

    for x, y, i in [(i%row, i%((col+1)/2), binary_str[i]) for i in range(len(binary_str))]:
        arr[x][y] = int(i)
        arr[x][row - 1 - y] = int(i)
    return arr

# 根据字符串的hash生成颜色值
def get_hash_color(str):
    hash_str = hashlib.md5(str).hexdigest()
    r = int(hash_str[:2],16)
    g = int(hash_str[6:8],16)
    b = int(hash_str[12:14],16)
    return (r,g,b)

# 根据hash生成图片
def get_hash_image(str='default',width=250,height=250,rect_width=50,rect_height=50):
    #背景颜色
    bgcolor = (255,255,255)
    #方块颜色
    rectcolor = get_hash_color(str)
    #生成背景图片
    image = Image.new('RGB',(width,height),bgcolor)
    #产生draw对象，draw是一些算法的集合
    draw = ImageDraw.Draw(image)

    arr = to_hash_array(str)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            fill = rectcolor if arr[i][j] == 1 else None
            draw.rectangle((j*rect_width,i*rect_height,(j+1)*rect_width,(i+1)*rect_height),fill=fill)
    # 释放draw
    del draw
    return image


img = get_hash_image()
img.save('1234_1.jpeg')
