import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
from utils import calculate_grade
import csv

class ExamCRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Exam Management System")
        self.root.geometry("900x700")
        self.root.configure(bg="#f8f9fa")
        self.root.resizable(True, True)
        
        # Set window icon and styling
        try:
            self.root.iconbitmap(default="")
        except:
            pass
        
        self.conn, self.cursor = connect_db()
        self.cursor.execute("INSERT OR IGNORE INTO users VALUES('admin','1234')")
        self.conn.commit()
        
        self.current_user = None
        self.setup_login_ui()
    
    def setup_login_ui(self):
        self.clear_window()
        
        # Background gradient effect
        canvas = tk.Canvas(self.root, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Create gradient background
        for i in range(600):
            color = f"#{int(102 + (118-102) * i/600):02x}{int(126 + (75-126) * i/600):02x}{int(234 + (162-234) * i/600):02x}"
            canvas.create_line(0, i, 800, i, fill=color, width=1)
        
        # Login Frame with modern styling
        login_frame = tk.Frame(canvas, bg="white", padx=50, pady=50, relief="flat", bd=0)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Add shadow effect
        shadow_frame = tk.Frame(canvas, bg="#d0d0d0", padx=52, pady=52)
        shadow_frame.place(relx=0.502, rely=0.502, anchor="center")
        login_frame.lift()
        
        # Title with emoji
        title_label = tk.Label(login_frame, text="🎓 Student Exam Management", 
                              font=("Segoe UI", 24, "bold"), bg="white", fg="#2c3e50")
        title_label.pack(pady=(0, 30))
        
        # Username section
        user_frame = tk.Frame(login_frame, bg="white")
        user_frame.pack(pady=10, fill="x")
        
        tk.Label(user_frame, text="👤 Username:", font=("Segoe UI", 14, "bold"), 
                bg="white", fg="#34495e").pack(anchor="w", pady=(0, 5))
        
        self.username_entry = tk.Entry(user_frame, font=("Segoe UI", 14), width=25, 
                                      relief="flat", bd=10, bg="#f8f9fa", 
                                      highlightthickness=2, highlightcolor="#667eea")
        self.username_entry.pack(pady=(0, 10), ipady=8)
        
        # Buttons with modern styling
        btn_frame = tk.Frame(login_frame, bg="white")
        btn_frame.pack(pady=20, fill="x")
        
        login_btn = tk.Button(btn_frame, text="Sign In", command=self.login, 
                             bg="#667eea", fg="white", font=("Segoe UI", 12, "bold"), 
                             width=22, relief="flat", bd=0, cursor="hand2")
        login_btn.pack(pady=5, ipady=10)
        
        # Divider
        tk.Label(btn_frame, text="or", font=("Segoe UI", 10), bg="white", fg="#6c757d").pack(pady=10)
        
        register_btn = tk.Button(btn_frame, text="Create Account", command=self.register, 
                                bg="#28a745", fg="white", font=("Segoe UI", 12, "bold"), 
                                width=22, relief="flat", bd=0, cursor="hand2")
        register_btn.pack(pady=5, ipady=10)
        
        # Hover effects
        def on_enter_login(e): login_btn.config(bg="#5a6fd8")
        def on_leave_login(e): login_btn.config(bg="#667eea")
        def on_enter_register(e): register_btn.config(bg="#218838")
        def on_leave_register(e): register_btn.config(bg="#28a745")
        
        login_btn.bind("<Enter>", on_enter_login)
        login_btn.bind("<Leave>", on_leave_login)
        register_btn.bind("<Enter>", on_enter_register)
        register_btn.bind("<Leave>", on_leave_register)
        
        # Focus on username entry
        self.username_entry.focus_set()
        
        # Enter key binding
        self.username_entry.bind("<Return>", lambda e: self.login())
    
    def login(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter username")
            return
        
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if self.cursor.fetchone():
            self.current_user = username
            self.setup_main_ui()
        else:
            messagebox.showerror("Error", "User not found")
    
    def register(self):
        username = self.username_entry.get()
        if not username:
            messagebox.showerror("Error", "Please enter username")
            return
        
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        if self.cursor.fetchone():
            messagebox.showerror("Error", "Username already exists")
        else:
            self.cursor.execute("INSERT INTO users VALUES(?, '')", (username,))
            self.conn.commit()
            messagebox.showinfo("Success", "Registration successful! Please login.")
    
    def setup_main_ui(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg="#34495e", height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        tk.Label(header, text=f"Welcome, {self.current_user}", font=("Arial", 16, "bold"), bg="#34495e", fg="white").pack(side="left", padx=20, pady=15)
        tk.Button(header, text="Logout", command=self.logout, bg="#e74c3c", fg="white", font=("Arial", 10)).pack(side="right", padx=20, pady=15)
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg="white", width=300)
        left_panel.pack(side="left", fill="y", padx=(0, 10))
        left_panel.pack_propagate(False)
        
        tk.Label(left_panel, text="Student Management", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=20)
        
        # Add Student Section
        add_frame = tk.LabelFrame(left_panel, text="Add Student", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
        add_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(add_frame, text="Roll No:", bg="white").pack(anchor="w")
        self.roll_entry = tk.Entry(add_frame, width=25)
        self.roll_entry.pack(pady=2)
        
        tk.Label(add_frame, text="Name:", bg="white").pack(anchor="w")
        self.name_entry = tk.Entry(add_frame, width=25)
        self.name_entry.pack(pady=2)
        
        tk.Label(add_frame, text="Marks:", bg="white").pack(anchor="w")
        self.marks_entry = tk.Entry(add_frame, width=25)
        self.marks_entry.pack(pady=2)
        
        tk.Button(add_frame, text="Add Student", command=self.add_student, bg="#27ae60", fg="white", width=20).pack(pady=10)
        
        # Update/Delete Section
        update_frame = tk.LabelFrame(left_panel, text="Update/Delete", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
        update_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(update_frame, text="Roll No:", bg="white").pack(anchor="w")
        self.update_roll_entry = tk.Entry(update_frame, width=25)
        self.update_roll_entry.pack(pady=2)
        
        tk.Label(update_frame, text="New Marks:", bg="white").pack(anchor="w")
        self.update_marks_entry = tk.Entry(update_frame, width=25)
        self.update_marks_entry.pack(pady=2)
        
        tk.Button(update_frame, text="Update", command=self.update_student, bg="#f39c12", fg="white", width=20).pack(pady=5)
        tk.Button(update_frame, text="Delete", command=self.delete_student, bg="#e74c3c", fg="white", width=20).pack(pady=2)
        
        # Export Button
        tk.Button(left_panel, text="Export to CSV", command=self.export_csv, bg="#9b59b6", fg="white", font=("Arial", 12), width=20).pack(pady=20)
        
        # Right panel - Student List
        right_panel = tk.Frame(main_frame, bg="white")
        right_panel.pack(side="right", fill="both", expand=True)
        
        tk.Label(right_panel, text="Student Records", font=("Arial", 16, "bold"), bg="white", fg="#2c3e50").pack(pady=20)
        
        # Treeview for student data
        columns = ("Roll No", "Name", "Marks", "Grade")
        self.tree = ttk.Treeview(right_panel, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
        
        scrollbar = ttk.Scrollbar(right_panel, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True, padx=20, pady=20)
        scrollbar.pack(side="right", fill="y", pady=20)
        
        tk.Button(right_panel, text="Refresh", command=self.refresh_data, bg="#3498db", fg="white").pack(pady=10)
        
        self.refresh_data()
    
    def add_student(self):
        try:
            roll = int(self.roll_entry.get())
            name = self.name_entry.get()
            marks = int(self.marks_entry.get())
            
            if not name:
                messagebox.showerror("Error", "Please enter student name")
                return
            
            grade = calculate_grade(marks)
            self.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (roll, name, marks, grade))
            self.conn.commit()
            
            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_entries()
            self.refresh_data()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for Roll No and Marks")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add student: {str(e)}")
    
    def update_student(self):
        try:
            roll = int(self.update_roll_entry.get())
            marks = int(self.update_marks_entry.get())
            grade = calculate_grade(marks)
            
            self.cursor.execute("UPDATE students SET marks=?, grade=? WHERE roll_no=?", (marks, grade, roll))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student updated successfully!")
                self.update_roll_entry.delete(0, tk.END)
                self.update_marks_entry.delete(0, tk.END)
                self.refresh_data()
            else:
                messagebox.showerror("Error", "Student not found")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
    
    def delete_student(self):
        try:
            roll = int(self.update_roll_entry.get())
            
            if messagebox.askyesno("Confirm", f"Delete student with Roll No {roll}?"):
                self.cursor.execute("DELETE FROM students WHERE roll_no=?", (roll,))
                self.conn.commit()
                
                if self.cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Student deleted successfully!")
                    self.update_roll_entry.delete(0, tk.END)
                    self.refresh_data()
                else:
                    messagebox.showerror("Error", "Student not found")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid Roll No")
    
    def export_csv(self):
        try:
            self.cursor.execute("SELECT * FROM students")
            data = self.cursor.fetchall()
            
            with open("students.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Roll No", "Name", "Marks", "Grade"])
                writer.writerows(data)
            
            messagebox.showinfo("Success", "Data exported to students.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")
    
    def refresh_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.cursor.execute("SELECT * FROM students")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)
    
    def clear_entries(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def logout(self):
        self.current_user = None
        self.setup_login_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExamCRUDApp(root)
    root.mainloop()