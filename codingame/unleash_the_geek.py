import sys
import math
from collections import deque


# Deliver more amadeusium to hq (left side of the map) than your opponent. 
# Use radars to find amadeusium but beware of traps!

# height: size of the map
width, height = [int(i) for i in input().split()]

NONE = -1
ROBOT_ALLY = 0
ROBOT_ENEMY = 1
HOLE = 1
RADAR = 2
TRAP = 3
AMADEUSIUM = 4

STATE_IDLE = 100
STATE_INSTALL_RADAR = 101
STATE_INSTALL_TRAP = 102
STATE_DIG_HOLE = 103
STATE_MINING = 104
STATE_MOVING = 105
STATE_REQUEST_RADAR = 106
STATE_REQUEST_TRAP = 107

MISSION_INSTALL_RADAR = 200
MISSION_INSTALL_TRAP = 201
MISSION_DIG_HOLE = 202
MISSION_MINING = 203
MISSION_MOVE = 204


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pos):
        return abs(self.x - pos.x) + abs(self.y - pos.y)


class Entity(Pos):
    def __init__(self, x, y, type, id):
        super().__init__(x, y)
        self.type = type
        self.id = id


class Robot(Entity):
    def __init__(self, x, y, type, id, item):
        super().__init__(x, y, type, id)
        self.item = item
        self.state = STATE_IDLE
        self.command = ''
        self.mission = NONE
        self.mission_data = NONE

    def is_dead(self):
        return self.x == -1 and self.y == -1

    def radar_install(self, x, y):
        self.mission = MISSION_INSTALL_RADAR
        self.mission_data = (x, y)

    def trap_install(self, x, y):
        self.mission = MISSION_INSTALL_TRAP
        self.mission_data = (x, y)

    def mining(self, x, y):
        self.mission = MISSION_MINING
        self.mission_data = (x, y)
    
    def digging(self, x, y):
        self.mission = MISSION_DIG_HOLE
        self.mission_data = (x, y)

    def moving(self, x, y):
        self.missoin = MISSION_MOVE
        self.mission_data = (x, y)

    def do(self, game):
        if self.mission == NONE:
            self.state = STATE_IDLE
            self.wait(f'wait.. {self.id}')
        elif self.mission == MISSION_INSTALL_RADAR:
            if self.state == STATE_IDLE and self.item == NONE:
                self.state = STATE_REQUEST_RADAR
                self.request(RADAR, f'give me RADAR!!! {self.id}')
            elif self.state == STATE_REQUEST_RADAR and self.item == RADAR:
                self.state = STATE_INSTALL_RADAR
                self.dig(self.mission_data[0], self.mission_data[1], f'install radar to {self.mission_data[0]}{self.mission_data[1]}')
            elif self.state == STATE_INSTALL_RADAR:
                for radar in game.radars:
                    if radar.x == self.mission_data[0] and radar.y == self.mission_data[1]:
                        self.state = STATE_IDLE
                        self.mission = NONE
                        self.wait(f'wait... {self.id}')
                        break
                else:
                    self.dig(self.mission_data[0], self.mission_data[1], f'install radar to..')
        elif self.mission == MISSION_INSTALL_TRAP:
            if self.state == STATE_IDLE and self.item == NONE:
                self.state = STATE_REQUEST_TRAP
                self.request(TRAP, f'give me Trap!!! {self.id}')
            elif self.state == STATE_REQUEST_TRAP and self.item == TRAP:
                self.state = STATE_INSTALL_TRAP
                self.dig(self.mission_data[0], self.mission_data[1], f'install trap to {self.mission_data[0]}{self.mission_data[1]}')
            elif self.state == STATE_INSTALL_TRAP:
                for trap in game.traps:
                    if trap.x == self.mission_data[0] and trap.y == self.mission_data[1]:
                        self.state = STATE_IDLE
                        self.mission = NONE
                        self.wait(f'wait... {self.id}')
                        break
                else:
                    self.dig(self.mission_data[0], self.mission_data[1], f'install trap to..')
        elif self.mission == MISSION_DIG_HOLE:
            if game.grid.get_cell(self.mission_data[0], self.mission_data[1]).hole == 0:
                self.state = STATE_DIG_HOLE
                self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            else:
                self.state = STATE_IDLE
                self.wait(f'{self.id}')
                self.mission = NONE
        elif self.mission == MISSION_MINING:
            if self.item != AMADEUSIUM and self.state == STATE_IDLE:
                self.state = STATE_MINING
                self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            elif self.item == AMADEUSIUM and self.state == STATE_MINING:
                self.state = STATE_MOVING
                self.move(0, self.y)
            elif self.item == NONE and self.state == STATE_MINING:
                self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            elif self.item == NONE and self.state == STATE_MOVING:
                self.mission = NONE
                self.state = STATE_IDLE
                self.wait(f'{self.id}')
        elif self.mission == MISSION_MOVE:
            self.state = STATE_MOVING
            if self.mission_data[0] == self.x and self.mission_data[1] == self.y:
                self.state = STATE_IDLE
                self.mission = NONE
                self.wait(f'{self.id}')
            else:
                self.move(self.mission_data[0], self.mission_data[1], f'{self.id}')


    @staticmethod
    def move(x, y, message=""):
        print(f"MOVE {x} {y} {message}")

    @staticmethod
    def wait(message=""):
        print(f"WAIT {message}")

    @staticmethod
    def dig(x, y, message=""):
        print(f"DIG {x} {y} {message}")

    @staticmethod
    def request(requested_item, message=""):
        if requested_item == RADAR:
            print(f"REQUEST RADAR {message}")
        elif requested_item == TRAP:
            print(f"REQUEST TRAP {message}")
        else:
            raise Exception(f"Unknown item {requested_item}")


