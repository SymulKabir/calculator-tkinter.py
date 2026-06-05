import tkinter as tk
from app.ui.calculator_view import CalculatorView


def main():
    root = tk.Tk()
    root.title("Calculator")

    root.resizable(False, False)  # optional: prevents stretching

    CalculatorView(root)

    root.update_idletasks()

    screen_width = root.winfo_screenwidth()

    x = screen_width - root.winfo_reqwidth()
    y = 0

    root.geometry(f"+{x}+{y}") 

    root.mainloop()

    
    
main()