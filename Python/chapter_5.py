# import turtle
# def draw_bar(t, height):
#     """ Get turtle t to draw one bar, of height. """
#     t.begin_fill() # Added this line
#     t.left(90)
#     t.forward(height)
#     t.write(" "+ str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill() # Added this line
#     t.forward(10)
# wn = turtle.Screen() # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle() # Create tess and set some attributes
# tess.color("blue", "red")
# tess.pensize(3)
# xs = [48,117,200,240,160,260,220]
# for a in xs:
#     draw_bar(tess, a)
# wn.mainloop()

#1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a
# function which is given the day number, and it returns the day name (a string)
# day = ["Sunday","Monday","Tusday","Wednesday","Thrusday","Friday","Saturday"]
#
# def day_by_day(n):
#     return day[n]
# print(day_by_day(int(input())))

#2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on
# day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the
# program which asks for the starting day number, and the length of your stay, and it will tell
# you the name of day of the week you will return on.
# def wonderfulday(n):
#     day = ["Sunday", "Monday", "Tusday", "Wednesday", "Thrusday", "Friday", "Saturday"]
#     print(day[n])
# daystart = int(input('Number Of Day: '))
# stay = int(input('lenght of away: '))
# wonderfulday((daystart+(stay % 7)) % 7)

#3.Give the logical opposites of these conditions
# 1 a > b                         a <= b # not (a > b)
# 2 a >= b                        a < b  # not (a >= b )
# 3 a >= 18 and day == 3          a < 18 or day != 3 # not (a < 18 or day != 3)
# 4 a >= 18 and day != 3          a < 18 or day == 3 # not (a >= 18 and day != 3)

#4. What do these expressions evaluate to?
# 1 3 == 3      True
# 2 3 != 3      False
# 3 3 >= 4      False
# 4 not (3 < 4) False

#5. Complete this truth table?
# p q r (not (p and q)) or r
# F F F T
# F F T T
# F T F T
# F T T T
# T F F T
# T F T T
# T T F F
# T T T T

#6. Write a function which is given an exam mark, and it returns a string — the grade for that
# mark — according to this scheme:
# Mark      Grade
# >= 75     First
# [70-75)   Upper Second
# [60-70)   Second
# [50-60)   Third
# [45-50)   F1 Supp
# [40-45)   F2
# # < 40 F3
# The square and round brackets denote closed and open intervals. A closed interval includes the
# number, and open interval excludes it. So 39.99999 gets grade F3, but 40 gets grade F2. Assume
# 1 xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
# 2 49.9, 45, 44.9, 40, 39.9, 2, 0]
# Test your function by printing the mark and the grade for all the elements in this list.
# def determinted_grade(mark):
#     if mark >=75:
#         return 'First'
#     elif mark >=70 < 75 :
#         return 'Upper Second'
#     elif mark >=60 < 70 :
#         return 'Second'
#     elif mark >=50 < 60 :
#         return 'Third'
#     elif mark >=45 < 50 :
#         return 'F1 Supp'
#     elif mark >=40 < 45 :
#         return 'F2'
#     else :
#         return 'F3'
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
# for i in xs :
#     mark =determinted_grade(i)
#     print('Student with exam mark',i,'will get',mark,'grade')

# 7. Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.
# import turtle
# swikey = turtle.Turtle()
# swikey.begin_fill()
# swikey.color('black','pink')
# turtle.Screen()
# turtle.bgcolor('lightgreen')
# def draw_bar (t,height):
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.write(" "+str(height))
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.penup()
#     t.forward(10)
#     t.pendown()
# xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
# for i in xs:
#     draw_bar(swikey,i)
# swikey.end_fill()
# turtle.mainloop()

#8. Modify the turtle bar chart program so that the bar for any value of 200 or more is filled with
# red, values between [100 and 200) are filled with yellow, and bars representing values less than
# 100 are filled with green
# import turtle
# def draw_bar(t,height):
#     t.begin_fill()
#     if height >= 200:
#         t.color('black','red')
#     elif height >= 100 and height < 200:
#         t.color('black','yellow')
#     else:
#         t.color('black','green')
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#
#     if height >=0:
#         t.write(" "+str(height) )
#     else:
#         t.speed(1)
#         t.penup()
#         t.right(90)
#         t.forward(15)
#         t.write(' '+str(height) )
#         t.left(180)
#         t.forward(15)
#         t.right(90)
#         t.pendown()
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.end_fill()
#
#
# swikey = turtle.Turtle()
# turtle.Screen()
# xs = [48, -30, 117, 200, 240, 160, 260, 220]
# for i in xs :
#     draw_bar(swikey,i)
# turtle.mainloop()

#10. Write a function find_hypot which, given the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse. (Hint: x ** 0.5 will return the square root.
# def find_hypot(x,y):
#     return (x**2 + y**2 )**0,5
# print(find_hypot(2,7))

# 11. Write a function is_rightangled which, given the length of three sides of a triangle, will
# determine whether the triangle is right-angled. Assume that the third argument to the function
# is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
# Hint: Floating point arithmetic is not always exactly accurate, so it is not safe to test floating
# point numbers for equality. If a good programmer wants to know whether x is equal or close
# enough to y, they would probably code it up as:
# 1 if abs(x-y) < 0.000001: # If x is approximately equal to y
# 2 ...

# def is_rightangled(a, b, c):
#     if a**2 + b**2 == c**2:
#         return True
#     else:
#         return False

# print(is_rightangled(3, 4, 12))

#12. Extend the above program so that the sides can be given to the function in any order.
