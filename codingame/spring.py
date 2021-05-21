from collections import defaultdict, deque
import sys
import math
from enum import Enum
import random
from typing import DefaultDict, List
from copy import copy, deepcopy


def plog(s: str) -> None:
    print(s, file=sys.stderr)


class Cell:
    def __init__(self, cell_index, richness, neighbors):
        self.cell_index = cell_index
        self.richness = richness
        self.neighbors = neighbors
    
    def __str__(self) -> str:
        return(f'index: {self.cell_index}, richness: {self.richness}, neighbors: {self.neighbors}')


class Tree:
    def __init__(self, cell_index, size, is_mine, is_dormant):
        self.cell_index = cell_index
        self.size = size
        self.is_mine = is_mine
        self.is_dormant = is_dormant
    
    def __str__(self) -> str:
        return f'index: {self.cell_index}, size: {self.size}, mine: {self.is_mine}, dormant: {self.is_dormant}'


class ActionType(Enum):
    WAIT = "WAIT"
    SEED = "SEED"
    GROW = "GROW"
    COMPLETE = "COMPLETE"


class Action:
    def __init__(self, type, target_cell_id=None, origin_cell_id=None):
        self.type = type
        self.target_cell_id = target_cell_id
        self.origin_cell_id = origin_cell_id

    def __str__(self):
        if self.type == ActionType.WAIT:
            return 'WAIT'
        elif self.type == ActionType.SEED:
            return f'SEED {self.origin_cell_id} {self.target_cell_id}'
        else:
            return f'{self.type.name} {self.target_cell_id}'

    @staticmethod
    def parse(action_string):
        split = action_string.split(' ')
        if split[0] == ActionType.WAIT.name:
            return Action(ActionType.WAIT)
        if split[0] == ActionType.SEED.name:
            return Action(ActionType.SEED, int(split[2]), int(split[1]))
        if split[0] == ActionType.GROW.name:
            return Action(ActionType.GROW, int(split[1]))
        if split[0] == ActionType.COMPLETE.name:
            return Action(ActionType.COMPLETE, int(split[1]))


class Node:
    def __init__(self, action=None, is_me=True, is_first=False) -> None:
        self.action = action
        self.score = 0
        self.visit = 0
        self.is_me = is_me
        self.childs = []
        self.first = is_first
    
    def add_child(self, action: Action, is_me: bool, is_first: bool) -> None:
        self.childs.append(self.__class__(action=action, is_me=is_me, is_first=is_first))

    def __str__(self) -> str:
        return f'Node(action:{self.action}, childs:{self.childs})'

grow_cost = [1, 3, 7]    

class Double:
    def __init__(self) -> None:
        self.day = 0
        self.nutrients = 0
        self.board = []
        self.trees = []
        self.possible_actions = []
        self.my_sun = 0
        self.my_score = 0
        self.opponents_sun = 0
        self.opponent_score = 0
        self.opponent_is_waiting = 0

