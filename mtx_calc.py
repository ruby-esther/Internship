import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox

# === GUI Setup ===
root = tk.Tk()
root.title("Matrix Calculator")
root.geometry("750x500")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Consolas", 12))

# === Input Area ===
input_frame = tk.Frame(root, bg="#e1e1e1", padx=10, pady=10)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Matrix A (comma-separated rows)", bg="#e1e1e1").grid(row=0, column=0, padx=5, sticky="w")
matrix_a_entry = tk.Text(input_frame, height=4, width=30, font=("Consolas", 12))
matrix_a_entry.grid(row=1, column=0, padx=5)

tk.Label(input_frame, text="Matrix B (comma-separated rows)", bg="#e1e1e1").grid(row=0, column=1, padx=5, sticky="w")
matrix_b_entry = tk.Text(input_frame, height=4, width=30, font=("Consolas", 12))
matrix_b_entry.grid(row=1, column=1, padx=5)

# === Output Area ===
output_box = tk.Text(root, height=10, width=90, font=("Consolas", 12), bg="#ffffff")
output_box.pack(pady=10)

# === Matrix Parser ===
def parse_matrix(textbox):
    try:
        raw = textbox.get("1.0", "end").strip().split('\n')
        matrix = [list(map(float, row.strip().split())) for row in raw]
        return np.array(matrix)
    except:
        messagebox.showerror("Invalid Input", "Please check the matrix format.")
        return None

# === Operations ===
def display_result(result, op_name):
    output_box.insert(tk.END, f"\n--- {op_name} ---\n{result}\n")

def add_matrices():
    A, B = parse_matrix(matrix_a_entry), parse_matrix(matrix_b_entry)
    if A is not None and B is not None:
        if A.shape == B.shape:
            display_result(A + B, "A + B")
        else:
            messagebox.showerror("Shape Error", "Matrices must have the same shape.")

def subtract_matrices():
    A, B = parse_matrix(matrix_a_entry), parse_matrix(matrix_b_entry)
    if A is not None and B is not None:
        if A.shape == B.shape:
            display_result(A - B, "A - B")
        else:
            messagebox.showerror("Shape Error", "Matrices must have the same shape.")

def multiply_matrices():
    A, B = parse_matrix(matrix_a_entry), parse_matrix(matrix_b_entry)
    if A is not None and B is not None:
        try:
            display_result(np.dot(A, B), "A × B")
        except:
            messagebox.showerror("Shape Error", "Matrix A's columns must match Matrix B's rows.")

def transpose_matrix():
    A = parse_matrix(matrix_a_entry)
    if A is not None:
        display_result(A.T, "Transpose of A")

def determinant_matrix():
    A = parse_matrix(matrix_a_entry)
    if A is not None and A.shape[0] == A.shape[1]:
        display_result(round(np.linalg.det(A), 3), "Determinant of A")
    else:
        messagebox.showerror("Square Matrix Only", "Determinant can only be calculated for square matrices.")

def clear_all():
    matrix_a_entry.delete("1.0", tk.END)
    matrix_b_entry.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

# === Buttons ===
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack()

ttk.Button(btn_frame, text="A + B", command=add_matrices).grid(row=0, column=0, padx=8, pady=5)
ttk.Button(btn_frame, text="A - B", command=subtract_matrices).grid(row=0, column=1, padx=8)
ttk.Button(btn_frame, text="A × B", command=multiply_matrices).grid(row=0, column=2, padx=8)
ttk.Button(btn_frame, text="Transpose A", command=transpose_matrix).grid(row=1, column=0, padx=8, pady=5)
ttk.Button(btn_frame, text="Determinant A", command=determinant_matrix).grid(row=1, column=1, padx=8)
ttk.Button(btn_frame, text="Clear All", command=clear_all).grid(row=1, column=2, padx=8)

# === Start the App ===
root.mainloop()
