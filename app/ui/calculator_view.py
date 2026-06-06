from functools import partial
import math
from textwrap import fill
import tkinter as tk
from app.config.symbols import SYMBOL_MAP
from app.config.colors import BG_COLOR, TEXT_COLOR, PRIMARY_COLOR

class CalculatorView:
    def __init__(self, root):
        
        
        # Full Screen Wrapper Widget
        self.root = tk.Frame(
            root,  
            padx=15,
            pady=5,
            bg=BG_COLOR
        )
        self.root.pack(
            fill="both",
            expand=True,
            
        )
        
        
        # Calculator Result Display
        self.result_display_container = tk.Frame(
            self.root, 
            bg=BG_COLOR
        )
        
        self.result_display_container.pack(
            fill='x',
            padx=4,
        ) 
        self.calculation_display = tk.Label(
            self.result_display_container,
            font=("Arial", 17),
            anchor="e",
            fg="#666666",
            # bg="#FFFFFF",
            bg=BG_COLOR,
            bd=0,
            relief="flat", 
            highlightthickness=0
        )
        self.calculation_display.pack(
            fill="x",
            padx=2,
            pady=2
        )
        self.display = tk.Entry(
            self.result_display_container,
            font=("Arial", 19),
            justify="right",
            bd=0,
            relief="flat",
            highlightthickness=0,
            highlightbackground=BG_COLOR,
            highlightcolor=BG_COLOR, 
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            takefocus=0,
            validate="key",
        )
        self.display.pack(
            fill="x", 
            ipady=5
        )
        self.display.bind("<Key>", self.on_keypress)
        
        
        # Calculator Buttons
        buttons = [
            {"label": "⌫"}, {"label": "AC"}, {"label": "%"}, {"label": "÷"},
            {"label": "7"}, {"label": "8"}, {"label": "9"}, {"label": "×"},
            {"label": "4"}, {"label": "5"}, {"label": "6"}, {"label": "−"},
            {"label": "1"}, {"label": "2"}, {"label": "3"}, {"label": "+"},
            {"label": "+/-"}, {"label": "0"}, {"label": "."}, {"label": "="}
        ]
        
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(fill="x")
  
        
        for col in range(4):
            btn_frame.grid_columnconfigure(col, weight=1)
        
        for index, btn in enumerate(buttons, start=0):
            item = 4
            row = math.floor(index / item)
            collumn = index % item
            bg = "#454a4a"
            if collumn == 3:
                bg = "#ff8b00"
            elif row == 0:
                bg = "#717575"
                
            # button = tk.Button(
            #     btn_frame,   
            #     text=btn["label"],
            #     font=("Arial", 18),
            #     height=2,
            #     command=lambda value = btn["label"]: self.on_click(value)
            # )

            # button.grid(
            #     row=row,
            #     column=collumn,
            #     padx=2,
            #     pady=2,
            #     sticky="nsew",

            # )
            self.circle_button(
                btn_frame,
                text=btn["label"],
                row=row,
                col=collumn,
                bg=bg, 
                command=lambda value = btn["label"]: self.on_click(value)
            )
    
    def circle_button(self, parent, text, row, col, bg="#717575", command=None):
        size = 90
        radius = size // 2

        canvas = tk.Canvas(
            parent,
            width=size,
            height=size,
            bg=BG_COLOR,
            # bg="white",
            highlightthickness=0
        )
        canvas.grid(row=row, column=col, padx=5, pady=5)

        # circle
        circle = canvas.create_oval(
            5, 5, size-5, size-5,
            fill=bg,
            outline=""
        )

        # text
        canvas.create_text(
            radius,
            radius,
            text=text,
            font=("Arial", 19),
            fill=TEXT_COLOR
        )

        def on_click(event):
            if command:
                command(text)

        canvas.bind("<Button-1>", on_click)

        return canvas
                
    def on_keypress(self, event): 
        char = event.char
        # allow control keys (backspace, etc.)
        if event.keysym in ("BackSpace", "Left", "Right", "Delete"):
            return

        # allow digits
        if char.isdigit() or char == ".":
            return

        # replace operators
        if char in SYMBOL_MAP:
            self.display.insert(tk.END, SYMBOL_MAP[char])
            return "break"

        # block everything else
        return "break"

    def on_click(self, value):
        current = self.display.get()
        calculation_display_value = self.calculation_display.cget("text")
        if calculation_display_value:
            self.calculation_display.config(text="") 

        if value == "AC":
            self.display.delete(0, tk.END)

        elif value == "⌫":
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])

        elif value == "=":
            try:
                expression = current
                self.calculation_display.config(text=expression)

                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")
                expression = expression.replace("−", "-")

                result = eval(expression)

                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))

            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif value == "%":
            try:
                expression = current

                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")
                expression = expression.replace("−", "-")

                result = eval(expression) / 100

                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))

            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif value == "+/-":
            try:
                if current.startswith("-"):
                    current = current[1:]
                else:
                    current = "-" + current

                self.display.delete(0, tk.END)
                self.display.insert(0, current)

            except Exception:
                pass

        else:
            self.display.insert(tk.END, value)
            
    def validate_input(self, value_if_allowed):
        allowed_chars = "0123456789++--*x/%. " 

        if value_if_allowed == "":
            return True

        return all(char in allowed_chars for char in value_if_allowed)