# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 18:29:26 2025

@author: grgej
"""

import random
import tkinter as tk
from tkinter import *

# game variables
score = 0
lives = 2
answer = ""        # store the current correct answer
userchoice = ""    # stores difficulty choice
question_count = 0
total_questions = 10

# generate random math questions based on difficulty
def generative_questions(choice):
    if choice == "1":  # easy numbers
        x, y = random.randint(1, 9), random.randint(1, 9)
    elif choice == "2":  # medium numbers
        x, y = random.randint(10, 90), random.randint(10, 99)
    elif choice == "3":  # hard numbers
        x, y = random.randint(1000, 9999), random.randint(1000, 9999)
        
    op = random.choice(["+","-"])  # random operator

    # return both question text and the answer as a string
    if op == "+":
        return f"{x} + {y} = ", str(x + y)
    else:
        return f"{x} - {y} = ", str(x - y)

# show the next question
def question(choice):
    global answer 
    question, answer = generative_questions(choice)
    question_label.config(text=question)  # show question on screen
    answer_entry.delete(0, tk.END)        # clear previous answer
    feedback_label.config(text=f"Score: {score} | Lives: {lives}")  # update score/lives

# check the answer and go to next question
def nextquestion(choice):
    global score, lives, question_count
    userinput = answer_entry.get()  # what player typed
    try:
       user_answer = int(userinput)  
       correct_answer = int(answer)
       if user_answer == correct_answer:
           score += 1
           feedback_label.config(text=f"Correct! Score: {score} | Lives: {lives}")
       else:
           lives -= 1
           feedback_label.config(text=f"Wrong! Score: {score} | Lives: {lives}")
    except ValueError:  # handle if user types something that isn't a number
       lives -= 1
       feedback_label.config(text=f"Invalid input! Score: {score} | Lives: {lives}")
   
    question_count += 1  # keep track of how many questions we've done
        
    # stop the game if no lives or max questions reached
    if lives == 0 or question_count == total_questions:
            question_label.config(text=f"Game Over! Final Score: {score}")
            answer_entry.config(state="disabled")  # can't type anymore
            submit_btn.config(state="disabled")    # can't click submit
    else:
            question(choice)  # show next question
        
# start the game after selecting difficulty
def gamestart():
    global userchoice
    userchoice = entry_box.get()
    if userchoice not in ["1", "2", "3"]:  # only allow valid options
        result_label.config(text="Please enter 1, 2, or 3")
        return
    
    # hide the difficulty selection UI
    label1.pack_forget()
    label2.pack_forget()
    label3.pack_forget()
    entry_box.pack_forget()
    start_btn.pack_forget()
    result_label.pack_forget()
    
    # show quiz UI
    question_label.pack(pady=20)
    answer_entry.pack(pady=10)
    submit_btn.pack(pady=10)
    feedback_label.pack(pady=10)   
    question(userchoice)  # show first question
    
root = tk.Tk()
root.title("Exercise One - QUIZ")
root.geometry("600x600")

# difficulty labels
label1 = tk.Label(root, text = "1 : EASY", font = ("Arial", 18, "bold"), fg = "#5ae87c", justify = "center")
label1.pack(padx = 10, pady = 20)

label2 = tk.Label(root, text = "2 : MEDIUM", font = ("Arial", 18, "bold"), fg = "#d0d932", justify = "center")
label2.pack(padx = 10, pady = 20)

label3 = tk.Label(root, text = "3 : HARD", font = ("Arial", 18, "bold"), fg = "#d93a32", justify = "center")
label3.pack(padx = 10, pady = 20)

entry_box = tk.Entry(root, width = 30, justify = "center")
entry_box.pack(padx = 10, pady = 20)

start_btn = tk.Button(root, text="Start", command=gamestart)
start_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# quiz elements (hidden at start)
question_label = tk.Label(root, text="", font=("Arial", 18))
answer_entry = tk.Entry(root, width=10, justify="center")
feedback_label = tk.Label(root, text="", font=("Arial", 14))

submit_btn = tk.Button(root, text="Submit", command=lambda: nextquestion(userchoice))

root.mainloop()
