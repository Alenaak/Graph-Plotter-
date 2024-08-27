#!/usr/bin/env python
# coding: utf-8

# In[1]:
import tkinter as tk
from tkinter import ttk
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PiecewiseFunctionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Piecewise Function Plotter")

        # Create a scrollable frame
        self.canvas = tk.Canvas(root)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Initialize lists to hold widgets
        self.function_entries = []
        self.interval_start_entries = []
        self.interval_end_entries = []

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.scrollable_frame, text="Number of Functions:").grid(column=0, row=0, padx=10, pady=10)
        self.num_functions_entry = ttk.Entry(self.scrollable_frame)
        self.num_functions_entry.grid(column=1, row=0, padx=10, pady=10)
        
        self.add_functions_button = ttk.Button(self.scrollable_frame, text="Set Number of Functions", command=self.add_function_entries)
        self.add_functions_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        
        self.plot_button = ttk.Button(self.scrollable_frame, text="Plot", command=self.plot_function)
        self.plot_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas_plot = FigureCanvasTkAgg(self.figure, master=self.scrollable_frame)
        self.canvas_plot.get_tk_widget().grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def add_function_entries(self):
        # Clear existing entries if they exist
        for entry in self.function_entries + self.interval_start_entries + self.interval_end_entries:
            entry.destroy()

        self.function_entries.clear()
        self.interval_start_entries.clear()
        self.interval_end_entries.clear()
        
        try:
            num_functions = int(self.num_functions_entry.get())
        except ValueError:
            num_functions = 0
        
        for i in range(num_functions):
            ttk.Label(self.scrollable_frame, text=f"Function {i+1} (e.g., x, π - x):").grid(column=0, row=4+i*3, padx=10, pady=10)
            func_entry = ttk.Entry(self.scrollable_frame)
            func_entry.grid(column=1, row=4+i*3, padx=10, pady=10)
            self.function_entries.append(func_entry)

            ttk.Label(self.scrollable_frame, text=f"Interval {i+1} Start (e.g., -π):").grid(column=0, row=5+i*3, padx=10, pady=10)
            interval_start_entry = ttk.Entry(self.scrollable_frame)
            interval_start_entry.grid(column=1, row=5+i*3, padx=10, pady=10)
            self.interval_start_entries.append(interval_start_entry)

            ttk.Label(self.scrollable_frame, text=f"Interval {i+1} End (e.g., 0):").grid(column=0, row=6+i*3, padx=10, pady=10)
            interval_end_entry = ttk.Entry(self.scrollable_frame)
            interval_end_entry.grid(column=1, row=6+i*3, padx=10, pady=10)
            self.interval_end_entries.append(interval_end_entry)

    def parse_function(self, expr_str):
        x = sp.symbols('x')
        expr_str = expr_str.replace("π", "pi")
        expr = sp.sympify(expr_str)
        func = sp.lambdify(x, expr, modules=['numpy'])

        if expr.is_constant():
            return lambda x_val: np.full_like(x_val, float(expr))
        
        return func

    def parse_interval(self, interval_str):
        return float(sp.sympify(interval_str.replace("π", "pi")))

    def plot_function(self):
        self.ax.clear()
        
        num_functions = len(self.function_entries)
        functions = []
        intervals = []
        colors = plt.cm.get_cmap("tab10", num_functions)  # Get a colormap with num_functions distinct colors

        for i in range(num_functions):
            func_str = self.function_entries[i].get()
            interval_start = self.parse_interval(self.interval_start_entries[i].get())
            interval_end = self.parse_interval(self.interval_end_entries[i].get())
            
            functions.append((self.parse_function(func_str), interval_start, interval_end))
            intervals.append((interval_start, interval_end))

        ymin, ymax = float('inf'), float('-inf')
        period = intervals[-1][1] - intervals[0][0]

        for i, (func, start, end) in enumerate(functions):
            x = np.linspace(start, end, 400)
            y = func(x)
            ymin = min(ymin, np.min(y))
            ymax = max(ymax, np.max(y))
            color = colors(i)  # Assign a unique color to each function
            self.ax.plot(x, y, label=f'Function {i+1}: {start} < x < {end}', color=color)
        
        repetitions = 3
        for i in range(1, repetitions + 1):
            for j, (func, start, end) in enumerate(functions):
                x = np.linspace(start, end, 400) + i * period
                y = func(x)
                color = colors(j)  # Reuse the same color for the repeated segments
                self.ax.plot(x, y, color=color)

        self.ax.set_xlabel('x')
        self.ax.set_ylabel('f(x)')
        self.ax.set_title('Piecewise Function with Repeating Segments')
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.set_ylim([ymin*1.5-2, ymax*1.5+2])
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)
        self.ax.legend()
        self.canvas_plot.draw()

root = tk.Tk()
app = PiecewiseFunctionGUI(root)
root.mainloop()


# In[ ]: