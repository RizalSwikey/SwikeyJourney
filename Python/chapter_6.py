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
# 1. The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”.
# Write a function turn_clockwise that takes one of these four compass points as its parameter,
# and returns the next compass point in the clockwise direction. Here are some tests that should
# pass:
# 1 test(turn_clockwise("N") == "E")
# 2 test(turn_clockwise("W") == "N")
# You might ask “What if the argument to the function is some other value?” For all other cases,
# the function should return the value None:
# 1 test(turn_clockwise(42) == None)
# 2 test(turn_clockwise("rubbish") == None)
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
# 2. Write a function day_name that converts an integer number 0 to 6 into the name of a day.
# Assume day 0 is “Sunday”. Once again, return None if the arguments to the function are not
# valid. Here are some tests that should pass:

def day_name(x):
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    if x <= 6:
        return days[x]
    else:
        return

# 3. Write the inverse function day_num which is given a day name, and returns its number:

def day_num(day):
    days = {'SUNDAY':0, 'MONDAY':1, 'TUESDAY': 2, 'WEDNESDAY': 3, 'THURSDAY': 4, 'FRIDAY': 5, 'SATURDAY': 6}
    if day in days : 
        return days [day]
    else :
        return

# 4. Write a function that helps answer questions like ‘“Today is Wednesday. I leave on holiday
# in 19 days time. What day will that be?”’ So the function must take a day name and a delta
# argument — the number of days to add — and should return the resulting day name:

# 5. Can your day_add function already work with negative deltas? For example, -1 would be
# yesterday, or -7 would be a week ago:

def day_add(day, delta):
    days = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']
    if delta > 7 or delta < 7 :
        return days [(day_num(day) + delta % 7 )% 7]

# 6. Write a function days_in_month which takes the name of a month, and returns the number of
# days in the month. Ignore leap years:
# 1 test(days_in_month("February") == 28)
# 2 test(days_in_month("December") == 31)
# If the function is given invalid arguments, it should return None.

def day_in_month(month):
    month = {'January': 31, 'February':28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    if month in month:
        return month[month]
    else:
        return

# 7. Write a function to_secs that converts hours, minutes and seconds to a total number of seconds.
# Here are some tests that should pass:

def to_secs (hours,minutes,seconds):
    return int ((hours ** 3600) + (minutes*60) +seconds)

# 8. Extend to_secs so that it can cope with real values as inputs. It should always return an integer
# number of seconds (truncated towards zero):

def hours_in(secs):
    return secs // 3600
def minutes_in(secs):
    return secs // 60 % 60
def seconds_in(secs):
    return secs - (to_secs(hours_in(secs), 0, 0) + to_secs (0, minutes_in(secs) , 0))
