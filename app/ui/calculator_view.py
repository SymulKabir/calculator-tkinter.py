import tkinter as tk


class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.container = tk.Frame(
            root,
            bg="red",
            padx=2,
            pady=2
        ).pack(
            fill='x',
            padx=10,
            pady=10,
            ipady=12
        )
        self.display = tk.Entry(
            self.root,
            font=("Arial", 18),
            justify="right"

        ).pack(
            fill="x",
            padx=10,
            # pady=10,
            ipady=12
        )
        
    