class Game:
    def __init__(self):
        self.day = 0
        self.nutrients = 0
        self.board = []
        self.trees = []
        self.possible_actions = []
        self.my_sun = 0
        self.my_score = 0
        self.opponents_sun = 0
        self.opponent_score = 0
        self.opponent_is_waiting = 0
        self.double = Double()

    def compute_next_action(self):
        self.mcts()
        return self.possible_actions[random.randint(0, len(self.possible_actions)-1)]

    def create_double(self) -> None:
        self.double = Double()
        self.double.day = self.day
        self.double.nutrients = self.nutrients
        self.double.board = deepcopy(self.board)
        self.double.trees = deepcopy(self.trees)
        self.double.my_sun = self.my_sun
        self.double.my_score = self.my_score
        self.double.opponents_sun = self.opponents_sun
        self.double.opponent_score = self.opponent_score
        self.double.opponent_is_waiting = self.opponent_is_waiting

    def get_possible_actions_of(self, action: Action, is_me: bool) -> List:
        actions = []
        tree_count = [[0, 0, 0, 0], [0, 0, 0, 0]] # [enermy's, mine]

        for tree in self.double.trees:
            tree_count[tree.is_mine][tree.size] += 1

        # update for parents action
        if action.type == ActionType.SEED:
            self.double.my_sun -= tree_count[is_me][0]
            self.double.trees.append(Tree(action.target, 0, is_me, True))
        elif action.type == ActionType.GROW:
            tree_size = self.trees[action.target].size
            self.double.my_sun -= (grow_cost[tree_size] + tree_count[is_me][tree_size+1])
            for tree in self.double.trees:
                if tree.cell_index == action.target:
                    tree.size += 1
                    tree.is_dormant = True
                    break
        elif action.type == ActionType.COMPLETE:
            self.double.my_sun -= 4
            r_idx = 0
            for i, tree in enumerate(self.double.trees):
                if tree.cell_index == action.target:
                    r_idx = i
                    break
            self.double.trees.remove(r_idx)

        # find child actions
        sun_points = [self.double.opponents_sun, self.double.my_sun]
        tree_count = [[0, 0, 0, 0], [0, 0, 0, 0]] # [enermy's, mine]
        for tree in self.double.trees:
            tree_count[not tree.is_mine][tree.size] += 1

        for tree in self.double.trees:
            if tree.is_mine == is_me or tree.is_dormant:
                continue
            if tree.size > 0  and tree_count[not is_me][0] <= sun_points[not is_me]:
                for i in self.double.board[tree.cell_index].neighbors:
                    if i != -1:
                        actions.append(Action(ActionType.SEED, i, tree.cell_index))
            if tree.size < 3 and grow_cost[tree.size] + tree_count[not is_me][tree.size+1] <= sun_points[not is_me]:
                actions.append(Action(ActionType.GROW, tree.cell_index))
            if tree.size == 3 and 4 <= sun_points[not is_me]:
                actions.append(Action(ActionType.COMPLETE, tree.cell_index))
        plog('xxxx')
        return actions

    def selection(self, node: Node, path: List):
        path.append(node)
        if len(node.childs) == 0:
            return
        max_val = -1
        max_node = None
        for child in node.childs:
            if child.visit == 0:
                max_node = child
                break
            ubc1 = child.score/child.visit + math.sqrt(2)*math.sqrt(math.log(node.visit)/child.visit)
            if ubc1 > max_val:
                max_val = ubc1
                max_node = child
        self.selection(max_node, path)

    def expansion(self, node: Node):
        plog(f'expansion for {node.action}')
        self.create_double()
        actions = self.get_possible_actions_of(node.action, node.is_me)
        for action in actions:
            plog(action)
            node.add_child(action, not node.is_me, False)
        return node.childs[0]

    def playout(self, node: Node):
        plog(f'playout for {node.action}')

        while True: # until end the game
            actions = self.get_possible_actions_of(node.action, node.is_me)
            random.shuffle(actions)
            self.do_action(actions[0])
            if self.is_game_end():
                break
    
    def backpropagation(self, path: List, score: int):
        plog('backpropagation')


    def mcts(self):
        # init tree
        root = Node('root', is_me=False, is_first=True)
        for i, action in enumerate(self.possible_actions):
            root.add_child(action, True, True)

        path = []
        for _ in range(10):
            plog('selection')
            self.selection(root, path)
            selected = path[-1]
            plog(selected)
            if selected.visit > 0 or selected.first:
                selected = self.expansion(selected)
            score = self.playout(selected)
            self.backpropagation(path, score)

        return 'WAIT'


number_of_cells = int(input())
game = Game()
for i in range(number_of_cells):
    cell_index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    game.board.append(Cell(cell_index, richness, [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]))

while True:
    _day = int(input())
    game.day = _day
    nutrients = int(input())
    game.nutrients = nutrients
    sun, score = [int(i) for i in input().split()]
    game.my_sun = sun
    game.my_score = score
    opp_sun, opp_score, opp_is_waiting = [int(i) for i in input().split()]
    game.opponent_sun = opp_sun
    game.opponent_score = opp_score
    game.opponent_is_waiting = opp_is_waiting
    number_of_trees = int(input())
    game.trees.clear()
    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])
        size = int(inputs[1])
        is_mine = inputs[2] != "0"
        is_dormant = inputs[3] != "0"
        game.trees.append(Tree(cell_index, size, is_mine == 1, is_dormant))

    # plog('-- trees --')
    # for i in range(number_of_trees):
    #     plog(game.trees[i])
    # plog('-- nutrients --')
    # plog(game.nutrients)
    # plog('-- cells --')
    # for cell in game.board:
    #     plog(cell)


    number_of_possible_actions = int(input())
    game.possible_actions.clear()
    plog('-- possible actions --')
    for i in range(number_of_possible_actions):
        possible_action = input()
        plog(possible_action)
        game.possible_actions.append(Action.parse(possible_action))

    print(game.compute_next_action())