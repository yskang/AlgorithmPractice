import sys
import subprocess
import os
import argparse


TEST_FILE_NAME = 'test_input.in'


def run_input_generater(script_name: str):
    out = subprocess.check_output(['time','python3', script_name], encoding='UTF-8')
    f = open(TEST_FILE_NAME, 'w')
    f.write(out)
    f.close()


def run_solution(solution: str):
    input_file = open(TEST_FILE_NAME, 'r')
    if solution.endswith('.py'):
        res = subprocess.check_output(['time','python3', solution], encoding='UTF-8', stdin=input_file)
    else:
        res = subprocess.check_output(['time', solution], encoding='UTF-8', stdin=input_file)
    input_file.close
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='script of your solution to test')
    parser.add_argument('-g', help='good solution to be compaired')
    parser.add_argument('-i', help='input generation script')
    args = parser.parse_args()

    while True:
        if not (args.s and args.g and args.i):
            print('see help using --h')
            return


        run_input_generater(args.i)
        try:
            test_sol = run_solution(args.s)
        except:
            f = open(TEST_FILE_NAME, 'r')
            input_data = f.readlines()
            input_data = ''.join(input_data)
            f.close()
            print('Input:')
            print(input_data)

        answer = run_solution(args.g)

        if test_sol.split('\n')[0] == answer.split('\n')[0]:
            print('good')
            print(answer.split('\n')[0])
        else:
            f = open(TEST_FILE_NAME, 'r')
            input_data = f.readlines()
            input_data = ''.join(input_data)
            f.close()
            print('Fail!!')
            print('your answer:')
            print(test_sol)
            print('right ansser:')
            print(answer)
            print('Input:')
            print(input_data)
            break



if __name__ == '__main__':
    main()