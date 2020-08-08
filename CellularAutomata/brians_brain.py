#Brian's Brain

import time

global on
on = 1
global dying
dying = 2
global off
off = 3

import colorama

import sys

import random


def print_finite_map():
    str_prnt = ""
    y = 0
    while (y < y_bound + 1):
        x = 0
        str_prnt += " "
        while (x < x_bound + 1):
            chr_num = map_instances[len(map_instances) - 1][x + (y * (x_bound + 1))]
            str_X_O = ""
            if (chr_num == on):
                str_X_O = "X"
            if (chr_num == dying):
                str_X_O = "*"
            if (chr_num == off):
                str_X_O = " "
            str_prnt += str_X_O + " "
            x += 1
        str_prnt += "\n"
        y += 1
    print(str_prnt)

def generate_initial_table(l, side_one, side_two):
    global map_instances
    map_instances = []
    global x_bound
    x_bound = side_one - 1
    global y_bound
    y_bound = side_two - 1
    global finite_map
    finite_map = [off] * (side_one * side_two)
    global len_map
    len_map = len(finite_map)
    if(type(l) != type([])):
        return
    if(len(l) == 0):
        return
    n = 0
    while (n < len(l)):
        point = l[n]
        if (type(point) != type([]) or len(point) != 2):
            print("invalid entry: "+str(point))
            n += 1
            continue
        x = point[0]
        y = point[1]
        if (x > x_bound or y > y_bound):
            print("invalid point: "+str(point))
        else:
            finite_map[x + ((y_bound + 1) * y)] = 1
        n += 1

    map_instances.append(finite_map)

def generate_initial_table_square(l, square):
    generate_initial_table(l, square, square)

def generate_initial_table_random(side):
    random_points = []
    x = 0
    while(x < side):
        y = 0
        while (y < side):
            rand_num = random.randint(0,3)
            if (rand_num % 2 == 0):
                random_points.append([x,y])
            y += 1
        x += 1
    generate_initial_table(random_points,side,side)

def find_score_for_point(point):
    x = point % (x_bound + 1)
    y = (point - x) / (x_bound + 1)
    current_map = map_instances[len(map_instances) - 1]
    value = current_map[point]

    score = 0
    if (y != 0):
        top = current_map[point - x_bound - 1]
        if (top == on):
            score += 1

    if (x != x_bound and y != 0):
        top_right = current_map[point - x_bound]
        if (top_right == on):
            score += 1

    if (x != x_bound):
        right = current_map[point + 1]
        if (right == on):
            score += 1

    if  (x != x_bound and y != y_bound):
        bottom_right = current_map[point + x_bound + 2]
        if (bottom_right == on):
            score += 1

    if (y != y_bound):
        bottom = current_map[point + x_bound + 1]
        if (bottom == on):
            score += 1

    if (y != y_bound and x != 0):
        bottom_left = current_map[point + x_bound]
        if (bottom_left == on):
            score += 1

    if (x != 0):
        left = current_map[point - 1]
        if (left == on):
            score += left

    if (x != 0 and y != 0):
        top_left = current_map[point - x_bound - 2]
        if (top_left == on):
            score += 1

    return(score, value)


def new_value_from_score(point):
    score_value = find_score_for_point(point)
    score = score_value[0]
    value = score_value[1]
    if (value == on):
        return dying
    if (value == dying):
        return off
    if (value == off and score >1):
        return on
    else:
        return off

def run_tick():
    temp_new_finite_map = [off] * ((x_bound + 1) * (y_bound + 1))
    n = 0
    while (n < len_map):
        temp_new_finite_map[n] = new_value_from_score(n)
        n += 1
    map_instances.append(temp_new_finite_map)

def run_cycle():
    str_clear_screen = "\n" * (x_bound + 25)
    print(str_clear_screen)
    cycles_count = 0
    while (on in map_instances[cycles_count] and cycles_count < 100):
        #print("cycle:"+str(cycles_count))
        print_finite_map()
        run_tick()
        cycles_count += 1
        time.sleep(.3)
    sys.stdout.write("\033[1000000;3H"+"\n")
    print("\nEND\n")

#generate_initial_table_square([[25,20],[26,20],[25,21],[26,21],[25,22],[26,22],[25,23],[26,23],[25,24],[26,24],[25,25],[26,25],[25,26],[26,26],[25,27],[26,27],[25,28],[26,28],[25,29],[26,29],[25,30],[26,30],     [12,12],[13,12],[12,13],[13,13],[37,37],[38,37],[37,38],[38,38],[37,12],[38,12],[37,13],[38,13],[12,37],[13,37],[12,38],[13,38]],52)
generate_initial_table_random(25)
run_cycle()
#print("butt")

#cross looking thing [25,25],[26,25],[25,26],[26,26],[12,12],[13,12],[12,13],[13,13],[37,37],[38,37],[37,38],[38,38],[37,12],[38,12],[37,13],[38,13],[12,37],[13,37],[12,38],[13,38]
