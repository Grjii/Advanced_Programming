# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 10:38:01 2025
@author: grgej
"""

import random as ran
import tkinter as tk
from tkinter import messagebox

# read all jokes from file
with open("randomJokes.txt", "r") as file:
    read = file.readlines()

setup = ""       # current joke setup
punchline = ""   # current joke punchline

# pick a random joke and show the setup
def tell_joke():
    global setup, punchline
    setup_system = ran.choice(read).strip()  # pick a random line, remove newline
    setup, punchline = setup_system.split("?")  # split at the ? into setup & punchline
    setup += "?"  # add the ? back to setup
    setup_label.config(text=setup)  # show setup on screen
    punchline_label.config(text="")  # clear old punchline
    show_punchline_btn.config(state="normal")  # enable punchline button

# show the punchline when button clicked
def show_punchline():
    punchline_label.config(text=punchline, fg="#f7e6e6")  # reveal punchline
    show_punchline_btn.config(state="disabled")  # can't click again

# quit button with a message
def quit_app():
    messagebox.showinfo("Goodbye", "Oh well! Missed your chance.")  # just a fun message
    root.destroy()  # close the window

root = tk.Tk()
root.title("Alexa Joke Teller")
root.geometry("500x400")
root.configure(bg="#4040db")

title_label = tk.Label(root, text="Alexa Joke Teller", font=("Anton", 20, "bold"), bg="#4040db")
title_label.pack(pady=20)

setup_label = tk.Label(root, text="Click below to get a joke!", font=("Arial", 14), bg="#4040db", wraplength=400, justify="center")
setup_label.pack(pady=30)

punchline_label = tk.Label(root, text="", font=("Arial", 13, "italic"), bg="#4040db", fg="#555", wraplength=400, justify="center")
punchline_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#4040db")
button_frame.pack(pady=10)

# button to get a random joke
tell_joke_btn = tk.Button(button_frame, text="Alexa tell me a joke", font=("Arial", 12), bg="#4CAF50", fg="white", width=20, command=tell_joke)
tell_joke_btn.grid(row=0, column=0, padx=10)

# button to reveal punchline, starts disabled
show_punchline_btn = tk.Button(button_frame, text="Show punchline", font=("Arial", 12), bg="##f7e6e6", fg="white", width=20, command=show_punchline, state="disabled")
show_punchline_btn.grid(row=0, column=1, padx=10)

# button to quit
quit_btn = tk.Button(root, text="Quit", font=("Arial", 11), bg="#E53935", fg="white", width=10, command=quit_app)
quit_btn.pack(pady=10)

root.mainloop()
