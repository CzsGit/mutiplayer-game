import pygame
import Person
import time
from Bullet import *
from imgload_ import *

# p1x = 400  # 620  60   |   780  60  | 950  500 |  490  520  map1.gif
# p1y = 520
# persondo=Person.Persondo(p1x,p1y)
# def move_to(keypas, p1x, p1y):
#
#     if keypas[pygame.K_w] and keypas[pygame.K_a]:  # 左上
#         persondo.p1x, persondo.p1y = persondo.jumpleft()
#         time.sleep(0.3)
#         persondo.p1x, persondo.p1y = persondo.up()
#
#         return persondo.p1x, persondo.p1y
#     elif keypas[pygame.K_w] and keypas[pygame.K_d]:  # 右上
#         persondo.p1x, persondo.p1y = persondo.jumpright()
#         time.sleep(0.3)
#         persondo.p1x, persondo.p1y = persondo.up()
#         return persondo.p1x, persondo.p1y
#     elif keypas[pygame.K_w]:
#         time.sleep(0.3)
#         persondo.p1x,persondo.p1y=persondo.up()
#         return persondo.p1x, persondo.p1y  # 上移动
#     elif keypas[pygame.K_a]:
#         p1x,p1y=persondo.left()
#         return p1x, p1y  # 左移动
#     elif keypas[pygame.K_s]:
#         p1x,p1y=persondo.down()
#         return p1x, p1y  # 下移动
#     elif keypas[pygame.K_d]:
#         p1x,p1y=persondo.right()
#         return p1x, p1y  # 右移动
#
#
#
# def move_down(p1x,p1y):
#     time.sleep(0.1)
#     persondo.p1x, persondo.p1y = persondo.island()
#     print('daozheli')
#     return persondo.p1x, persondo.p1y


keynum = 0
F_direction = 'right'
F_img = '0'
F_keypas = '0'


def fire_to(keypas):
    # direction = shoot_leftdown()
    # img = Load_('./img/q1/q1LD.gif')
    # return [direction, img]

    global keynum
    global F_direction
    global F_img
    # print('进入fire_to')
    if F_keypas == keypas:
        if keynum > 0:
            # print('{} 快速加载中'.format(keynum))
            return [F_direction, F_img]
    else:

        if keypas[pygame.K_LEFT] and keypas[pygame.K_UP]:  # 左上
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_leftup()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1LU.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_LEFT] and keypas[pygame.K_DOWN]:  # 左下

            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_leftdown()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1LD.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_RIGHT] and keypas[pygame.K_UP]:  # 右上
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_rightup()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1RU.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_RIGHT] and keypas[pygame.K_DOWN]:  # 右下
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_rightdown()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1RD.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_LEFT]:  # 左
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_left()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1L.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_RIGHT]:  # 右
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_right()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1R.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_UP]:  # 上
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_up()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1U.gif')
                F_direction = direction
                F_img = img

            return [direction, img]

        elif keypas[pygame.K_DOWN]:  # 下
            # print(keynum)
            if keynum > 10:
                keynum = 0
                return [F_direction, F_img]
            else:
                keynum += 1
                # print(keynum)
                direction = shoot_down()
                # print('进入图片加载函数')
                img = Load_('./img/q1/q1D.gif')
                F_direction = direction
                F_img = img

            return [direction, img]
