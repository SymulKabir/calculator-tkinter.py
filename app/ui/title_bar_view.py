import tkinter as tk



class TitleBarView:
    def __init__(self, root):
        title_bar = tk.Frame(root, bg="#0048ba", height=35)
        title_bar.pack(fill="x")
        title_bar.pack_propagate(False)

        # LEFT BUTTONS
        btn_frame = tk.Frame(title_bar, bg="#0048ba")
        btn_frame.pack(side="left", padx=10)

        self.make_circle(btn_frame, "#ff5f57", lambda: self.close_app(root))
        self.make_circle(btn_frame, "#febc2e", lambda: self.minimize_app(root))
        self.make_circle(btn_frame, "#28c840", lambda: None)

        # TITLE
        title_label = tk.Label(
            title_bar,
            text="Calculator",
            bg="#0048ba",
            fg="white",
            font=("Arial", 11, "bold")
        )
        title_label.pack(side="top", pady=6)

        # =========================
        # DRAG SUPPORT
        # =========================
        title_bar.bind("<Button-1>", lambda e: self.start_move(e, root))
        title_bar.bind("<B1-Motion>", lambda e: self.do_move(e, root))

        title_label.bind("<Button-1>", lambda e: self.start_move(e, root))
        title_label.bind("<B1-Motion>", lambda e: self.do_move(e, root))

        # restore after minimize
        root.bind("<Map>", lambda e: self.restore_window(e, root))
        
        
    def make_circle(self, parent, color, command):
        size = 24  # IMPORTANT: bigger canvas

        btn = tk.Canvas(
            parent,
            width=size,
            height=size,
            bg="#0048ba",
            highlightthickness=0
        )
        btn.pack(side="left", padx=6)

        # perfect centered circle
        circle = btn.create_oval(
            3, 3, size - 3, size - 3,
            fill=color,
            outline=""
        )

        # -------------------
        # hover (ONLY outline)
        # -------------------
        def on_enter(e):
            btn.itemconfig(circle, outline="white", width=1)

        def on_leave(e):
            btn.itemconfig(circle, outline="", width=0)

        # -------------------
        # click (darken effect)
        # -------------------
        def on_press(e):
            btn.itemconfig(circle, fill="#cccccc")

        def on_release(e):
            btn.itemconfig(circle, fill=color)
            command()

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.bind("<ButtonPress-1>", on_press)
        btn.bind("<ButtonRelease-1>", on_release)

        return btn
    
    def close_app(self, root):
        root.destroy()


    def minimize_app(self, root):
        root.overrideredirect(False)
        root.iconify()


    def restore_window(self, event, root):
        root.overrideredirect(True)
        
    def start_move(self, event, root):
        root._x = event.x
        root._y = event.y


    def do_move(self, event, root):
        x = event.x_root - root._x
        y = event.y_root - root._y
        root.geometry(f"+{x}+{y}")