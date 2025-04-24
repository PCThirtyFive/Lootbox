import customtkinter as ctk

class SettingsMenu(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Settings")
        self.geometry("300x200")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.volume_label = ctk.CTkLabel(self, text="Volume:")
        self.volume_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        self.volume_slider = ctk.CTkSlider(self, from_=0, to=100)
        self.volume_slider.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="e")

        self.difficulty_label = ctk.CTkLabel(self, text="Difficulty:")
        self.difficulty_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")
        self.difficulty_optionmenu = ctk.CTkOptionMenu(self, values=["Easy", "Normal", "Hard"])
        self.difficulty_optionmenu.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="e")

        self.fullscreen_switch = ctk.CTkSwitch(self, text="Fullscreen")
        self.fullscreen_switch.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")



class GameUI(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.health_label = ctk.CTkLabel(self, text="Health:")
        self.health_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        self.health_bar = ctk.CTkProgressBar(self, progress_color="red")
        self.health_bar.set(1)
        self.health_bar.grid(row=0, column=1, padx=20, pady=(20, 0), sticky="e")

        self.score_label = ctk.CTkLabel(self, text="Score: 0")
        self.score_label.grid(row=1, column=0, padx=20, pady=(10, 20), sticky="w")

        self.pause_button = ctk.CTkButton(self, text="Pause", command=self.pause_game)
        self.pause_button.grid(row=1, column=1, padx=20, pady=(10, 20), sticky="e")

    def pause_game(self):
        print("Game paused!")



class MainMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.title_label = ctk.CTkLabel(self, text="Game Title", font=("Arial", 30))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.play_button = ctk.CTkButton(self, text="Play", command=self.start_game)
        self.play_button.grid(row=1, column=0, padx=20, pady=10)

        self.settings_button = ctk.CTkButton(self, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=2, column=0, padx=20, pady=10)

        self.quit_button = ctk.CTkButton(self, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=3, column=0, padx=20, pady=10)

    def start_game(self):
        print("Game started!")

    def open_settings(self):
        print("Settings opened!")

    def quit_game(self):
        self.master.destroy()

class Mainwindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LootBox")
        self.geometry("1200x900")
        MainMenu(self).pack(expand=True, fill="both")


if __name__ == "__main__":
    app = Mainwindow()
    app.mainloop()