import pygame


def loadY(filename):
    '''
    :param filename: 音乐文件
    :return: 频道对象  音乐对象  return[0].play(return[1])
    '''
    pygame.mixer.init()

    mu = pygame.mixer.Sound(filename)

    pind_ = pygame.mixer.find_channel(True)

    return [pind_, mu]
