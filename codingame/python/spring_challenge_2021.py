from collections import defaultdict, deque
import sys
import math
from enum import Enum
import random
from typing import DefaultDict, List, Set, Tuple
from copy import copy, deepcopy
import time

NUMBER_OF_CELL = 37
richness_point = [0, 0, 2, 4]
grow_cost = [1, 3, 7]
sun_points = [0, 1, 2, 3]
board = []

def plog(s: str) -> None:
    print(s, file=sys.stderr)
    pass

def pinput(s: str) -> None:
    # print(f'input:{s}', file=sys.stderr, flush=True)
    pass

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
        self.is_shadow = False
    
    def __str__(self) -> str:
        return f'index: {self.cell_index}, size: {self.size}, mine: {self.is_mine}, dormant: {self.is_dormant}'
    
    def __hash__(self) -> int:
        return self.cell_index


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

class ActionPool:
    def __init__(self) -> None:
        self.pool = [Action(ActionType.WAIT) for _ in range(500000)]
    
    def get_action(self, type: ActionType, target=None, origin=None) -> Action:
        if self.pool:
            action = self.pool.pop()
            action.type = type
            action.target_cell_id = target
            action.origin_cell_id = origin
            return action
        plog('out of pool')
        return Action(type, target, origin)

    def return_action(self, action: Action):
        if action:
            self.pool.append(action)
    
    def return_actions(self, actions: List[Action]):
        for action in actions:
            self.pool.append(action)
        actions.clear()

