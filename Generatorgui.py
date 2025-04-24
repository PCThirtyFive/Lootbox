import customtkinter as ctk

class GameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Game")
        self.geometry("1200x800")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.current_screen = None
        self.show_main_menu()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_connect_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self) # Removed padx, pady from here
        self.current_screen.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.current_screen.grid_columnconfigure(0, weight=1)
        self.current_screen.grid_rowconfigure(0, weight=1)
        self.current_screen.configure(border_width=2, border_color="black") # Added to configure

        # Added padding within the frame
        connect_button = ctk.CTkButton(self.current_screen, text="Connect", command=self.show_login_screen)
        connect_button.grid(row=0, column=0, padx=20, pady=(20, 10))  # Added padding

        quit_button = ctk.CTkButton(self.current_screen, text="Quit", command=self.destroy)
        quit_button.grid(row=1, column=0, padx=20, pady=(10, 20))    # Added padding

    def show_login_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self) # Removed padx, pady from here
        self.current_screen.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.current_screen.grid_columnconfigure(0, weight=1)
        self.current_screen.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.current_screen.configure(border_width=2, border_color="black") # Added to configure

        # Added padding within the frame
        login_button = ctk.CTkButton(self.current_screen, text="Login", command=self.open_login_popup)
        login_button.grid(row=0, column=0, padx=20, pady=(20, 10))  # Added padding

        register_button = ctk.CTkButton(self.current_screen, text="Register", command=self.open_register_popup)
        register_button.grid(row=1, column=0, padx=20, pady=10)  # Added padding

        reset_button = ctk.CTkButton(self.current_screen, text="Reset Login", command=self.open_reset_popup)
        reset_button.grid(row=2, column=0, padx=20, pady=10)  # Added padding

        quit_button = ctk.CTkButton(self.current_screen, text="Quit", command=self.destroy)
        quit_button.grid(row=3, column=0, padx=20, pady=(10, 20))  # Added padding

    def open_login_popup(self):
        login_popup = ctk.CTkToplevel(self)
        login_popup.title("Login")
        login_popup.geometry("400x200")
        login_popup.grid_columnconfigure(1, weight=1)

        username_label = ctk.CTkLabel(login_popup, text="Username:")
        username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        username_entry = ctk.CTkEntry(login_popup)
        username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        password_label = ctk.CTkLabel(login_popup, text="Password:")
        password_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        password_entry = ctk.CTkEntry(login_popup, show="*")
        password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        confirm_button = ctk.CTkButton(login_popup, text="Confirm", command=self.show_main_menu) # Replace with actual login logic
        confirm_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)



    def open_register_popup(self):
        register_popup = ctk.CTkToplevel(self)
        register_popup.title("Register")
        register_popup.geometry("400x300")
        register_popup.grid_columnconfigure(1, weight=1)

        # Add your text boxes and confirm button for registration here
        username_label = ctk.CTkLabel(register_popup, text="Username:")
        username_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        username_entry = ctk.CTkEntry(register_popup)
        username_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        password_label = ctk.CTkLabel(register_popup, text="Password:")
        password_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        password_entry = ctk.CTkEntry(register_popup, show="*")
        password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        email_label = ctk.CTkLabel(register_popup, text="Email:")
        email_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        email_entry = ctk.CTkEntry(register_popup)
        email_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

        pin_label = ctk.CTkLabel(register_popup, text="4-Digit Pin:")
        pin_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        pin_entry = ctk.CTkEntry(register_popup)
        pin_entry.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        confirm_button = ctk.CTkButton(register_popup, text="Confirm", command=lambda: print("Registration confirmed")) # Replace with actual registration logic
        confirm_button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)



    def open_reset_popup(self):
        reset_popup = ctk.CTkToplevel(self)
        reset_popup.title("Reset Login")
        reset_popup.geometry("400x200")
        reset_popup.grid_columnconfigure(1, weight=1)

        # Add your text boxes and confirm button for reset here
        email_label = ctk.CTkLabel(reset_popup, text="Email:")
        email_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        email_entry = ctk.CTkEntry(reset_popup)
        email_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        pin_label = ctk.CTkLabel(reset_popup, text="4-Digit Pin:")
        pin_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        pin_entry = ctk.CTkEntry(reset_popup)
        pin_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        confirm_button = ctk.CTkButton(reset_popup, text="Confirm", command=lambda: print("Reset confirmed")) # Replace with actual reset logic
        confirm_button.grid(row=2, column=0, columnspan=2, padx=20, pady=10)



    def show_main_menu(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self) # Removed padx, pady from here
        self.current_screen.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.current_screen.grid_columnconfigure(0, weight=1)
        self.current_screen.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.current_screen.configure(border_width=2, border_color="black") # Added to configure

        # Added padding within the frame
        arena_button = ctk.CTkButton(self.current_screen, text="Arena", command=self.show_arena_screen)
        arena_button.grid(row=0, column=0, padx=20, pady=(20, 10))

        armoury_button = ctk.CTkButton(self.current_screen, text="Armoury", command=self.show_armoury_screen)
        armoury_button.grid(row=1, column=0, padx=20, pady=10)

        lootbox_button = ctk.CTkButton(self.current_screen, text="LootBox", command=self.show_lootbox_screen)
        lootbox_button.grid(row=2, column=0, padx=20, pady=10)

        quit_button = ctk.CTkButton(self.current_screen, text="Quit", command=self.destroy)
        quit_button.grid(row=3, column=0, padx=20, pady=(10, 20))

    def show_arena_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self)
        self.current_screen.pack(fill="both", expand=True, padx=10, pady=10)
        self.current_screen.grid_columnconfigure(1, weight=3)
        self.current_screen.grid_rowconfigure((0, 1), weight=1)

        # Left Frame
        left_frame = ctk.CTkFrame(self.current_screen, width=int(1200 * 0.25))
        left_frame.grid(row=0, column=0, rowspan=2, padx=(10, 5), pady=10, sticky="nsew")
        left_frame.grid_columnconfigure(0, weight=1)
        # Added padding

        enter_arena_button = ctk.CTkButton(left_frame, text="Enter Arena Pool", fg_color="green", command=lambda: enter_arena_button.configure(text="Exit Arena Pool", fg_color="red", command=lambda: enter_arena_button.configure(text="Enter Arena Pool", fg_color="green", command=enter_arena_button.cget("command")))) # Toggle button
        enter_arena_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        main_menu_button = ctk.CTkButton(left_frame, text="Main menu", command=self.show_main_menu)
        main_menu_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        stats_button = ctk.CTkButton(left_frame, text="Stats", command=self.show_stats_screen)
        stats_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        quit_button = ctk.CTkButton(left_frame, text="Quit", command=self.destroy)
        quit_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Right Frame
        right_frame = ctk.CTkFrame(self.current_screen)
        right_frame.grid(row=0, column=1, rowspan=2, padx=(5, 10), pady=10, sticky="nsew")
        right_frame.grid_rowconfigure((0, 1), weight=1)
        right_frame.grid_columnconfigure((0, 1), weight=1)
        # Added padding

        previous_fight_frame = ctk.CTkFrame(right_frame)
        previous_fight_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        previous_fight_label = ctk.CTkLabel(previous_fight_frame, text="Previous Fight")
        previous_fight_label.pack(padx=10, pady=10)

        current_fight_frame = ctk.CTkFrame(right_frame)
        current_fight_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        current_fight_label = ctk.CTkLabel(current_fight_frame, text="Current Fight")
        current_fight_label.pack(padx=10, pady=10)

        bottom_frame = ctk.CTkFrame(right_frame)
        bottom_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        bottom_frame.grid_columnconfigure((0, 1, 2), weight=1)

        left_health_frame = ctk.CTkFrame(bottom_frame)
        left_health_frame.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        left_health_label = ctk.CTkLabel(left_health_frame, text="Left Health")
        left_health_label.pack(padx=5, pady=5)
        left_health_bar = ctk.CTkProgressBar(left_health_frame)
        left_health_bar.pack(padx=5, pady=5, fill="x")

        fight_updates_frame = ctk.CTkFrame(bottom_frame)
        fight_updates_frame.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
        fight_updates_label = ctk.CTkLabel(fight_updates_frame, text="Fight Updates (Scrolling)")
        fight_updates_label.pack(padx=5, pady=5)

        right_health_frame = ctk.CTkFrame(bottom_frame)
        right_health_frame.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")
        right_health_label = ctk.CTkLabel(right_health_frame, text="Right Health")
        right_health_label.pack(padx=5, pady=5)
        right_health_bar = ctk.CTkProgressBar(right_health_frame)
        right_health_bar.pack(padx=5, pady=5, fill="x")

    def show_armoury_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self)
        self.current_screen.pack(fill="both", expand=True)
        self.current_screen.grid_columnconfigure(1, weight=1)
        self.current_screen.grid_rowconfigure(0, weight=1)

        # Left Button Frame
        left_button_frame = ctk.CTkFrame(self.current_screen, width=int(1200 * 5/16))
        left_button_frame.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="nswe")
        left_button_frame.grid_columnconfigure(0, weight=1)


        buttons = ["Head", "Shoulders", "Arms", "Chest", "Hands", "Pants", "Boots", "Weapon", "Jewellery"]
        for i, text in enumerate(buttons):
            button = ctk.CTkButton(left_button_frame, text=text, command=lambda t=text: self.show_armoury_sub_screen(t)) # Example sub-screen function
            button.grid(row=i, column=0, padx=10, pady=5, sticky="ew")

        main_menu_button = ctk.CTkButton(left_button_frame, text="Main menu", command=self.show_main_menu)
        main_menu_button.grid(row=len(buttons), column=0, padx=10, pady=10, sticky="ew")

        arena_button = ctk.CTkButton(left_button_frame, text="Arena", command=self.show_arena_screen)
        arena_button.grid(row=len(buttons) + 1, column=0, padx=10, pady=10, sticky="ew")

        lootbox_button = ctk.CTkButton(left_button_frame, text="Lootbox", command=self.show_lootbox_screen)
        lootbox_button.grid(row=len(buttons) + 2, column=0, padx=10, pady=10, sticky="ew")

        quit_button = ctk.CTkButton(left_button_frame, text="Quit", command=self.destroy)
        quit_button.grid(row=len(buttons) + 3, column=0, padx=10, pady=10, sticky="ew")

        # Center Frames
        center_frame = ctk.CTkFrame(self.current_screen)
        center_frame.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="nsew")
        center_frame.grid_rowconfigure((0, 1), weight=1)
        center_frame.grid_columnconfigure(0, weight=1)
        # Added padding

        self.center_top_frame = ctk.CTkFrame(center_frame)
        self.center_top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.center_top_frame.grid_columnconfigure((0,1), weight=1)
        self.center_bottom_frame = ctk.CTkFrame(center_frame)
        self.center_bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        #Populate the center top frame
        self.selected_item_text = ctk.StringVar()
        self.selected_item_text.set("No Item Selected")

        left_frame_top = ctk.CTkFrame(self.center_top_frame)
        left_frame_top.grid(row=0, column=0, sticky="nsew")
        self.item_image_label = ctk.CTkLabel(left_frame_top, text="[Image Placeholder]")
        self.item_image_label.pack(padx=10, pady=10)
        self.item_stats_label = ctk.CTkLabel(left_frame_top, textvariable=self.selected_item_text)
        self.item_stats_label.pack(padx=10, pady=10)
        self.equip_button = ctk.CTkButton(left_frame_top, text="Equip", command=self.equip_item)
        self.equip_button.pack(padx=10, pady=10)

        right_frame_top = ctk.CTkFrame(self.center_top_frame)
        right_frame_top.grid(row=0, column=1, sticky="nsew")
        self.equipped_item_image_label = ctk.CTkLabel(right_frame_top, text="[Equipped Image]")
        self.equipped_item_image_label.pack(padx=10, pady=10, anchor="e")
        self.equipped_item_label = ctk.CTkLabel(right_frame_top, text="Currently Equipped: None", anchor="e")
        self.equipped_item_label.pack(padx=10, pady=10, anchor="e")

        # Create number buttons for center bottom frame.
        for i in range(9):
            button = ctk.CTkButton(self.center_bottom_frame, text=str(i + 1), command=lambda val=i+1: self.update_stats(val))
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="nsew")
        self.center_bottom_frame.grid_columnconfigure(tuple(range(3)), weight=1)
        self.center_bottom_frame.grid_rowconfigure(tuple(range(3)), weight=1)

    def show_lootbox_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self)
        self.current_screen.pack(fill="both", expand=True)
        self.current_screen.grid_columnconfigure(0, weight=1)
        self.current_screen.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(self.current_screen, text="Lootbox Screen (TBD)", font=("Arial", 24))
        label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def show_stats_screen(self):
        self.clear_screen()
        self.current_screen = ctk.CTkFrame(self)
        self.current_screen.pack(fill="both", expand=True)
        self.current_screen.grid_columnconfigure(0, weight=1)
        self.current_screen.grid_rowconfigure(0, weight=1)

        label = ctk.CTkLabel(self.current_screen, text="Stats Screen (TBD)", font=("Arial", 24))
        label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def show_armoury_sub_screen(self, selected_slot):
        # Placeholder for armory sub-screen functionality.
        print(f"Displaying items for {selected_slot}")
        self.selected_slot = selected_slot # make selected slot available to other methods
        self.update_center_top_frame()

    def update_stats(self, item_number):
        # Placeholder: Update displayed stats based on the button clicked in the center_bottom_frame
        # This is where you would fetch and display the stats of the selected item.
        # For now, we'll just update the label with a placeholder.
        self.selected_item_text.set(f"Stats for Item {item_number} from {self.selected_slot}") # show which slot we are in
        print(f"Displaying stats for item {item_number} from slot {self.selected_slot}")

    def equip_item(self):
        #  Equip functionality
        print(f"Equipping item for slot: {self.selected_slot}")
        self.equipped_item_label.configure(text=f"Currently Equipped: Item from {self.selected_slot}") # show which item is equipped.

    def update_center_top_frame(self):
        # Update the center top frame based on selectedarmoury category
        # Clear previous content
        for widget in self.center_top_frame.winfo_children():
            widget.destroy()

        # Create the frames inside the center_top_frame
        left_frame_top = ctk.CTkFrame(self.center_top_frame)
        left_frame_top.grid(row=0, column=0, sticky="nsew")
        self.item_image_label = ctk.CTkLabel(left_frame_top, text="[Image Placeholder]")
        self.item_image_label.pack(padx=10, pady=10)
        self.item_stats_label = ctk.CTkLabel(left_frame_top, textvariable=self.selected_item_text)
        self.item_stats_label.pack(padx=10, pady=10)
        self.equip_button = ctk.CTkButton(left_frame_top, text="Equip", command=self.equip_item)
        self.equip_button.pack(padx=10, pady=10)

        right_frame_top = ctk.CTkFrame(self.center_top_frame)
        right_frame_top.grid(row=0, column=1, sticky="nsew")
        self.equipped_item_image_label = ctk.CTkLabel(right_frame_top, text="[Equipped Image]")
        self.equipped_item_image_label.pack(padx=10, pady=10, anchor="e")
        self.equipped_item_label = ctk.CTkLabel(right_frame_top, text="Currently Equipped: None", anchor="e")
        self.equipped_item_label.pack(padx=10, pady=10, anchor="e")

        self.center_top_frame.grid_columnconfigure((0,1), weight=1)

if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
