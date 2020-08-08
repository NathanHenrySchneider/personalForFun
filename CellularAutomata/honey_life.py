#honey life eight life pedestrian life

import time

import random

import colorama

from colorama import Back, Fore, Style

import math

import sys

global switch_boo

def print_finite_map():
    current_map = map_instances[len(map_instances) - 1]
    colorama.init()
    str_prnt = ""

    y = 0
    while(y <= bound):
        x = 0
        while (x <= bound):
            chr_num = current_map[x + (y * (bound + 1))]
            if (chr_num == 0):
                str_prnt += (Back.BLACK + "   " + Style.RESET_ALL)
            else:
                str_prnt += (Back.YELLOW + "   " + Style.RESET_ALL)
            x += 1
            sys.stdout.write(Style.RESET_ALL)
            sys.stdout.flush()

        str_prnt += (Style.RESET_ALL + "\n")

        y += 1
    sys.stdout.write(str_prnt)
    sys.stdout.flush()
    sys.stdout.write('\x1b['+str(bound + 1)+'A')
    sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    colorama.deinit()

def set_rules(rules_type):

    if (rules_type == "HONEY"):
        born = [3,8]
        survive = [2, 3, 8]

    elif (rules_type == "EIGHT"):
        born = [3]
        survive = [2, 3, 8]

    elif (rules_type == "PED"):
        born = [3, 8]
        survive = [2, 3]

    elif (rules_type == "MAZE"):
        born = [3]
        survive = [1, 2, 3, 4, 5]

    elif (rules_type == "REPLICATOR"):
        born = [1, 3, 5, 7]
        survive = born

    elif (life_type == "DAY&NIGHT"):
        born = [3, 6, 7, 8]
        survive = [3, 4, 6, 7, 8]

    else:
        #honey
        born = [3,8]
        survive = [2, 3, 8]

def set_rules_second():
    if (second_rules == "HONEY"):
        born = [3,8]
        survive = [2, 3, 8]

    elif (second_rules == "EIGHT"):
        born = [3]
        survive = [2, 3, 8]

    elif (second_rules == "PED"):
        born = [3, 8]
        survive = [2, 3]

    elif (second_rules == "MAZE"):
        born = [3]
        survive = [1, 2, 3, 4, 5]

    elif (second_rules == "REPLICATOR"):
        born = [1, 3, 5, 7]
        survive = born

    elif (life_type == "DAY&NIGHT"):
        born = [3, 6, 7, 8]
        survive = [3, 4, 6, 7, 8]

    else:
        #honey
        born = [3,8]
        survive = [2, 3, 8]


def generate_initial_table(l, side, life_type):
    global map_instances
    map_instances = []
    global bound
    bound = side - 1
    global first_map
    first_map = [0] * (side * side)
    global len_map
    len_map = len(first_map)
    global born
    born = []
    global survive
    survive = []
    global rules
    rules = life_type
    global switch_boo
    switch_boo = False


    if (life_type == "HONEY"):
        born = [3,8]
        survive = [2, 3, 8]

    elif (life_type == "EIGHT"):
        born = [3]
        survive = [2, 3, 8]

    elif (life_type == "PED"):
        born = [3, 8]
        survive = [2, 3]

    elif (life_type == "MAZE"):
        born = [3]
        survive = [1, 2, 3, 4, 5]

    elif (life_type == "REPLICATOR"):
        born = [1, 3, 5, 7]
        survive = born

    elif (life_type == "DAY&NIGHT"):
        born = [3, 6, 7, 8]
        survive = [3, 4, 6, 7, 8]

    else:
        #honey
        born = [3,8]
        survive = [2, 3, 8]
    #set_rules(life_type)

    #print("BORN INIT:"+str(born))
    #print("SURVIVE init:"+str(survive))


    if (type(l) != type([])):
        return
    if (len(l) == 0):
        return

    n = 0
    while (n < len(l)):

        point = l[n]
        if (type(point) != type([]) or len(point) != 2):
            print("invalid entry: " + str(point))
            n += 1
            continue

        x = point[0]
        y = point[1]

        if (x > bound or y > bound):
            print("invalid point: " + str(point))
        else:
            first_map[ x + ((bound + 1) * y)] = 1
        n += 1

    map_instances.append(first_map)


def generate_initial_table_random(side, type):
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

    generate_initial_table(random_points, side, type)

def generate_initial_table_random_middle(side, life_type):
    random_points = []

    range = 2 * (side / 3)
    y = side / 3
    while (y < range):
        x = side / 3
        while (x < range):
            rand_num = random.randint(0,1)
            if (rand_num % 2 == 0):
                random_points.append([x,y])
            x += 1
        y += 1

    generate_initial_table(random_points, side, life_type)

def generate_initial_table_random_middle_specific(side, life_type, random_size):
    random_points = []

    start = (side / 2) - (random_size / 2)

    range = (side / 2) + (random_size / 2)
    y = start
    while (y < range):
        x = start
        while (x < range):
            rand_num = random.randint(0,1)
            if (rand_num % 2 == 0):
                random_points.append([x,y])
            x += 1
        y += 1

    generate_initial_table(random_points, side, life_type)

