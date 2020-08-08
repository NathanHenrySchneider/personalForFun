#alternating neighborhoods

import time

import random

import colorama

from colorama import Back, Fore, Style

import sys

def print_finite_map():
    colorama.init()
    str_prnt = ""

    y = 0
    while (y <= bound):

        x = 0
        while (x <= bound):
            chr_num = map_instances[len(map_instances) - 1][x + (y * (bound + 1))]
            if (chr_num == 0):
                str_prnt += (Back.BLACK + "   " + Style.RESET_ALL)
            else:
                str_prnt += (Back.GREEN + "   " + Style.RESET_ALL)
            x += 1
            sys.stdout.write(Style.RESET_ALL)

        str_prnt += (Style.RESET_ALL + "\n")

        y += 1

    sys.stdout.write(str_prnt)
    sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL +'\x1b['+str(bound + 1)+'A')
    sys.stdout.flush()
    #sys.stdout.write(Style.RESET_ALL)
    #sys.stdout.flush()
    colorama.deinit()

def generate_initial_table(l, side, n_one, n_two):
    print("\n\n\nINTITAL TABLE\n\n\n\n\n")
    global map_instances
    map_instances = []
    global bound
    bound = side - 1
    global first_map
    first_map = [0] * (side * side)
    global len_map
    len_map = len(first_map)

    global neighborhood_one_birth
    neighborhood_one_birth = n_one[0]

    global neighborhood_one_survival
    neighborhood_one_survival = n_one[1]

    global neighborhood_two_birth
    neighborhood_two_birth = n_two[0]

    global neighborhood_two_survival
    neighborhood_two_survival = n_two[1]

    if (type(l) != type([])):
        return
    if (len(l) == 0):
        return

    n = 0
    while (n < len(l)):

        point = l[n]
        if (type(point) != type([]) or len(point) != 2):
            print("invalid entry:" + str(point))
            n += 1
            continue
        x = point[0]
        y = point[1]
        if (x > bound or y > bound):
            print("invalid point:" + str(point))

        else:
            first_map[x + (y * (bound + 1))] = 1

        n += 1

        map_instances.append(first_map)

def generate_initial_table_random(side, n_one, n_two):
    random_points = []
    x = 0
    while (x < side):

        y = 0
        while (y < side):
            rand_num = random.randint(0,1)
            if (rand_num % 2 == 0):
                random_points.append([x,y])
            y += 1

        x += 1
    #print("random_points:"+str(random_points))
    #print("\n\n")
    generate_initial_table(random_points, side, n_one, n_two)

def find_score_for_point(point):
    x = point % (bound + 1)
    y = (point - x) / (bound + 1)
    current_map = map_instances[len(map_instances) - 1]
    value = current_map[point]

    score = 0

    if (cycle_count % 2 == 0):

        #top
        if (y != 0):
            top = current_map[point - bound - 1]
            score += top

        #right
        if (x != bound):
            right = current_map[point + 1]
            score += right

        #bottom
        if (y != bound):
            bottom = current_map[point + bound + 1]
            score += bottom

        #left
        if (x != 0):
            left = current_map[point - 1]
            score += left

    else:

        #diagonal top right
        if (x != bound and y != 0):
            top_right = current_map[point - bound]
            score += top_right

        #diagonal bottom right
        if (x != bound and y != bound):
            bottom_right = current_map[point + bound + 2]
            score += bottom_right

        #diagonal bottom left
        if (y != bound and x != 0):
            bottom_left = current_map[point + bound]
            score += bottom_left

        #diagonal top left
        if (x != 0 and y != 0):
            top_left = current_map[point - bound - 2]
            score += top_left

    return (score, value)

def new_value_from_score(point):
    score_value = find_score_for_point(point)
    score = score_value[0]
    value = score_value[1]

    if (cycle_count % 2 == 0):

        #birth
        if (value == 0 and score in neighborhood_one_birth):
            return 1

        #survival
        elif (value == 1 and score in neighborhood_one_survival):
            return 1

        else:
            return 0

    else:

        #birth
        if (value == 0 and score in neighborhood_two_birth):
            return 1

        #survival
        elif (value == 1 and score in neighborhood_two_survival):
            return 1

        else:
            return 0

def run_tick():
    temp_new_finite_map = [0] * ((bound + 1)**2)

    n = 0
    while (n < len_map):
        temp_new_finite_map[n] = new_value_from_score(n)
        n += 1

    map_instances.append(temp_new_finite_map)

def run_cycle():
    str_clear_screen = "\n" * (bound + 100)
    print(str_clear_screen)
    global cycle_count
    cycle_count = 0

    while (cycle_count < 500):
        print_finite_map()
        run_tick()
        cycle_count += 1
        time.sleep(.05)

    print_finite_map()
    sys.stdout.write("\033[1000000;3H"+"\n")
    sys.stdout.flush()
    print("\nEND\n")


#(points, side, n_one, n_two)
#n[0] = birth
#n[1] = survival
generate_initial_table_random(150,[[1,3],[3]],[[4,3],[0,3,4]])
run_cycle()

#pseudo traffic [3,1],[3,4]],[[3,4],[3,2]]
#pseudo expanding ameoba
#grid thing [[0,4],[4]],[[2,1,4],[3,4]]
#oscilating hypnotism [[0],[4]],[[4],[4]]
#repopulation [[0],[4]],[[4],[1,2]]
#rapidly shrinking amoeba [[3,4],[0,1,2,4]],[[4,3],[3,4,2]]
#few gliders [[1,3],[3]],[[4,3],[0,3,4]]
#gliders and diamonds [[1,3],[3]],[[4,3],[0,4]]
#small gliders [[2,3],[2,3,4]],[[2,3],[1,4]]
#rivers [[1,2,3,4],[]],[[0],[]]
#small diamonds [[1,2],[2]],[[2],[0]]
#only oscilators [[1,3,2],[2,3]],[[3,4],[0,4,3]]
#bizzare chaotic spaceships and oscillators [[3,4],[]],[[2,1],[0,1]]
#oscilating abstract blobs [[3,4,2,1],[0]],[[3,4],[4]]

#######################################################
#AWESOME GLIDERS & DIAMONDS [[1,3],[2,3]],[[3,4],[0,4]]
#######################################################




#few gliders [[1,3],[3]],[[4,3],[0,3,4]]
#gliders and diamonds [[1,3],[3]],[[4,3],[0,4]]
#small gliders [[2,3],[2,3,4]],[[2,3],[1,4]]
#small diamonds [[1,2],[2]],[[2],[0]]