class Cell(Pos):
    def __init__(self, x, y, amadeusium, hole):
        super().__init__(x, y)
        self.amadeusium = amadeusium
        self.hole = hole

    def has_hole(self):
        return self.hole == HOLE

    def update(self, amadeusium, hole):
        self.amadeusium = amadeusium
        self.hole = hole


class Grid:
    def __init__(self):
        self.cells = []
        for y in range(height):
            for x in range(width):
                self.cells.append(Cell(x, y, 0, 0))

    def get_cell(self, x, y):
        if width > x >= 0 and height > y >= 0:
            return self.cells[x + width * y]
        return None


class Game:
    def __init__(self):
        self.grid = Grid()
        self.my_score = 0
        self.enemy_score = 0
        self.radar_cooldown = 0
        self.trap_cooldown = 0
        self.radars = []
        self.traps = []
        self.my_robots = []
        self.enemy_robots = []

    def reset(self):
        self.radars = []
        self.traps = []
        self.my_robots = []
        self.enemy_robots = []


def analysis(game: Game, missions: deque):
    pass


def find_best_robot(game: Game, mission: str):
    for robot in game.my_robots:
        if robot.mission == NONE:
            return robot.id


def is_robot(game: Game):
    for robot in game.my_robots:
        if robot.mission == NONE:
            return True
    return False


def set_mission(game, id, mission):
    commands = mission.split()
    if commands[0] == 'install':
        if commands[1] == 'radar':
            game.my_robots[id].radar_install(commands[3], commands[4])
        elif commands[1] == 'trap':
            game.my_robots[id].trap_install(commands[3], commands[4])
    elif commands[0] == 'mining':
        game.my_robots[id].mining(commands[2], commands[3])
    elif commands[0] == 'move':
        game.my_robots[id].moving(commands[2], commands[3])
    elif commands[0] == 'wait':
        game.my_robots[id].wait()


    game.my_robots[id]


game = Game()
missions = deque()

missions.append('install radar on 5 5')
missions.append('install trap on 6 6')
missions.append('mining at 5 6')
missions.append('move to 10 20')
missions.append('wait')


# game loop
while True:
    # my_score: Players score
    game.my_score, game.enemy_score = [int(i) for i in input().split()]
    for i in range(height):
        inputs = input().split()
        for j in range(width):
            # amadeusium: amount of amadeusium or "?" if unknown
            # hole: 1 if cell has a hole
            amadeusium = inputs[2 * j]
            hole = int(inputs[2 * j + 1])
            game.grid.get_cell(j, i).update(amadeusium, hole)
    # entity_count: number of entities visible to you
    # radar_cooldown: turns left until a new radar can be requested
    # trap_cooldown: turns left until a new trap can be requested
    entity_count, game.radar_cooldown, game.trap_cooldown = [int(i) for i in input().split()]

    game.reset()

    for i in range(entity_count):
        # id: unique id of the entity
        # type: 0 for your robot, 1 for other robot, 2 for radar, 3 for trap
        # y: position of the entity
        # item: if this entity is a robot, the item it is carrying (-1 for NONE, 2 for RADAR, 3 for TRAP, 4 for AMADEUSIUM)
        id, type, x, y, item = [int(j) for j in input().split()]

        if type == ROBOT_ALLY:
            game.my_robots.append(Robot(x, y, type, id, item))
        elif type == ROBOT_ENEMY:
            game.enemy_robots.append(Robot(x, y, type, id, item))
        elif type == TRAP:
            game.traps.append(Entity(x, y, type, id))
        elif type == RADAR:
            game.radars.append(Entity(x, y, type, id))

    analysis(game, missions)

    while is_robot(game) and missions:
        mission = missions.popleft()
        print(f'patched mission is: {mission}', file=sys.stderr)
        id = find_best_robot(game, mission)
        print(f'best robot for this mission is: {id}', file=sys.stderr)
        set_mission(game, id, mission)

    for robot in game.my_robots:
        robot.do(game)
