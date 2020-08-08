#Game of Life

import unicodedata

import time

import random

import colorama

import sys

def underscores():
    global underscores
    underscores = u'\uFF3F'
    n = 0
    while (n < x_bound):
        underscores += (u'\uFF3F\uFF3F\uFF3F')#"______"
        n += 1

def overscores():
    global overscores
    overscores = u'\u2594'
    n = 0
    while (n < x_bound + 1):
        overscores += (u'\u2594\u2594\u2594\u2594')
        n += 1

def print_finite_map():
    str_prnt = ""
    #str_prnt += underscores + "\n"
    y = 0
    while (y < y_bound + 1):
        x = 0
        str_prnt += " "
        while (x < x_bound + 1):
            #print(x)
            chr_num = map_instances[len(map_instances) - 1][x + (y * (x_bound + 1))]
            str_X_O = ""
            if (chr_num == 1):
                str_X_O = "X"
            else:
                str_X_O = " "
            str_prnt += str_X_O + " "
            #print("x:"+str(x)+" y:"+str(y)+" point:"+str(x + (y*(x_bound+1)))+" value:"+str(finite_map[x + (y * (x_bound + 1))]))
            x += 1
        str_prnt += "\n"
        y += 1
    #str_prnt += overscores + "\n"
    sys.stdout.write(str_prnt)
    sys.stdout.flush()
    sys.stdout.write('\x1b['+str(x_bound + 1)+'A')
    sys.stdout.flush()

def generate_initial_table(l,side_one,side_two):
    global map_instances
    map_instances = []
    global x_bound
    x_bound = side_one - 1
    global y_bound
    y_bound = side_two - 1
    global finite_map
    finite_map = [0] * (side_one * side_two)
    global len_map
    len_map = len(finite_map)
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
        if (x > x_bound or y > y_bound):
            print("invalid point: " + str(point))
        else:
            finite_map[x + ((y_bound + 1) * y)] = 1
        n += 1
    #print("finite map instantiated")
    #print_finite_map()
    #underscores()
    #overscores()
    map_instances.append(finite_map)
    #print(finite_map)
    #l is a list of lists of length 2
    #each element in l is a coordinate in the table

def generate_initial_table_square(l, square):
    generate_initial_table(l, square, square)

def generate_initial_table_random(side):
    random_points = []
    x = 0
    while(x < side):
        y = 0
        while (y < side):
            rand_num = random.randint(0,1)
            if (rand_num % 2 == 0):
                random_points.append([x,y])
            y += 1
        x += 1
    generate_initial_table(random_points,side,side)

#null_injection_space[0] = side
#null_injection_space[1] = start point
#start_point[0] = x
#start_point[1] = y
def special_generater_intial_table_rand(side,null_injection_space, injection_points_special):
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

    length_null = null_injection_space[0]
    x_start = null_injection_space[1][0]
    y_start = null_injection_space[1][1]
    y_count = y_start
    while (y_count < y_start + length_null and y_count < side):
        #print(y_count)
        x_count = x_start
        while (x_count < x_start+length_null and x_count < side):
            #print(x_count)
            if ([x_count,y_count] in random_points):
                random_points.remove([x_count,y_count])
            x_count += 1
        y_count += 1
    #print(injection_points_special)
    n = 0
    while(n < len(injection_points_special)):
        random_points.append(injection_points_special[n])
        n += 1
    generate_initial_table_square(random_points,side)



def find_score_for_point(point):
    x = point % (x_bound + 1)
    y = (point - x) / (x_bound + 1)
    current_map = map_instances[len(map_instances) - 1]
    value = current_map[point]

    #get score for each adjacent tile starting at top going clockwise
    score = 0
    #top
    if (y != 0):
        top = current_map[point - x_bound - 1]
        score += top
        #print("top:"+str(top))

    #diagonal top right
    if (x != x_bound and y != 0):
        top_right = current_map[point - x_bound]
        score += top_right
        #print("top_right:"+str(top_right))

    #right
    if (x != x_bound):
        right = current_map[point + 1]
        score += right
        #print("right:"+str(right))

    #diagonal bottom right
    if (x != x_bound and y != y_bound):
        bottom_right = current_map[point + x_bound + 2]
        score += bottom_right
        #print("bottom_right:"+str(bottom_right))

    #bottom
    if (y != y_bound):
        bottom = current_map[point + x_bound + 1]
        score += bottom
        #print("bottom:"+str(bottom))

    #diagonal bottom left
    if (y != y_bound and x != 0):
        bottom_left = current_map[point + x_bound]
        score += bottom_left
        #print("bottom_left:"+str(bottom_left))

    #left
    if (x != 0):
        left = current_map[point - 1]
        score += left
        #print("left:"+str(left))

    #diagonal top left
    if (x != 0 and y != 0):
        top_left = current_map[point - x_bound - 2]
        score += top_left
        #print("top_left:"+str(top_left))

    return(score, value)

