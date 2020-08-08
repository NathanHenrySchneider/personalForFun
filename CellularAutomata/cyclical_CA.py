#cyclical_CA
import colorama
from colorama import Fore, Back, Style
#from termcolor import colored, cprint
import time

import math

import random

import sys

#import tkinter as tk

#colorama colors black, red, green, yellow, blue, magenta, cyan, white, reset
#all caps
#roygbiv

def print_finite_map():
    colorama.init()
    str_prnt = ""
    y = 0
    while (y < bound + 1):
        x = 0
        #str_prnt += " "
        while (x < bound + 1):
            chr_num = map_instances[len(map_instances) - 1][x + (y * (bound + 1))]
            #str_X_color = ""
            if (chr_num == 0):
                #str_X_color += (Back.MAGENTA + " ")
                #sys.stdout.write(Back.MAGENTA + "  " + Style.RESET_ALL)
                str_prnt += (Back.GREEN + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 1):
                #str_X_color += (Back.RED + " ")
                #sys.stdout.write(Back.RED + "  " + Style.RESET_ALL)
                str_prnt += (Back.RED + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 2):
                #str_X_color += (Back.YELLOW + " ")
                #sys.stdout.write(Back.YELLOW + "  " + Style.RESET_ALL)
                str_prnt += (Back.BLUE + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 3):
                str_prnt += (Back.YELLOW + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 4):
                str_prnt += (Back.MAGENTA + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 5):
                str_prnt += (Back.CYAN + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 6):
                str_prnt += (Back.BLACK + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 7):
                str_prnt += (Back.WHITE + "   " + Style.RESET_ALL)
            elif (chr_num == 8):
                #str_X_color += (Back.MAGENTA + " ")
                #sys.stdout.write(Back.MAGENTA + "  " + Style.RESET_ALL)
                str_prnt += (Back.GREEN + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 9):
                #str_X_color += (Back.RED + " ")
                #sys.stdout.write(Back.RED + "  " + Style.RESET_ALL)
                str_prnt += (Back.RED + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 10):
                #str_X_color += (Back.YELLOW + " ")
                #sys.stdout.write(Back.YELLOW + "  " + Style.RESET_ALL)
                str_prnt += (Back.BLUE + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 11):
                str_prnt += (Back.YELLOW + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 12):
                str_prnt += (Back.MAGENTA + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 13):
                str_prnt += (Back.CYAN + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            elif (chr_num == 14):
                str_prnt += (Back.BLACK + "   " + Style.RESET_ALL)
                #sys.stdout.flush()
            else:
                str_prnt += (Back.WHITE + "   " + Style.RESET_ALL)
            x += 1
            sys.stdout.write(Style.RESET_ALL)

            #sys.stdout.flush()
        str_prnt += (Style.RESET_ALL + "\n")
        #sys.stdout.write("\n")

        y += 1
    sys.stdout.write(str_prnt)
    sys.stdout.flush()
    sys.stdout.write('\x1b['+str(bound + 1)+'A')
    sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.flush()
    colorama.deinit()


def generate_initial_table(l,side,enumerated_states,thresh, neighbr, rnge):
    global map_instances
    map_instances = []
    global bound
    bound = side - 1
    global finite_map
    finite_map = [0] * (side**2)
    global len_map
    len_map = side**2
    global states
    states = enumerated_states
    global threshold
    threshold = thresh
    global neighbor_hood
    neighbor_hood = neighbr
    global range
    range = rnge

    if (type(l) != type([])):
        return
    if (len(l) == 0):
        return

    n = 0
    while (n < len(l)):
        point = l[n]
        if (type(point) != type([]) or len(point) != 3):
            print("invalid entry: " + str(point))
            n += 1
            continue
        x = point[0]
        y = point[1]
        if (x > bound or y > bound):
            print("invalid point: " + str(point))
        else:
            finite_map[x + ((bound + 1) * y)] = point[2]
        n += 1
    map_instances.append(finite_map)

def generate_initial_table_random(side, enum_states, thresh, nbrhd, R):
    random_points = []
    x = 0
    while (x < side):
        y = 0
        while (y < side):
            random_points.append([x,y,random.randint(0, enum_states - 1)])
            y += 1
        x += 1
    generate_initial_table(random_points, side, enum_states, thresh, nbrhd, R)

def find_score_for_point(point):
    x = point % (bound + 1)
    y = (point - x) / (bound + 1)
    current_map = map_instances[len(map_instances) - 1]
    value = current_map[point]

    score = 0
    zero_score = 0
    x_0 = x
    y_0 = y

    if (neighbor_hood == "MOORE"):
        ###print("PROBLEM")
        #left
        x_neg = x_0 - 1
        while (x_neg >= 0 and abs(x_neg - x_0) <= range):
            ###print("X_neg:"+str(x_neg))
            ###print("LEFT")

            #up
            y_pos = y_0 - 1
            while (y_pos >= 0 and abs(x_neg - x_0) <= range and abs(y_pos - y_0) <= range):
                top_left = current_map[x_neg + (y_pos * (bound + 1))]
                if (value == states - 1):
                    if (top_left == 0):
                        zero_score += 1
                else:
                    if (top_left == value + 1):
                        score += 1
                y_pos -= 1

            #down
            y_neg = y_0
            while (y_neg <= bound and abs(x_neg - x_0) <= range and abs(y_neg - y_0) <= range):
                bottom_left = current_map[x_neg + (y_neg * (bound + 1))]
                if (value == states - 1):
                    if (bottom_left == 0):
                        zero_score += 1
                else:
                    if (bottom_left == value + 1):
                        score += 1
                y_neg += 1
            x_neg -= 1

        if (score >= threshold):
            ###print("hit threshold:"+str(value + 1))
            return value + 1
        elif (zero_score >= threshold):
            ###print("hit threshold:"+str(0))
            return 0

        #right
        x_pos = x_0 + 1
        while (x_pos <= bound and abs(x_pos - x_0) <= range):
            ##print("X_pos:"+str(x_pos))
            ###print("RIGHT")

            #top_right
            y_pos = y_0 - 1
            while (y_pos >= 0 and abs(x_pos - x_0) <= range and abs(y_pos - y_0) <= range):
                top_right = current_map[x_pos + (y_pos * (bound + 1))]
                if (value == states - 1):
                    if (top_right == 0):
                        zero_score += 1
                else:
                    if (top_right == value + 1):
                        score += 1
                y_pos -= 1

            #bottom_right
            y_neg = y_0
            while (y_neg <= bound and abs(x_pos - x_0) <= range and abs(y_neg - y_0) <= range):
                bottom_right = current_map[x_pos + (y_neg * (bound + 1))]
                if (value == states - 1):
                    if (bottom_right == 0):
                        zero_score += 1
                else:
                    if (bottom_right == value + 1):
                        score += 1
                y_neg += 1
            x_pos += 1

        if (score >= threshold):
            ###print("hit threshold:"+str(value + 1))
            return value + 1
        elif (zero_score >= threshold):
            ###print("hit threshold:"+str(0))
            return 0

        #x vertical up
        y_vert_pos = y_0 - 1
        while (y_vert_pos >= 0 and abs(y_vert_pos - y_0) <= range):
            top = current_map[x_0 + (y_vert_pos * (bound + 1))]
            if (value == states - 1):
                if (top == 0):
                    zero_score += 1
            else:
                if (top == value + 1):
                    score += 1
            y_vert_pos -= 1

        #x vertical down
        y_vert_neg = y_0 + 1
        while (y_vert_neg <= bound and abs(y_vert_neg - y_0) <= range):
            bottom = current_map[x_0 + (y_vert_neg * (bound + 1))]
            if (value == states - 1):
                if (bottom == 0):
                    zero_score += 1
            else:
                if (bottom == value + 1):
                    score += 1
            y_vert_neg += 1

        if (score >= threshold):
            return value + 1
        elif (zero_score >= threshold):
            return 0
        else:
            ###print("score:"+str(score)+" value:"+str(value))
            return value



    if (neighbor_hood == "VN"):
        #left
        x_neg = x_0 - 1
        while(abs(x_neg - x_0) <= range and x_neg >= 0 and x_neg <= bound):

            #top_left
            y_pos = y_0 - 1
            while(y_pos >= 0 and abs(x_neg - x_0) + abs(y_pos - y_0) <= range):
                top_left = current_map[x_neg + (y_pos * (bound + 1))]
                if (value == states - 1):
                    if (top_left == 0):
                        zero_score += 1
                else:
                    if (top_left == value + 1):
                        score += 1
                y_pos -= 1

            #bottom_left
            y_neg = y_0
            while (y_neg <= bound and abs(y_neg - y_0) <= range and abs(x_neg - x_0) + abs(y_neg - y_0) <= range):
                bottom_left = current_map[x_neg + (y_neg * (bound + 1))]
                if (value == states - 1):
                    if (bottom_left == 0):
                        zero_score += 1
                else:
                    if (bottom_left == value + 1):
                        score += 1
                y_neg += 1
            x_neg -= 1

        if (score >= threshold):
            return value + 1
        elif (zero_score >= threshold):
            return 0

        x_pos = x_0 + 1
        while(abs(x_pos - x_0) <= range and x_pos >= 0 and x_pos <= bound):

            #top_right
            y_pos = y_0 - 1
            while (y_pos >= 0 and abs(x_pos - x_0) + abs(y_pos - y_0) <= range):
                top_right = current_map[x_pos + (y_pos * (bound + 1))]
                if (value == states - 1):
                    if (top_right == 0):
                        zero_score += 1
                else:
                    if (top_right == value + 1):
                        score += 1
                y_pos -= 1

            #bottom_right
            y_neg = y_0
            while (y_neg <= bound and abs(x_pos - x_0) + abs(y_neg - y_0) <= range):
                bottom_right = current_map[x_pos + (y_neg * (bound + 1))]
                if (value == states - 1):
                    if (bottom_right == 0):
                        zero_score += 1
                else:
                    if (bottom_right == value + 1):
                        score += 1
                y_neg += 1
            x_pos += 1

        if (score >= threshold):
            return value + 1
        elif (zero_score >= threshold):
            return 0

        #x vertical up
        y_vert_pos = y_0 - 1
        while (y_vert_pos >= 0 and abs(y_vert_pos - y_0) <= range):
            top = current_map[x_0 + (y_vert_pos * (bound + 1))]
            if (value == states - 1):
                if (top == 0):
                    zero_score += 1
            else:
                if (top == value + 1):
                    score += 1
            y_vert_pos -= 1

        #x vertical down
        y_vert_neg = y_0 + 1
        while (y_vert_neg <= bound and abs(y_vert_neg - y_0) <= range):
            bottom = current_map[x_0 + (y_vert_neg * (bound + 1))]
            if (value == states - 1):
                if (bottom == 0):
                    zero_score += 1
            else:
                if (bottom == value + 1):
                    score += 1
            y_vert_neg += 1

        if (score >= threshold):
            return value + 1
        elif (zero_score >= threshold):
            return 0
        else:
            return value

def run_tick():
    temp_new_finite_map = [0] * ((bound + 1)**2)
    n = 0
    while(n < len_map):
        temp_new_finite_map[n] = find_score_for_point(n)
        n += 1
    map_instances.append(temp_new_finite_map)

def run_cycle():
    str_clear_screen = "\n" * (bound + 50)
    print(str_clear_screen)
    cycles_count = 0
    while(cycles_count < 15 or map_instances[cycles_count] != map_instances[cycles_count - states]):
        #print("Cycle: "+str(cycles_count))
        print_finite_map()
        run_tick()
        cycles_count += 1
        time.sleep(.03)
    sys.stdout.write("\033[1000000;3H"+"\n")
    print("\nEND\n")


#side, states (c), threshold (t), neighbor_hood, range
generate_initial_table_random(100,4,2,"MOORE",1)
run_cycle()

###imperfect range=1/threshold=2/states=4/neighbor_hood=moore
#cyclical spirals range=3/threshold=5/states=8/neighbor_hood=moore high power
#macaroni range=2/threshold=4/states=5/neighbor_hood=moore
#amoeba range=3/threshold=10/states=2/neighbor_hood=Von Neuman
###multistrands range=5/threshold=15/states=6/neighbor_hood=Moore
###CCA range=1/threshold=1/states=14/neighbor_hood=moore
#GH range=3/threshold=5/states=8/neighbor_hood=moore
#weak spirals range=4/threshold=9/states=7/neighbor_hood=moore
#cubism range=2/threshold=5/states=3/neighbor_hood=von neuman
#percolation range=5/threshold=10/states=8/neighbor_hood=moore
###boiling range=2/threshold=2/states=6/neighbor_hood=von neuman



"""
sys.stdout.write("yeet \nyeeet\nyeeeet\nyeeeet\nyeeet\n")
sys.stdout.flush()
sys.stdout.write('\x1b[4A')
sys.stdout.flush()
sys.stdout.write("\033[80;3H"+"\n")
print("WEED")
"""
#


"""
score = 0
zero_score = 0
x_0 = x
y_0 = y

#left
x_neg = x_0 - 1
while(abs(x_neg - x_0) <= range and x_neg >= 0 and x_neg <= bound):

    #top_left
    y_pos = y_0 - 1
    while(y_pos >= 0 and abs(x_neg - x_0) + abs(y_pos - y_0) <= range):
        top_left = current_map[x_neg + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (top_left == 0):
                zero_score += 1
        else:
            if (top_left == value + 1):
                score += 1
        y_pos -= 1

    #bottom_left
    y_neg = y_0
    while (y_neg <= bound and abs(n_neg - x_0) + abs(y_neg - y_0) <= range):
        bottom_left = current_map[x_neg + (y_neg * (bound + 1))]
        if (value == states - 1):
            if (bottom_left == 0):
                zero_score += 1
        else:
            if (bottom_left == value + 1):
                score += 1
        y_neg + 1
    x_neg -= 1



x_pos = x_0 + 1
while(abs(x_pos - x_0) <= range and x_pos >= 0 and x_pos <= bound):

    #top_right
    y_pos = y_0 - 1
    while (y_pos >= 0 and abs(x_pos - x_0) + abs(y_pos - y_0) <= range):
        top_right = current_map[x_pos + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (top_right == 0):
                zero_score += 1
        else:
            if (top_right == value + 1):
                score += 1
        y_pos -= 1

    #bottom_right
    y_neg = y_0
    while (y_neg <= bound and abs(x_pos - x_0) + abs(y_neg - y_0) <= range):
        bottom_right = current_map[x_pos + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (top_right == 0):
                zero_score += 1
        else:
            if (top_right == value + 1):
                score += 1
        y_neg += 1
    x_pos += 1

#x vertical up
y_vert_pos = y_0 - 1
while (y_vert_pos >= 0 and abs(y_vert_pos - y_0) <= range):
    top = current_map[x_0 + (y_vert_pos * (bound + 1))]
    if (value == states - 1):
        if (top == 0):
            zero_score += 1
    else:
        if (top == value + 1):
            score += 1
    y_vert_pos -= 1

#x vertical down
y_vert_neg = y_0 + 1
while (y_vert_pos <= bound and abs(y_vert_pos - y_0) <= range):
    bottom = current_map[x_0 + (y_vert_neg * (bound + 1))]
    if (value == states - 1):
        if (bottom == 0):
            zero_score += 1
    else:
        if (bottom == value + 1):
            score += 1
    y_vert_pos += 1
"""





"""
#left
x_neg = x_0 -1
while (x_neg >= 0 and abs(x_neg - x_0) <= range):

    #up
    y_pos = y_0 - 1
    while (y_pos <= 0 and abs(x_neg - x_0) + abs(x_pos - y_0) <= range):
        top_left = current_map[x_neg + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (top_left == 0):
                zero_score += 1
        else:
            if (top_left == value + 1):
                score += 1
        y_pos -= 1

    #down
    y_neg = y_0
    while (y_neg <= bound and abs(x_neg - x_0) + abs(x_pos - y_0) <= range):
        bottom_left = current_map[x_neg + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (bottom_left == 0):
                zero_score += 1
        else:
            if (bottom_left == value + 1):
                score += 1
        y_neg += 1
    x_neg -= 1

#right
x_pos = x_0 + 1
while (x_pos <= bound and abs(x_pos - x_0) <= range):

    #top_right
    y_pos = y_0 - 1
    while (y_pos >= 0 and abs(x_pos - x_0) + abs(y_pos - y_0) <= range):
        top_right = current_map[x_pos + (y_pos * (bound + 1))]
        if (value == states - 1):
            if (top_right == 0):
                zero_score += 1
        else:
            if (top_right == value + 1):
                score += 1
        y_pos -= 1

    #bottom_right
    y_neg = y_0
    while (y_neg <= bound and abs(x_pos - x_0) + abs(y_neg - y_0) <= range):
        bottom_right = current_map[x_pos + (y_neg * (bound + 1))]
        if (value == states - 1):
            if (bottom_right == 0):
                zero_score += 1
        else:
            if (top_right == vlaue + 1):
                score += 1
        y_neg += 1
    x_pos += 1

#x vertical up
y_vert_pos = y_0 - 1
while (y_vert_pos >= 0 and abs(y_vert_pos - y_0) <= range):
    top = current_map[x_0 + (y_vert_pos * (bound + 1))]
    if (value == states - 1):
        if (top == 0):
            zero_score += 1
    else:
        if (top == value + 1):
            score += 1
    y_vert_pos -= 1

#x vertical down
y_vert_neg = y_0 + 1
while (y_vert_neg <= bound and abs(y_vert_pos - y_0) <= range):
    bottom = current_map[x_0 + (y_vert_neg * (bound + 1))]
    if (value == states - 1):
        if (bottom == 0):
            zero_score += 1
    else:
        if (bottom == value + 1):
            score += 1
    y_vert_pos += 1

"""
