# coding:utf-8
import sys,time,os

# 这个是图片保存本地的路径
# log_path是存放图片的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
img_path = os.path.join(os.path.dirname(cur_path), 'Img')
# 如果不存在这个Img文件夹，就自动创建一个
if not os.path.exists(img_path):os.mkdir(img_path)


def get_screen(self,driver):
    u'截图'
    nowTime = time.strftime('%Y_%m_%d_%H_%M_%S')
    driver.get_screenshot_as_file('%s.jpg' % nowTime)


def screen(self,func):
    def inner(*args, **kwargs):
        try:
            f = func(*args, **kwargs)
            return f
        except:
            self.get_screen()
            raise
    return inner

class Screenshot(object):

    def __init__(self,driver):
        self.driver=driver

    def __call__(self, f):

        def inner(*args):
            try:
                return f(*args)
            except Exception as e:
                import time
                nowTime=time.strftime('%Y_%m_%d_%H_%M_%S')
                self.driver.get_screenshot_as_file('%s/%s.jpg'%(img_path,nowTime))
                with open('/Users/Macx/PycharmProjects/GYL_project/Log/BaseException.log', 'w+') as file:
                    file.write(str(e))
                raise
        return inner

def Screen1(self,func):
    def inner(*args, **kwargs):
        try:
            f = func(*args, **kwargs)
            return f
        except:
            self.get_screen()
            raise
    return inner