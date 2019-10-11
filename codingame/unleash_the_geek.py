import sys
import math
from collections import deque, defaultdict
from random import randint


radar_positions = [(5, 4), (5, 10), (10, 8), (15, 4), (15, 10)]

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

state_text = {
    STATE_IDLE: 'IDLE STATE',
    STATE_INSTALL_RADAR: 'INSTALL RADAR',
    STATE_INSTALL_TRAP: 'INSTALL TRAP',
    STATE_DIG_HOLE: 'DIG HOLE',
    STATE_MINING: 'MINING',
    STATE_MOVING: 'MOVING',
    STATE_REQUEST_RADAR: 'REQUEST RADAR',
    STATE_REQUEST_TRAP: 'REQUEST TRAP'
}

mission_text = {
    NONE: 'No Mission',
    MISSION_INSTALL_RADAR: 'Mission install radar',
    MISSION_INSTALL_TRAP: 'Mission install trap',
    MISSION_DIG_HOLE: 'Mission dig hole',
    MISSION_MINING: 'Missoin mining',
    MISSION_MOVE: 'Mission move'
}

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

    def update(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item

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
        self.mission = MISSION_MOVE
        self.mission_data = (x, y)

    def do(self, game):
        print(f'DO GAME: id:{self.id}, state:{state_text[self.state]}, mission:{mission_text[self.mission]}, item:{self.item}', file=sys.stderr)
        print(f'MISSION DATA: {self.mission_data}', file=sys.stderr)
        if self.mission == NONE:
            self.state = STATE_IDLE
            self.wait(f'wait.. {self.id}')
        elif self.mission == MISSION_INSTALL_RADAR:
            if self.state == STATE_IDLE and self.item == NONE:
                self.state = STATE_REQUEST_RADAR
                self.request(RADAR, f'give me RADAR!!! {self.id}')
            elif self.state == STATE_REQUEST_RADAR and self.item == NONE:
                self.request(RADAR, f'give me RADAR!!! waiting.. {self.id}')
            elif self.state == STATE_REQUEST_RADAR and self.item == RADAR:
                self.state = STATE_INSTALL_RADAR
                self.dig(self.mission_data[0], self.mission_data[1], f'install radar to {self.mission_data[0]}{self.mission_data[1]}')
            elif self.state == STATE_INSTALL_RADAR and self.item == RADAR:
                self.dig(self.mission_data[0], self.mission_data[1], f'install radar to {self.mission_data[0]}{self.mission_data[1]}')                
            elif self.state == STATE_INSTALL_RADAR and self.item == NONE:
                self.state = STATE_IDLE
                self.mission = NONE
                self.wait(f'wait... {self.id}')
            elif self.state == STATE_INSTALL_RADAR and self.item == AMADEUSIUM:
                self.mission = MISSION_MINING
                self.state = STATE_MOVING
                self.move(0, self.y, 'go home..')

        elif self.mission == MISSION_INSTALL_TRAP:
            if self.state == STATE_IDLE and self.item == NONE:
                self.state = STATE_REQUEST_TRAP
                self.request(TRAP, f'give me Trap!!! {self.id}')
            elif self.state == STATE_REQUEST_TRAP and self.item == NONE:
                self.request(TRAP, f'give me Trap!!! waiting.. {self.id}')
            elif self.state == STATE_REQUEST_TRAP and self.item == TRAP:
                self.state = STATE_INSTALL_TRAP
                self.dig(self.mission_data[0], self.mission_data[1], f'install trap to {self.mission_data[0]}{self.mission_data[1]}')
            elif self.state == STATE_INSTALL_TRAP and self.item == TRAP:
                self.dig(self.mission_data[0], self.mission_data[1], f'install trap to {self.mission_data[0]}{self.mission_data[1]}')                
            elif self.state == STATE_INSTALL_TRAP and self.item == NONE:
                self.state = STATE_IDLE
                self.mission = NONE
                self.wait(f'wait... {self.id}')
            elif self.state == STATE_INSTALL_TRAP and self.item == AMADEUSIUM:
                self.mission = MISSION_MINING
                self.state = STATE_MOVING
                self.move(0, self.y, 'go home..')

        elif self.mission == MISSION_DIG_HOLE:
            if game.grid.get_cell(int(self.mission_data[0]), int(self.mission_data[1])).hole == 0:
                self.state = STATE_DIG_HOLE
                self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            elif self.item == 4:
                self.mission = MISSION_MINING
                self.state = STATE_MOVING
                self.move(0, self.y, f'wow lucky!! {self.id}')
            else:
                self.state = STATE_IDLE
                self.wait(f'{self.id}')
                self.mission = NONE

        elif self.mission == MISSION_MINING:
            if self.item != AMADEUSIUM and self.state == STATE_IDLE:
                self.state = STATE_MINING
                self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            elif self.state == STATE_MINING and self.item == NONE:
                print(f'here!!! ama left {game.grid.get_cell(int(self.mission_data[0]), int(self.mission_data[1])).amadeusium}', file=sys.stderr)
                if game.grid.get_cell(int(self.mission_data[0]), int(self.mission_data[1])).amadeusium == '0' or game.grid.get_cell(int(self.mission_data[0]), int(self.mission_data[1])).amadeusium == '?':
                    print('AAAAAA', file=sys.stderr)
                    self.state = STATE_IDLE
                    self.mission = NONE
                    self.wait('no amadeusium!!')
                else:
                    print('BBB', file=sys.stderr)
                    self.state = STATE_MINING
                    self.dig(self.mission_data[0], self.mission_data[1], f'{self.id}')
            elif self.item == AMADEUSIUM and self.state == STATE_MINING:
                self.state = STATE_MOVING
                self.move(0, self.y, 'gogogo')
            elif self.item == AMADEUSIUM and self.state == STATE_MOVING:
                self.move(0, self.y, 'keep going')
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
        self.my_robots = defaultdict(lambda: None)
        self.enemy_robots = []

    def reset(self):
        self.radars = []
        self.traps = []
        self.enemy_robots = []


def get_amadeusiums(game):
    amadeusiums = []
    for x in range(1, 29):
        for y in range(0, 14):
            if game.grid.get_cell(x, y).amadeusium != '?' and int(game.grid.get_cell(x, y).amadeusium) > 0:
                amadeusiums.append((x, y))
    return amadeusiums


def analysis(game: Game, missions: deque):
    if game.radar_cooldown <= 1 and radar_positions:
        x, y = radar_positions.pop(0)
        missions.append(f'install radar on {x} {y}')

    amadeusiums = get_amadeusiums(game)

    if len(missions) < 5 and len(amadeusiums) == 0:
        for _ in range(5-len(missions)):
            x, y = randint(1, 5), randint(0, 14)
            missions.append(f'dig on {x} {y}')
    
    for x, y in amadeusiums:
        missions.append(f'mining on {x} {y}')



def find_best_robot(game: Game, mission: str):
    for id in game.my_robots:
        if game.my_robots[id].mission == NONE:
            return id


def is_robot(game: Game):
    for id in game.my_robots:
        if game.my_robots[id].mission == NONE:
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
    elif commands[0] == 'dig':
        game.my_robots[id].digging(commands[2], commands[3])
    elif commands[0] == 'wait':
        pass


def log_robots(game):
    print('- log robots -', file=sys.stderr)
    for id in game.my_robots:
        print(f'robot id:{id} mission:{mission_text[game.my_robots[id].mission]} state:{state_text[game.my_robots[id].state]}', file=sys.stderr)


game = Game()
missions = deque()

# missions.append('install radar on 5 4')
# missions.append('install radar on 5 10')
# missions.append('install radar on 15 4')
# missions.append('install radar on 15 10')
# missions.append('install trap on 10 8')

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
    ids = []
    for i in range(entity_count):
        # id: unique id of the entity
        # type: 0 for your robot, 1 for other robot, 2 for radar, 3 for trap
        # y: position of the entity
        # item: if this entity is a robot, the item it is carrying (-1 for NONE, 2 for RADAR, 3 for TRAP, 4 for AMADEUSIUM)
        id, type, x, y, item = [int(j) for j in input().split()]

        if type == ROBOT_ALLY:
            ids.append(id)
            if game.my_robots[id]:
                game.my_robots[id].update(x, y, item)
            else:
                game.my_robots[id] = Robot(x, y, type, id, item)
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


    log_robots(game)
    for id in ids:
        game.my_robots[id].do(game)