def new_value_from_score(point):
    score_value = find_score_for_point(point)
    score = score_value[0]
    value = score_value[1]
    if (value == 1 and score < 2):
        return 0
    if (value == 1 and (score == 2 or score == 3)):
        return 1
    if (value == 1 and score > 3):
        return 0
    if (value == 0 and score == 3):
        return 1
    return 0


def run_tick():
    #temp_new_finite_map
    temp_new_finite_map = [0] * ((x_bound + 1) * (y_bound + 1))
    n = 0
    while (n < len_map):
        temp_new_finite_map[n] = new_value_from_score(n)
        n += 1
    map_instances.append(temp_new_finite_map)
    #print (temp_new_finite_map)

def run_cycle():
    str_clear_screen = "\n" * (x_bound + 25)
    print(str_clear_screen)
    cycles_count = 0
    while(cycles_count < 1000):# or 1 in map_instances[cycles_count]  or map_instances[cycles_count] != map_instances[cycles_count - 1]):
        #print("Cycle: "+str(cycles_count))
        print_finite_map()
        #print("\n")
        run_tick()
        cycles_count += 1
        time.sleep(.2)
    sys.stdout.write("\033[1000000;3H"+"\n")
    print("\nEND\n")

def move_points(points_list, x_move, y_move):
    n = 0
    while(n < len(points_list)):
        points_list[n][0] = points_list[n][0] + x_move
        points_list[n][1] = points_list[n][1] + y_move
        n += 1
    return points_list



###################################
#generate_initial_table(move_points([[4,0],[5,0],[6,0],[7,1],[4,1],[4,2],[4,3],[4,4],[4,5],[5,6],[7,6],[8,3],[8,4],[13,0],[12,1],[12,2],[13,1],[14,1],[14,2],[15,2],[17,2],[18,1],[19,1],[19,0],[20,1],[20,2],[10,5],[11,6],[12,6],[13,5],[13,7],[14,6],[18,6],[19,5],[19,7],[20,7],[20,6],[21,6],[22,5],[25,1],[26,0],[27,0],[28,0],[28,1],[28,2],[28,3],[28,4],[28,5],[27,6],[25,6],[1,12],[2,11],[3,11],[4,11],[4,12],[4,13],[4,15],[4,16],[3,17],[1,17],[0,14],[0,15],[31,12],[30,11],[29,11],[28,11],[28,12],[28,13],[28,14],[28,15],[28,16],[29,17],[31,17],[32,14],[32,15],[4,38],[5,37],[6,37],[7,37],[7,38],[7,39],[7,40],[7,41],[6,42],[4,42],[3,40],[28,38],[27,37],[26,37],[25,37],[25,38],[25,39],[25,40],[25,41],[26,42],[28,42],[29,40],[7,97],[8,97],[9,97],[6,98],[9,98],[9,99],[9,100],[9,101],[8,102],[6,102],[5,100],[26,98],[25,97],[24,97],[23,97],[23,98],[23,99],[23,100],[23,101],[24,102],[26,102],[27,100],[18,2],[12,7],[24,3],[24,4],[4,14]],50,50),200,200)
generate_initial_table_random(50)
#special_generater_intial_table_rand(200,[90,[55,55]], move_points([[36,19],[37,19],[36,20],[37,20],[34,23],[35,23],[34,24],[35,24],[21,33],[22,33],[21,34],[22,34],[20,37],[21,37],[20,38],[21,38],[16,39],[17,39],[16,40],[17,40],[36,59],[37,59],[36,60],[37,60],[38,55],[39,55],[38,56],[39,56],[42,54],[43,54],[42,55],[43,55],[51,45],[52,45],[51,46],[52,46],[52,41],[53,41],[52,42],[53,42],[56,39],[57,39],[56,40],[57,40],[31,31],[30,32],[31,32],[32,32],[32,33],[29,33],[28,34],[29,34],[29,35],[30,35],[26,45],[28,45],[26,46],[27,46],[27,47],[31,48],[29,49],[30,49],[30,50],[31,50],[43,44],[44,44],[44,45],[45,45],[44,46],[41,46],[41,47],[42,47],[43,47],[42,48],[42,29],[43,29],[43,30],[44,30],[42,31],[46,32],[46,33],[47,33],[45,34],[47,34],[30,24],[31,24],[30,25],[31,25],[12,7]],60,60))
run_cycle()
###################################

