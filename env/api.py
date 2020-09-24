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

class Canvas():

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.shapes = []

    def __repr__(self):
        return f'<Length="{self.length}" Width="{self.width}">'

    def _print_grid(self, grid):
        for row in range(self.length):
            row_str = ""
            for col in range(self.width):
                row_str += grid[row][col]
            print(row_str)

    def _add_shape_to_grid(self, grid, shape):
        for i in range(shape.start_x, shape.end_x + 1):
            for j in range(shape.start_x, shape.end_x + 1):
                grid[i][j] = shape.fill_char
        return grid

    def render_canvas(self):
        # Print the canvas 
        # any shapes to standard output
        grid = []
        for row in range(self.length):
            grid.append([" "] * self.width)

        for shape in self.shapes:
            grid = self._add_shape_to_grid(grid, shape)

        self._print_grid(grid)

    

        
    def add_shape(self, shape):
        # shape is a Rectangle
        self.shapes.append(shape)

    def clear_all_shapes(self):
        self.shapes = []
 
api = Canvas(5, 5)
r = Rectangle(0, 2, 2, 0, "x")
api.add_shape(r)
api.render_canvas()
 