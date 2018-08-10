import time
import signal
import os
import pygame
import random
import Person
import client
import fire_move
from Bullet import *
from imgload_ import *  # 图片加载
from music import *  # 音乐加载
from greenlet import greenlet
from multiprocessing import *
from threading import Thread

# from fire_move import *  # 开火方向和移动的函数

def play_music():
    pygame.mixer.init()

    mu = pygame.mixer.Sound('./yinyue/01.wav')
    

    pind= pygame.mixer.find_channel(True)
    while True:

        pind.play(mu)
        time.sleep(60)
        # print('播放音乐')
    # backgroundM[0].play(backgroundM[1])


def updata(person_x, person_y, plat, background):
    root = pygame.display.set_mode((1500, 800),pygame.HWSURFACE | pygame.DOUBLEBUF)  # 双缓冲窗口, pygame.HWSURFACE | pygame.DOUBLEBUF
    pygame.display.set_caption('poi')

    ##########################################

    # 图片加载

    person_img = Load_('./img/guang.gif')
    person_gun_one = Load_('./img/q1/q1R.gif')
    person_gun_two = Load_('./img/q1/q1R.gif')
    # person_gun_one = Load_('./img/q1/q1R.gif')
    # # print(person_gun_one)
    bullet_img = Load_('./img/q1/zd1.gif')
    root.blit(background, (0, 0))
    root.blit(plat, (0, 0))
    person_coord = (person_x, person_y)
    root.blit(person_img, person_coord)
    if Person.HAVEGUN:
        # print(Person.HAVEGUN)
        # # print(person_gun_one)
        root.blit(person_gun_one, (person_x + 20, person_y + 30))

    ########################################################

    # 刷新
    pygame.display.flip()  # 交替刷新　uptate 是覆盖　这个适用双缓存


