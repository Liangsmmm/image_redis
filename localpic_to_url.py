import cv2
import io
import os
import sys
from PIL import Image
#os.environ['DJANGO_SETTINGS_MODULE']= 'detect.settings'
#import django
#django.setup()
#settings.configure()

#from django.core.cache import cache






def pic_to_bytes(path, url_name):
    img_url = path
    try:
        with open(img_url, 'rb') as f:
            a = f.read()
    except FileNotFoundError as e:
        return 0

    print(type(a))
    # 将字节对象转为Byte字节流数据,供Image.open使用
    byte_stream = io.BytesIO(a)
    sImg = Image.open(byte_stream)
    from io import BytesIO as StringIO
    out = StringIO()
    sImg.save(out,format="png")
    res = out.getvalue()
    return res
    '''
    cache.set("photoPic_{}".format(url_name), res, timeout=60 * 10)
    url = "http:*.*.*.*:port/avatardownload/photoPic_{}/".format(url_name)
    return url
    '''













# local pic to url
def make_pic_url(img_path, url_name):
    from io import BytesIO as StringIO

    image = cv2.imread(img_path)
    #filename = os.path.basename(img_path)
    out = StringIO()
    image.save(out,format="png")  # 也可以用srcFile原路径保存,或者更改后缀保存，save这个函数后面可以加压缩编码选项JPEG之类的
    res_pic =  out.getvalue()
    #cache.set("photoPic_{}".format(url_name), image, timeout=60 * 10)
    cache.set("photoPic_{}".format(url_name), res_pic, timeout=60 * 10)
    url = "http:*.*.*.*:port/avatardownload/photoPic_{}/".format(url_name)
    return url



if __name__ == "__main__":
    url = pic_to_bytes('2018-06-27-16-06-57.jpg','a')
    print(url)
