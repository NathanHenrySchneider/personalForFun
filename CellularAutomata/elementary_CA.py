#Elementary Cellular Automata


import time

import math

import random

from colorama import Fore, Back, Style

def generate_intial_table(l, leng, iters,inj_p,p_char,pat_desig,inject_val):
    global length
    length = leng
    global map_instances
    map_instances = []
    global iterations
    iterations = iters
    global injection_points
    injection_points = inj_p
    global print_char
    print_char = p_char
    global pattern_deisgnation
    pattern_deisgnation = pat_desig
    global injection_value
    injection_value = inject_val

    first_instance = [0]* (length)

    if (type(l) != type([])):
        return
    if (len(l) == 0):
        return
    n = 0
    while (n <len(l)):
        point = l[n]
        if (type(point) != type(0)):
            print("invalid entry: "+str(point))
            n += 1
            continue
        if (point >= length or point < 0):
            print("invalid point: "+str(point))
        else:
            first_instance[point] = 1
        n += 1
    print(first_instance)
    map_instances.append(first_instance)

def generate_intial_table_random(leng,iters,inj_p,p_char,pat_desig,inject_val):
    random_points = []
    n = 0
    while (n < leng):
        rand_num = random.randint(0,1)
        if (rand_num % 2 == 0):
            random_points.append(n)
        n += 1
    generate_intial_table(random_points, leng, iters, inj_p, p_char, pat_desig, inject_val)



def print_finite_map():
    str_prnt = ""
    empty_lines = "\n"
    str_prnt += ((iterations - len(map_instances)) * empty_lines)
    n = 0
    while(n < len(map_instances)):
        x = 0
        str_prnt_line = ""
        while (x < length and len(str_prnt_line) < 700):
            chr_num = map_instances[n][x]
            str_X_O = ""
            if (chr_num == 0):
                str_X_O = " "
            else:
                str_X_O = print_char

            str_prnt_line += str_X_O
            x += 1
        str_prnt += str_prnt_line + "\n"
        n += 1
    return(str_prnt)

def print_overlayed_maps():
    final_final_map = ""
    x = 0
    len_final_maps = len(final_maps)
    print(len(final_maps))
    len_singl_map = len(final_maps[0])
    while(x < len_singl_map):
        if (final_maps[0][x] == "\n"):
            final_final_map += "\n"
            x += 1
            continue
        chars_at_index_x = []
        n = 0
        while (n < len_final_maps):
            if (final_maps[n][x] != " "):
                chars_at_index_x += final_maps[n][x]
            n += 1
        if (len(chars_at_index_x) == 0):
            final_final_map += " "
        elif (len(chars_at_index_x) == 1):
            final_final_map += chars_at_index_x[0]
        else:
            final_final_map += interferance_char
        x += 1
    return(final_final_map)


def find_pattern_for_point(point):
    current_map = map_instances[len(map_instances) - 1]

    str_pattern = ""
    if (point == 0):
        str_pattern += str(0) + str(current_map[point]) + str(current_map[point + 1])
    elif (point == length - 1):
        str_pattern += str(current_map[point - 1]) + str(current_map[point]) + str(0)
    else:
        str_pattern += str(current_map[point - 1]) + str(current_map[point]) + str(current_map[point + 1])
    return str_pattern

def new_value_from_pattern(point):
    pattern = find_pattern_for_point(point)
    pattern_sierpinski = ["111","101","010","000"] #90
    pattern_conus = ["111","110","101","000"] #30
    pattern_184 = ["110","010","001","000"]
    pattern_58 = ["111","110","010","000"]
    pattern_150 = ["110","101","011","000"]
    pattern_110 = ["111","100","000"] #Turing Complete
    pattern_custom = []
    selected_pattern = []
    if (pattern_deisgnation == "s"):
        selected_pattern = pattern_sierpinski
    elif (pattern_deisgnation == "c"):
        selected_pattern = pattern_conus
    elif (pattern_deisgnation == "184"):
        selected_pattern = pattern_184
    elif (pattern_deisgnation == "58"):
        selected_pattern = pattern_58
    elif (pattern_deisgnation == "150"):
        selected_pattern = pattern_150
    elif (pattern_deisgnation == "110"):
        selected_pattern = pattern_110
    else:
        selected_pattern = pattern_sierpinski

    if (pattern in selected_pattern):
        return 0
    else:
        return 1

