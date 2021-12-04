import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
     # tree_top = scene_top + 100
    island_width = 650
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_sun(canvas, scene_left+650, scene_top+40, 100)
    draw_cloud(canvas, scene_left+60, scene_top+60, 200, 30)
    draw_cloud(canvas, scene_left+120, scene_top+80, 200, 30)
    draw_cloud(canvas, scene_left+380, scene_top+30, 200, 30)
    draw_bird(canvas, scene_left+130, scene_top+150)
    draw_bird(canvas, scene_left+400, scene_top+200)
    draw_bird(canvas, scene_left+350, scene_top+100)
    draw_bird(canvas, scene_left+520, scene_top+120)
    draw_bird(canvas, scene_left+600, scene_top+80)
    draw_bird(canvas, scene_left+40, scene_top+50)
    draw_bird(canvas, scene_left+750, scene_top+130)
    draw_bird(canvas, scene_left+20, scene_top+200)
    draw_island(canvas, scene_left-100, scene_top+320, island_width, scene_bottom, "#50b24f")
    draw_island(canvas, scene_left+350, scene_top+320, island_width, scene_bottom, "#abda18")
    draw_house(canvas, scene_left+575, scene_top+275, 150, 75)
    draw_sea(canvas, scene_left, scene_top+415, scene_right, scene_bottom)
    draw_waves(canvas, scene_left, scene_right, 150, scene_top+400, 30)
    draw_waves(canvas, scene_left-45, scene_right, 150, scene_top+425, 30)
    draw_boat(canvas, scene_left+80, scene_top+365, 300, 100)
    draw_waves(canvas, scene_left, scene_right, 150, scene_top+450, 30)
    draw_waves(canvas, scene_left-45, scene_right, 150, scene_top+475, 30)


def draw_bird(canvas, coord_x0, coord_y0):
    """Draw bird.
    Parameters
        canvas: The tkinter canvas where this function will draw the bird.
        scene_left, scene_right: The initial and final x location.
        coord_y0: The initial y location.
    Return: nothing
    """

    wing_width = 10
    height = 10

    canvas.create_arc( coord_x0, coord_y0, coord_x0 + wing_width, coord_y0 + height, extent="120", width=2, fill="black", outline="black", style=tk.ARC)
    canvas.create_arc( coord_x0 + wing_width, coord_y0, coord_x0 + 2 * wing_width, coord_y0 + height, start="60", extent="120", width=2, fill="black", outline="black", style=tk.ARC)
     

def draw_boat(canvas, coord_x0, coord_y0, boat_width, boat_height):
    """Draw a boat.
    Parameters
        canvas: The tkinter canvas where this function will draw a boat.
        coord_x0, coord_y0: The initial x and y location.
        boat_width: The boat width in pixels.
        boat_height: The boat height in pixels.
    Return: nothing
    """
    # Draw a boat
    coord_x1 = coord_x0 + boat_width
    coord_y1 = coord_y0 + boat_height
    edges_distance = 50
    coord_base_distance = boat_width - edges_distance
    # draw base
    canvas.create_polygon(coord_x0, coord_y0, coord_x0 + edges_distance, coord_y1, coord_x0 + coord_base_distance, coord_y1, coord_x1, coord_y0, fill="#714738", outline="black") 
    # draw mast 
    canvas.create_rectangle(coord_x0 + boat_width/2, coord_y0 - 1.8 * boat_height, coord_x0 + boat_width/2 + 6, coord_y0, fill="#714738" )
    # draw mainsail
    canvas.create_polygon(coord_x0 + 30, coord_y0 - 4, coord_x0 + boat_width/2 - 2, coord_y0 - 4, coord_x0 + boat_width/2 - 2, coord_y0 - 1.77 * boat_height , fill="#dfdcdc", outline="black" ) 
    # draw jib
    canvas.create_polygon(coord_x1 - 50, coord_y0 - 4, coord_x0 + boat_width/2 + 9, coord_y0 - 4, coord_x0 + boat_width/2 + 9, coord_y0 - 1.5 * boat_height , fill="#dfdcdc", outline="black" ) 
    # draw flag
    canvas.create_polygon(coord_x0 + boat_width/2 + 9, coord_y0 - 1.77 * boat_height, coord_x0 + boat_width/2 + 56, coord_y0 - 1.77 * boat_height, coord_x0 + boat_width/2 + 9, coord_y0 - 1.6 * boat_height , fill="red", outline="black") 