"""
#null_injection_space[0] = side
#null_injection_space[1] = start point
#start_point[0] = x
#start_point[1] = y
def special_generater_intial_table_rand(side,null_injection_space, injection_points):


[86, 69], [87, 69], [86, 70], [87, 70], [84, 73], [85, 73], [84, 74], [85, 74], [71, 83], [72, 83], [71, 84], [72, 84], [70, 87], [71, 87], [70, 88], [71, 88], [66, 89], [67, 89], [66, 90], [67, 90], [86, 109], [87, 109], [86, 110], [87, 110], [88, 105], [89, 105], [88, 106], [89, 106], [92, 104], [93, 104], [92, 105], [93, 105], [101, 95], [102, 95], [101, 96], [102, 96], [102, 91], [103, 91], [102, 92], [103, 92], [106, 89], [107, 89], [106, 90], [107, 90], [81, 81], [80, 82], [81, 82], [82, 82], [82, 83], [79, 83], [78, 84], [79, 84], [79, 85], [80, 85], [76, 95], [78, 95], [76, 96], [77, 96], [77, 97], [81, 98], [79, 99], [80, 99], [80, 100], [81, 100], [93, 94], [94, 94], [94, 95], [95, 95], [94, 96], [91, 96], [91, 97], [92, 97], [93, 97], [92, 98], [92, 79], [93, 79], [93, 80], [94, 80], [92, 81], [96, 82], [96, 83], [97, 83], [95, 84], [97, 84], [80, 74], [81, 74], [80, 75], [81, 75]
"""


#print((finite_map))
#print_finite_map()



#seeds
#beaon [0,0],[1,0],[0,1],[3,2],[2,3],[3,3]
#glider [2,0],[0,1],[2,1],[1,2],[2,2]
#beacon [3, 1], [4, 1], [10, 1], [11, 1], [4, 2], [5, 2], [9, 2], [10, 2], [1, 3], [4, 3], [6, 3], [8, 3], [10, 3], [13, 3], [1, 4], [2, 4], [3, 4], [5, 4], [6, 4], [8, 4], [9, 4], [11, 4], [12, 4], [13, 4], [2, 5], [4, 5], [6, 5], [8, 5], [10, 5], [12, 5], [3, 6], [4, 6], [5, 6], [9, 6], [10, 6], [11, 6], [3, 8], [4, 8], [5, 8], [9, 8], [10, 8], [11, 8], [2, 9], [4, 9], [6, 9], [8, 9], [10, 9], [12, 9], [1, 10], [2, 10], [3, 10], [5, 10], [6, 10], [8, 10], [9, 10], [11, 10], [12, 10], [13, 10], [1, 11], [4, 11], [6, 11], [8, 11], [10, 11], [13, 11], [4, 12], [5, 12], [9, 12], [10, 12], [3, 13], [4, 13], [10, 13], [11, 13]
#gosper's glider gun [2,7],[3,7],[2,6],[3,6],[28, 1], [28, 2], [30, 2], [11, 3], [29, 3], [31, 3], [11, 4], [12, 4], [29, 4], [32, 4], [36, 4], [37, 4], [6, 5], [7, 5], [12, 5], [13, 5], [29, 5], [31, 5], [36, 5], [37, 5], [6, 6], [7, 6], [12, 6], [13, 6], [14, 6], [28, 6], [30, 6], [6, 7], [7, 7], [12, 7], [13, 7], [21, 7], [23, 7], [28, 7], [11, 8], [12, 8], [22, 8], [23, 8], [11, 9], [22, 9]
#period 156 glider gun [36,19],[37,19],[36,20],[37,20],[34,23],[35,23],[34,24],[35,24],[21,33],[22,33],[21,34],[22,34],[20,37],[21,37],[20,38],[21,38],[16,39],[17,39],[16,40],[17,40],[36,59],[37,59],[36,60],[37,60],[38,55],[39,55],[38,56],[39,56],[42,54],[43,54],[42,55],[43,55],[51,45],[52,45],[51,46],[52,46],[52,41],[53,41],[52,42],[53,42],[56,39],[57,39],[56,40],[57,40],[31,31],[30,32],[31,32],[32,32],[32,33],[29,33],[28,34],[29,34],[29,35],[30,35],[26,45],[28,45],[26,46],[27,46],[27,47],[31,48],[29,49],[30,49],[30,50],[31,50],[43,44],[44,44],[44,45],[45,45],[44,46],[41,46],[41,47],[42,47],[43,47],[42,48],[42,29],[43,29],[43,30],[44,30],[42,31],[46,32],[46,33],[47,33],[45,34],[47,34],[30,24],[31,24],[30,25],[31,25]
#pentadecathlon[[4, 5], [7, 5], [12, 5], [15, 5], [2, 6], [3, 6], [4, 6], [7, 6], [8, 6], [9, 6], [10, 6], [11, 6], [12, 6], [15, 6], [16, 6], [17, 6], [4, 7], [7, 7], [12, 7], [15, 7]]
#lidka[[1,0],[0,1],[2,1],[1,2],[8,10],[8,11],[8,12],[6,11],[6,12],[5,12],[4,14],[5,14],[6,14]]
#honey farm 1 [10,10],[11,10],[12,10],[13,10],[14,10],[15,10],[16,10],[17,10]
#eureka[[1,0],[0,1],[2,1],[1,2],[5,2],[6,2],[7,1],[7,3],[8,2],[9,2],[16,0],[15,1],[17,1],[16,2],[1,8],[0,9],[2,9],[1,10],[5,8],[6,8],[7,7],[7,9],[8,8],[9,8],[16,8],[15,9],[17,9],[16,10]]
#backrake3 [[4,0],[5,0],[6,0],[7,1],[4,1],[4,2],[4,3],[4,4],[4,5],[5,6],[7,6],[8,3],[8,4],[13,0],[12,1],[12,2],[13,1],[14,1],[14,2],[15,2],[17,2],[18,1],[19,1],[19,0],[20,1],[20,2],[10,5],[11,6],[12,6],[13,5],[13,7],[14,6],[18,6],[19,5],[19,7],[20,7],[20,6],[21,6],[22,5],[25,1],[26,0],[27,0],[28,0],[28,1],[28,2],[28,3],[28,4],[28,5],[27,6],[25,6],[1,12],[2,11],[3,11],[4,11],[4,12],[4,13],[4,15],[4,16],[3,17],[1,17],[0,14],[0,15],[31,12],[30,11],[29,11],[28,11],[28,12],[28,13],[28,14],[28,15],[28,16],[29,17],[31,17],[32,14],[32,15],[4,38],[5,37],[6,37],[7,37],[7,38],[7,39],[7,40],[7,41],[6,42],[4,42],[3,40],[28,38],[27,37],[26,37],[25,37],[25,38],[25,39],[25,40],[25,41],[26,42],[28,42],[29,40],[7,97],[8,97],[9,97],[6,98],[9,98],[9,99],[9,100],[9,101],[8,102],[6,102],[5,100],[26,98],[25,97],[24,97],[23,97],[23,98],[23,99],[23,100],[23,101],[24,102],[26,102],[27,100],[18,2],[12,7],[24,3],[24,4],[4,14]]


