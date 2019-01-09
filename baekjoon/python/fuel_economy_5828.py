# Title: Fuel Economy
# Link: https://www.acmicpc.net/problem/5828

import sys


sys.setrecursionlimit(10 ** 6)


read_list_int = lambda: list(map(int, sys.stdin.readline().strip().split(' ')))


INF = 9999999999999999


def solution(num_station: int, tank_full: int, initial_fuel: int, total_distance: int, gas_stations: list):
    gas_stations = sorted(gas_stations, key=lambda gs: gs[0]) + [[total_distance, 0]]
    current_position = 0
    current_value = INF
    current_gas = initial_fuel
    total_cost = 0
    idx = 1

    if gas_stations[0][0] == 0:
        current_position = 0
        current_value = gas_stations[0][1]
        current_gas = initial_fuel
    else:
        current_position = gas_stations[0][0]
        current_value = gas_stations[0][1]
        current_gas = initial_fuel - current_position

    while True:
        cheap_gas_value = INF
        cheap_idx = -1

        is_cheaper_station = False
        while gas_stations[idx][0] <= current_position + tank_full:
            if current_value >= gas_stations[idx][1]:
                if gas_stations[idx][0] - current_position <= current_gas:
                    current_gas -= (gas_stations[idx][0] - current_position)
                else:
                    total_cost += ((gas_stations[idx][0] - current_position) - current_gas) * current_value
                    current_gas = 0
                current_position = gas_stations[idx][0]
                current_value = gas_stations[idx][1]
                is_cheaper_station = True
                idx = idx + 1
                break
            if gas_stations[idx][1] < cheap_gas_value:
                cheap_gas_value = gas_stations[idx][1]
                cheap_idx = idx
            idx += 1

        if not is_cheaper_station:
            if cheap_idx == -1:
                return -1
            total_cost += (tank_full - current_gas) * current_value
            current_gas = tank_full - (gas_stations[cheap_idx][0] - current_position)
            current_position = gas_stations[cheap_idx][0]
            current_value = cheap_gas_value
            idx = cheap_idx + 1
        
        if current_position == total_distance:
            break

    return total_cost        



def main():
    n, g, b, d = read_list_int()
    gas_stations = []
    for _ in range(n):
        gas_stations.append(read_list_int())
    print(solution(n, g, b, d ,gas_stations))


if __name__ == '__main__':
    main()