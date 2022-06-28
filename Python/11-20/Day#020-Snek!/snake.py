from turtle import Turtle
MOVE_SPEED = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """ Snake class handles segments & movement """
    def __init__(self):
        self.spawn_positions = STARTING_POSITION
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def new_snake(self):
        for position in self.spawn_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('lime')
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # def snake_skin(self):
    #     alt = True
    #     for segment in self.segments:
    #         if alt:
    #             segment.color('yellow')
    #             alt = False
    #         else:
    #             segment.color('blue')
    #             alt = True

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def phoenix(self):
        for seg_num in range(len(self.segments)):
            self.segments[seg_num].reset()
        self.segments.clear()
        self.new_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_SPEED)

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