#n = 0
#points = [[1,0],[0,1],[2,1],[1,2],[5,2],[6,2],[7,1],[7,3],[8,2],[9,2],[16,0],[15,1],[17,1],[16,2],[1,8],[0,9],[2,9],[1,10],[5,8],[6,8],[7,7],[7,9],[8,8],[9,8],[16,8],[15,9],[17,9],[16,10]]
#while (n < len(points)):
#    points[n][0]=points[n][0]+5
#    points[n][1]=points[n][1]+5
#    n += 1
#print (points)

"""
glider_mod = [36,19],[37,19],[36,20],[37,20],[34,23],[35,23],[34,24],[35,24],[21,33],[22,33],[21,34],[22,34],[20,37],[21,37],[20,38],[21,38],[16,39],[17,39],[16,40],[17,40],[36,59],[37,59],[36,60],[37,60],[38,55],[39,55],[38,56],[39,56],[42,54],[43,54],[42,55],[43,55],[51,45],[52,45],[51,46],[52,46],[52,41],[53,41],[52,42],[53,42],[56,39],[57,39],[56,40],[57,40],[31,31],[30,32],[31,32],[32,32],[32,33],[29,33],[28,34],[29,34],[29,35],[30,35],[26,45],[28,45],[26,46],[27,46],[27,47],[31,48],[29,49],[30,49],[30,50],[31,50],[43,44],[44,44],[44,45],[45,45],[44,46],[41,46],[41,47],[42,47],[43,47],[42,48],[42,29],[43,29],[43,30],[44,30],[42,31],[46,32],[46,33],[47,33],[45,34],[47,34],[30,24],[31,24],[30,25],[31,25]
x = 0
while (x < len(glider_mod)):
    glider_mod[x][0] += 50
    glider_mod[x][1] += 50
    x += 1

print(glider_mod)
"""
