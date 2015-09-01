from cs1lib import *
from load_graph import load_graph


# The lower left corner of the window has a pixel value (0, 0) and the upper right corner has a pixel value (740, 380)
# The lower left corner of the map has a pixel value (10, 10) and the upper right corner has a pixel value (730, 370)
# I have added a padding of 10px either side for the map inside the window


WINDOW_WIDTH = 1012  # Width of the graphics window in pixels
WINDOW_HEIGHT = 811  # Height of the graphics window in pixels
MAP_WIDTH = 1012.0  # Map width in pixels
MAP_HEIGHT = 811.0  # Map height in pixels


def draw_red_vertex():
    disable_stroke()
    x = mouse_x()
    y = mouse_y()
    enable_fill()
    set_fill_color(1, 0, 0)
    draw_circle(x, y, 7)
    enable_stroke()


def draw_map():
    """
    Draws the map on the graphics window and plots the campus paths connecting various locations
    :return: None
    """
    img = load_image("dartmouth_map.png")  # Load the image
    vertex_dict = load_graph("dartmouth_graph.txt")

    enable_smoothing()
    draw_image(img, WINDOW_WIDTH/2, WINDOW_HEIGHT/2, MAP_WIDTH/2, MAP_HEIGHT/2)

    for v in vertex_dict.values():
        enable_fill()
        v.draw_vertex(0, 0, 1)
        for u in v.adjacent_vertices:
            v.draw_edge(u, 0, 0, 1)

    set_mouse_button_function(draw_red_vertex)
    while not window_closed():
        dest_x = mouse_x()
        dest_y = mouse_y()

        request_redraw()


def draw_window():
    """
    Draws the graphics window and calls the draw_map function that draws the dartmouth map
    :return: None
    """
    start_graphics(draw_map, "World Map Showing Most Populated Cities", WINDOW_WIDTH, WINDOW_HEIGHT)


draw_window()