def draw_cloud(canvas, coord_x0, coord_y0, cloud_width, cloud_height):
    """Draw a cloud.
    Parameters
        canvas: The tkinter canvas where this function will draw a cloud.
        coord_x0, coord_y0: The x and y location in pixels where this 
                function will draw the 'rectangle' in which the 
                oval will be in.
        cloud_width: The cloud width in pixels.
        cloud_height: The cloud height in pixels.
    Return: nothing
    """
    # Draw a cloud
    coord_x1 = coord_x0 + cloud_width
    coord_y1 = coord_y0 + cloud_height

    canvas.create_oval(coord_x0, coord_y0, coord_x1 , coord_y1,
             width=0, fill="white") 

def draw_house(canvas, coord_x0, coord_y0, house_width, house_height):
    """Draw a house.
    Parameters
        canvas: The tkinter canvas where this function will draw a house.
        coord_x0, coord_y0: The initial x and y location for the base/body 
                of the house.
        house_width: The house width in pixels.
        house_height: The house height in pixels.
    Return: nothing
    """
    # Draw a house
    coord_x1 = coord_x0 + house_width
    coord_y1 = coord_y0 + house_height

    # draw base
    canvas.create_rectangle(coord_x0, coord_y0, coord_x1, coord_y1, fill="#d2837a", width = 0)
    # draw door
    canvas.create_rectangle(coord_x0 + house_width/2 - 15, coord_y0 + 20, coord_x0 + house_width/2 + 15, coord_y1, fill = "#3a3a41", width = 0 )
    # draw roof
    canvas.create_polygon(coord_x0 - 15, coord_y0, coord_x0 + house_width/2, coord_y0 - house_height/2, coord_x1 + 15, coord_y0, fill="#714738")    

def draw_island(canvas, coord_x0, coord_y0, island_width, scene_bottom, color):
    """Draw an island(ground)
    Parameters
        canvas: The tkinter canvas where this function will draw an island.
        coord_x0, coord_y0: The x and y location in pixels where this function
                will draw the 'rectangle' in which the arch will be in.
        island_width: The island width in pixels.
        scene_bottom: bottom of the canvas
        color: The color of the island
    Return: nothing
    """
    # Draw an island
    coord_x1 = coord_x0 + island_width
    coord_y1 = coord_y0+ 2 * (scene_bottom - coord_y0)
    canvas.create_arc(coord_x0, coord_y0, coord_x1 , coord_y1, extent="180", fill=color, width=0, outline=color)

def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw the sky.
    Parameters
        canvas: The tkinter canvas where this function will draw the sky.
        scene_left, scene_top, scene_right, scene_bottom: The x and y location 
                will be the same as the canvas dimensions.
    Return: nothing
    """
    # Draw the sky
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom,
             width=0, fill="#cbecf3")

def draw_sea(canvas, scene_left, coord_y0, scene_right, scene_bottom):
    """Draw the sea.
    Parameters
        canvas: The tkinter canvas where this function will draw the sea.
        scene_left, scene_right: The x location will be the same as the 
                canvas dimensions.
        coord_y0, scene_bottom: the initial and final y location.
    Return: nothing
    """
    # Draw the sea
    canvas.create_rectangle(scene_left, coord_y0, scene_right, scene_bottom,
             width=2, fill='#30a3e7', outline='#fac32b')

def draw_sun(canvas, coord_x0, coord_y0, sun_radius):
    """Draw a sun.
    Parameters
        canvas: The tkinter canvas where this function will draw a sun.
        coord_x0, coord_y0: The x and y location in pixels where this 
                function will draw the 'rectangle' in which the 
                oval will be in.
        sun_radius: The sun radius in pixels.
    Return: nothing
    """
    # Draw a sun
    coord_x1 = coord_x0 + sun_radius
    coord_y1 = coord_y0 + sun_radius

    canvas.create_oval(coord_x0, coord_y0, coord_x1 , coord_y1,
             width=0, fill="#ffe430") 

def draw_waves(canvas, scene_left, scene_right, width, coord_y0, height):
    """Draw waves.
    Parameters
        canvas: The tkinter canvas where this function will draw the waves.
        scene_left, scene_right, width: The initial and final x location, 
                and the width of the arcs will be the same as the canvas 
                dimensions.
        coord_y0, height: The y location and the relative height of the arc.
    Return: nothing
    """

    for i in range(scene_left, scene_right, width):
        canvas.create_arc( i, coord_y0, i + width, coord_y0 + height, extent="180", width=5, fill="#30a3e7", outline="#44f4fb")
     
    canvas.create_line(scene_left, coord_y0 + height/2, scene_right, coord_y0 + height/2, width=5, fill="#30a3e7")


# Call the main function so that
# this program will start executing.
main()