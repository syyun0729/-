import os
import pickle

FILENAME = 'score.bin'

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    if not s:
        return 0
    return sum(s) / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(scores):
    with open(FILENAME, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    with open(FILENAME, 'rb') as f:
        return pickle.load(f)

scores = []


if os.path.exists(FILENAME):
    print('[파일 읽기]')
    scores = load_scores()
else:
    print('[점수 입력]')
    scores = input_scores()
    save_scores(scores)

# 출력
print('\n[점수 출력]')
print('개인점수: ', end='')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg}')
