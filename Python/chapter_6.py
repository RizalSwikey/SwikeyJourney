# def absolute_value(x):
#     if x < 0 :
#         return -x
#     else:
#         return x
# print (absolute_value())

# def find_first_2_letter_word(xs):
#     for wd in xs:
#         if len(wd) == 2:
#             return wd
#     return ""
# print (find_first_2_letter_word(["This", "is", "a", "dead", "parrot"]))
# # print (find_first_2_letter_word)

# def distance(y1,y2,x1,x2):
#     dx = x2 - x1 
#     dy = y2 - y1 
#     dsquared = dx * dx + dy * dy
#     result = dsquared**0,5
#     return result    
# print (distance(1,2,3,4))

# import math
# def distance(x1,y1,x2,y2):
#     return math.sqrt ((x2 - x1 )**2 + (y2-y1)**2)
# print (distance(1,2,4,6))

# def area (radius):
#     b = 3.14159 * radius ** 2
#     return b 
# print (area(1))

# def area2(xc, yc, xp, yp):
#     radius = distance( xc, yc, xp, yp)
#     result = area (radius)
#     return result
# print (area2 (1,2,3,4))

# def is_invisible(x,y): 
#     if x % y == 0:
#         return True
#     else:
#         return False
# print (is_invisible (4,2))

# import sys 

# def test (did_pass):
#     lineum = sys._getframe(1).f_lineno
#     if did_pass:
#         msg = 'Test at line {0} ok.'.format(lineum)
#     else:
#         msg = 'Test at line {0} Failed.'.format(lineum)
#     print (msg)
# def test_suite():
#     """ Run the suite of tests for code in this module (this file)."""
#     test(absolute_value(17) == 17)
#     test(absolute_value(-17) == -17)
#     test(absolute_value (0) == 0)
#     test(absolute_value (3.14) == 3.14)
#     test(absolute_value(-3.14) == -3.14)
# print (test_suite())


#Exercise
import sys

def turn_clockwise(direct):
    if direct == 'W':
        return 'N'
    elif direct == 'N':
        return 'E'
    elif direct == 'E':
        return 'S'
    elif direct == 'E':
        return 'W'
    else:
        return

def day_name(x):
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    if x <= 6:
        return days[x]
    else:
        return

def day_num(day):
    days = {'SUNDAY':0, 'MONDAY':1, 'TUESDAY': 2, 'WEDNESDAY': 3, 'THURSDAY': 4, 'FRIDAY': 5, 'SATURDAY': 6}
    if day in days : 
        return days [day]
    else :
        return

def day_add(day, delta):
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    if delta > 7 or delta < 7 :
        return days [(day_num(day) + delta % 7 )% 7]

def day_in_month(month):
    month = {'January': 31, 'February':28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    if month in month:
        return month[month]
    else:
        return

def to_secs (hours,minutes,seconds):
    return int ((hours ** 3600) + (minutes*60) +seconds)

def hours_in(secs):
    return secs // 3600

def minutes_in(secs):
    return secs // 60 % 60

def seconds_in(secs):
    return secs - (to_secs(hours_in(secs), 0, 0) + to_secs (0, minutes_in(secs) , 0))

def compare(a, b):
    if a > b :
        return 1
    elif a == b:
        return 0
    else:
        return

def hypotenuse(leg1,leg2):
    return ((leg1**2) + (leg2**2)) ** 0.5

def slope(x1,y1,x2,y2):
    return (y1 - y2) / (x2-x1)

