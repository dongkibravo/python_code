class Coord(object):
    def __init__(self,x,y):
        self.x, self.y = x,y
    def __str__(self):
        return '({},{})'.format(self.x, self.y)


x = input("X coord: ")
y = input("Y coord: ")

new_coord = Coord(x,y)

print(new_coord)
