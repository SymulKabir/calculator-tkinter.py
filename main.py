import tkinter as tk
from app.ui.calculator_view import CalculatorView


def main():
    root = tk.Tk()
    root.title("Calculator")
    

    width = 350
    height = 500

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()

    # Position at top-right corner
    x = screen_width - width
    y = 0

    root.geometry(f"{width}x{height}+{x}+{y}")
    
    CalculatorView(root)

    root.mainloop()

    
    
main()