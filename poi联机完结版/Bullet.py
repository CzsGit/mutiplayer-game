import Person

LONGMOVE = 5
SHORTMOVE = 2
WIN_LONG = 1500
WIN_WIDTH = 800
BULLETLONG = 50
direction = 'right'


def shoot(direction, bullet_x, bullet_y):
    print(Person.HAVEGUN)
    if Person.HAVEGUN == True:
        if direction == 'up' and bullet_y > 0:
            bullet_y -= BULLETLONG
        if direction == 'down' and bullet_y < WIN_WIDTH:
            bullet_y += BULLETLONG
        if direction == 'left' and bullet_x > 0:
            bullet_x -= BULLETLONG
        if direction == 'right' and bullet_x < WIN_LONG:
            bullet_x += BULLETLONG
        if direction == 'rightup' and bullet_x < WIN_LONG and bullet_y > 0:
            bullet_x += BULLETLONG
            bullet_y -= BULLETLONG
        if direction == 'rightdown' and bullet_x < WIN_LONG and bullet_y < WIN_WIDTH:
            bullet_x += BULLETLONG
            bullet_y += BULLETLONG
        if direction == 'leftup' and bullet_x > 0 and bullet_y > 0:
            bullet_x -= BULLETLONG
            bullet_y -= BULLETLONG
        if direction == 'leftdown' and bullet_x > 0 and bullet_y < WIN_WIDTH:
            bullet_x -= BULLETLONG
            bullet_y += BULLETLONG
        return bullet_x, bullet_y
    else:
        return False


def shoot_up():
    direction = 'up'
    return direction


def shoot_down():
    direction = 'down'
    return direction


def shoot_right():
    direction = 'right'
    return direction


def shoot_left():
    direction = 'left'
    return direction


def shoot_leftup():
    direction = 'leftup'
    return direction


def shoot_rightup():
    direction = 'rightup'
    return direction


def shoot_leftdown():
    direction = 'leftdown'
    return direction


def shoot_rightdown():
    direction = 'rightdown'
    return direction
