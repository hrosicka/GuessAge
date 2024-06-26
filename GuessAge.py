from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import os
import tkinter as tk
import customtkinter
from CTkMessagebox import CTkMessagebox
import EstimateAge
from idlelib.tooltip import Hovertip
from tktooltip import ToolTip


class GuessAge(tk.Tk):
    """
    This class creates a simple GUI application that allows users to enter a name 
    and guesses their age (from free API).
    """

    MIN_NAME_LENGTH = 2

    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("Guess Age")

        self.resizable(False, False) 

        self.geometry("680x280")

        dirname = os.path.dirname(__file__)
        self.icon_path = os.path.join(dirname, 'IconUser.ico')  # Replace with your icon file path
        self.iconbitmap(self.icon_path)  # Set the window icon
        self.warning_ico_path = os.path.join(dirname, 'warning.png') 

        # Create a frame for the inputs
        self.input_frame = tk.Frame(self)

        # Create the name label and entry field
        self.name_label = customtkinter.CTkLabel(self.input_frame, text="Name:")
        self.name_entry = customtkinter.CTkEntry(master=self.input_frame)

        # Tooltip for name entry
        self.name_entry_tooltip = "Enter your name here (including Czech characters)."
        Hovertip(self.name_entry, self.name_entry_tooltip)

        # Create the age label and entry field
        self.age_label = customtkinter.CTkLabel(self.input_frame, 
                                                text="Age:")
        self.age_entry = customtkinter.CTkEntry(master=self.input_frame,
                                                fg_color="lightgrey",
                                                state="readonly")


        # Create a frame for the buttons
        self.button_frame = tk.Frame(self)

        # Create the guess age button
        self.guess_age_button = customtkinter.CTkButton(master=self.button_frame,
                                                        text="Guess Age",
                                                        command=self.guess_age,
                                                        width=120,
                                                        text_color="white",
                                                        fg_color="#2D1E2F",
                                                        hover_color="#F15946") 

        # Create the clear button
        self.clear_button = customtkinter.CTkButton(master=self.button_frame,
                                                    text="Clear",
                                                    command=self.clear,
                                                    width=120,
                                                    text_color="white",
                                                    fg_color="#2D1E2F",
                                                    hover_color="#F15946") 

        # Create the close button
        self.close_button = customtkinter.CTkButton(master=self.button_frame, 
                                                    text="Close",
                                                    command=self.close,
                                                    width=120,
                                                    text_color="white",
                                                    fg_color="#2D1E2F",
                                                    hover_color="#F15946")  
        
        
        # Tooltips
        self.guess_age_button_tooltip = "Click to guess your age based on your name."
        self.clear_button_tooltip = "Click to clear name and age fields.."
        self.close_button_tooltip = "Click to close the application."

        # Layout the widgets
        self.input_frame.pack(side=tk.LEFT, padx=40, pady=40)
        self.button_frame.pack(side=tk.RIGHT, padx=40, pady=40)

        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        self.guess_age_button.grid(row=0, column=0, pady=5)
        self.clear_button.grid(row=1, column=0, pady=5)
        self.close_button.grid(row=2, column=0, pady=5)

        # Set tooltips
        Hovertip(self.guess_age_button, self.guess_age_button_tooltip)
        Hovertip(self.clear_button, self.clear_button_tooltip)
        Hovertip(self.close_button, self.close_button_tooltip)


    # Define the guess age function
    def guess_age(self):
        
        # Get the name from the entry field
        name = self.name_entry.get()
        valid_chars = set("aábcčdeéěfghiíjklmnňoópqrřsštuúůvwxyzžAÁBCČDEÉFGHIJKLMNOÓPQRŘSŠTUVWXYZŽ")

        # Check if the name is empty after removing spaces
        if not name.strip():  
                self.name_entry.configure(fg_color="#F7ABA2")
                CTkMessagebox(title="Error", 
                  message="Please enter a name!",
                  icon=self.warning_ico_path,
                  height=150,
                  width=300,
                  button_text_color="white",
                  button_width=80,
                  button_color="#2D1E2F",
                  button_hover_color="#F15946") 
                return
        
        if len(name) < self.MIN_NAME_LENGTH:
            self.name_entry.configure(fg_color="#F7ABA2")
            CTkMessagebox(title="Error", 
                  message="Name must contain at least 2 characters!",
                  icon=self.warning_ico_path,
                  height=150,
                  width=300,
                  button_text_color="white",
                  button_width=80,
                  button_color="#2D1E2F",
                  button_hover_color="#F15946") 
            return

        # Check if all characters are valid
        if not all(char in valid_chars or char.isspace() for char in name):
            self.name_entry.configure(fg_color="#F7ABA2")
            CTkMessagebox(title="Error", 
                  message="Name can only contains letters!",
                  icon=self.warning_ico_path,
                  height=150,
                  width=300,
                  button_text_color="white",
                  button_width=80,
                  button_color="#2D1E2F",
                  button_hover_color="#F15946") 
            return

        self.name_entry.configure(fg_color="white")
        guess_age = EstimateAge.AgifyAPI(name)
        age = guess_age.get_estimated_age()

        self.age_entry.configure(state="normal")

        # Generate a random age between 1 and 100
        # age = random.randint(1, 100)

        # Display the age in the age entry field
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, age)

        self.age_entry.configure(state="readonly")

    # Define the clear function
    def clear(self):
        # Clear the name and age entry fields
        self.age_entry.configure(state="normal")
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.age_entry.configure(state="readonly")
        self.name_entry.configure(fg_color="white")

    # Define the close function
    def close(self):
        # Close the window
        self.destroy()


# Create the main window
if __name__ == "__main__":
    form = GuessAge()
    form.mainloop()