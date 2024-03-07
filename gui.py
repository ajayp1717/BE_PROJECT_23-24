import tkinter as tk
import subprocess
from tkinter import Tk, Label, Canvas
from PIL import ImageTk, Image
 

# Create a Tkinter window
root = tk.Tk()
root.title("Drowsiness Detection System")
#image = Image.open("download.jpg")
#tk_image = ImageTk.PhotoImage(image)
#image = image.resize((100, 100))


# Set the window size and position to cover the whole screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Set the background image
#background_label = Label(root, image=tk_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create a function to run the Python file
def run_file():
    subprocess.run(["python", "drowsiness detection.py"])


message_label = tk.Label(root, text="AISSMS College of Engineering",
                         font=("Arial", 20), fg="red")
message_label.pack(pady=20)


message_label = tk.Label(root, text="Department of Computer Engineering",
                         font=("Arial", 20), fg="red")
message_label.pack(pady=25)


# Create a label widget to display the message
message_label = tk.Label(root, text="Drowsiness Detection and Alert System",
                         font=("Arial", 20), fg="black")
message_label.pack(pady=50)

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create the start button
start_button = tk.Button(button_frame, text="Start", font=("Arial", 16),
                         fg="green", bg="white", width=10, height=3, command=run_file)
start_button.pack(side=tk.TOP, pady=20)


# Run the Tkinter event loop
root.mainloop()