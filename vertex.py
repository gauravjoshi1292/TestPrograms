# from cs1lib import *


class Vertex:
    """
    Vertex class that contains all the information for a vertex
    """
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent_vertices = []

    def __str__(self):
        """
        :return: string representation for the vertex
        """
        retVal = self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: "

        for v in self.adjacent_vertices:
            retVal += str(v.name) + ", "
        retVal = retVal.rstrip(", ")
        return retVal

    def draw_vertex(self, r, g, b):
        """
        Draw a circle corresponding to the verex
        :param r: red
        :param g: green
        :param b: blue
        :return: none
        """
        # set_fill_color(r, g, b)
        # draw_circle(self.x, self.y, 5)
        # disable_fill()
        pass

    def draw_edge(self, destination, r, g, b):
        """
        Draw an edge between two vertices
        :param destination: destination vertex
        :param r: red
        :param g: green
        :param b: blue
        :return: none
        """
        # set_stroke_color(r, g, b)
        # set_stroke_width(2)
        # draw_line(self.x, self.y, destination.x, destination.y)
        pass