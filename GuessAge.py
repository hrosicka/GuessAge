import tkinter as tk
from tkinter import messagebox
import EstimateAge
# import random
from idlelib.tooltip import Hovertip


class GuessAge(tk.Tk):
    """
    This class creates a simple GUI application that allows users to enter a name 
    and guesses their age (from free API).
    """
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title("Guess Age")

        # Set the window size
        self.geometry("300x150")

        self.resizable(False, False) 

        # **Adding a custom icon**
        # 1. Prepare your icon image:
        #  - You can use a free image editing software to create a small icon (e.g. 32x32 pixels)
        #  - Save the image in a format supported by Tkinter, like ICO (.ico) or PNG (.png)
        #  - Place the icon file in the same directory as your Python script
        # self.icon_path = "my_icon.ico"  # Replace with your icon file path
        # self.iconbitmap(self.icon_path)  # Set the window icon

        # Create a frame for the inputs
        self.input_frame = tk.Frame(self)

        # Create the name label and entry field
        self.name_label = tk.Label(self.input_frame, text="Name:")
        self.name_entry = tk.Entry(self.input_frame)

        # Tooltip for name entry
        self.name_entry_tooltip = "Enter your name here (including Czech characters)."
        Hovertip(self.name_entry, self.name_entry_tooltip)

        # Create the age label and entry field
        self.age_label = tk.Label(self.input_frame, text="Age:")
        self.age_entry = tk.Entry(self.input_frame, state="readonly")

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self)

        # Create the guess age button
        self.guess_age_button = tk.Button(self.button_frame, text="Guess Age",
                                        command=self.guess_age, bg="dodgerblue4", 
                                        fg="white", width=10)

        # Create the clear button
        self.clear_button = tk.Button(self.button_frame, text="Clear",
                                    command=self.clear, bg="palegreen4", 
                                    fg="white", width=10)

        # Create the close button
        self.close_button = tk.Button(self.button_frame, text="Close",
                                    command=self.close, bg="darkorchid", 
                                    fg="white", width=10)
        
        # Tooltips
        self.guess_age_button_tooltip = "Click to guess your age based on your name."
        self.clear_button_tooltip = "Click to clear name and age fields.."
        self.close_button_tooltip = "Click to close the application."

        # Layout the widgets
        self.input_frame.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_frame.pack(side=tk.RIGHT, padx=5, pady=5)

        self.name_label.grid(row=0, column=0, pady=5)
        self.name_entry.grid(row=0, column=1, pady=5)

        self.age_label.grid(row=1, column=0, pady=5)
        self.age_entry.grid(row=1, column=1, pady=5)

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

        # Check if all characters are valid
        if not all(char in valid_chars or char.isspace() for char in name):
            self.name_entry.config(bg="pink")
            messagebox.showerror("Error", "Name can only contains letters.")
            return

        self.name_entry.config(bg="white")
        guess_age = EstimateAge.AgifyAPI(name)
        age = guess_age.get_estimated_age()

        self.age_entry.config(state="normal")

        # Generate a random age between 1 and 100
        # age = random.randint(1, 100)

        # Display the age in the age entry field
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, age)

        self.age_entry.config(state="readonly")

    # Define the clear function
    def clear(self):
        # Clear the name and age entry fields
        self.age_entry.config(state="normal")
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.age_entry.config(state="readonly")

    # Define the close function
    def close(self):
        # Close the window
        self.destroy()


# Create the main window
if __name__ == "__main__":
    form = GuessAge()
    form.mainloop()