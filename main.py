import tkinter as tk
from app.ui.calculator_view import CalculatorView
from app.ui.title_bar_view import TitleBarView
 

# =========================
# MAIN APP
# =========================
def main():
    root = tk.Tk()
    root.title("Calculator")

    # remove native title bar
    root.overrideredirect(True)
    root.resizable(False, False)
 
    TitleBarView(root)
    CalculatorView(root)

    # =========================
    # POSITION WINDOW (top-right)
    # =========================
    root.update_idletasks()

    screen_width = root.winfo_screenwidth()

    x = screen_width - root.winfo_reqwidth()
    y = 0

    root.geometry(f"+{x}+{y}")

    root.mainloop()


main()