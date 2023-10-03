"""
from tkinter import *
root=Tk()
root.title("I am in Center of screen")
wind_width=300
wind_height=300

# Getting the screen dimensions
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()

# Finding center point
center_x=int(screen_w/2-wind_width/2)
center_y=int(screen_h/2-wind_height/2)


# Setting the geometry
root.geometry(f"{wind_width}x{wind_height}+{center_x}+{center_y}")

root.mainloop()


"""
from tkinter import *
#root=Tk()
#root.title("center")

def center_screen(w_w,w_h,root):
    screen_w=root.winfo_screenwidth()
    screen_h=root.winfo_screenheight()
    x_c=int(screen_w/2-w_w/2)
    y_c=int(screen_h/2-w_h/2)
    root.geometry(f"{w_w}x{w_h}+{x_c}+{y_c}")

