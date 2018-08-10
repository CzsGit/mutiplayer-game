length = 300
width = 200
person_length = 3
person_width = 3


class players(object):
    def __init__(self, x, y, person_x, person_y, bullet_x, bullet_y):
        self.x = x
        self.y = y
        self.person_x = person_x
        self.person_y = person_y
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y

    def border(self, x, y):
        if list_map[x][y] == 0:
            return True
        elif list_map[x][y] == 1:
            return False

    def hit(self):
        for i in range(64):
            if person_x == bullet_x and person_y + i == bullet_y:
                return True
            if person_x + 63 == bullet_x and person_y + i == bullet_y:
                return True
            if person_x + i == bullet_x and person_y == bullet_y:
                return True
            if person_x + i == bullet_x and person_y + 63 == bullet_y:
                return True
        return False
