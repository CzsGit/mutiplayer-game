import pygame

F_IMG = '0'  # 上一个图片名
F_RETURN = '0'  # 上一个返回的img
i = 0


def Load_(filename):
    # print('开始加载图片')
    global F_IMG
    global F_RETURN
    if filename == F_IMG:
        # print('快速加载')
        return F_RETURN
    # print('正常加载')
    global i
    i += 1
    img = pygame.image.load(filename).convert()  # 加载图片
    img.set_colorkey((255, 255, 255))  # 透明处理
    # img.set_colorkey((0, 0, 255))
    # if i > 5:
    #     print('图片加载{}'.format(filename))  # 发送正在加载打图片
    F_IMG = filename
    F_RETURN = img

    return img
