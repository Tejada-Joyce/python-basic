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
    isle_width = 650
    # draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    draw_cloud(canvas, scene_left+60, scene_top+60, 200, 30)
    draw_cloud(canvas, scene_left+120, scene_top+80, 200, 30)
    draw_cloud(canvas, scene_left+380, scene_top+30, 200, 30)
    draw_isle(canvas, scene_left-100, scene_top+320, isle_width, scene_bottom, "#50b24f")
    draw_isle(canvas, scene_left+350, scene_top+320, isle_width, scene_bottom, "#abda18")
    draw_sea(canvas, scene_left, scene_top + 415, scene_right, scene_bottom)
    # draw_waves(canvas, scene_left, scene_right, 300, 400, 30)
    # draw_waves(canvas, scene_left-45, scene_right, 300, 425, 30)
    # draw_waves(canvas, scene_left, scene_right, 300, 450, 30)
    # draw_waves(canvas, scene_left-45, scene_right, 300, 475, 30)
    draw_waves(canvas, scene_left, scene_right, 150, 400, 30)
    draw_waves(canvas, scene_left-45, scene_right, 150, 425, 30)
    draw_waves(canvas, scene_left, scene_right, 150, 450, 30)
    draw_waves(canvas, scene_left-45, scene_right, 150, 475, 30)



    # draw_cloud(canvas, scene_left+250, scene_top+60, 125, 50)

    # draw_cloud(canvas, scene_left+150, scene_top+50, 150, 50)

    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 65)

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


# def draw_pine_tree(canvas, peak_x, peak_y, height):
#     """Draw a single pine tree.
    # Parameters
    #     canvas: The tkinter canvas where this
    #         function will draw a pine tree.
    #     peak_x, peak_y: The x and y location in pixels where
    #         this function will draw the top peak of a pine tree.
    #     height: The height in pixels of the pine tree that
    #         this function will draw.
#     Return: nothing
#     """
#     trunk_width = height / 10
#     trunk_height = height / 8
#     trunk_left = peak_x - trunk_width / 2
#     trunk_right = peak_x + trunk_width / 2
#     trunk_bottom = peak_y + height

#     skirt_width = height / 2
#     skirt_height = height - trunk_height
#     skirt_left = peak_x - skirt_width / 2
#     skirt_right = peak_x + skirt_width / 2
#     skirt_bottom = peak_y + skirt_height

#     # Draw the trunk of the pine tree.
#     canvas.create_rectangle(trunk_left, skirt_bottom,
#             trunk_right, trunk_bottom,
#             outline="gray20", width=1, fill="tan3")

#     # Draw the crown (also called skirt) of the pine tree.
#     canvas.create_polygon(peak_x, peak_y,
#             skirt_right, skirt_bottom,
#             skirt_left, skirt_bottom,
#     
#         outline="gray20", width=1, fill="dark green")

def draw_cloud(canvas, coord_x0, coord_y0, cloud_width, cloud_height):
    """Draw a cloud.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        coord_x0, coord_y0: The x and y location in pixels where
            this function will draw the 'rectangle' in which the 
            oval will be in.
        cloud_width: The cloud width in pixels.
        cloud_height: The cloud width in pixels.
    Return: nothing
    """
    # Draw a cloud
    coord_x1 = coord_x0 + cloud_width
    coord_y1 = coord_y0 + cloud_height

    canvas.create_oval(coord_x0, coord_y0, coord_x1 , coord_y1,
             width=0, fill="white", outline="white") 

def draw_isle(canvas, coord_x0, coord_y0, isle_width, scene_bottom, color):
    """Draw an isle(ground)
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        coord_x0, coord_y0: The x and y location in pixels where
            this function will draw the 'rectangle' in which the 
            arch will be in.
        isle_width: The isle width in pixels.
        scene_bottom: bottom of the canvas
        color: The color of the isle
    Return: nothing
    """
    # Draw an isle
    coord_x1 = coord_x0 + isle_width
    coord_y1 = coord_y0+ 2 * (scene_bottom - coord_y0)
    canvas.create_arc(coord_x0, coord_y0, coord_x1 , coord_y1, extent="180", fill=color, width=0, outline=color)

def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw the sky.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the sky.
        scene_left, scene_top, scene_right, scene_bottom: The x and y location 
            will be the same as the canvas dimensions
    Return: nothing
    """
    # Draw the sky
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom,
             width=0, fill="#cbecf3", outline="#cbecf3")

def draw_sea(canvas, scene_left, y0, scene_right, scene_bottom):
    """Draw the sky.
    Parameters
        canvas: The tkinter canvas where this
            function will draw the sky.
        scene_left, scene_top, scene_right, scene_bottom: The x and y location 
            will be the same as the canvas dimensions
    Return: nothing
    """
    # Draw the sky
    canvas.create_rectangle(scene_left, y0, scene_right, scene_bottom,
             width=0, fill='#30a3e7', outline='#30a3e7')

# def draw_waves(canvas, scene_left, scene_top, scene_right, scene_bottom, grid_spacing):
def draw_waves(canvas, scene_left, scene_right, grid_spacing, coord_y0, height):

    # canvas.create_arc(coord_x0, coord_y0, coord_x1 , coord_y1, extent="180", fill=color, width=0, outline=color)
    # canvas.create_arc(0, 400, 80 , 430, extent="180", fill='blue', width=1, outline='blue')
    # canvas.create_arc(80, 400, 160 , 430, extent="-180", style=tk.ARC,width=1, outline='blue')
    for i in range(scene_left, scene_right, grid_spacing):
        canvas.create_arc( i, coord_y0, i + grid_spacing, coord_y0 + height, extent="180", width=5, fill="#30a3e7", outline="#44f4fb")
     

        # canvas.create_arc(i+ grid_spacing/2, coord_y0, i + grid_spacing , coord_y0 + height, extent="-180", style=tk.ARC,width=1, outline='blue')
        # canvas.create_arc(i+ grid_spacing/2, coord_y0, i + grid_spacing , coord_y0 + height, extent="180", width=5, fill="#30a3e7", outline="#44f4fb")
        
        # canvas.create_line(i+ grid_spacing/2, coord_y0 + height/2, i + grid_spacing , coord_y0 + height/2, fill="blue", width=2 )
    canvas.create_line(scene_left, coord_y0 + height/2, scene_right, coord_y0 + height/2, width=5, fill="#30a3e7")
def draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 20

    for i in range(scene_top, scene_bottom, grid_spacing):
        canvas.create_line(scene_left, i, scene_right, i)
        canvas.create_text(scene_left + text_horizontal_margin, i  + text_vertical_margin, text=f"{i}")
    for i in range(scene_left, scene_right, grid_spacing):
        canvas.create_line( i, scene_top, i, scene_bottom)
        canvas.create_text( i, scene_top + text_vertical_margin, text=f"{i}")

# Call the main function so that
# this program will start executing.
main()