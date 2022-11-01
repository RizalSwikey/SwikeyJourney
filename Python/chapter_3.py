# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# wn.title("Swikey The Loop Master")
# swikey = turtle.Turtle()
# swikey.color ("black")
#
# swikey.pensize(5)
# for i in range (100):
#     swikey.forward(50)
#     swikey.left(5)
#     wn.mainloop()
#3.4
# for f in ["joe","Zoe","Brad","angelica","thandi","paris"]:
#     invite = "hi " + f + " Come Play with me!"
#     print(invite)

#3.5 the loop
# for i in [0,1,2,3]:
#     swikey.forward(50)
#     swikey.left(90)

# for i in range(4):
#     swikey.forward(50)
#     swikey.left(90)

# for c in ["yellow", "red", "purple", "blue"]:
#     swikey.pensize(5)
#     swikey.color(c)
#     swikey.forward(60)
#     swikey.left(90)

# clrs = ["yellow", "red", "purple", "blue"]
# for c in clrs:
#     swikey.color(c)
#     swikey.forward(50)
#     swikey.left(90)

# 3.6
# import turtle
# wn =turtle.Screen()
# wn.bgcolor("lightgreen")
# swikey = turtle.Turtle()
#
# swikey.speed(10)
# swikey.pensize(10)
# swikey.penup()
# swikey.forward(100)
# swikey.pendown()
# swikey.shape("turtle")
# wn.mainloop()
#
# swikey.shape("turtle")
# swikey.color("blue")
# swikey.penup()
# size = 20
# for i in range (30):
#     swikey.stamp()
#     size = size + 3
#     swikey.forward(size)
#     swikey.right(24)
#
# wn.mainloop()

#Exercises 3.8
#1. Write a program that prints We like Python's turtles! 1000 times.
#  for i in range (1000):
#     print("we like Phyton's turtles!")

#2. Give three attributes of your cellphone object. Give three methods of your cellphone.
# volume = (100)
# def volumeup():
#     print("gambar volume")
# volumeup()

#3. Write a program that uses a for loop to print
# month = ["January", "February", "March", "April", "May", "June", "August", "Sept", "October", "November", "Desember"]
#
# for i in range(12):
#     print("One of the months is the year is", month[i])

#4. Suppose our turtle tess is at heading 0 — facing east. We execute the statement tess.left(3645).
#What does tess do, and what is her final heading?
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("blue")
# swikey = turtle.Turtle()
# swikey.shape("turtle")
# swikey.color("red")
# swikey.left(3645)
# swikey.forward(100)
# wn.mainloop()

#5. Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# a. Write a loop that prints each of the numbers on a new line.
# b. Write a loop that prints each number and its square on a new line.
# c. Write a loop that adds all the numbers from the list into a variable called total. You should
# set the total variable to have the value 0 before you start adding them up, and print the value
# in total after the loop has completed.
# d. Print the product of all the numbers in the list. (product means all multiplied together)

# #a. Answer
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs:
#     print([i])

#b. Answer
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs:
#     print(i,"=", i**2)

#c. Answer
# total = 0
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs:
#     total = total + i
# print(total)

#d. Answer
# total = 1
# xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for i in xs :
#     total = total * i
# print(total)

#6. Use for loops to make a turtle draw these regular polygons (regular means all sides the same
# lengths, all angles the same):
# - An equilateral triangle
# - A square
# - A hexagon (six sides)
# - An octagon (eight sides)

# Triangel
# import turtle
# swikey = turtle.Turtle()
# swikey.shape("turtle")
# swikey.color("red")
# for i in range(3):
#     swikey.pensize(5)
#     swikey.forward(90)
#     swikey.left(120)
# wn.mainloop()
#Square
# for i in range (4):
#     swikey.pensize(5)
#     swikey.forward(90)
#     swikey.left(90)
# turtle.bgcolor("lightgreen")
# turtle.mainloop()
#Hexagon
# for i in range (6):
#     swikey.pensize(5)
#     swikey.forward(90)
#     swikey.left(60)
# turtle.bgcolor("lightgreen")
# turtle.mainloop()
#Octagon
# for i in range (8):
#     swikey.pensize(5)
#     swikey.forward(81)
#     swikey.left(51)
# turtle.bgcolor("lightgreen")
# turtle.mainloop()

#7. drunk pirate makes a random turn and then takes 100 steps forward, makes another random
# turn, takes another 100 steps, turns another random amount, etc. A social science student
# records the angle of each turn before the next 100 steps are taken. Her experimental data is
# [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend
# import turtle
# import random
# num = random.random()
# swikey = turtle.Turtle()
# swikey.color("red")
# swikey.speed(10)
# swikey.shape("turtle")
# turtle.bgcolor("lightgreen")
# list = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# move = 0
# a = []
# b = []
# for i in range(100):
#     if (move == 8):
#         move = 0
#     a.append(random.choice(list))
#     b.append(random.choice(list))
#     swikey.left(a[i])
#     swikey.forward(b[i])
#     move += 1
# print("Samlekom")
# a.reverse()
# b.reverse()
# for i in range(100):
#     if (move == 8):
#         move = 0
#     swikey.back(b[i])
#     swikey.right(a[i])
#     move +=1
# turtle.mainloop()

# #8. Enhance your program above to also tell us what the drunk pirate’s heading is after he has
# finished stumbling around. (Assume he begins at heading 0).

# #9. If you were going to draw a regular polygon with 18 sides, what angle would you need to turn
# the turtle at each corner? answ : 20 step
# import turtle
# swikey = turtle.Turtle()
# swikey.color("red")
# swikey.shape("turtle")
# turtle.bgcolor("lightgreen")
# for i in range(18):
#     swikey.pensize(5)
#     swikey.right(20)
#     swikey.forward(80)
# turtle.mainloop()

# 10.At the interactive prompt, anticipate what each of the following lines will do, and then record
# # what happens. Score yourself, giving yourself one point for each one you anticipate correctly:
# import turtle
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.right(90)
# tess.left(3600)
# tess.right(-90)
# tess.speed(10)
# tess.left(3600)
# tess.speed(0)
# tess.left(3645)
# tess.forward(-100)
# wn.mainloop()

# 11.Draw a Stars
# import turtle
# swikey = turtle.Turtle()
# swikey.hideturtle()
# for i in range(5):
#     swikey.pensize(5)
#     swikey.forward(50)
#     swikey.right(144)
#     swikey.forward(100)
#
# turtle.mainloop()

# 12. Write a program to draw a face of a clock that looks something like this
import turtle
swikey = turtle.Turtle()
list = [100,20,20]
swikey.pensize(5)
swikey.shape("turtle")
swikey.color("blue")
turtle.bgcolor("lightgreen")
for i in range (12):
    swikey.penup()
    swikey.forward(list[0])
    swikey.pendown()
    swikey.forward(list[1])
    swikey.penup()
    swikey.forward(list[2])
    swikey.stamp()
    swikey.back(140)
    swikey.left(30)
for i in range (3600):
    swikey.speed(1)
    swikey.right(1)
turtle.mainloop()
# 13. Create a turtle, and assign it to a variable. When you ask for its type, what do you get?
# <class 'turtle.Turtle'>
# import turtle
# swikey = turtle.Turtle()
# print(type(swikey))
#14. What is the collective noun for turtles? (Hint: they don’t come in herds.)
# Turtoise
#15. What the collective noun for pythons? Is a python a viper? Is a python venomous?
#pythos, no is not a viper, its not venomous