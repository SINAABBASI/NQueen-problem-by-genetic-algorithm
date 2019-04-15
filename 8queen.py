import random

QUEEN_NUM = 6
INF = 10000000011111111
state = [0 for i in range(QUEEN_NUM)]

def initial_state() :
    for i in range(QUEEN_NUM) :
        state[i] = int(10 * random.random()) % QUEEN_NUM


def show_state() :
    for i in range(QUEEN_NUM) :
        for j in range(QUEEN_NUM):
            if state[j] == i :
                print('1',end = ' ')
            else :
                print('0',end = ' ')
        print()

def check_solution() :
    for i in range(QUEEN_NUM) :
        for j in range(i + 1,QUEEN_NUM):
            if (state[i] == state[j]) or (abs(state[i] - state[j]) == j - i) : 
                return False
    return True

def get_fitness():
    cnt = 0
    for i in range(QUEEN_NUM) :
        for j in range(i + 1,QUEEN_NUM):
            if (state[i] == state[j]) or (abs(state[i] - state[j]) == j - i) :
                 cnt += 1
    return cnt

def GEN_ALGO ():
    random_selection = int(10 * random.random()) % QUEEN_NUM
    mn = INF
    for i in range(QUEEN_NUM) :
        state[random_selection] = i
        temp = get_fitness()
        if temp < mn :
            mn = temp
            idd = i  
    state[random_selection] = idd


def main():
    initial_state()
    show_state()
    while check_solution() == False:
        GEN_ALGO()
    print(QUEEN_NUM , ' Queen Answer;)')
    show_state()

if __name__ == "__main__":
    main()