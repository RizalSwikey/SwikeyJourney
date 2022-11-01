#4.1 Fungtions
# import turtle
#
# def draw_square(t, sz):
#     """Make turtle t draw a square of sz."""
#     for i in range(4):
#         t.forward(sz)
#         t.left(90)
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# wn.title("Alex meets a function")
# alex = turtle.Turtle()
# draw_square(alex, 50)
# wn.mainloop()

# import turtle
# def draw_multicolor_square(t, sz):
#     """Make turtle t draw a multi-color square of sz."""
#     for i in ["red", "purple", "hotpink", "blue"]:
#         t.color(i)
#         t.forward(sz)
#         t.left(90)
# swikey = turtle.Screen() # Set up the window and its attributes
# swikey.bgcolor("lightgreen")
# sky = turtle.Turtle() # Create tess and set some attributes
# sky.pensize(3)
#
# size = 20 # Size of the smallest square
# for i in range(15):
#     draw_multicolor_square(sky, size)
#     size = size + 10 # Increase the size for next tim
#     sky.forward(10)
#     sky.right(18)
# swikey.mainloop()

#4.2 Funtions can call other fungtions
# def draw_rectangle(t, w, h):
#     """Get turtle t to draw a rectangle of width w and height h."""
#     for i in range(2):
#         t.forward(w)
#         t.left(90)
#         t.forward(h)
#         t.left(90)
#     def draw_square(tx, sz):  # A new version of draw_square
#         draw_rectangle(tx, sz, sz)
# import turtle
# __import__("turtle").__traceable__ = False
# # print (pow(7,4))
# def final_amt(p, r, n, t):
#     """Apply the compound interest formula to p to produce the final amount."""
#     a = p * (1 + r/n) ** (n*t)
#     return a # This is new, and makes the function fruitfu
# # now that we have the function above, let us call it.
# toInvest = float(input("How much do you want to invest?"))
# fnl = final_amt(toInvest, 0.08, 12, 5)
# # print("At the end of the period you'll have", fnl)
# def final_amt_v2(principalAmount, nominalPercentageRate,
#                     numTimesPerYear, years):
#     a = principalAmount * (1 + nominalPercentageRate /
#     numTimesPerYear) ** (numTimesPerYear*years)
#     return a
#
# def final_amt_v3(amt, rate, compounded, years):
#     a = amt * (1 + rate/compounded) ** (compounded*years)
#     return a
# import turtle
# def make_window(colr, ttle):
#     """
#     Set up the window with the given background color and title.
#     Returns the new window.
#     """
#     w = turtle.Screen()
#     w.bgcolor(colr)
#     w.title(ttle)
#     return w
# def make_turtle(colr, sz):
#     """
#     Set up a turtle with the given color and pensize.
#     Returns the new turtle.
#     """
#     t = turtle.Turtle()
#     t.color(colr)
#     t.pensize(sz)
#     return t
# wn = make_window("lightgreen", "Tess and Alex dancing")
# tess = make_turtle("hotpink", 5)
# alex = make_turtle("black", 1)
# dave = make_turtle("yellow", 2)
# wn.mainloop()
#1.Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image
# shown below. Assume each side is 20 units. (Hint: notice that the turtle has already moved away
# from the ending point of the last square when the program ends.)
# import turtle
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey=turtle.Turtle()
# swikey.pensize(5)
# swikey.color("pink")
# turtle.bgcolor("lightgreen")
# def drawa_square():
#     for i in range (4):
#         swikey.forward(40)
#         swikey.left(90)
# def drawfour_square():
#     for i in range(5):
#         drawa_square()
#         swikey.penup()
#         swikey.forward(60)
#         swikey.pendown()
# drawfour_square()
# turtle.mainloop()
#2. Write a program to draw this. Assume the innermost square is 20 units per side, and each
# successive square is 20 units bigger, per side, than the one inside it.
# import turtle
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey=turtle.Turtle()
# swikey.pensize(5)
# swikey.color("blue")
# turtle.bgcolor("lightgreen")
# def drawa_square(moreforward):
#     for i in range (4):
#         swikey.forward(moreforward)
#         swikey.left(90)
# def squares():
#     morefoward = 40
#     for i in range(5):
#         drawa_square(morefoward)
#         swikey.right(90+45)
#         swikey.penup()
#         swikey.forward(20)
#         swikey.pendown()
#         swikey.left(90+45)
#         morefoward += 30
# squares()
# turtle.mainloop()