class GameStatus:
    def __init__(self) -> None:
        self.day = 0
        self.nutrients = 0
        self.trees = defaultdict(lambda: None)
        self.possible_actions = []
        self.my_sun = 0
        self.my_score = 0
        self.my_trees = {0: set(), 1: set(), 2: set(), 3: set()}
        self.opponent_sun = 0
        self.opponent_score = 0
        self.opponent_is_waiting = 0
        self.opponent_trees = {0: set(), 1: set(), 2: set(), 3: set()}
        self.tree_pool = []
        self.origin = {
            'day': 0,
            'nutrients': 0,
            'trees': [],
            'possible_actions': [],
            'my_sun': 0,
            'my_score': 0,
            'my_trees': {0: set(), 1: set(), 2: set(), 3: set()},
            'opponent_sun': 0,
            'opponent_score': 0,
            'opponent_is_waiting': 0,
            'opponent_trees': {0: set(), 1: set(), 2: set(), 3: set()},
        }
        for _ in range(NUMBER_OF_CELL):
            self.tree_pool.append(Tree(-1, 0, True, False))
        self.action_pool = ActionPool()

    def init_trees(self):
        for tree in self.trees.values():
            self.tree_pool.append(tree)
        self.trees.clear()
        for i in range(4):
            self.my_trees[i].clear()
            self.opponent_trees[i].clear()
    
    def save_origin(self):
        self.origin['day'] = self.day
        self.origin['nutrients'] = self.nutrients

        for i in range(4):
            self.origin['my_trees'][i].clear()
            self.origin['opponent_trees'][i].clear()

        for size in self.my_trees:
            for tree in self.my_trees[size]:
                self.origin['my_trees'][size].add((tree.cell_index, tree.is_dormant))
        for size in self.opponent_trees:
            for tree in self.opponent_trees[size]:
                self.origin['opponent_trees'][size].add((tree.cell_index, tree.is_dormant))
        self.origin['my_sun'] = self.my_sun
        self.origin['my_score'] = self.my_score
        self.origin['opponent_sun'] = self.opponent_sun
        self.origin['opponent_score'] = self.opponent_score
        self.origin['opponent_is_waiting'] = self.opponent_is_waiting

    def revert_to_origin(self):
        # plog('start revert to origin')
        self.day = self.origin['day']
        self.nutrients = self.origin['nutrients']
        self.init_trees()
        for size in self.origin['my_trees']:
            for index, is_dormant in self.origin['my_trees'][size]:
                self.add_tree(index, size, True, is_dormant)
        for size in self.origin['opponent_trees']:
            for index, is_dormant in self.origin['opponent_trees'][size]:
                self.add_tree(index, size, False, is_dormant)
        self.my_sun = self.origin['my_sun']
        self.my_score = self.origin['my_score']
        self.opponent_sun = self.origin['opponent_sun']
        self.opponent_score = self.origin['opponent_score']
        self.opponent_is_waiting = self.origin['opponent_is_waiting']
        # plog('end revert to origin')

    def _push_tree(self, tree: Tree):
        if tree.is_mine:
            self.my_trees[tree.size].add(tree)
        else:
            self.opponent_trees[tree.size].add(tree)        
    
    def _pop_tree(self, tree: Tree):
        if tree.is_mine:
            self.my_trees[tree.size].discard(tree)
        else:
            self.opponent_trees[tree.size].discard(tree)

    def _add_sun_point(self, is_mine: bool, my_delta: int, opp_delta: int):
        if is_mine:
            self.my_sun += my_delta
        else:
            self.opponent_sun += opp_delta

    def add_tree(self, index: int, size: int, is_mine: bool, is_dormant: bool) -> None:
        tree = self.tree_pool.pop()
        tree.cell_index = index
        tree.size = size
        tree.is_mine = is_mine
        tree.is_dormant = is_dormant
        self.trees[index] = tree
        self._push_tree(tree)

    def set_tree(self, index: int, size=None, dormant=None) -> None:
        if size != None:
            tree = self.trees[index]
            self._pop_tree(tree)
            tree.size = size
            self._push_tree(tree)
        if dormant != None:
            self.trees[index].is_dormant = dormant

    def get_tree(self, index: int) -> Tree:
        return self.trees[index]

    def remove_tree(self, index: int) -> None:
        tree = self.trees[index]
        self.tree_pool.append(tree)
        self._pop_tree(tree)
        del self.trees[index]

    def do_action(self, action: Action, is_me: bool):
        # plog(f'do action: {action.type}, by {"me" if is_me else "opp"}')
        if action.type == ActionType.SEED:
            self._add_sun_point(is_me, -len(self.my_trees[0]), -len(self.opponent_trees[0]))
            self.add_tree(action.target_cell_id, 0, is_me, True)
            self.set_tree(action.origin_cell_id, dormant=True)
        elif action.type == ActionType.GROW:
            tree_size = self.get_tree(action.target_cell_id).size
            self._add_sun_point(is_me, -(grow_cost[tree_size] + len(self.my_trees[tree_size+1])), -(grow_cost[tree_size] + len(self.opponent_trees[tree_size+1])))
            self.set_tree(action.target_cell_id, size=tree_size+1, dormant=True)
        elif action.type == ActionType.COMPLETE:
            self._add_sun_point(is_me, -4, -4)
            self.remove_tree(action.target_cell_id)
            self.my_score += (self.nutrients + richness_point[board[action.target_cell_id].richness])
            self.nutrients -= 1

    def get_possible_actions_of(self, is_me: bool) -> Tuple:
        # plog(f'get possible actions of {"me" if is_me else "opp"}')
        seed_actions = []
        grow_actions = []
        complete_actions = []
        trees_by_size = self.my_trees if is_me else self.opponent_trees

        for tree in trees_by_size[3]:
            if tree.is_dormant:
                continue
            self.add_complete_actions(tree, is_me, complete_actions)
            self.add_seed_actions(tree, is_me, seed_actions)

        for tree in trees_by_size[2]:
            if tree.is_dormant:
                continue
            self.add_grow_actions(tree, is_me, grow_actions)
            self.add_seed_actions(tree, is_me, seed_actions)

        for tree in trees_by_size[1]:
            if tree.is_dormant:
                continue
            self.add_grow_actions(tree, is_me, grow_actions)
            self.add_seed_actions(tree, is_me, seed_actions)

        for tree in trees_by_size[0]:
            if tree.is_dormant:
                continue
            self.add_grow_actions(tree, is_me, grow_actions)

        complete_actions = sorted(complete_actions, key=lambda s: s.target_cell_id)
        grow_actions = sorted(grow_actions, key=lambda s: self.trees[s.target_cell_id].size, reverse=True)
        seed_actions = sorted(seed_actions, key=lambda s: s.target_cell_id)

        # actions = complete_actions + grow_actions + seed_actions
        wait_action = None
        if not complete_actions and not grow_actions and not seed_actions:
            wait_action = self.action_pool.get_action(ActionType.WAIT)
        return complete_actions, grow_actions, seed_actions, wait_action

    def get_seed_indexes(self, index: int, res: Set, depth: int) -> None:
        if depth == 0:
            return
        for i in board[index].neighbors:
            if i == -1:
                continue
            res.add(i)
            self.get_seed_indexes(i, res, depth-1)
            
    def add_seed_actions(self, tree: Tree, is_me: bool, actions: List[Action]) -> None:
        if tree.size == 0:
            return
        if (is_me and len(self.my_trees[0]) <= self.my_sun) or \
            (not is_me and len(self.opponent_trees[0]) <= self.opponent_sun):
            indexes = set()
            self.get_seed_indexes(tree.cell_index, indexes, tree.size)
            for i in indexes:
                if board[i].richness == 0 or i == tree.cell_index or i in self.trees:
                    continue
                actions.append(self.action_pool.get_action(ActionType.SEED, i, tree.cell_index))

    def add_grow_actions(self, tree: Tree, is_me: bool, actions: List[Action]) -> None:
        if tree.size == 3:
            return
        if (is_me and grow_cost[tree.size] + len(self.my_trees[tree.size+1]) < self.my_sun) or \
            (not is_me and grow_cost[tree.size] + len(self.opponent_trees[tree.size+1]) < self.opponent_sun):
            actions.append(self.action_pool.get_action(ActionType.GROW, tree.cell_index))

    def add_complete_actions(self, tree: Tree, is_me: bool, actions: List[Action]) -> None:
        if tree.size != 3:
            return
        if (is_me and self.my_sun >= 4) or (not is_me and self.opponent_sun >= 4):
            actions.append(self.action_pool.get_action(ActionType.COMPLETE, tree.cell_index))

    def pass_one_day(self):
        for tree in self.trees.values():
            tree.is_dormant = False
            tree.is_shadow = False
        self.day += 1


    def set_spooky(self):
        sun_dir = self.day % 6
        for tree in self.trees.values():
            index = tree.cell_index
            if tree.size > 0:
                next_pos = board[index].neighbors[sun_dir]
                for _ in range(tree.size):
                    if next_pos in self.trees:
                        next_tree = self.trees[next_pos]
                        if next_tree.size <= tree.size and tree.is_mine != next_tree.is_mine:
                            next_tree.is_shadow = True
                        next_pos = board[next_pos].neighbors[sun_dir]
                        if next_pos == -1:
                            break

    def start_day(self):
        for index in self.trees:
            tree = self.trees[index]
            if tree.is_shadow == True:
                continue
            if tree.is_mine:
                self.my_sun += sun_points[tree.size]
            else:
                self.opponent_sun += sun_points[tree.size]        

    def __str__(self) -> str:
        return f'status[day: {self.day}, nutrients: {self.nutrients}, my_sun: {self.my_sun}, my_score: {self.my_score}, opponenets_sun: {self.opponent_sun}, opponents_score: {self.opponent_score} ]'


