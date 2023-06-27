from turtle import Turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.addTurtle(pos)

    def move(self):
        for t_num in range(len(self.turtles)-1, 0, -1):
            self.turtles[t_num].goto( self.turtles[t_num-1].xcor(), self.turtles[t_num-1].ycor() )
        self.turtles[0].forward(MOVE_DISTANCE)
    
    def addTurtle(self, pos):
        newTurtle = Turtle("square")
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.goto(pos)
        self.turtles.append(newTurtle)

    def extend(self):
        self.addTurtle(self.turtles[-1].position())
    
    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)