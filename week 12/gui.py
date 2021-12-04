import tkinter as tk
import number_entry as numy


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Area of a Rectangle:")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and each
# widget is an object, the code to make a GUI usually has many variables
# to store the many objects. Because there are so many variable names,
# programmers often adopt a naming convention to help a programmer keep
# track of all the variables. One popular naming convention is to type a
# three letter prefix in front of the names of all variables that store
# GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main window
    Return: nothing
    """
    # Create a label that displays "Width of Rectangle:"
    lbl_width = tk.Label(frm_main, text="Width of Rectangle:")

    # Create a integer entry box where the user will enter the width.
    ent_width = numy.FloatEntry(frm_main, 1, 100, width=5)

    # Create a label that displays "Height of Rectangle::"
    lbl_height = tk.Label(frm_main, text="Height of Rectangle:")

    # Create a integer entry box where the user will enter the height.
    ent_height = numy.FloatEntry(frm_main, 1, 100, width=5)

    # Create a label that displays "Rates:"
    lbl_area = tk.Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_area_value = tk.Label(frm_main, width=6)

     # Create the Clear button.
    # btn_calc= tk.Button(frm_main, text="Calculate")

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(  row=0, column=0, padx=3, pady=3)
    ent_width.grid(  row=0, column=1, padx=3, pady=3)
    lbl_height.grid(  row=1, column=0, padx=3, pady=3)
    ent_height.grid(  row=1, column=1, padx=3, pady=3)
    lbl_area.grid(row=0, column=2, padx=(30,3), pady=3)
    lbl_area_value.grid( row=0, column=3, padx=3, pady=3)
    # btn_calc.grid(row=2, column=0, padx=3, pady=3, columnspan=2, sticky="W")
    btn_clear.grid(row=2, column=2, padx=3, pady=3, columnspan=2, sticky="W")


    # This function will be called each time the user releases a key.
    # If we're not using an event, we can use a button with a coomand to it
    def calc(e):
        """Compute and display the rectangle area.
        """
        try:
            # Get the width.
            width = ent_width.get()

            # Get the height.
            height = ent_height.get()

            area = width * height

            # Display the slowest and fastest benficial
            # heart area for the user to see.
            lbl_area_value.config(text=f"{area:.2f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_area_value.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_width.delete(0, tk.END)
        ent_height.delete(0, tk.END)

        lbl_area_value.config(text="")
        ent_width.focus()


    # Bind the calc function to the calculate button so
    # that the calc function will be called when the
    # user clicks the calculate button. 
    # btn_calc.config(command=calc)

    # Bind the calc function to the two text fields
    # so that the calc function will be called when the
    # user changes the text in the text fields.    
    ent_height.bind("<KeyRelease>", calc)
    ent_width.bind("<KeyRelease>", calc)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_width.focus()

    

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
