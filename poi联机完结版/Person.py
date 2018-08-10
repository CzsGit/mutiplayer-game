import time
import pygame
from PIL import Image

LONGMOVE = 100
JUMPMOVE = 80
SHORTMOVE = 7
WIN_LONG = 1500
WIN_WIDTH = 800
person_length = 64
person_width = 64
HAVEGUN = False


class Persondo(object):
    def __init__(self, person_x, person_y):
        self.person_x = person_x
        self.person_y = person_y
        self.img_src = Image.open('./img/map1/PD.gif')
        self.img_src = self.img_src.convert('RGBA')
        self.src_strlist = self.img_src.load()
        self.lv = 0

    def changePD(self):
        self.img_src = Image.open('./img/map2/PD.gif')
        self.img_src = self.img_src.convert('RGBA')
        self.src_strlist = self.img_src.load()
        print('更改判定图为：', self.img_src)

    # def border(self):
    #     if self.person_x == 0 or self.person_x == WIN_LONG - person_length or self.person_y == 0 or self.person_y == WIN_WIDTH - person_width:
    #         return True
    #     else:
    #         return False
    def getgun(self):

        # color1 = self.src_strlist[self.person_x + 45, self.person_y + 55]
        # color2 = self.src_strlist[self.person_x + 10, self.person_y + 55]
        #
        # if color1 == (0, 0, 255, 255) or color2 == (0, 0, 255, 255):
        #     HAVEGUN=True
        print(self.person_x)
        if self.person_x > 700 and self.person_x < 760:
            if self.person_y > 400 and self.person_y < 450:
                global HAVEGUN
                HAVEGUN = True
                global bullet_num
                bullet_num = 20

    def bul_num(self):
        if HAVEGUN == True:
            global bullet_num
            bullet_num -= 1
            print(bullet_num)
            if bullet_num < 0:
                global HAVEGUN
                HAVEGUN = False

    def island(self):
        while True:

            color1 = self.src_strlist[self.person_x + 55, self.person_y + 55]
            color2 = self.src_strlist[self.person_x + 10, self.person_y + 55]

            if color1 != (255, 255, 255, 255) or color2 != (255, 255, 255, 255):
                break
            self.person_y += 1
        return self.person_x, self.person_y

    def notgoright(self):
        for i in range(5):
            colorright = self.src_strlist[self.person_x + 60, self.person_y]
            print(colorright)
            if colorright == (0, 255, 0, 255):
                print(colorright)
                return self.person_x, self.person_y
            else:
                self.person_x += 1
        return self.person_x, self.person_y

    def up(self):

        for i in range(LONGMOVE):
            self.person_y -= 1
            self.getgun()
        return self.person_x, self.person_y
        # if border(self.person_x,self.person_y):
        #     return return self.person_x,self.person_y
        # else:
        #     return False

    def down(self):
        # if self.person_y + person_width >= 736:
        #     self.person_y += 0
        #     return self.person_x, self.person_y
        # else:
        #     self.person_y += LONGMOVE
        return self.person_x, self.person_y
        # if border(self.person_x,self.person_y):
        #     return self.person_x,self.person_y
        # else:
        #     return False

    def right(self):
        # if self.person_x + person_length >= 1500:
        #     self.person_x += 0
        #     return self.person_x, self.person_y
        # else:
        #     self.person_x += SHORTMOVE
        #     self.island()
        #     return self.person_x, self.person_y
        self.island()
        for i in range(7):
            colorright = self.src_strlist[self.person_x + 60, self.person_y]
            print(colorright)
            if colorright == (0, 255, 0, 255):
                print(colorright)
                return self.person_x, self.person_y
            else:
                self.person_x += 1
                self.getgun()
        return self.person_x, self.person_y

        # if border(self.person_x, self.person_y):
        #     return return self.person_x,self.person_y
        # else:
        #     return False

    def left(self):
        # if self.person_x <= 0:
        #     self.person_x += 0
        #     return self.person_x, self.person_y
        # else:
        #     self.person_x -= SHORTMOVE
        #     self.island()
        #     return self.person_x, self.person_y
        self.island()
        for i in range(7):
            colorright = self.src_strlist[self.person_x, self.person_y]
            print(colorright)
            if colorright == (0, 255, 0, 255):
                print(colorright)
                return self.person_x, self.person_y
            else:
                self.person_x -= 1
                self.getgun()
        return self.person_x, self.person_y
        # if border(self.person_x, self.person_y):
        #     return return self.person_x,self.person_y
        # else:
        #     return False

    def jumpleft(self):
        self.island()
        for i in range(80):
            colorright = self.src_strlist[self.person_x, self.person_y - 100]
            print(colorright)
            if colorright == (0, 255, 0, 255):
                print(colorright)
                return self.person_x, self.person_y
            else:
                self.person_x -= 1
                self.getgun()
        return self.person_x, self.person_y

    def jumpright(self):
        self.island()
        for i in range(80):
            colorright = self.src_strlist[self.person_x + 60, self.person_y - 100]
            print(colorright)
            if colorright == (0, 255, 0, 255):
                print(colorright)
                return self.person_x, self.person_y
            else:
                self.person_x += 1
                self.getgun()
        return self.person_x, self.person_y

    def move_to(self, keypas, p1x, p1y):

        if keypas[pygame.K_w] and keypas[pygame.K_a]:  # 左上
            self.p1x, self.p1y = self.jumpleft()
            time.sleep(0.3)
            self.p1x, self.p1y = self.up()

            return self.p1x, self.p1y

        elif keypas[pygame.K_w] and keypas[pygame.K_d]:  # 右上
            self.p1x, self.p1y = self.jumpright()
            time.sleep(0.3)
            self.p1x, self.p1y = self.up()
            return self.p1x, self.p1y
        elif keypas[pygame.K_w]:
            time.sleep(0.3)
            self.p1x, self.p1y = self.up()
            return self.p1x, self.p1y  # 上移动
        elif keypas[pygame.K_a]:
            p1x, p1y = self.left()
            return p1x, p1y  # 左移动
        elif keypas[pygame.K_s]:
            p1x, p1y = self.down()
            return p1x, p1y  # 下移动
        elif keypas[pygame.K_d]:
            p1x, p1y = self.right()
            return p1x, p1y  # 右移动

    def move_down(self, p1x, p1y):
        time.sleep(0.1)
        self.p1x, self.p1y = self.island()
        print('daozheli')
        return self.p1x, self.p1y

