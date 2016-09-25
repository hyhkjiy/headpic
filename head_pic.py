# coding:utf-8
import hashlib
# 导入图像相关模块
from PIL import Image,ImageDraw

# 根据字符串生成5*5的0，1矩阵
def to_hash_array(str):
    hash_str = hashlib.md5(str).hexdigest()
    binary_str = bin(int(hash_str,16))[2:][:64]
    
    # print binary_str

    arrs = [[0] * 5,[0] * 3]
    for i in range(5):
        arrs[0][i] = int(binary_str[i*3])

    for i in range(2):
        arrs[1][i] = int(binary_str[i*3])

    arrs2 = [([0] * 3) for i in range(5)]

    for i in range(5):
        for j in range(3):
            arrs2[i][j] = arrs[0][i]|arrs[1][j]

    arrs3 = [([0] * 5) for i in range(5)]
    for i in range(5):
        for j in range(3):
            arrs3[i][4-j] = arrs2[i][j]
            arrs3[i][j] = arrs2[i][j]
    return arrs3


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
            #fill = (arr[i][j] == 1) ? rectcolor : None
            fill = None
            if arr[i][j] == 1:
                fill = rectcolor
            draw.rectangle((j*rect_width,i*rect_height,(j+1)*rect_width,(i+1)*rect_height),fill=fill)
    # 释放draw
    del draw
    return image


img = get_hash_image('123123')
img.save('1234_1.jpeg')

# from datetime import datetime
# import time
# def get_file_name():
#    timestamp = str(int(time.mktime(datetime.utcnow().timetuple())))
#    file_name = 'head_pic_'+timestamp+'.jpge'
#    return file_name
# print get_file_name()

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))
# head_dir = basedir + '\\project\\static\\images\\heads\\'
# print head_dir