'''import tkinter as tk # Importing the tkinter module
from tkinter import ttk # Importing the themed tkinter
from tkinter import messagebox # Importing the messagebox
from tkinter import filedialog # Importing the filedialog
#from PIL import Image, ImageTk  --#need to fix this at some point to add images...
import sqlite3  # Assuming you are using SQLite
from ClassesandPlanetGeneration import generate_random_galactic_object
import sys # For command line arguments
import json # For converting JSON strings to Python dictionaries
#username = sys.argv[1] # Retrieve the username from the command line arguments
# Refresh the player data from the database




def create_agg_frame():
    global agg_frame
    if agg_frame:
        agg_frame.destroy()
    agg_frame = ttk.Frame(mainwindow)
    ttk.Label(agg_frame, text="Agriculture", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    agg_frame.grid(row=1, column=1, sticky="nw", padx=15, pady=15)



def create_inventory_frame(parent):
    refresh_player_data(username)
    objects = fetch_inv_from_db(username)
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Inventory Frame", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)
    global objid
    # Add inventory-specific widgets here
    row_index = 4  # Start from row 4 to avoid overlapping with existing widgets

    for obj_id, name, obj_type in objects:
        ttk.Label(frame, text=f"{name}", font=("Arial", 12)).grid(row=row_index, column=0, sticky=tk.W)
        ttk.Label(frame, text=f"{obj_type}", font=("Arial", 10)).grid(row=row_index + 1, column=0, sticky=tk.W)
        btn = ttk.Button(frame, text="Goto", command=lambda objid=obj_id: switch_left_frame(objid=objid))
        btn.grid(row=row_index, column=2, rowspan=2)  # Centered vertically

        row_index += 2  # Move down for the next object

        menu_label = ttk.Label(frame, text="Menu (see examples above)")
        menu_label.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=3)



    my_button = ttk.Button(frame, text="do something")
    my_button.grid(row=2, column=2)
    return frame

def create_market_frame(parent):
    refresh_player_data(username)
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Market Frame", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    # Add market-specific widgets here
    buyobj = tk.Button(frame, text="Make planets", command=lambda: generate_random_galactic_object(username, no_obj, maxobj))
    buyobj.grid(row=2, column=2)

    ttk.Label(frame, text="Item 1: Health Potion - $10").grid(row=1, column=0, pady=5)
    ttk.Label(frame, text="Item 2: Mana Potion - $15").grid(row=2, column=0, pady=5)
    return frame

def create_moneypump_frame(parent):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="moneypump", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)
    # Add other-specific widgets here
    b = tk.Button(frame, text="Don't click here", command=addcash)
    b.grid(row=2, column=4)


    ttk.Label(frame, text="Other Content 1").grid(row=1, column=0, pady=5)
    ttk.Label(frame, text="Other Content 2").grid(row=2, column=0, pady=5)
    return frame

def switch_frame(event=None):
    global current_frame
    if current_frame:
        current_frame.destroy()

    selected_frame = combobox_value.get()
    if selected_frame == "Inventory":
        current_frame = create_inventory_frame(frame1)
    elif selected_frame == "Market":
        current_frame = create_market_frame(frame1)
    elif selected_frame == "Moneypump":
        current_frame = create_moneypump_frame(frame1)

    current_frame.grid(row=1, column=1, sticky="ne", padx=15, pady=15)

def object_frame(obj_id):
    frame = ttk.Frame(mainwindow)
    ttk.Label(frame, text=f"Object {obj_id}", font=("Arial", 20)).pack(pady=20)
    return frame

def create_left_frame1(parent):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Left Frame 1", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    return frame

def create_left_frame2(parent, objid):
    get_object_data(objid)
    frame = ttk.Frame(parent)

    ttk.Label(frame, text=f"Name:{objectname}", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    ttk.Label(frame, text=f"Type:{objecttype}", font=("Arial", 12), anchor=tk.W).grid(row=1, column=0, pady=5, sticky=tk.W)
    ttk.Label(frame, text=f"Supports Life: {objlife}", font=("Arial",12), anchor=tk.W).grid(row=2, column=0, pady=5,sticky=tk.W)
    ttk.Label(frame, text=f"Population: {objpop:,}/{objmaxpop:,}", font=("Arial",13), anchor=tk.W).grid(row=3, column=0, pady=5, sticky=tk.W)

    row_index = 4
    for resource, quantity in objrssdict.items():
        ttk.Label(frame, text=f"{resource}: {quantity:,}", font=("Arial",10), anchor=tk.W).grid(row=row_index, column=0, pady=5, sticky=tk.W)
        row_index += 1

    if objspec == []:
        return frame
    else:
        ttk.Label(frame, text=f"Specials: {objspec} ", font=("Arial",10), anchor=tk.W).grid(row=row_index, column=0, pady=5, sticky=tk.W)
        #print ("object attributes: " + objectname + " " + objecttype + " " + str(objectreslevel) + " " + str(objlife) + " " + str(objmaxpop) + " " + str(objpop) + " " + str(objrssdict) + " " + str(objspec))
        return frame

def create_left_frame3(parent):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text="Left Frame 3", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    return frame

def switch_left_frame(event=None, objid=None):
    global left_current_frame
    if left_current_frame:
        left_current_frame.destroy()
    if objid is not None:
        left_current_frame = create_left_frame2(frame2, objid)
        left_current_frame.grid(row=1, column=0, sticky="nw", padx=15, pady=15)

mainwindow = tk.Tk()
mainwindow.config(bg="white")
mainwindow.geometry("800x600")
#mainwindow.attributes("-fullscreen", True)
#mainwindow.bind("<Escape>", lambda event: mainwindow.attributes("-fullscreen", False))
menubar = tk.Menu(mainwindow)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=filedialog.askopenfilename)
filemenu.add_command(label="Save", command=filedialog.asksaveasfilename)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=mainwindow.quit)
menubar.add_cascade(label="File", menu=filemenu)

mainwindow.config(menu=menubar)

# Configure grid
mainwindow.grid_rowconfigure(0, weight=1,)
mainwindow.grid_columnconfigure(0, weight=1,)
mainwindow.grid_columnconfigure(1, weight=1,)

frame1 = tk.LabelFrame(mainwindow, text=username, padx=100, pady=100, bg="white")
frame1.grid(row=0, column=1, sticky="ne", padx=15, pady=55)

frame2 = tk.LabelFrame(mainwindow, text="Left Side", padx=100, pady=100, bg="white")
frame2.grid(row=0, column=0, sticky="nw", padx=15, pady=55)

# Consistently displayed buttons

b2 = tk.Button(frame1, text="Quit", command=mainwindow.quit)
b2.grid(row=4, column=1)

moneybox = tk.Label(frame1, text=f"Current Money: {fetch_money_from_db()}", font=("Arial",15), bg="white", fg="red")
moneybox.grid(row=0, column=0, columnspan=2)

combobox_value = tk.StringVar()
combobox = ttk.Combobox(mainwindow, textvariable=combobox_value)
combobox['values'] = ("Inventory", "Market", "Moneypump")
combobox.current(0)
combobox.bind("<<ComboboxSelected>>", switch_frame)
combobox.grid(row=0, column=1, sticky="ne", padx=15, pady=15)

left_combobox_value = tk.StringVar()
left_combobox = ttk.Combobox(mainwindow, textvariable=left_combobox_value)
left_combobox['values'] = ("Left Frame 1", "Left Frame 2", "Left Frame 3")
left_combobox.current(0)
left_combobox.bind("<<ComboboxSelected>>", switch_left_frame)
left_combobox.grid(row=0, column=0, sticky="nw", padx=15, pady=15)


current_frame = None
left_current_frame = None
switch_frame()
switch_left_frame()

mainwindow.mainloop()'''


from tkinter import *
import customtkinter
from PIL import Image, ImageTK

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.title('LootBox')
root.iconbitmap('c:/gui/Lootbox.ico')
root.geometry("500x170")

add_folder_image = ImageTK.PhotoImage(Image.open("test_images/add-folder.png").resize(("20x20"), Image.ANTIALIAS))
add_list_image = ImageTK.PhotoImage(Image.open("test_images/add-list.png").resize(("20x20"), Image.ANTIALIAS))

root.mainloop