# 3.Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon.
# When called with draw_poly(tess, 8, 50), it will draw a shape like this:
# import turtle
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey = turtle.Turtle()
# def draw_poly (t,n,sz):
#     for i in range(n):
#         t.forward(sz)
#         t.right(360/n)
# draw_poly(swikey,8,50)
# turtle.mainloop()

# 4. Draw this pretty pattern.
# import turtle
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey = turtle.Turtle()
# swikey.color("blue")
# swikey.pensize(2)
# def draw_squres(geser):
#     swikey.right(geser)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(360)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(360)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(360)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.right(90)
#     swikey.forward(180)
#     swikey.left(90)
# def draw_flower():
#     putar = 0
#     for i in range(5):
#         draw_squres(putar)
#         putar = 72
# draw_flower()
# turtle.mainloop()

# 5. The two spirals in this picture differ only by the turn angle. Draw both.
# A.
# import turtle
# swikey= turtle.Turtle()
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey.color("blue")
# swikey.pensize(2)
# def maze (a,b):
#     for i in range(88):
#         a.right(90)
#         a.forward(b)
#         b+=3
# maze(swikey,5)
# turtle.mainloop()
# B.
# import turtle
# swikey= turtle.Turtle()
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey.color("blue")
# swikey.pensize(2)
# def maze (a,b,c):
#     for i in range(88):
#         a.right(c)
#         a.forward(b)
#         b+=4
#         c+=0.01
# maze(swikey,5,90)
# turtle.mainloop()

# 6. Write a void function draw_equitriangle(t, sz) which calls draw_poly from the previous
# question to have its turtle draw a equilateral triangle.
# import turtle
# turtle.Screen()
# turtle.bgcolor("lightgreen")
# swikey = turtle.Turtle()
# def draw_poly (t,sz):
#     for i in range(3):
#         t.forward(sz)
#         t.right(360/-3)
# draw_poly(swikey,50)
# turtle.mainloop()
# 7. Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and
# including n. So sum_to(10) would be 1+2+3…+10 which would return the value 55.
# def sum_to(n):
#     perhitungan = []
#     for i in range(1,n+1):
#         perhitungan.append(i)
#     return sum(perhitungan)
# print(sum_to(10))
# 8. Write a function area_of_circle(r) which returns the area of a circle of radius r.
# def area_of_circle(r):
#     luas = 3.14*r**2
#     return luas
# print(area_of_circle(7))
# 9. Write a void function to draw a star, where the length of each side is 100 units. (Hint: You
# should turn the turtle by 144 degrees at each point.)
# import turtle
# swikey = turtle.Turtle()
# swikey.color("blue")
# turtle.bgcolor("lightgreen")
# turtle.Screen()
# swikey.pensize(4)
# def stars (a,b,c):
#     for i in range(5):
#         a.forward(b)
#         a.right(c)
# stars(swikey,100,144)
# turtle.mainloop()

# 10. Extend your program above. Draw five stars, but between each, pick up the pen, move forward
# by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll get something like
# this
# import turtle
# swikey = turtle.Turtle()
# swikey.color("blue")
# turtle.bgcolor("lightgreen")
# turtle.Screen()
# swikey.pensize(4)
# def stars (a,b,c):
#     for i in range(5):
#         a.forward(b)
#         a.right(c)
# def positions ():
#     for i in range(5):
#         swikey.penup()
#         swikey.forward(300)
#         swikey.right(144)
#         swikey.pendown()
#         stars(swikey,100,144)
# positions()
# turtle.mainloop()