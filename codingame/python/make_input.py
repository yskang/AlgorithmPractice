import os

folder = './codingame/test_data/'
temp_file = 'temp.in'
log_file = 'spring_challenge_2021.in'
temp2_file = 'temp2.in'

temp = open(f'{folder}{temp_file}', 'w')
with open(f'{folder}{log_file}', 'r') as fp:
    while True:
        line = fp.readline()
        if line == '':
            break
        if line.startswith('input:'):
            temp.write(line.split(':')[1])

temp.close()

os.rename(f'{folder}{log_file}', f'{folder}{temp2_file}')
os.rename(f'{folder}{temp_file}', f'{folder}{log_file}')
os.rename(f'{folder}{temp2_file}', f'{folder}{temp_file}')
