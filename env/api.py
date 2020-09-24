class Rectangle():

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        # create a rectangle and return it
        pass

    def change_fill_char(self, new_fill_char):
        # update fill char
        pass
    
    def translate(self, axis, num):
        pass

class API():

    def __init__(self):
        pass

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
 