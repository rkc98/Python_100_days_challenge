from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segemnts = []
        self.start_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.move_distance = 20
        self.head = self.segemnts[0]

    def create_snake(self):
        for position in self.start_positions:
            self.add_segment(position)
            
    def add_segment(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segemnts.append(tim)
    def extend(self):
        self.add_segment(self.segemnts[-1].position())

    def move(self):
        for seg_num in range(len(self.segemnts)-1, 0, -1):
            new_x = self.segemnts[seg_num-1].xcor()
            new_y = self.segemnts[seg_num-1].ycor()
            self.segemnts[seg_num].goto(new_x, new_y)
        self.segemnts[0].forward(self.move_distance)
        # self.segemnts[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:

            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