class Node:
    def __init__(self, action=None, is_me=True) -> None:
        self.action = action
        self.score = 0
        self.visit = 0
        self.is_me = is_me
        self.childs = []
    
    def add_child(self, child) -> None:
        self.childs.append(child)

    def get_child(self) -> List:
        return self.childs

    def __str__(self) -> str:
        return f'Node(action:{self.action}, childs:{self.childs})'

class Game:
    def __init__(self):
        self.status = GameStatus()
        self.prev_action = None

    def compute_next_action(self):
        return self.mcts()
        # return self.possible_actions[random.randint(0, len(self.possible_actions)-1)]

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
            ucb1 = child.score/child.visit + math.sqrt(2)*math.sqrt(math.log(node.visit)/child.visit)
            if ucb1 > max_val:
                max_val = ucb1
                max_node = child
        self.selection(max_node, path)

    def expansion(self, path: List[Node]):
        for node in path[1:]:
            self.status.do_action(node.action, node.is_me)
        complete, grow, seed, wait = self.status.get_possible_actions_of(not path[-1].is_me)

        # actions = complete[:1] + grow[:1] + seed[:1]
        actions = complete + grow + seed

        if not actions:
            actions = [wait]

        for action in actions:
            child = Node(action, not path[-1].is_me)
            node.add_child(child)

    def select_best_action(self, complete: List[Action], grow: List[Action], seed: List[Action], wait: Action, prev_action: Action, is_me: bool):
        # complete-grow2-grow1-grow0-seed-wait 
        if wait:
            self.status.action_pool.return_action(prev_action[is_me])
            prev_action[is_me] = wait
            return prev_action[is_me]

        prev = prev_action[is_me]
        if not prev:
            res = None
            self.status.action_pool.return_action(prev_action[is_me])
            if complete:
                self.status.action_pool.return_actions(complete[1:])
                self.status.action_pool.return_actions(grow)
                self.status.action_pool.return_actions(seed)
                res = complete[0]
            elif grow:
                self.status.action_pool.return_actions(grow[1:])
                self.status.action_pool.return_actions(seed)
                res = grow[0]
            elif seed:
                self.status.action_pool.return_actions(seed[1:])
                res = seed[0]

            prev_action[is_me] = res
            return prev_action[is_me]

        trees = self.status.trees
        if prev.type == ActionType.GROW:
            if  trees[prev.target_cell_id] == 2:
                self.status.action_pool.return_actions(complete)
                complete.clear()
            elif trees[prev.target_cell_id] == 1:
                temp = []
                while grow:
                    action = grow.pop()
                    if trees[action.target_cell_id] < 2:
                        temp.append(action)
                    else:
                        self.status.action_pool.return_action(action)
                grow = temp
            elif trees[prev.target_cell_id] == 0:
                temp = []
                while grow:
                    action = grow.pop()
                    if trees[action.target_cell_id] < 1:
                        temp.append(action)
                    else:
                        self.status.action_pool.return_action(action)
                grow = temp
        elif prev.type == ActionType.SEED:
            self.status.action_pool.return_actions(complete)
            complete.clear()
            self.status.action_pool.return_actions(grow)
            grow.clear()

        if not complete and not grow and not seed:
            self.status.action_pool.return_action(prev_action[is_me])
            prev_action[is_me] = self.status.action_pool.get_action(ActionType.WAIT)
            return prev_action[is_me]

        self.status.action_pool.return_action(prev_action[is_me])
        prev_action[is_me] = (complete + grow + seed)[0]
        return prev_action[is_me]

    def playout(self, path: List[Node]):
        for node in path[1:-1]:
            self.status.do_action(node.action, node.is_me)

        node = path[-1]
        action = node.action
        is_me = node.is_me
        new_day = False
        prev_action = [None, self.status.action_pool.get_action(action.type, action.target_cell_id, action.origin_cell_id)]

        for _ in range(2):
            self.status.set_spooky()
            if new_day:
                is_me = True
                complete, grow, seed, wait = self.status.get_possible_actions_of(is_me)
                action = self.select_best_action(complete, grow, seed, wait, prev_action, is_me)
            while True:
                self.status.do_action(action, is_me)
                complete, grow, seed, wait = self.status.get_possible_actions_of(not is_me)

                if wait:
                    if action.type == ActionType.WAIT:
                        break
                    else:
                        while True:
                            complete, grow, seed, wait = self.status.get_possible_actions_of(is_me)
                            if wait:
                                self.status.action_pool.return_action(wait)
                                break
                            action = self.select_best_action(complete, grow, seed, wait, prev_action, is_me)
                            self.status.do_action(action, is_me)
                        break

                action = self.select_best_action(complete, grow, seed, wait, prev_action, not is_me)
                is_me = not is_me
            
            # plog(f'pass day: {self.status.day}')
            self.status.pass_one_day()
            score = self.status.my_score
            # plog(f'score: {score}')
            if self.status.day == 23:
                break
            self.status.start_day()
            new_day = True
        return score
    
    def backpropagation(self, path: List[Node], score: int):
        # plog('backpropagation')
        for node in path:
            node.score += score
            node.visit += 1

    def mcts(self):
        # start = time.time()
        plog(f'prev action is {self.prev_action}')
        possible_actions = self.status.possible_actions
        if len(possible_actions) == 1:
            self.prev_action = self.status.action_pool.get_action(ActionType.WAIT)
            return 'WAIT'

        # init tree
        root = Node('root', is_me=False)
        for action in possible_actions[1:]:
            if self.prev_action != None:
                if self.prev_action.type == ActionType.GROW and self.status.trees[self.prev_action.target_cell_id] == 2:
                    if action.type == ActionType.COMPLETE:
                        continue
                if self.prev_action.type == ActionType.GROW and self.status.trees[self.prev_action.target_cell_id] == 1:
                    if action.type == ActionType.COMPLETE:
                        continue
                    if action.type == ActionType.GROW and self.status.trees[action.target_cell_id] == 2:
                        continue
                if self.prev_action.type == ActionType.GROW and self.status.trees[self.prev_action.target_cell_id] == 0:
                    if action.type == ActionType.COMPLETE:
                        continue
                    if action.type == ActionType.GROW and self.status.trees[action.target_cell_id] == 1:
                        continue
                    if action.type == ActionType.GROW and self.status.trees[action.target_cell_id] == 2:
                        continue
                if self.prev_action == ActionType.SEED:
                    if action.type != ActionType.SEED or action.type != ActionType.WAIT:
                        continue

            root.add_child(Node(action, True))

        for _ in range(len(root.childs)*2):
            path = []
            self.status.revert_to_origin()
            self.selection(root, path)
            if path[-1].visit != 0:
                self.expansion(path)
                continue
            score = self.playout(path)
            self.backpropagation(path, score)

        max_val = -1
        max_node = None
        for child in root.childs:
            if child.visit == 0:
                max_node = child
                assert()
                break
            ucb1 = child.score/child.visit + math.sqrt(2)*math.sqrt(math.log(root.visit)/child.visit)
            if ucb1 > max_val:
                max_val = ucb1
                max_node = child

        # plog(f'esp time: {time.time() - start}')
        # plog(f'root visit: {root.visit}, score: {root.score}')
        if not max_node:
            self.prev_action = self.status.action_pool.get_action(ActionType.WAIT)
            return self.status.action_pool.get_action(ActionType.WAIT)
        self.prev_action = max_node.action
        return max_node.action


