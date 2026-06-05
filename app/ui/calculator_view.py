from functools import partial
import math
import tkinter as tk


class CalculatorView:
    def __init__(self, root):
        
        # Full Screen Wrapper Widget
        self.root = tk.Frame(
            root,  
            padx=15,
            pady=5,
            bg='red'
        )
        self.root.pack(
            fill="both",
            expand=True,
            
        )
        
        # Calculator Result Display
        self.container = tk.Frame(
            self.root,
            bg="#e4e4e4",
            padx=2,
            pady=2
        )
        
        self.container.pack(
            fill='x',
        )
        self.display = tk.Entry(
            self.container,
            font=("Arial", 18),
            justify="right"

        )
        self.display.pack(
            fill="x", 
            ipady=12
        )
        # Calculator Buttons
        buttons = [
            {"label": "⌫"}, {"label": "AC"}, {"label": "%"}, {"label": "÷"},
            {"label": "7"}, {"label": "8"}, {"label": "9"}, {"label": "×"},
            {"label": "4"}, {"label": "5"}, {"label": "6"}, {"label": "−"},
            {"label": "1"}, {"label": "2"}, {"label": "3"}, {"label": "+"},
            {"label": "+/-"}, {"label": "0"}, {"label": "."}, {"label": "="}
        ]
        
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x")
        
        for col in range(4):
            btn_frame.grid_columnconfigure(col, weight=1)
        
        for index, btn in enumerate(buttons, start=0):
            item = 4
            row = math.floor(index / item)
            collumn = index % item
                
            button = tk.Button(
                btn_frame,   
                text=btn["label"],
                font=("Arial", 18),
                height=2,
                command=lambda value = btn["label"]: self.on_click(value)
            )

            button.grid(
                row=row,
                column=collumn,
                padx=2,
                pady=2,
                sticky="nsew",

            )
    def on_click(self, value):
        current = self.display.get()
        print("current --->>>", current) 
        print("value --->>>", value)
        if value == "⌫":
            new_value = str(current[1:])
            self.display.delete(0, tk.END)
            self.display.insert(0, new_value)
        elif value == "AC":
            self.display.delete(0, tk.END)
        else: 
            self.display.insert(0, str(value))
            
            
        
        
        
    