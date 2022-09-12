import random
import time
from datetime import datetime

n = int(input())

random_number = set()
# 숫자 중복 없음
# def baseball_game(n):

result = []
if n > 10:
    print('1~9 사이의 숫자를 입력해 주세요')
# for _ in range(n):
else:
    while len(random_number) < n:
        random_number.add(random.randint(0, 9))
    # result.append(random_number)
random_number = list(random_number)
random.shuffle(random_number)
print(random_number)
# return random_number

start_time = time.time()
count = 0
mynumber = []
while True:
    mynumber = list(input().split())
    if 'exit' in mynumber:
        break
    else:
        for i in range(len(mynumber)):
            mynumber[i] = int(mynumber[i])
    ball = 0
    strike = 0
    out = 0
    count += 1
    for i in range(len(mynumber)):
        if mynumber[i] == random_number[i]:
            strike += 1
        elif mynumber[i] in random_number:
            ball += 1
        else:
            out += 1
    if mynumber == random_number:
        end_time = time.time()
        time_taken = end_time - start_time
        print('성공!!')
        print(f'정답을 맞추기까지 입력한 횟수:{count}')
        print(f'정답을 맞추기까지 소요된 시간:{time_taken}')
        print('정답을 맞춘 시간:', datetime.now())
    else:
        print(f'ball: {ball}, strike: {strike}')
    # if input() == 'exit':
    #     break