def main():
    # 接受客户端信息
    # p2list = []
    # backgroundM = loadY('./yinyue/bg.ogg')  # 背景音乐变量
    

    pygame.init()

    root = pygame.display.set_mode((1500, 800),pygame.HWSURFACE | pygame.DOUBLEBUF)  # 双缓冲窗口, pygame.HWSURFACE | pygame.DOUBLEBUF
    pygame.display.set_caption('poi')

    ##########################################

    # 图片加载
    background = Load_('./img/bg1.gif')
    plat = Load_('./img/map1/map1.gif')
    person_img = Load_('./img/p1/p1L.gif')
    person_gun_one = Load_('./img/q1/q1R.gif')
    # print(person_gun_one)
    bullet_img = Load_('./img/q1/zd1.gif')
    shunyi = Load_('./img/guang.gif')
    
    START = Load_('./img/START.gif')
    WIN = Load_('./img/WIN.gif')
    LOST = Load_('./img/LOST.gif')
    begin_person_gun = Load_('./img/q1/q1RU.gif')

    AKF = loadY('./yinyue/AKF.wav')  # 开火音效  AKF[0].paly(AKF[1])
    # 固定位置随机
    # location = [(400, 520), (590, 60), (790, 60), (960, 500)]
    # person_x, person_y = random.choice(location)
    # persondo = Person.Persondo(person_x, person_y)
    # person_x, person_y = persondo.island()

    # 全地图随机位置
    person_x=random.randint(100,1390)
    person_y=random.randint(100,690)
    persondo = Person.Persondo(person_x, person_y)
    person_x,person_y=persondo.island()
    old_bullet_x, old_bullet_y = 0, 0
    old_bullet_x2, old_bullet_y2 = 0, 0

    bullet_x = person_x + 32
    bullet_y = person_y + 35
    FPS = pygame.time.Clock().tick()

    # 移动计数
    Lmove_time = 0
    Rmove_time = 0
    Last_move = 0
    # 音乐
   

    direction = 'right'

    # bullet = DoSomething.Bulletdo(bullet_x, bullet_y)
    def bullet_img_direction(bullet_img_or_qiang, bullet_x, bullet_y):

        root.blit(bullet_img_or_qiang, (bullet_x, bullet_y))
        pygame.display.flip()
        return bullet_x, bullet_y

    def person_direction(direction, person_x, person_y, bullet_img_or_qiang, bullet_x, bullet_y):

        FPS = 30
        root.blit(background, (0, 0))
        root.blit(plat, (0, 0))
        person_coord = (person_x, person_y)
        root.blit(person_img, person_coord)

        root.blit(bullet_img_or_qiang, (bullet_x, bullet_y))
        if Person.HAVEGUN:
            if direction == 'right':
                root.blit(person_gun_one, (person_x + 20, person_y + 30))
            if direction == 'left':
                root.blit(person_gun_one, (person_x, person_y + 30))
            if direction == 'up':
                root.blit(person_gun_one, (person_x + 10, person_y + 10))
            if direction == 'down':
                root.blit(person_gun_one, (person_x + 20, person_y + 30))
            if direction == 'rightup':
                root.blit(person_gun_one, (person_x + 20, person_y + 20))
            if direction == 'leftdown':
                root.blit(person_gun_one, (person_x + 10, person_y + 30))
            if direction == 'leftup':
                root.blit(person_gun_one, (person_x, person_y + 20))
            if direction == 'rightdown':
                root.blit(person_gun_one, (person_x + 20, person_y + 30))
        return bullet_x, bullet_y

    while True:
        client.func()
        s = client.fooc()
        
        while True:
            # sendlist = [fire_move.person_x, fire_move.person_y, bullet_x, bullet_y, 0, 0, 0, 0]
            # backgroundM[0].play(backgroundM[1])  # 加载背景音乐
             
            # AKST = loadY('./yinyue/AKST.wav')  # 捡到枪的上膛音效  AKST[0].paly(AKST[1])
            
            
            FPS = 60

            keypas = pygame.key.get_pressed()  # 274 275 276 277

            # # print(keypas)
            #######################################################
            if keypas[pygame.K_m]:
                os.kill(os.getpid(),signal.SIGKILL)
            # 移动
            if (keypas[pygame.K_w] and keypas[pygame.K_a]) or (keypas[pygame.K_w] and keypas[pygame.K_d]) or keypas[
                pygame.K_w]:
                person_x, person_y = persondo.move_to(keypas, person_x, person_y)
                updata(person_x, person_y, plat, background)
                time.sleep(0.1)
                person_x, person_y = persondo.move_down(person_x, person_y)

                # 移动走路动画
            elif keypas[pygame.K_a] or keypas[pygame.K_s] or keypas[pygame.K_d]:
                if keypas[pygame.K_a]:
                    Last_move = "L"
                    Lmove_time += 1
                    Rmove_time = 0
                    if 60 > Lmove_time > 30:
                        person_img = Load_('./img/p1/p1L2.gif')
                    elif 30 > Lmove_time > 0 or Lmove_time > 60:
                        person_img = Load_('./img/p1/p1L.gif')
                        Lmove_time += 1
                        if Lmove_time == 100:
                            Lmove_time = 0
                    person_x, person_y = persondo.move_to(keypas, person_x, person_y)
                elif keypas[pygame.K_d]:
                    Last_move = "R"
                    Rmove_time += 1
                    Lmove_time = 0
                    if 60 > Rmove_time > 30:
                        person_img = Load_('./img/p1/p1R2.gif')
                    elif 30 > Rmove_time > 0 or Rmove_time > 60:
                        person_img = Load_('./img/p1/p1R.gif')
                        Rmove_time += 1
                        if Rmove_time == 100:
                            Rmove_time = 0
                    person_x, person_y = persondo.move_to(keypas, person_x, person_y)



                elif keypas[pygame.K_s]:
                    person_x, person_y = persondo.move_to(keypas, person_x, person_y)
            else:
                if Last_move == 'R':
                    person_img = Load_('./img/p1/p1R.gif')
                else:
                    person_img = Load_('./img/p1/p1L.gif')

            #######################################################

            # 射击方向 与 射击
            if Person.HAVEGUN:  


                if keypas[pygame.K_LEFT] or keypas[pygame.K_UP] or keypas[pygame.K_RIGHT] or \
                        keypas[pygame.K_DOWN]:
                    fire_return = fire_move.fire_to(keypas)
                    # print('fire_return:', fire_return)
                    direction = fire_return[0]
                    person_gun_one = fire_return[1]

                if keypas[pygame.K_SPACE]:
                    AKF[0].play(AKF[1])
                    bullet_x = person_x + 32
                    bullet_y = person_y + 35
                    while True:
                        bullet_x, bullet_y = person_direction(direction, person_x, person_y, bullet_img, bullet_x, bullet_y)
                        bullet_x, bullet_y = shoot(direction, bullet_x, bullet_y)
                        pygame.display.flip()

                        if (keypas[pygame.K_w] and keypas[pygame.K_a]) or (keypas[pygame.K_w] and keypas[pygame.K_d]) or \
                                keypas[pygame.K_w]:
                            person_x, person_y = persondo.move_to(keypas, person_x, person_y)
                            updata(person_x, person_y, plat, background)
                            time.sleep(0.3)
                            person_x, person_y = persondo.move_down(person_x, person_y)

                            # 移动走路动画
                        elif keypas[pygame.K_a] or keypas[pygame.K_s] or keypas[pygame.K_d]:
                            if keypas[pygame.K_a]:
                                Last_move = "L"
                                Lmove_time += 1
                                Rmove_time = 0
                                if 60 > Lmove_time > 30:
                                    person_img = Load_('./img/p1/p1L2.gif')
                                elif 30 > Lmove_time > 0 or Lmove_time > 60:
                                    person_img = Load_('./img/p1/p1L.gif')
                                    Lmove_time += 1
                                    if Lmove_time == 100:
                                        Lmove_time = 0
                                person_x, person_y = persondo.move_to(keypas, person_x, person_y)
                            elif keypas[pygame.K_d]:
                                Last_move = "R"
                                Rmove_time += 1
                                Lmove_time = 0
                                if 60 > Rmove_time > 30:
                                    person_img = Load_('./img/p1/p1R2.gif')
                                elif 30 > Rmove_time > 0 or Rmove_time > 60:
                                    person_img = Load_('./img/p1/p1R.gif')
                                    Rmove_time += 1
                                    if Rmove_time == 100:
                                        Rmove_time = 0
                                person_x, person_y = persondo.move_to(keypas, person_x, person_y)



                            elif keypas[pygame.K_s]:
                                person_x, person_y = persondo.move_to(keypas, person_x, person_y)
                        else:
                            if Last_move == 'R':
                                person_img = Load_('./img/p1/p1R.gif')
                            else:
                                person_img = Load_('./img/p1/p1L.gif')

                            #######################################################
                        try:
                            if l[0] == 2:

                                # print(l[1:8])
                                if l[5] == 1:
                                    person_gun_two = Load_('./img/q1/q1R.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 2:
                                    person_gun_two = Load_('./img/q1/q1L.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 3:
                                    person_gun_two = Load_('./img/q1/q1U.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 4:
                                    person_gun_two = Load_('./img/q1/q1D.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 5:
                                    person_gun_two = Load_('./img/q1/q1RU.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 6:
                                    person_gun_two = Load_('./img/q1/q1LD.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 7:
                                    person_gun_two = Load_('./img/q1/q1LU.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                                elif l[5] == 8:
                                    person_gun_two = Load_('./img/q1/q1RD.gif')
                                    root.blit(person_gun_two, (l[1] + 20, l[2] + 30))

                                if l[6] == 1:
                                    p2 = Load_('./img/p2/p2L.gif')
                                elif l[6] == 2:
                                    p2 = Load_('./img/p2/p2R.gif')
                                root.blit(p2, (l[1], l[2]))
                                if l[3] != old_bullet_x or l[4] != old_bullet_y:
                                    root.blit(bullet_img, (l[3], l[4]))
                                old_bullet_x = l[3]
                                old_bullet_y = l[4]

                            else:

                                # print(l[8:15])
                                if l[12] == 1:
                                    person_gun_two = Load_('./img/q1/q1R.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 2:
                                    person_gun_two = Load_('./img/q1/q1L.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 3:
                                    person_gun_two = Load_('./img/q1/q1U.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 4:
                                    person_gun_two = Load_('./img/q1/q1D.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 5:
                                    person_gun_two = Load_('./img/q1/q1RU.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 6:
                                    person_gun_two = Load_('./img/q1/q1LD.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 7:
                                    person_gun_two = Load_('./img/q1/q1LU.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                                elif l[12] == 8:
                                    person_gun_two = Load_('./img/q1/q1RD.gif')
                                    root.blit(person_gun_two, (l[8] + 20, l[9] + 30))

                                if l[13] == 1:
                                    p2 = Load_('./img/p2/p2L.gif')
                                elif l[13] == 2:
                                    p2 = Load_('./img/p2/p2R.gif')

                                root.blit(p2, (l[8], l[9]))

                                if l[10] != old_bullet_x or l[11] != old_bullet_y:
                                    root.blit(bullet_img, (l[10], l[11]))
                                old_bullet_x = l[10]
                                old_bullet_y = l[11]
                        except:
                            pass

                        def direction_func():
                            # print(direction)
                            if direction == 'right':
                                direction_A = 1
                            if direction == 'left':
                                direction_A = 2
                            if direction == 'up':
                                direction_A = 3
                            if direction == 'down':
                                direction_A = 4
                            if direction == 'rightup':
                                direction_A = 5
                            if direction == 'leftdown':
                                direction_A = 6
                            if direction == 'leftup':
                                direction_A = 7
                            if direction == 'rightdown':
                                direction_A = 8
                            return direction_A

                        def Last_move_func():
                            # print(Last_move)
                            if Last_move == 'L':
                                Last_move_A = 1
                            elif Last_move == 'R':
                                Last_move_A = 2
                            else:
                                Last_move_A = Last_move
                            return Last_move_A

                        if s % 2 == 1:
                            direction_B = direction_func()
                            Last_move_B = Last_move_func()
                            # if hit() == 'None':
                            #     l_vs_A = 0
                            #     # print('11111',l_vs_A)
                            # else:l_vs_A = hit()
                            l_vs_A = hit()
                            if l_vs_A == None:
                                l_vs_A = 0
                                # print('11111', l_vs_A)
                            #else:
                                # print('sss')

                            # print('sdasd', l_vs_A)
                            sendlist = [person_x, person_y, bullet_x, bullet_y, direction_B, Last_move_B, l_vs_A, 0, 0, 0, 0, 0, 0, 0]
                            l = client.main(sendlist)
                            if l[7] == 2 or l[14] == 2:
                                plat = Load_('./img/map2/map2.gif')
                                background = Load_('./img/map2/bg.gif')
                                persondo.changePD()
                                person_x, person_y = persondo.island()
                                persondo.lv+=1
                            elif l[7] == 4:
                                root.blit(WIN, (0, 0))
                                while True:
                                    pygame.display.flip()
                                    time.sleep(5)
                                    
                                    os.kill(os.getpid(),signal.SIGKILL)
                                    # os.kill(os.getpid(),signal.SIGKILL)
                                    exit()
                            elif l[14] == 5:
                                root.blit(LOST, (0, 0))
                                while True:
                                    pygame.display.flip()
                                    time.sleep(5)
                                    
                                    os.kill(os.getpid(),signal.SIGKILL)
                                    # os.kill(os.getpid(),signal.SIGKILL)
                                    exit()
                            elif l[15] == 2:
                                pygame.display.flip()
                            else:
                                root.blit(START, (0, 0))
                                pygame.display.flip()

                        if s % 2 == 0:
                            direction_B = direction_func()
                            Last_move_B = Last_move_func()
                            l_vs_A = hit()
                            if l_vs_A == None:
                                l_vs_A = 0
                                # print('11111', l_vs_A)
                            # else:
                                # print('sss')

                            # print('sdasd', l_vs_A)
                            sendlist = [0, 0, 0, 0, 0, 0, 0, person_x, person_y, bullet_x, bullet_y, direction_B, Last_move_B, l_vs_A]
                            l = client.main(sendlist)
                            if l[7] == 2 or l[14] == 2:
                                plat = Load_('./img/map2/map2.gif')
                                background = Load_('./img/map2/bg.gif')
                                persondo.changePD()
                                person_x, person_y = persondo.island()
                                persondo.lv+=1
                            elif l[7] == 4:
                                root.blit(LOST, (0, 0))
                                while True:
                                    pygame.display.flip()
                                    time.sleep(5)
                                    
                                    # os.kill(os.getpid(),signal.SIGKILL)
                                    os.kill(os.getpid(),signal.SIGKILL)
                                    exit()
                            elif l[14] == 5:
                                root.blit(WIN, (0, 0))
                                while True:
                                    pygame.display.flip()
                                    time.sleep(5)
                                  
                                    # os.kill(os.getpid())
                                    # os.kill(os.getpid(),signal.SIGKILL)
                                    os.kill(os.getpid(),signal.SIGKILL)
                                    exit()
                            else:
                                pygame.display.flip()

                        #############################
                        if bullet_x > 1500 or bullet_x < 0 or bullet_y > 800 or bullet_y < 0:
                            bullet_x = person_x + 32
                            bullet_y = person_y + 35
                            break

            # KEYNUM = 0
            ######################################################

            # 退出判断
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    os.kill(os.getpid(),signal.SIGKILL)
                    

            ###################################################

            # 绘制初始枪的位置
            person_direction(direction, person_x, person_y, begin_person_gun, 732, 445)

            ########################################################

            def hit():

                try:
                    if l[0] == 2:
                        # print('这是客户端2')
                        if l[10] > l[1] and l[10] < l[1] + 64:
                            if l[11] > l[2] and l[11] < l[2] + 64:
                                Person.DEAD = True
                                # print('你被打死了')

                                persondo.lv += 1
                                bullet_x = l[8] + 32
                                bullet_y = l[9] + 35
                                # print('persondo的值是：', persondo.lv)
                                return persondo.lv
                        else:
                            # print('这是返回l_vs', persondo.lv)
                            return persondo.lv
                    else:
                        # print('这是客户端1')
                        if l[3] > l[8] and l[3] < l[8] + 64:
                            if l[4] > l[9] and l[4] < l[9] + 64:
                                Person.DEAD = True
                                # print('你被打死了')
                                # print(Person.DEAD)
                                persondo.lv += 1
                                bullet_x = l[1] + 32
                                bullet_y = l[2] + 35
                                # print('persondo的值是：', persondo.lv)
                                return persondo.lv
                        else:
                            # print('这是返回l_vs', persondo.lv)
                            # print('没有打到时persondo的值是：', persondo.lv)
                            return persondo.lv

                except Exception as e:
                    # print('cuole', e)
                    pass

            # 服务器传输

            try:
                if l[0] == 2:

                    # print(l[1:8])
                    if l[5] == 1:
                        person_gun_two = Load_('./img/q1/q1R.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 2:
                        person_gun_two = Load_('./img/q1/q1L.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 3:
                        person_gun_two = Load_('./img/q1/q1U.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 4:
                        person_gun_two = Load_('./img/q1/q1D.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 5:
                        person_gun_two = Load_('./img/q1/q1RU.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 6:
                        person_gun_two = Load_('./img/q1/q1LD.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 7:
                        person_gun_two = Load_('./img/q1/q1LU.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))
                    elif l[5] == 8:
                        person_gun_two = Load_('./img/q1/q1RD.gif')
                        root.blit(person_gun_two, (l[1] + 20, l[2] + 30))

                    if l[6] == 1:
                        p2 = Load_('./img/p2/p2L.gif')
                    elif l[6] == 2:
                        p2 = Load_('./img/p2/p2R.gif')

                    root.blit(p2, (l[1], l[2]))

                    if l[3] != old_bullet_x or l[4] != old_bullet_y:
                        root.blit(bullet_img, (l[3], l[4]))
                    old_bullet_x = l[3]
                    old_bullet_y = l[4]
                else:

                    
                    if l[12] == 1:
                        person_gun_two = Load_('./img/q1/q1R.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 2:
                        person_gun_two = Load_('./img/q1/q1L.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 3:
                        person_gun_two = Load_('./img/q1/q1U.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 4:
                        person_gun_two = Load_('./img/q1/q1D.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 5:
                        person_gun_two = Load_('./img/q1/q1RU.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 6:
                        person_gun_two = Load_('./img/q1/q1LD.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 7:
                        person_gun_two = Load_('./img/q1/q1LU.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))
                    elif l[12] == 8:
                        person_gun_two = Load_('./img/q1/q1RD.gif')
                        root.blit(person_gun_two, (l[8] + 20, l[9] + 30))

                    if l[13] == 1:
                        p2 = Load_('./img/p2/p2L.gif')
                    elif l[13] == 2:
                        p2 = Load_('./img/p2/p2R.gif')
                    root.blit(p2, (l[8], l[9]))

                    if l[10] != old_bullet_x or l[11] != old_bullet_y:
                        root.blit(bullet_img, (l[10], l[11]))
                    old_bullet_x = l[10]
                    old_bullet_y = l[11]
            except:
                pass

            def direction_func():
                # print(direction)
                if direction == 'right':
                    direction_A = 1
                if direction == 'left':
                    direction_A = 2
                if direction == 'up':
                    direction_A = 3
                if direction == 'down':
                    direction_A = 4
                if direction == 'rightup':
                    direction_A = 5
                if direction == 'leftdown':
                    direction_A = 6
                if direction == 'leftup':
                    direction_A = 7
                if direction == 'rightdown':
                    direction_A = 8
                return direction_A

            def Last_move_func():
                # print(Last_move)
                if Last_move == 'L':
                    Last_move_A = 1
                elif Last_move == 'R':
                    Last_move_A = 2
                else:
                    Last_move_A = Last_move
                return Last_move_A

            if s % 2 == 1:
                direction_B = direction_func()
                Last_move_B = Last_move_func()
                # if hit() == 'None':
                #     l_vs_A = 0
                #     # print('11111',l_vs_A)
                # else:l_vs_A = hit()
                l_vs_A = hit()
                # print('l_vs_A:', l_vs_A)
                if l_vs_A == None:
                    l_vs_A = 0
                    # print('11111', l_vs_A)
                #else:
                    # print('sss')

                # print('sdasd', l_vs_A)
                sendlist = [person_x, person_y, bullet_x, bullet_y, direction_B, Last_move_B, l_vs_A, 0, 0, 0, 0, 0, 0, 0]
                l = client.main(sendlist)
                if l[7] == 2 or l[14] == 2:
                    plat = Load_('./img/map2/map2.gif')
                    background = Load_('./img/map2/bg.gif')
                    persondo.changePD()
                    person_x, person_y = persondo.island()
                elif l[7] == 4:
                    root.blit(WIN, (0, 0))
                    while True:
                        pygame.display.flip()
                        time.sleep(5)
                      
                        # os.kill(os.getpid())
                        # os.kill(os.getpid(),signal.SIGKILL)
                        os.kill(os.getpid(),signal.SIGKILL)
                        exit()
                elif l[14] == 5:
                    root.blit(LOST, (0, 0))
                    while True:
                        pygame.display.flip()
                        time.sleep(5)
                        
                        os.kill(os.getpid(),signal.SIGKILL)
                        # os.kill(os.getpid(), signal.SIGKILL)
                        exit()
                elif l[15] == 2:
                    pygame.display.flip()
                else:
                    root.blit(START, (0, 0))
                    pygame.display.flip()

            if s % 2 == 0:
                direction_B = direction_func()
                Last_move_B = Last_move_func()
                l_vs_A = hit()
                if l_vs_A == None:
                    l_vs_A = 0
                    # print('11111', l_vs_A)
                #else:
                    # print('sss')

                # print('sdasd', l_vs_A)
                sendlist = [0, 0, 0, 0, 0, 0, 0, person_x, person_y, bullet_x, bullet_y, direction_B, Last_move_B, l_vs_A]
                l = client.main(sendlist)
                # print(l)
                if l[7] == 2 or l[14] == 2:
                    plat = Load_('./img/map2/map2.gif')
                    background = Load_('./img/map2/bg.gif')
                    persondo.changePD()
                    person_x, person_y = persondo.island()
                elif l[7] == 4:
                    root.blit(LOST, (0, 0))
                    while True:
                        pygame.display.flip()
                        time.sleep(5)
                        
                        os.kill(os.getpid(),signal.SIGKILL)
                        exit()
                elif l[14] == 5:
                    root.blit(WIN, (0, 0))
                    while True:
                        pygame.display.flip()
                        time.sleep(5)
                        
                        os.kill(os.getpid(),signal.SIGKILL)
                        exit()
                else:
                    pygame.display.flip()


if __name__ == '__main__':
    
    # s1=Process(target=play_music)
    # s1.daemon=True
    # s1.start()
    
    # print(os.getpid())

    # pid=os.fork()
    # PID = Value('i', 0)
    # if pid==0:
    #     play_music()
    #     PID.value=os.getpid()
    t1=Thread(target=play_music)
    t1.start()
    main()