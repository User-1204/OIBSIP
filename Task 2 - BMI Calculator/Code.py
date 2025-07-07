import tkinter as tk # GUI library
from tkinter import messagebox # For pop-up messages
import json # For data storage
import csv # For exporting data to CSV
from datetime import datetime # For timestamps
import os # For file handling

BACKGROUND_COLOR = "#FDE6F2"        
FIELD_BG = "#FFFFFF"                
TEXT_DARK = "#2C3E50"               
RESULT_COLOR = "#3D3C58"            
TITLE_FONT = ("Poppins", 20, "bold")
LABEL_FONT = ("Poppins", 12, "bold")
ENTRY_FONT = ("Poppins", 11)
RESULT_FONT = ("Poppins", 11, "italic")
BUTTON_FONT = ("Poppins", 11, "bold")
FOOTER_FONT = ("Poppins", 9)
DATA_FILE = "bmi_data.json"

# define the data file path
def load_data():
    if os.path.exists(DATA_FILE):   # Check if the data file exists
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):  # Save data to the JSON file
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Function to categorize BMI and provide advice
# The function returns a tuple with the category and advice message
def categorize_bmi(bmi):
    if bmi < 18.5:
        return ("Underweight", "Consider a  proper nutritious diet and consult a professional.")
    elif bmi < 24.9:
        return ("Normal weight", "Great job. Maintain your healthy habits.")
    elif bmi < 29.9:
        return ("Overweight", "Try regular exercise and mindful eating.")
    else:
        return ("Obese", "Consider seeking advice from a health professional.")

def calculate_bmi(event=None):  # Calculate BMI based on user input
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            messagebox.showwarning("Missing Name", "Please enter your name.")
            return
        if not (10 <= weight <= 300 and 0.5 <= height <= 2.5):
            raise ValueError

        bmi = weight / (height ** 2) # BMI formula: weight (kg) / (height (m) ** 2)
        category, advice = categorize_bmi(bmi)

        result_label.config(
            text=f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}\n\n{advice}"
        )

        data = load_data() # Load existing data
        timestamp = datetime.now().strftime("%b %d, %I:%M %p")
        entry = {
            "time": timestamp,
            "bmi": round(bmi, 2),
            "category": category,
            "weight": weight,
            "height": height
        }
        data.setdefault(name, []).append(entry)
        save_data(data)
        show_history(data[name])
        messagebox.showinfo("BMI Calculated", f"{name}, your BMI is {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight (10–300) and height (0.5–2.5).")

def show_history(entries):
    recent = entries[-5:]  # Get the last 5 entries
    lines = [f"{e['time']}: BMI {e['bmi']} ({e['category']})" for e in recent] # Format recent entries
    history_label.config(text="Recent Entries:\n" + "\n".join(lines))     

def export_to_csv():
    name = name_entry.get().strip()  
    if not name:
        messagebox.showwarning("Missing Name", "Please enter your name.")
        return

    data = load_data()
    if name not in data or not data[name]:
        messagebox.showinfo("No Data", f"No records found for {name}.")
        return

    filename = f"bmi_export_{name}.csv"   # Export filename
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date/Time", "Weight (kg)", "Height (m)", "BMI", "Category"])
        for e in data[name]:
            writer.writerow([e["time"], e["weight"], e["height"], e["bmi"], e["category"]])

    messagebox.showinfo("Export Complete", f"Exported to {filename}")

def reset_fields():  # Reset input fields and results
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    name_entry.focus()

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg=BACKGROUND_COLOR)
root.geometry("470x580")
root.resizable(False, False)

# Title
tk.Label(root, text="BMI Calculator", font=TITLE_FONT, bg=BACKGROUND_COLOR, fg=TEXT_DARK).pack(pady=(20, 10))

# Input Frame
input_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
input_frame.pack(pady=10)

# Name
tk.Label(input_frame, text="Name:", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=0, column=0, sticky="e", padx=12, pady=8)
name_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG, fg=TEXT_DARK, relief="solid", bd=1)
name_entry.grid(row=0, column=1, padx=12)
name_entry.bind("<Return>", lambda e: weight_entry.focus())

# Weight
tk.Label(input_frame, text="Weight (kg):", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=1, column=0, sticky="e", padx=12, pady=8)
weight_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG, fg=TEXT_DARK, relief="solid", bd=1)
weight_entry.grid(row=1, column=1, padx=12)
weight_entry.bind("<Return>", lambda e: height_entry.focus())

# Height
tk.Label(input_frame, text="Height (m):", font=LABEL_FONT, bg=BACKGROUND_COLOR, fg=TEXT_DARK).grid(row=2, column=0, sticky="e", padx=12, pady=8)
height_entry = tk.Entry(input_frame, font=ENTRY_FONT, bg=FIELD_BG, fg=TEXT_DARK, relief="solid", bd=1)
height_entry.grid(row=2, column=1, padx=12)
height_entry.bind("<Return>", calculate_bmi)

# Buttons
button_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi,
          font=BUTTON_FONT, bg="#AED9C8", activebackground="#AED9C8", width=14).pack(side="left", padx=10)

tk.Button(button_frame, text="Export to CSV", command=export_to_csv,
          font=BUTTON_FONT, bg="#AED9C8", activebackground="#AED9C8", width=14).pack(side="left", padx=10)

tk.Button(button_frame, text="Reset", command=reset_fields,
          font=BUTTON_FONT, bg="#AED9C8", activebackground="#AED9C8", width=10).pack(side="left", padx=10)

# Result Area
result_label = tk.Label(root, text="", font=RESULT_FONT, bg=BACKGROUND_COLOR, fg=RESULT_COLOR, justify="left", wraplength=420)
result_label.pack(pady=(10, 5))

# History Area
history_label = tk.Label(root, text="", font=FOOTER_FONT, bg=BACKGROUND_COLOR, fg="#7D8884", justify="left", wraplength=420)
history_label.pack(pady=(5, 15))

# Footer
tk.Label(root, text="Made by Sakshi | 2025", font=FOOTER_FONT, fg="#999999", bg=BACKGROUND_COLOR).pack(side="bottom", pady=10)

# Launch App
name_entry.focus()
root.mainloop()
