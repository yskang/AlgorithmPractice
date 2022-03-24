import sys
import subprocess
import os
import argparse


TEST_FILE_NAME = 'test_input.in'
OUT_FILE_NAME = 'out.out'


def run_input_generater(script_name: str):
    out = subprocess.check_output(['python3', script_name], encoding='UTF-8')
    f = open(TEST_FILE_NAME, 'w')
    f.write(out)
    f.close()


def run_solution(solution: str):
    input_file = open(TEST_FILE_NAME, 'r')
    if solution.endswith('py'):
        res = subprocess.check_output(['time','python3', solution], encoding='UTF-8', stdin=input_file)
    else:
        res = subprocess.check_output(['./' + solution], encoding='UTF-8', stdin=input_file)
    input_file.close
    return res

def run_verifier(verifier: str):
    res = subprocess.check_output(['python3', verifier, TEST_FILE_NAME, OUT_FILE_NAME], encoding='UTF-8')
    if res.strip() == 'True':
        print('wow true')
        return True
    print('Hmm not true')
    return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', help='script of your solution to test')
    parser.add_argument('-g', help='good solution to be compaired')
    parser.add_argument('-i', help='input generation script')
    parser.add_argument('-v', help='verifier')
    args = parser.parse_args()

    while True:
        if args.s and args.g and args.i:
            run_input_generater(args.i)
            f = open(TEST_FILE_NAME, 'r')
            input_data = f.readlines()
            input_data = ''.join(input_data)
            f.close()
            print('Input:')
            print(input_data)
            test_sol = run_solution(args.s)
            answer = run_solution(args.g)


            if test_sol == answer:
                print('good')
            else:
                f = open(TEST_FILE_NAME, 'r')
                input_data = f.readlines()
                input_data = ''.join(input_data)
                f.close()
                print('Fail!!')
                print('your answer:')
                print(test_sol)
                print('right answer:')
                print(answer)
                print('Input:')
                print(input_data)
                break
        elif args.s and args.v and args.i:
            run_input_generater(args.i)
            test_sol = run_solution(args.s)
            f = open(OUT_FILE_NAME, 'w')
            f.write(test_sol)
            f.close()
            if run_verifier(args.v):
                print('good')
            else:
                f = open(TEST_FILE_NAME, 'r')
                input_data = f.readlines()
                input_data = ''.join(input_data)
                f.close()
                print('Fail!!')
                print('your answer:')
                print(test_sol)
                print('Input:')
                print(input_data)
                break
        else:
            print('all of -s -g -i or -s -v -i should be existed.')
            print('see help using --h')
            return



if __name__ == '__main__':
    main()