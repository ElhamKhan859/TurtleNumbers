import turtle
import graphics
from tkinter import *
from tkinter import ttk

root = Tk()

paned_window = ttk.PanedWindow(root, orient = HORIZONTAL)
paned_window.pack(fill = BOTH, expand = True)

left_frame = ttk.Frame(paned_window, width = 100, height = 400, relief= SUNKEN)
right_frame = ttk.Frame(paned_window, width = 300, height = 400, relief= SUNKEN)

graphics_list = (' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ',
         ' 6 ', ' 7 ', ' 8 ', ' 9 ', ' 0 ')

graphics_label = ttk.Label(left_frame, text = "GRAPHICS", font=("Times New Roman", 16, "bold"))
graphics_label.pack(padx=3, pady=3)

graphics_var = StringVar(value=graphics_list)

graphics_listbox = Listbox(left_frame, listvariable = graphics_var, selectmode = SINGLE , borderwidth=3)
graphics_listbox.pack(expand= TRUE, fill=BOTH, padx=1, pady=1)

config_label = ttk.Labelframe(left_frame, text = "CONFIGURATION")
config_label.pack(expand= TRUE, fill=BOTH, padx=5, pady=5)

pen_size_label = ttk.Label(config_label, text = "Pen Size", font= ("Arial", 12, "bold"), anchor="center")
pen_size_label.grid(row = 0, column = 0, padx = 5, pady = 5)

pen_size_var = StringVar(root, value = 3)

pen_size_spinbox = ttk.Spinbox(config_label, from_= 1, to = 10, textvariable = pen_size_var)
pen_size_spinbox.grid(row = 1, column = 0, padx = 10, pady = 10)

graphic_size_label = ttk.Label(config_label, text = "Graphic Size", font= ("Arial", 12, "bold"), anchor="center")
graphic_size_label.grid(row = 0, column = 1, padx = 5, pady = 5)

graphic_size_var = StringVar(root, value = 5)

graphic_size_spinbox = ttk.Spinbox(config_label, from_= 1, to = 10, textvariable = graphic_size_var)
graphic_size_spinbox.grid(row = 1, column = 1, padx = 10, pady = 10)

pen_color_label = ttk.Label(config_label, text = "Pen Color", font= ("Arial", 12, "bold"), anchor="center")
pen_color_label.grid(row = 2, column = 0, padx = 5, pady = 5 )

tkinter_colors = [
    "black",
    "white",
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "gray",
    "orange",
    "purple",
    "brown",
    "pink",
    "light blue",
    "dark blue",
    "light green",
    "dark green",
    "light gray",
    "dark gray",
    "gold"
]

colors_var = StringVar(root, value = tkinter_colors[0])

pen_color_combox = ttk.Combobox(config_label, textvariable = colors_var, values=tkinter_colors)
pen_color_combox.grid(row = 3, column = 0, padx = 10, pady= 10)

paned_window.add(left_frame, weight = 1)
paned_window.add(right_frame, weight = 3)

canvas = Canvas(right_frame, width=300, height=400, bg="grey", borderwidth=3)
canvas.pack(fill = BOTH, expand = True, padx = 3, pady = 3)

# Create a turtle object and link it to the canvas
turtle_screen = turtle.TurtleScreen(canvas)
t_obj = turtle.RawTurtle(turtle_screen)
    


def item_selected(event):
    selected_indice = graphics_listbox.curselection()[0]
    selected_graphic = graphics_list[selected_indice]
    t_obj.reset()
    t_obj.pencolor(colors_var.get())
    graphics.draw_number(t_obj, int(selected_graphic), int(pen_size_var.get()), int(graphic_size_var.get()))
    t_obj.home()

graphics_listbox.bind('<<ListboxSelect>>', item_selected)
#pen_color_combox.bind('<<ComboboxSelected>>', set_pen_color)



root.mainloop()