import random

QUEEN_NUM = 10
INF = 10000000011111111
K_BEST  = 4

k_best_state = []


def initial_state() :
    state = [0 for i in range(QUEEN_NUM)]
    for i in range(QUEEN_NUM) :
        state[i] = random.randint(0,QUEEN_NUM - 1)
    return state

def show_state(state) :
    for i in range(QUEEN_NUM) :
        for j in range(QUEEN_NUM):
            if state[j] == i :
                print('1',end = ' ')
            else :
                print('0',end = ' ')
        print()

def get_fitness (state,a,b) :
    cnt = 0
    for i in range(a,b) :
        for j in range(i + 1,b):
            if (state[i] == state[j]) or (abs(state[i] - state[j]) == j - i) : 
                cnt += 1
    return cnt

def check_solution(state):
    for i in range(QUEEN_NUM) :
        for j in range(i + 1,QUEEN_NUM):
            if (state[i] == state[j]) or (abs(state[i] - state[j]) == j - i) :
                return False
    return True

def cross(l_state , r_state , m) :
    state = [0 for i in range(QUEEN_NUM)]
    for j in range(QUEEN_NUM):
        if j < m :
            state[j] = l_state[j]
        else :
            state[j] = r_state[j]
    return state

def compare(elm) :
    return get_fitness(elm,0,QUEEN_NUM)


def GEN_ALGO ():
    #CrossOver 

    for i in range(K_BEST) :
        random_selection = random.randint(0,QUEEN_NUM - 1)
        k_best_state.append(cross(k_best_state[i],k_best_state[i+1],random_selection))
        k_best_state.insert(0,cross(k_best_state[i+1],k_best_state[i],random_selection))


    # Mutation
    for i in range(K_BEST) :
        for ii in  range(20) :
            random_selection = random.randint(0,QUEEN_NUM - 1)
            mn = INF
            for j in range(QUEEN_NUM) :
                k_best_state[i][random_selection] = j
                temp = get_fitness(k_best_state[i],0,QUEEN_NUM)
                if temp < mn :
                    mn = temp
                    idd = j  
            k_best_state[i][random_selection] = idd


    k_best_state.sort(key = compare)
    for i in range(0,K_BEST // 2):
       k_best_state.pop()

def main():
    for i in range(K_BEST) :
        k_best_state.append(initial_state())
    
    isAns = 0
    while True:
        GEN_ALGO()
        print("##############")
        for i in range(K_BEST):
            print(get_fitness(k_best_state[i],0,QUEEN_NUM))
            # show_state(k_best_state[i])
            if check_solution(k_best_state[i]) == True : 
                print(QUEEN_NUM , ' Queen Answer;)')
                show_state(k_best_state[i])
                isAns = 1 
                break
        if isAns :
            break   

        


if __name__ == "__main__":
    main()