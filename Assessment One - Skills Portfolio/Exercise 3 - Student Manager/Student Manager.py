import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

FILE_PATH = 'studentMarks.txt'

def load_students():
    students = []
    with open(FILE_PATH, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            parts = line.strip().split(',')
            code = parts[0]
            name = parts[1]
            c1, c2, c3 = map(int, parts[2:5])
            exam = int(parts[5])
            students.append({
                'code': code,
                'name': name,
                'coursework': [c1, c2, c3],
                'exam': exam
            })
    return students

def save_students(students):
    with open(FILE_PATH, 'w') as f:
        f.write(str(len(students)) + "\n")
        for s in students:
            f.write(f"{s['code']},{s['name']},{s['coursework'][0]},{s['coursework'][1]},{s['coursework'][2]},{s['exam']}\n")

def compute_stats(student):
    coursework_total = sum(student['coursework'])
    exam = student['exam']
    overall = (coursework_total + exam) / 160 * 100

    if overall >= 70:
        grade = 'A'
    elif overall >= 60:
        grade = 'B'
    elif overall >= 50:
        grade = 'C'
    elif overall >= 40:
        grade = 'D'
    else:
        grade = 'F'

    return coursework_total, exam, overall, grade

def view_all_students():
    students = load_students()
    output = ''
    total_percentage = 0

    for s in students:
        cw, exam, overall, grade = compute_stats(s)
        total_percentage += overall
        output += (
            f"Name: {s['name']}\n"
            f"Student Number: {s['code']}\n"
            f"Coursework Total: {cw}\n"
            f"Exam Mark: {exam}\n"
            f"Overall %: {overall:.2f}%\n"
            f"Grade: {grade}\n"
            "-----------------------------------------\n"
        )

    avg = total_percentage / len(students)
    output += f"\nTotal Students: {len(students)}\nAverage Percentage: {avg:.2f}%"

    update_output(output)

def view_individual():
    students = load_students()
    code = simpledialog.askstring("Find Student", "Enter student code:")

    for s in students:
        if s['code'] == code:
            cw, exam, overall, grade = compute_stats(s)
            output = (
                f"Name: {s['name']}\n"
                f"Student Number: {s['code']}\n"
                f"Coursework Total: {cw}\n"
                f"Exam Mark: {exam}\n"
                f"Overall %: {overall:.2f}%\n"
                f"Grade: {grade}"
            )
            update_output(output)
            return
    messagebox.showerror("Error", "Student not found.")

def show_highest():
    students = load_students()
    best = max(students, key=lambda s: compute_stats(s)[2])
    cw, exam, overall, grade = compute_stats(best)

    output = (
        f"📌 HIGHEST MARK\n"
        f"-----------------------------------------\n"
        f"Name: {best['name']}\n"
        f"Student Number: {best['code']}\n"
        f"Coursework Total: {cw}\n"
        f"Exam Mark: {exam}\n"
        f"Overall %: {overall:.2f}%\n"
        f"Grade: {grade}"
    )

    update_output(output)

def show_lowest():
    students = load_students()
    worst = min(students, key=lambda s: compute_stats(s)[2])
    cw, exam, overall, grade = compute_stats(worst)

    output = (
        f"📌 LOWEST MARK\n"
        f"-----------------------------------------\n"
        f"Name: {worst['name']}\n"
        f"Student Number: {worst['code']}\n"
        f"Coursework Total: {cw}\n"
        f"Exam Mark: {exam}\n"
        f"Overall %: {overall:.2f}%\n"
        f"Grade: {grade}"
    )

    update_output(output)

def sort_students():
    students = load_students()
    order = messagebox.askquestion("Sort", "Sort ascending? (No = descending)")

    students.sort(key=lambda s: compute_stats(s)[2], reverse=(order == 'no'))

    output = "📌 SORTED STUDENTS\n-----------------------------------------\n"
    for s in students:
        _, _, overall, _ = compute_stats(s)
        output += f"{s['name']} ({s['code']}) - {overall:.2f}%\n"

    update_output(output)

def add_student():
    students = load_students()

    code = simpledialog.askstring("New Student", "Enter student code:")
    name = simpledialog.askstring("New Student", "Enter student name:")
    c1 = int(simpledialog.askstring("Coursework", "Enter mark 1:"))
    c2 = int(simpledialog.askstring("Coursework", "Enter mark 2:"))
    c3 = int(simpledialog.askstring("Coursework", "Enter mark 3:"))
    exam = int(simpledialog.askstring("Exam", "Enter exam mark:"))

    students.append({
        'code': code,
        'name': name,
        'coursework': [c1, c2, c3],
        'exam': exam
    })

    save_students(students)
    messagebox.showinfo("Success", "Student added.")

def delete_student():
    students = load_students()
    code = simpledialog.askstring("Delete", "Enter student code to delete:")

    new_list = [s for s in students if s['code'] != code]

    if len(new_list) == len(students):
        messagebox.showerror("Error", "Student not found.")
    else:
        save_students(new_list)
        messagebox.showinfo("Deleted", "Student removed.")

def update_student():
    students = load_students()
    code = simpledialog.askstring("Update", "Enter student code to update:")

    for s in students:
        if s['code'] == code:
            field = simpledialog.askstring("Update", "Update name/coursework/exam?")

            if field.lower() == 'name':
                s['name'] = simpledialog.askstring("Name", "Enter new name:")
            elif field.lower() == 'coursework':
                s['coursework'][0] = int(simpledialog.askstring("CW1", "Enter new mark 1:"))
                s['coursework'][1] = int(simpledialog.askstring("CW2", "Enter new mark 2:"))
                s['coursework'][2] = int(simpledialog.askstring("CW3", "Enter new mark 3:"))
            elif field.lower() == 'exam':
                s['exam'] = int(simpledialog.askstring("Exam", "Enter new exam mark:"))
            else:
                messagebox.showerror("Error", "Invalid field.")
                return

            save_students(students)
            messagebox.showinfo("Updated", "Record updated.")
            return

    messagebox.showerror("Error", "Student not found.")

def update_output(text):
    text_box.config(state="normal")  
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, text)
    text_box.config(state="disabled")

# Main window
root = tk.Tk()
root.title("📚 Student Manager")
root.geometry("900x600")
root.config(bg="#6a0dad")  # Purple background

title = tk.Label(root, text="Student Records Manager", font=("Arial", 20, "bold"), bg="#6a0dad", fg="white")
title.pack(pady=10)

main_frame = tk.Frame(root, bg="#6a0dad")
main_frame.pack(fill=tk.BOTH, expand=True, padx=10)

button_frame = tk.Frame(main_frame, bg="#6a0dad")
button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=8, background="#FFBBFD", foreground="black")
style.map("TButton",
          background=[("active", "#A077A0")])  # Darker lavender on hover

buttons = [
    ("View All Records", view_all_students),
    ("View Individual", view_individual),
    ("Highest Mark", show_highest),
    ("Lowest Mark", show_lowest),
    ("Sort Records", sort_students),
    ("Add Record", add_student),
    ("Delete Record", delete_student),
    ("Update Record", update_student)
]

for text, cmd in buttons:
    ttk.Button(button_frame, text=text, width=22, command=cmd).pack(pady=6)

output_frame = tk.Frame(main_frame, bg="#6a0dad")
output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_box = tk.Text(
    output_frame,
    wrap=tk.WORD,
    font=("Consolas", 12),
    yscrollcommand=scrollbar.set,
    bg="#E6E6FA",  # Lavender background
    fg="black"     # Text in black
)
text_box.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=text_box.yview)

root.mainloop()
