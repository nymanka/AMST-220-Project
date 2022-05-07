"""for i in range(500): # this "for" loop will repeat these functions 500 times
    turtle.speed(150)
    forward(i)
    left(91)

"""

import turtle
from turtle import Turtle, done, penup
from random import randint
from typing import Tuple

"""Summary: This Program draws a lovely scene with the turtle function."""

"""Description: This program draws a mountain scenery with random sized mountains, 
randomly located trees, clouds, and lilypads and has a little pond and 
a big sun setting behind the mountains. The functions do look a little complicated, 
they are encapsulated similar to classes at this point, but i didnt want to implement 
classes because we havent covered the topic yet."""

__author__ = "730389459"

def draw_sun() -> None:
    """Draws the sun."""
    sun = turtle.Turtle() 
    sun.penup()
    sun.speed(0)
    sun.goto(-155, 120)
    sun.pendown()
    sun.color("orange", "orange")
    sun.begin_fill()
    sun.circle(50, 360)
    sun.end_fill()

    """Draws the rays of the sun"""
    for i in range(18):
        sun.right(90)
        sun.penup()
        sun.forward(10)
        sun.pendown()
        sun.forward(10)
        sun.penup()
        sun.backward(20)
        sun.left(90)
        sun.circle(50, 20)
    
    sun.hideturtle()


def clouddraw(check: int) -> None:
    """Draws clouds in the sky."""
    cloud = Turtle()
    if check == 0:
        cloud.color('white')
    else:
        cloud.color('grey')
    cloud.speed(0)

    def randloc() -> Tuple[int, int]:
        """Gets random location for turtle to go to."""
        if check == 0:
            location = (randint(-400, -190), randint(250, 350))
            return location
        else:
            location = (randint(-110, 110), randint(250, 350))
            return location


    def brushstroke(randloc: Tuple[int, int]) -> None:
        """Sets brush stroke and moves turtle to random loc."""
        cloud.penup()
        cloud.goto(randloc)
        cloud.pendown()
        cloud.pensize(randint(3, 5))

    def singlecloud() -> None:
        """Draws individual cloud."""
        brushstroke(randloc())
        if check == 0:
            cloud.fillcolor("white")
        else: 
            cloud.fillcolor("grey")
        cloud.begin_fill()

        cloud.forward(30)
        cloud.left(90)
        cloud.forward(4)

        for x in range(1, 15):
            cloud.left(10)
            cloud.forward(2)

        cloud.left(220)
        for y in range(1, 18):
            cloud.left(10)
            cloud.forward(2.2)

        cloud.left(200)
        for z in range(1, 18):
            cloud.left(10)
            cloud.forward(3)

        cloud.forward(3.2)
        cloud.left(90)
        cloud.forward(52)
        cloud.end_fill()
        cloud.hideturtle()

    for i in range(3):
        singlecloud()


def draw_mountain() -> None:
    """Draws the mountain ranges."""
    mountain = Turtle()
    mountain.penup()
    mountain.speed(5)
    mountain.goto(-340, 70)
    mountain.pendown()
    mountain.pensize(0)
    mountain.color('#a9a9a9')
    mountain.fillcolor('#a9a9a9')
    
    def single_mountain(x: int) -> None:
        """Draws an individual mountain."""
        mountain.begin_fill()

        for i in range(3):
            mountain.forward(x)
            mountain.right(-120)
        mountain.end_fill()
        mountain.setheading(0)

    def first_range() -> None:
        """Draws the first mountain range."""
        mountain.setheading(120)

        for i in range(3):
            """Draws the first set of mountains."""
            distance = randint(120,130)
            single_mountain(distance)
            mountain.penup()
            mountain.forward(distance - 35)
            mountain.pendown()
            mountain.setheading(120)

    def second_range() -> None:
        """Draws the second mountain range."""
        mountain.color('#d3d3d3')
        mountain.fillcolor('#d3d3d3')
        mountain.penup()
        mountain.goto(-450, 70)
        mountain.pendown()
        mountain.begin_fill()
        mountain.setheading(0)
        
        for i in range(2):
            templen = 91
            tempang = 35
            mountain.left(tempang)
            mountain.forward(templen)
            mountain.right(2 * tempang)
            mountain.forward(templen)
            mountain.setheading(0)

        mountain.goto(-450, 70)
        mountain.end_fill()
        mountain.hideturtle()

    first_range()
    second_range()
    mountain.hideturtle()