number_of_cells = int(input())
pinput(number_of_cells)
game = Game()
status = game.status
for i in range(number_of_cells):
    cell_index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    pinput(f'{cell_index} {richness} {neigh_0} {neigh_1} {neigh_2} {neigh_3} {neigh_4} {neigh_5}')
    board.append(Cell(cell_index, richness, [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]))

while True:
    _day = int(input())
    pinput(_day)
    status.day = _day
    nutrients = int(input())
    pinput(nutrients)
    status.nutrients = nutrients
    sun, score = [int(i) for i in input().split()]
    pinput(f'{sun} {score}')
    status.my_sun = sun
    status.my_score = score
    opp_sun, opp_score, opp_is_waiting = [int(i) for i in input().split()]
    pinput(f'{opp_sun} {opp_score} {opp_is_waiting}')
    status.opponent_sun = opp_sun
    status.opponent_score = opp_score
    status.opponent_is_waiting = opp_is_waiting

    number_of_trees = int(input())
    pinput(number_of_trees)
    status.init_trees()
    for i in range(number_of_trees):
        inputs = input().split()
        pinput(' '.join(inputs))
        cell_index = int(inputs[0])
        size = int(inputs[1])
        is_mine = inputs[2] != "0"
        is_dormant = inputs[3] != "0"
        status.add_tree(cell_index, size, is_mine == 1, is_dormant)

    # plog('-- trees --')
    # for i in range(number_of_trees):
    #     plog(status.trees[i])
    # plog('-- nutrients --')
    # plog(status.nutrients)
    # plog('-- cells --')
    # for cell in status.board:
    #     plog(cell)

    number_of_possible_actions = int(input())
    pinput(number_of_possible_actions)
    status.possible_actions.clear()
    # plog('-- possible actions --')
    for i in range(number_of_possible_actions):
        possible_action = input()
        pinput(possible_action)
        split = possible_action.split(' ')
        if split[0] == ActionType.WAIT.name:
            status.possible_actions.append(status.action_pool.get_action(ActionType.WAIT))
        if split[0] == ActionType.SEED.name:
            status.possible_actions.append(status.action_pool.get_action(ActionType.SEED, int(split[2]), int(split[1])))
        if split[0] == ActionType.GROW.name:
            status.possible_actions.append(status.action_pool.get_action(ActionType.GROW, int(split[1])))
        if split[0] == ActionType.COMPLETE.name:
            status.possible_actions.append(status.action_pool.get_action(ActionType.COMPLETE, int(split[1])))

    status.save_origin()

    print(game.compute_next_action())