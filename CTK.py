from customtkinter import *

LootBox = CTk()
LootBox.geometry("1280x920")

frame = CTkFrame(master=LootBox, border_width=2, fg_color="#8D6F3A", border_color="#FFCC70")
frame.pack(expand=True)
set_appearance_mode("dark")

Mainmenu = CTkButton(master=frame,text="Mainmenu")
Mainmenu.place(relx=0.5, rely=0.5, anchor="center")
Mainmenu2 = CTkButton(master=frame)
Mainmenu2.place(relx=0.5, rely=0.6, anchor="center")


LootBox.mainloop()