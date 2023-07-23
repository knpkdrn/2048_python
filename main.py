import tkinter as tk
import field as grid_map
from tkinter import font

window = tk.Tk()
window.title("2048")

_width = 512
_height = 512
window.geometry(f"{_width}x{_height}")

window.resizable(False, False)
custom_fontSize = font.Font(size=12)

frame = tk.Frame(window, padx=0, pady=100)
frame.pack()

label = tk.Label(frame, text="Keys: \nUp arrow OR 'A' : Move UP\nRight arrow OR 'D' : Move RIGHT\nDown arrow OR 'S' : Move DOWN\nLeft arrow OR 'A' : Move LEFT",font=custom_fontSize, padx=0, pady=50)
label.pack(anchor=tk.CENTER)

def btn_click():
    # open the game window
    grid_map.handle_game(window)

btn = tk.Button(frame,width=10, height=2, borderwidth=1,relief="solid", text="Start", command=btn_click)
btn.pack(anchor = tk.CENTER)

window.mainloop()
