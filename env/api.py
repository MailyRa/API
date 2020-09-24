class Rectangle():

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        # create a rectangle and return it
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char


    def __repr__(self):

        return f'<start_x="{self.start_x}" start_y="{self.start_y} end_x="{self.end_x} end_y="{self.end_y}" fill_char="{self.fill_char}">'



    def change_fill_char(self, new_fill_char):
        # update fill char
        self.fill_char = new_fill_char
    
    def translate(self, axis, num):
        #move left, right, up, or down
        # x = moves left/right
        # y = move up/down

        if axis == 'x':
            self.start_x += num
            self.end_x += num

        elif axis == 'y':
            self.start_y += num
            self.end_y += num
        else:
            ('Invalid, try again')

class API():

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def __repr__(self):

        return f'<Length="{self.length}" Width="{self.width}">'

    def render_canvas(self):
        # Print the canvas and any shapes to standard output
        pass

    def add_shape(self, shape):
        # shape is a Rectangle
        pass

    def clear_all_shapes(self):
        pass 
 
api = API()
r = Rectangle(0, 0, 0, 0, "x")
api.add_shape(r)
api.render_canvas()
 