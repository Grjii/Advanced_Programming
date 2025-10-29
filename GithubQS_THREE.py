# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:59:55 2025

@author: grgej
"""

import tkinter as tk
import tkinter.ttk as ttk # For dropdown menu
from tkinter import messagebox # For sort button
from tkinter import simpledialog # For adding a new students record

with open("studentMarks.txt", "r") as file:
    read = file.readlines()  # Reads .txt file

# get student names for drop-down menu
names = []
for line in read:
    parts = line.strip().split(",")
    if len(parts) == 6:  # Splits a record after every 6 commas
        names.append(parts[1])  # Name is the second value

root = tk.Tk()
root.geometry("700x700")
root.configure(bg="#f0f0f0")
root.title("Student Manager | Exercise 3")

# Defining Functions.
def show_records():
    display.delete("1.0", tk.END) # Makes sure display box is empty
    for line in read:
        parts = line.strip().split(",")
        if len(parts) == 6:  # Divide entries into six parts
            student_id = parts[0]
            name = parts[1]
            coursework1 = int(parts[2])
            coursework2 = int(parts[3])
            coursework3 = int(parts[4])
            overall = int(parts[5])
            
            # Calculate grade
            if overall >= 70:
                grade = "A"
            elif overall >= 60:
                grade = "B"
            elif overall >= 50:
                grade = "C"
            elif overall >= 40:
                grade = "D"
            else:
                grade = "F"
            
            # Calculate total coursework
            total_coursework = coursework1 + coursework2 + coursework3
            
            # Insert formatted text
            display.insert(tk.END, f"Name: {name}\n")
            display.insert(tk.END, f"Number: {student_id}\n")
            display.insert(tk.END, f"Coursework Total: {total_coursework}\n")
            display.insert(tk.END, f"Exam Mark: {overall}\n")
            display.insert(tk.END, f"Overall Percentage: {overall}%\n")
            display.insert(tk.END, f"Grade: {grade}\n")
            display.insert(tk.END, "-"*40 + "\n")  # separator

def highest_score():
    display.delete("1.0", tk.END)
    
    highest_student = None  # Variable to store the highest students record
    highest_score_val = -1  # Loops through all the students scores and checks which one is the highest
    
    for line in read:
        parts = line.strip().split(",")
        if len(parts) == 6:
            overall = int(parts[5])  # Converts the sixth value in the list (overall score) into a integer
            if overall > highest_score_val:  # compares the current students overall score with the highest score and gets updated accordingly
                highest_score_val = overall
                highest_student = parts
    
    if highest_student:
        student_id = highest_student[0]
        name = highest_student[1] 
        coursework1 = int(highest_student[2])
        coursework2 = int(highest_student[3])
        coursework3 = int(highest_student[4])
        overall = int(highest_student[5])
        
        # Calculate grade
        if overall >= 70:
            grade = "A"
        elif overall >= 60:
            grade = "B"
        elif overall >= 50:
            grade = "C"
        elif overall >= 40:
            grade = "D"
        else:
            grade = "F"
        
        total_coursework = coursework1 + coursework2 + coursework3
        
        # Display formatted info
        display.insert(tk.END, f"Name: {name}\n")
        display.insert(tk.END, f"Number: {student_id}\n")
        display.insert(tk.END, f"Coursework Total: {total_coursework}\n")
        display.insert(tk.END, f"Exam Mark: {overall}\n")
        display.insert(tk.END, f"Overall Percentage: {overall}%\n")
        display.insert(tk.END, f"Grade: {grade}\n")
        display.insert(tk.END, "-"*40 + "\n")

def lowest_score():
    display.delete("1.0", tk.END)
    
    lowest_student = None  # Variable to store the lowest student's record
    lowest_score_val = 1000  # Starts high so first student will replace it
    
    for line in read:
        parts = line.strip().split(",")
        if len(parts) == 6:
            overall = int(parts[5])
            if overall < lowest_score_val:  # find the lowest score
                lowest_score_val = overall
                lowest_student = parts
                
    if lowest_student:
        student_id = lowest_student[0]
        name = lowest_student[1]
        coursework1 = int(lowest_student[2])
        coursework2 = int(lowest_student[3])
        coursework3 = int(lowest_student[4])
        overall = int(lowest_student[5])
        
        # Calculate grade
        if overall >= 70:
            grade = "A"
        elif overall >= 60:
            grade = "B"
        elif overall >= 50:
            grade = "C"
        elif overall >= 40:
            grade = "D"
        else:
            grade = "F"
            
        total_coursework = coursework1 + coursework2 + coursework3
        
        # Display formatted info
        display.insert(tk.END, f"Name: {name}\n")
        display.insert(tk.END, f"Number: {student_id}\n")
        display.insert(tk.END, f"Coursework Total: {total_coursework}\n")
        display.insert(tk.END, f"Exam Mark: {overall}\n")
        display.insert(tk.END, f"Overall Percentage: {overall}%\n")
        display.insert(tk.END, f"Grade: {grade}\n")
        display.insert(tk.END, "-"*40 + "\n")
        
def sort_records():
    display.delete("1.0", tk.END)
    
    ascending = messagebox.askyesno("Sort", "Sort ascending? (Yes = Ascending, No = Descending)")
        
    students = [] # Stores all the student records 
    for line in read:
        parts = line.strip().split(",")
        if len(parts) == 6:
            students.append(parts) # Adds records to the list
    
    students.sort(key=lambda x: int(x[5]), reverse=not ascending) # Sorts the list accordingly
    
    # Display sorted students
    for parts in students:
        student_id = parts[0]
        name = parts[1]
        coursework1 = int(parts[2])
        coursework2 = int(parts[3])
        coursework3 = int(parts[4])
        overall = int(parts[5])
        
        if overall >= 70:
            grade = "A"
        elif overall >= 60:
            grade = "B"
        elif overall >= 50:
            grade = "C"
        elif overall >= 40:
            grade = "D"
        else:
            grade = "F"
        
        total_coursework = coursework1 + coursework2 + coursework3
        
        display.insert(tk.END, f"Name: {name}\n")
        display.insert(tk.END, f"Number: {student_id}\n")
        display.insert(tk.END, f"Coursework Total: {total_coursework}\n")
        display.insert(tk.END, f"Exam Mark: {overall}\n")
        display.insert(tk.END, f"Overall Percentage: {overall}%\n")
        display.insert(tk.END, f"Grade: {grade}\n")
        display.insert(tk.END, "-"*40 + "\n")
        
def add_student():
    # Ask user for each piece of information in a popup
    new_id = simpledialog.askstring("Student ID", "Enter student ID:")
    if new_id is None:
        return  # user canceled
    
    new_name = simpledialog.askstring("Name", "Enter student name:")
    if new_name is None:
        return
    
    cw1 = simpledialog.askinteger("Coursework 1", "Enter Coursework 1 mark:")
    if cw1 is None:
        return
    
    cw2 = simpledialog.askinteger("Coursework 2", "Enter Coursework 2 mark:")
    if cw2 is None:
        return
    
    cw3 = simpledialog.askinteger("Coursework 3", "Enter Coursework 3 mark:")
    if cw3 is None:
        return
    
    overall = simpledialog.askinteger("Overall", "Enter Overall mark:")
    if overall is None:
        return
    
    # Save to file
    with open("studentMarks.txt", "a") as file:
        file.write(f"{new_id},{new_name},{cw1},{cw2},{cw3},{overall}\n")
    
    # Update dropdown names
    names.append(new_name)
    entry['values'] = names
    
    messagebox.showinfo("Success", "Student added!")
    
def delete_student():

    delete_id = simpledialog.askstring("Delete Student", "Enter the ID of the record to delete:") # Ask for student ID using a popup
    
    if delete_id:
        found = False
        for line in read:
            parts = line.strip().split(",")
            if parts[0] == delete_id:
                read.remove(line)  # remove from the list
                found = True
                break
        
        if found:
            # Update the file
            with open("studentMarks.txt", "w") as file: # W will overwrite the file with whatevers written inside that block
                file.writelines(read)
            messagebox.showinfo("Deleted", f"Student ID {delete_id} has been deleted.")
        else:
            messagebox.showerror("Not Found", f"No student found with ID {delete_id}")
            
def update_record():
    # Create a popup window
    popup = tk.Toplevel()
    popup.title("Update Student Record")
    popup.geometry("300x250")
    
    tk.Label(popup, text="Select Student:").pack(pady=10)
    
    # Dropdown of existing student names
    name_var = tk.StringVar()
    combo = ttk.Combobox(popup, values=names, textvariable=name_var)
    combo.pack(pady=10)
    combo.current(0)  # default selection
    
    def submit():
        select_name = name_var.get()
        popup.destroy()  # close the popup
        
        # Find the student in memory
        for i, line in enumerate(read):
            parts = line.strip().split(",")
            if len(parts) == 6 and parts[1] == select_name:
                # Ask for new values, pre-filled with current ones
                new_id = simpledialog.askstring("Student ID", "Enter student ID:", initialvalue=parts[0])
                if new_id is None: return

                new_name = simpledialog.askstring("Name", "Enter student name:", initialvalue=parts[1])
                if new_name is None: return

                new_cw1 = simpledialog.askinteger("Coursework 1", "Enter Coursework 1 mark:", initialvalue=int(parts[2]))
                if new_cw1 is None: return

                new_cw2 = simpledialog.askinteger("Coursework 2", "Enter Coursework 2 mark:", initialvalue=int(parts[3]))
                if new_cw2 is None: return

                new_cw3 = simpledialog.askinteger("Coursework 3", "Enter Coursework 3 mark:", initialvalue=int(parts[4]))
                if new_cw3 is None: return

                new_overall = simpledialog.askinteger("Overall", "Enter Overall mark:", initialvalue=int(parts[5]))
                if new_overall is None: return

                # Update in memory
                read[i] = f"{new_id},{new_name},{new_cw1},{new_cw2},{new_cw3},{new_overall}\n"

                # Save to file
                with open("studentMarks.txt", "w") as file:
                    file.writelines(read)

                # Update dropdown if name changed
                if new_name != select_name:
                    names[i] = new_name
                    entry['values'] = names

                messagebox.showinfo("Updated", f"Student {new_name} has been updated!")
                return
        
        messagebox.showerror("Not Found", f"No student found with name {select_name}")

    tk.Button(popup, text="Submit", command=submit).pack(pady=20)
    
def indiv_record():
    selected_name = entry.get()  # get selected student from dropdown
    display.delete("1.0", tk.END)

    for line in read:
       parts = line.strip().split(",")
       if len(parts) == 6 and parts[1] == selected_name:
           student_id = parts[0]
           coursework1 = int(parts[2])
           coursework2 = int(parts[3])
           coursework3 = int(parts[4])
           overall = int(parts[5])

           # Calculate grade
           if overall >= 70:
               grade = "A"
           elif overall >= 60:
               grade = "B"
           elif overall >= 50:
               grade = "C"
           elif overall >= 40:
               grade = "D"
           else:
               grade = "F"

           total_coursework = coursework1 + coursework2 + coursework3

           # Display formatted info
           display.insert(tk.END, f"Name: {selected_name}\n")
           display.insert(tk.END, f"Number: {student_id}\n")
           display.insert(tk.END, f"Coursework Total: {total_coursework}\n")
           display.insert(tk.END, f"Exam Mark: {overall}\n")
           display.insert(tk.END, f"Overall Percentage: {overall}%\n")
           display.insert(tk.END, f"Grade: {grade}\n")
           display.insert(tk.END, "-"*40 + "\n")
           return

    messagebox.showerror("Not Found", f"No record found for {selected_name}")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

label = tk.Label(root, text="Student Manager", font=("Arial", 18, "bold"), bg="#f0f0f0")
label.grid(row=0, column=1, pady=25)

allrecords = tk.Button(root, text="View All Student Records", width=20, command=show_records)
allrecords.grid(row=1, column=0, padx=10, pady=10)

highest = tk.Button(root, text="Show Highest Score", width=20, command=highest_score)
highest.grid(row=1, column=1, padx=10, pady=10)

lowest = tk.Button(root, text="Show Lowest Score", width=20, command=lowest_score)
lowest.grid(row=1, column=2, padx=10, pady=10)

sort = tk.Button(root, text="Sort", width=20, command = sort_records)
sort.grid(row=2, column=0, padx=10, pady=10)

add = tk.Button(root, text="Add Student Record", width=20, command = add_student)
add.grid(row=2, column=1, padx=10, pady=10)

delete = tk.Button(root, text="Delete student record", width=20, command = delete_student)
delete.grid(row=2, column=2, padx=10, pady=10)

update = tk.Button(root, text = "Update", width = 20, command = update_record)
update.grid(row = 3, column = 1, padx = 10, pady = 10)

labelfind = tk.Label(root, text="View Individual Student Record:", font=("Arial", 10), bg="#f0f0f0")
labelfind.grid(row=4, column=0, padx=10, pady=20)

entry = ttk.Combobox(root, values=names, width=27)  # Dropdown menu
entry.grid(row=4, column=1, padx=10, pady=20)

display = tk.Text(root, width=55, height=12)
display.grid(row=5, column=0, padx=10, pady=10, columnspan=3)

view = tk.Button(root, text="View Record", command = indiv_record)
view.grid(row=4, column=2, padx=10, pady=20)

root.mainloop()