def generate_initial_table_switch(side, first_rules, rules_2nd, switch_time, next_table_gen, *mid_specific):
    global second_rules
    second_rules = rules_2nd
    global switch_cycle
    switch_cycle = switch_time
    global switch_boo
    switch_boo = True
    #print("generate switch boo: "+str(switch_boo))

    if (next_table_gen == "RANDOM"):
        generate_initial_table_random(side, first_rules)
    elif (next_table_gen == "RANDOM_MIDDLE"):
        generate_initial_table_random_middle(side, first_rules)
    elif (next_table_gen == "SPECIFIC_MIDDLE"):
        generate_initial_table_random_middle_specific(side, first_rules, mid_specific[0])
    else:
        generate_initial_table_random(side, first_rules)


    global switch_boo
    switch_boo = True

    #print("special init switch boo: "+str(switch_boo))

def switch_rules_second():
    #print("\n\n\n\n\n\n CALLED SWITCH \n\n\n\n\n")
    #print(second_rules)
    #print("second_rules == MAZE:" + str(second_rules == "MAZE"))
    #print(born)
    #print("SURVIVE:"+str(survive))
    #print("switch boo: "+str(switch_boo))
    if (switch_boo == True and switch_cycle == cycle_count):
        #print("\n\n\n\n\n WORKED \n\n\n\n\n")
        global born
        global survive
        if (second_rules == "HONEY"):
            born = [3,8]
            survive = [2, 3, 8]

        elif (second_rules == "EIGHT"):
            born = [3]
            survive = [2, 3, 8]

        elif (second_rules == "PED"):
            born = [3, 8]
            survive = [2, 3]

        elif (second_rules == "MAZE"):
            #print("\n\n\n\n\ ARIVED AT MAZE SWITCH \n\n\n\n")
            born = [3]
            survive = [1, 2, 3, 4, 5]

        elif (second_rules == "REPLICATOR"):
            born = [1, 3, 5, 7]
            survive = born

        elif (life_type == "DAY&NIGHT"):
            born = [3, 6, 7, 8]
            survive = [3, 4, 6, 7, 8]

        else:
            #honey
            born = [3,8]
            survive = [2, 3, 8]
    else:
        return

def find_score_for_point(point):
    x = point % (bound + 1)
    y = (point - x) / (bound + 1)
    current_map = map_instances[len(map_instances) - 1]
    value = current_map[point]

    score = 0

    #EDGE
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

    #DIAGONAL
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

    if (value == 0 and score in born):
        return 1
    elif (value == 1 and score in survive):
        return 1
    else:
        return 0


def run_tick():
    temp_new_map = [0] * ((bound + 1) ** 2)

    n = 0
    while (n < len_map):
        temp_new_map[n] = new_value_from_score(n)
        n += 1

    map_instances.append(temp_new_map)


def run_cycle():
    str_clear_screen = "\n" * (bound + 100)
    sys.stdout.write(str_clear_screen)
    sys.stdout.flush()

    global cycle_count
    cycle_count = 0

    while (cycle_count < 900):
        #print("BORN CYCLE:"+str(born))
        #print("SURVIVE CYCLE:"+str(survive))
        switch_rules_second()
        print_finite_map()
        run_tick()
        cycle_count += 1
        time.sleep(0.4)

    #print(print_finite_map())
    sys.stdout.write("\033[1000000;3H"+"\n")
    sys.stdout.flush()
    print("\nEND\n")

#life types HONEY EIGHT PED MAZE REPLICATOR


#generate_initial_table([[57, 60], [59, 60], [61, 60], [62, 60], [63, 60], [65, 60], [66, 60], [67, 60], [57, 61], [59, 61], [63, 61], [65, 61], [67, 61], [57, 62], [58, 62], [59, 62], [62, 62], [65, 62], [67, 62], [59, 63], [61, 63], [65, 63], [67, 63], [59, 64], [61, 64], [62, 64], [63, 64], [65, 64], [66, 64], [67, 64]], 125, "REPLICATOR")
#generate_initial_table_random(125, "DAY&NIGHT")
#generate_initial_table_random_middle(125, "DAY&NIGHT")
#generate_initial_table([[49,49],[48,49],[49,50],[51,48],[47,49]],100,"MAZE")

#side, first_rules, rules_2nd, switch_time, next_table_gen
generate_initial_table_switch(125, "MAZE", "REPLICATOR", 10,"SPECIFIC_MIDDLE", 10)
run_cycle()

"""
move_array = [[0,0], [2,0],[4,0],[5,0],[6,0],[8,0],[9,0],[10,0],[0,1],[2,1],[6,1],[8,1],[10,1],[0,2],[1,2],[2,2],[5,2],[8,2],[10,2],[2,3],[4,3],[8,3],[10,3],[2,4],[4,4],[5,4],[6,4],[8,4],[9,4],[10,4]]
n = 0
while(n < len(move_array)):
    move_array[n][0] = move_array[n][0] + 57
    move_array[n][1] = move_array[n][1] + 60
    n += 1

print(move_array)
"""
