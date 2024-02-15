'''
IBEHS 1P10 Mini Milestone 7 Individual File

Name: Imran Chowdhury

Student Number: 400470828

Date: Nov 14, 2022
'''

""" GIVEN Functions """
## This function calculates the gear ratio of your gearing mechanism
## This is a repeat of Mini-Milestone 6 (CP3), Objective #1
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the pitch diameter (in mm) for a set of gears
## This is a repeat of Mini-Milestone 6 (CP3), Objective #2
def calc_PD(gear_list, module):
    pitch_diameter_list = []
    for gear in gear_list:
        pitch_diameter_list.append(gear * module)
    return pitch_diameter_list

## This function calculates the center distance (in mm) between input and output for a set of gears
## This is a repeat of Mini-Milestone 6 (CP3), Objective #3
def calc_CD(pitch_diameter_list):
    center_distance = 0
    for gear in pitch_diameter_list:
        center_distance += gear
    center_distance -= (pitch_diameter_list[0])/2
    center_distance -= (pitch_diameter_list[len(pitch_diameter_list)-1])/2
    return center_distance

##Student ID: 400470828
'''
ADD INDIVIDUAL OBJECTIVES IN THE SPACE BELOW (e.g., objective1(), objective2(), etc.)
'''
## CODE GOES HERE

def verify_center_distance(first_lvl, forefinger, thumb):
    x = []
    first_lvl_CD = 42
    forefinger_CD = 42
    thumb_CD = 36

    calc_first_lvl = calc_CD(first_lvl)
    calc_forefinger = calc_CD(forefinger)
    calc_thumb = calc_CD(thumb)

    if calc_first_lvl == first_lvl_CD:
        x.append(True)
    else:
        x.append(False)

    if calc_forefinger == forefinger_CD:
        x.append(True)
    else:
        x.append(False)

    if calc_thumb == thumb_CD:
        x.append(True)
    else:
        x.append(False)

    return x

'''
Do not include any function calls OUTSIDE of your written function - as they will be called in main()
- You SHOULD call the above given functions inside your own function WHERE APPROPRIATE
'''