def injection():
    n = 0
    while (n < len(injection_points)):
        if (len(injection_points[n]) == 0):
            n += 1
            continue
        if (cycles_count == injection_points[n][0]):
            x = 1
            while (x < len(injection_points[n])):
                map_instances[len(map_instances) - 1][injection_points[n][x]] = injection_value
                x += 1
        n += 1

def run_tick():
    temp_new_finite_map = [0] * (length)
    n = 0
    while(n < length):
        temp_new_finite_map[n] = new_value_from_pattern(n)
        n += 1
    map_instances.append(temp_new_finite_map)
    injection()

def run_cycle():
    global cycles_count
    cycles_count = 0
    while (cycles_count < 1000):
        #print("cycle:"+str(cycles_count))
        print(print_finite_map())
        run_tick()
        time.sleep(.05)

        cycles_count += 1
    print(print_finite_map())

def run_multiple(maps,interf_char):
    print("run_multiple")
    global final_maps
    final_maps = []
    global interferance_char
    interferance_char = interf_char
    X = 0
    print("while")
    while(X < len(maps)):
        print("X:"+str(X))
        generate_intial_table(maps[X][0],maps[X][1],maps[X][2],maps[X][3],maps[X][4],maps[X][5],maps[X][6])
        print("maps[X][0]:"+str(maps[X][0]))
        run_cycle()
        print(print_finite_map())
        final_maps.append(print_finite_map())
        X += 1
    print(print_overlayed_maps())

#generate_intial_table([0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,   150,152,153, 157,   163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,   257,258,259,260,   263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,   349,350,351,352,   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,   499,500,501,502,   503, 509, 521, 523, 541, 547, 557, 563,    569,570, 571,572,573,     577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009
#],700,300,[],"X","s",1)
generate_intial_table_random(600,500,[],"X","s",1)
#run_cycle()
#generate_intial_table([350], 700,500,[],"X","s",1)
run_cycle()



#run_multiple([[[1, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691], 700, 1000, [[0, 0], [1, 0], [2, 0], [3, 0], [5, 0], [7, 0], [11, 0], [13, 0], [17, 0], [19, 0], [23, 0], [29, 0], [31, 0], [37, 0], [41, 0], [43, 0], [47, 0], [53, 0], [59, 0], [61, 0], [67, 0], [71, 0], [73, 0], [79, 0], [83, 0], [89, 0], [97, 0], [101, 0], [103, 0], [107, 0], [109, 0], [113, 0], [127, 0], [131, 0], [137, 0], [139, 0], [149, 0], [151, 0], [157, 0], [163, 0], [167, 0], [173, 0], [179, 0], [181, 0], [191, 0], [193, 0], [197, 0], [199, 0]], "O", "s",0], [[10000], 700, 1000, [[50, 175, 176, 177, 178, 179, 180], [50, 525, 524, 523, 522, 521, 520], [50, 350, 349, 348, 351, 352], [25, 262, 263, 264, 265, 266], [25, 437, 438, 439, 436, 435],[50,83,84,85,86,87],[50,608,609,610,611,612]], "X", "s",1]], "X")





#even numbers [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]

#multiples of ten [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]

#primes  [1, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039]

#primes with clustering 0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,   150,152,153, 157,   163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,   257,258,259,260,   263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,   349,350,351,352,   353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,   499,500,501,502,   503, 509, 521, 523, 541, 547, 557, 563,    569,570, 571,572,573,     577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009