# class Bulletdo(object):
#     def __init__(self,bullet_x,bullet_y):
#         self.can_shoot=True
#         self.direction='right'
#         self.bullet_x=bullet_x
#         self.bullet_y=bullet_y
#     def shoot(self):
#         if self.can_shoot==True:
#             if self.direction=='up' and self.bullet_y > 0:
#                 # while True:
#                 #     self.bullet_y-=1
#                 #     if self.bullet_y<=0:
#                 #         break
#                 self.bullet_y-=1
#             if self.direction=='down' and self.bullet_y < WIN_WIDTH:
#                 self.bullet_y+=1
#             if self.direction == 'left' and self.bullet_x > 0:
#                 self.bullet_x -= 1
#             if self.direction == 'right' and self.bullet_x < WIN_LONG:
#                 self.bullet_x += 1
#             if self.direction == 'rightup' and self.bullet_x < WIN_LONG and self.bullet_y > 0:
#                 self.bullet_x += 1
#                 self.bullet_y -= 1
#             if self.direction == 'rightdown' and self.bullet_x < WIN_LONG and self.bullet_y < WIN_WIDTH:
#                 self.bullet_x += 1
#                 self.bullet_y += 1
#             if self.direction == 'leftup' and self.bullet_x > 0 and self.bullet_y > 0:
#                 self.bullet_x -= 1
#                 self.bullet_y -= 1
#             if self.direction == 'leftdown' and self.bullet_x > 0 and self.bullet_y < WIN_WIDTH:
#                 self.bullet_x -= 1
#                 self.bullet_y += 1
#             return self.bullet_x,self.bullet_y
#         else:
#             return False
#     def get_gun(self):
#         self.can_shoot=True
#
#     def shoot_up(self):
#         self.direction='up'
#         return self.direction
#
#     def shoot_down(self):
#         self.direction='down'
#         return self.direction
#
#     def shoot_right(self):
#         self.direction='right'
#         return self.direction
#
#     def shoot_left(self):
#         self.direction='left'
#         return self.direction
#
#     def shoot_leftup(self):
#         self.direction='leftup'
#         return self.direction
#
#     def shoot_rightup(self):
#         self.direction='rightup'
#         return self.direction
#
#     def shoot_leftdown(self):
#         self.direction='leftdown'
#         return self.direction
#
#     def shoot_rightdown(self):
#         self.direction='rightdown'
#         return self.direction