def drawsky(x: float, y: float, num: int) -> None:
    """Draws the background sky by changing colors in the array."""
    skycol = ['add8e6', 'b5d8e5', 'bdd8e4', 'c5d8e3', 'cdd8e3', 'd6d8e2', 
    'ded8e1', 'e6d8e1', 'eed8e0', 'f6d8df', 'ffd9df']
    skycol2 = ['1D1D1D', '202020', '232323', '252525', '272727', '292929', 
    '2B2B2B', '2D2D2D', '2F2F2F', '313131', '333333']
    
    if num == 0:
        sky = Turtle()
        sky.goto(x, y)
        sky.color('#e5e5ff')
        sky.pensize(100)
        sky.speed(0)
        
        for i in skycol:
            temp = '#' + i
            sky.color(temp)
            sky.forward(200)
            sky.left(90)
            sky.forward(20)
            sky.left(90)

            sky.color(temp)
            sky.forward(200)
            sky.right(90)
            sky.forward(20)
            sky.right(90)
    else:
        sky = Turtle()
        sky.goto(x, y)
        sky.color('#1A1A1A')
        sky.pensize(100)
        sky.speed(0)
        
        for i in skycol2:
            temp = '#' + i
            sky.color(temp)
            sky.forward(200)
            sky.left(90)
            sky.forward(20)
            sky.left(90)

            sky.color(temp)
            sky.forward(200)
            sky.right(90)
            sky.forward(20)
            sky.right(90)
    
    sky.hideturtle()


def tree(x: int) -> None:
    """Draws trees in certain perimeter."""
    tree = Turtle()

    def stump() -> None:
        """Draws the stump for the tree."""
        tree.pencolor("black")
        tree.fillcolor('brown')
        tree.begin_fill()
        tree.setheading(0)
        tree.forward(20)
        tree.right(90)
        tree.forward(20)
        tree.right(90)
        tree.forward(20)
        tree.right(90)
        tree.forward(20)
        tree.end_fill() 
    
    def leaves(x: int) -> None:
        """Draws out the 2 layers of leaves for tree."""
        tree.color("black")
        if x == 0:
            tree.fillcolor("#006400")
        else:
            tree.fillcolor("#bd9458")
        tree.goto(tree.xcor() - 20, tree.ycor())
        tree.begin_fill()
        tree.setheading(0)
        
        for i in range(3):
            tree.forward(60)
            tree.left(120)
        
        tree.end_fill()
        tree.penup()
        tree.goto(tree.xcor(), tree.ycor() + 30)
        tree.pendown()
        tree.begin_fill()
        tree.setheading(0)
        for i in range(3):
            tree.forward(60)
            tree.left(120)
        tree.end_fill()
    
    """Sets locations from top to bottom and draws the trees. Includes
        while loop even though it is unnecessary and for loop would be better due it 
        being deterministic."""
    k = 20
    w = 0
    while w < 4:
        if x == 0:
            tree.penup()
            tree.goto(randint(-445, -200), k)
            tree.pendown()
            stump()
            leaves(x)
            k -= 15
            w += 1
        else:
            tree.penup()
            tree.goto(randint(-120, 120), k)
            tree.pendown()
            stump()
            leaves(x)
            k -= 15
            w += 1
    tree.hideturtle()


def grass(x: int) -> None:
    """Draws the grass background."""
    grass = Turtle()
    if x == 0:
        grass.color('#008000')
        grass.fillcolor("#008000")
        grass.penup()
        grass.goto(-450, -100)
    else:
        grass.color('#274e13')
        grass.fillcolor("#274e13")
        grass.penup()
        grass.goto(-155, -100)
    
    grass.begin_fill()

    for i in range(2):
        grass.forward(300)
        grass.left(90) 
        grass.forward(175)
        grass.left(90)
    
    grass.end_fill()
    grass.hideturtle()