#stabalizers for conus [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0], [32, 0], [33, 0], [34, 0], [35, 0], [36, 0], [37, 0], [38, 0], [39, 0], [40, 0], [41, 0], [42, 0], [43, 0], [44, 0], [45, 0], [46, 0], [47, 0], [48, 0], [49, 0], [50, 0], [51, 0], [52, 0], [53, 0], [54, 0], [55, 0], [56, 0], [57, 0], [58, 0], [59, 0], [60, 0], [61, 0], [62, 0], [63, 0], [64, 0], [65, 0], [66, 0], [67, 0], [68, 0], [69, 0], [70, 0], [71, 0], [72, 0], [73, 0], [74, 0], [75, 0], [76, 0], [77, 0], [78, 0], [79, 0], [80, 0], [81, 0], [82, 0], [83, 0], [84, 0], [85, 0], [86, 0], [87, 0], [88, 0], [89, 0], [90, 0], [91, 0], [92, 0], [93, 0], [94, 0], [95, 0], [96, 0], [97, 0], [98, 0], [99, 0], [100, 0], [101, 0], [102, 0], [103, 0], [104, 0], [105, 0], [106, 0], [107, 0], [108, 0], [109, 0], [110, 0], [111, 0], [112, 0], [113, 0], [114, 0], [115, 0], [116, 0], [117, 0], [118, 0], [119, 0], [120, 0], [121, 0], [122, 0], [123, 0], [124, 0], [125, 0], [126, 0], [127, 0], [128, 0], [129, 0], [130, 0], [131, 0], [132, 0], [133, 0], [134, 0], [135, 0], [136, 0], [137, 0], [138, 0], [139, 0], [140, 0], [141, 0], [142, 0], [143, 0], [144, 0], [145, 0], [146, 0], [147, 0], [148, 0], [149, 0], [150, 0], [151, 0], [152, 0], [153, 0], [154, 0], [155, 0], [156, 0], [157, 0], [158, 0], [159, 0], [160, 0], [161, 0], [162, 0], [163, 0], [164, 0], [165, 0], [166, 0], [167, 0], [168, 0], [169, 0], [170, 0], [171, 0], [172, 0], [173, 0], [174, 0], [175, 0], [176, 0], [177, 0], [178, 0], [179, 0], [180, 0], [181, 0], [182, 0], [183, 0], [184, 0], [185, 0], [186, 0], [187, 0], [188, 0], [189, 0], [190, 0], [191, 0], [192, 0], [193, 0], [194, 0], [195, 0], [196, 0], [197, 0], [198, 0], [199, 0]]

#three evenly spaced numbers 175,87,263

#clusterings every 100 [100,101,102,103,200,201,202,203,300,301,302,303,400,401,402,403,500,501,502,503,600,601,602,603]

#injection peaks [[50,175,176,177,178,179,180],[50,525,524,523,522,521,520],[50,350,349,348,351,352],[25,262,263,264,265,266],[25,437,438,439,436,435]]



#rule 18 or 26 sierpinski triangle (pattern == "111" or pattern == "101" or pattern == "010" or pattern == "000")

#rule 54 (pattern == "111" or pattern == "110" or pattern == "011" or pattern == "000")

#rule 30 conus textille shell pattern == "111" or pattern == "110" or pattern == "101" or pattern == "000"

#rule 57 pattern == "111" or pattern == "110" or pattern == "010" or pattern == "001"
"""
n = 0
tabl = []
while (n < 200):
    if (n % 10 == 0):
        tabl.append(n)
    n += 1
print(tabl)
"""


def sieve_of_eratosthenes(limit):
    #print("")
    start_time = time.time()
    limit = limit + 2
    sieve = [True] * (limit)
    upper_bound_n = math.ceil(math.sqrt(limit))
    n = 2
    while (n <= math.ceil(math.sqrt(limit))):
        #sys.stdout.write(str(n)+"      "+'\r')
        #sys.stdout.flush()
        #print("n: "+str(n))
        m = 0
        while((n * n) + (n * m) < limit):
            #print("m: "+str(m))
            sieve[(n * n) + (n * m)] = False
            m += 1
        n += 1
        #sys.stdout.write("\r"+str(round((n*100)/upper_bound_n,4))+"%  Time: "+str(int((time.time() - start_time)))+"       ")
        #sys.stdout.flush()
    primes_ans = []
    z = 0
    len_sieve = len(sieve)
    while (z < len_sieve):
        #print(sieve[z])
        if (sieve[z]):
            primes_ans.append(z)
        z += 1
        #sys.stdout.write("\r"+str((z*100)/len_sieve)+"%  Time: "+str(int((time.time() - start_time)))+"        ")
        #sys.stdout.flush()
    end_time = time.time()
    #print("")
    #sys.stdout.write(\end_time - start_time)
    #print("\n")
    return primes_ans

#print(sieve_of_eratosthenes(5000))
"""
x = 0
stabalizers = []
prime = sieve_of_eratosthenes(200)
while(x < len(prime)):
    stabalizers.append([prime[x],0])
    x += 1
print(stabalizers)
"""

"""
str_ing = ""
str_ing += (Back.GREEN + " ")

str_ing += (Back.RED + " ")
print(str_ing + Style.RESET_ALL)
print(Style.RESET_ALL + "")
"""
