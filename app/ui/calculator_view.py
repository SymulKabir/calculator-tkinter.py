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
        current_value = self.display.get()
        current_new_value = f"{current_value}{value}"
        print("current_value --->>>", current_value) 
        print("value --->>>", value)
        print("current_new_value --->>>", current_new_value)
        
        
        
        if value == "⌫":
            new_value = str(current_value[1:])
            self.display.delete(0, tk.END)
            self.display.insert(0, new_value)
        elif value == "AC":
            self.display.delete(0, tk.END)
        elif value == "%":
            split_result = self.split_calculation(current_value) or {}
            last_operator = split_result.get('last_operator')
            left_value = split_result.get('left_value')
            right_value = split_result.get('right_value')
            last_char = split_result.get('last_char')
            print("last_operator ->", last_operator)
            print("left_value ->", left_value)
            print("right_value ->", right_value)
            print("last_char ->", last_char)
            print("====")
            
            if last_char == "%":
                if last_operator:
                    inner_split_result = self.split_calculation(left_value) or {}
                    inner_last_operator = inner_split_result.get('last_operator') 
                    inner_left_value = inner_split_result.get('left_value') 
                    inner_right_value = inner_split_result.get('right_value') 
                    print("inner_last_operator->", inner_last_operator)
                    print("inner_left_value->", inner_left_value)
                    print("inner_right_value->", inner_right_value)
                    new_value = f"{inner_left_value}{last_operator}({right_value}"
                
                pass
                
            self.display.insert("end", str(value))
            
        elif value == "+/-":
            
            pass
        else:
            self.display.insert("end", str(value))
            
    def split_calculation(self, value):
        operators = ['+', '-', '*', '/', '%']

        last_pos = -1
        last_operator = None
        last_char = value[-1:]

        for op in operators:
            pos = value.rfind(op)
            
            if pos > last_pos:
                last_pos = pos
                last_operator = op

        if last_operator:
            left = value[:last_pos]
            right = value[last_pos + 1:]
            
            
            return {
                "last_operator": last_operator, 
                "left_value": left, 
                "right_value": right,
                'last_char': last_char
                }
            
        return {'last_char': last_char}
            
            
            
        
        
        
    