def draw_skyline():
    nael = turtle.Turtle()
    # base rectangle
    nael.color("grey")

    # first function
    def draw(x,y):
        nael.penup()
        nael.goto(x,y)
        nael.pendown()
    
    # second function
    def move(length1,angle1,length2,angle2):
        nael.forward(length1)
        nael.right(angle1)
        nael.forward(length2)
        nael.left(angle2)
        

    draw(-155,75)
    nael.left(90)
    nael.penup

    #first building(left)
    nael.color("black")
    nael.begin_fill()
    move(40,90,10,90)
    nael.forward(20)
    nael.right(90)
    move(30,90,10,90)
    move(10,90,10,90)
    nael.forward(10)

    # second building
    nael.left(90)
    nael.forward(20)
    nael.right(90)
    move(20,90,20,90)
    nael.forward(10)
    nael.left(90)

    # third building
    nael.forward(30)
    nael.right(90)
    nael.forward(4)
    nael.circle(3)
    move(4,90,4,90)



    # 4th building
    move(5,90,2,90)
    nael.forward(5)
    nael.left(90)
    move(7,90,10,90)
    move(10,90,6,90)
    move(20,90,3,90)
    move(10,90,3,90)
    nael.forward(5)
    nael.right(90)
    move(10,90,5,90)
    move(3,90,10,90)
    move(3,90,20,90)
    move(6,90,20,90)
    move(3,90,5,90)
    move(4,90,8,90)

    #between 4th building and Empire state building

    nael.forward(7)
    nael.left(90)
    move(9,90,10,90)


    #Empire State Building

    move(10,90,10,90)
    move(100,90,5,90)
    move(20,90,5,90)
    move(15,90,2,90)
    move(10,90,10,90)


    # top of ESB

    move(10,90,20,95)
    move(90,190,89,95)
    move(20,90,10,90)
    move(10,90,10,90)
    move(2,90,15,90)
    move(5,90,20,90)
    move(5,90,142,90)

    #between Empire and Chrysler
    nael.forward(4)
    nael.left(90)
    nael.forward(90)
    nael.right(90)
    move(50,90,4,90)
    nael.right(90)
    nael.forward(115)
    nael.right(110)

    nael.end_fill()
    nael.hideturtle()


def draw_shrub(x: int):
    a_turtle = turtle.Turtle()
    
    def teleport(a_turtle: Turtle, x: float, y: float) -> None:
        a_turtle.penup()

        a_turtle.home()

        a_turtle.goto(x, y)

        a_turtle.pendown()
    
    def crecent(a_turtle: Turtle, size: float) -> None:

        """Makes a crecent shape."""

        a_turtle.begin_fill()

        a_turtle.circle(size, 180)

        a_turtle.left(120)

        a_turtle.circle(-size * 2, 60)

        a_turtle.end_fill()

    

    def shrub(a_turtle: Turtle, x: float, y: float, size: float, check: int) -> None:

        """Makes a tiny grass plant."""

        if check == 0:
            a_turtle.color("#86DC3D")
        else:
            a_turtle.color("#bd9458")

        teleport(a_turtle, x, y)

        crecent(a_turtle, size)

        a_turtle.left(60)

        crecent(a_turtle, size)

        a_turtle.right(120)

        crecent(a_turtle, size)

    

    def bunch_o_shrubs(a_turtle: Turtle, check: int) -> None:

        i: int = 0
        k = -50
        while i < 5:
            if check == 0:
                shrub(a_turtle, randint(-445, -175), k, 6, check)
            else:
                shrub(a_turtle, randint(-120, 120), k, 6, check)
            k -= 8
            i += 1
    
    bunch_o_shrubs(a_turtle, x)
    turtle.hideturtle()

def draw_birds():
    x = -380
    y = 230
    for i in range(4):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        x+=50
        y-=10
        for j in range(2):
            turtle.setheading(90)
            for k in range(1, 15):
                turtle.left(10)
                turtle.forward(2)
    turtle.hideturtle
        



def main() -> None:
    """The entrypoint of my scene."""
    turtle.speed(0)
    drawsky(-400, -50, 0)
    drawsky(-105,-50, 1)
    clouddraw(0)
    clouddraw(1)
    draw_sun()
    grass(0)
    grass(1)
    draw_skyline()
    draw_mountain()
    tree(0)
    tree(1)
    draw_shrub(0)
    draw_shrub(1)
    draw_birds()
    done()


if __name__ == "__main__":
    main()
else:
    print(__name__)