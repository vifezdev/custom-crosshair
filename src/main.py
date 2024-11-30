import tkinter as tk
from tkinter import ttk
import pygame
import threading
import win32gui
import win32con
from pyautogui import size
from crosshairs import Crosshairs


class CrosshairOverlayApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Crosshair Overlay")
        self.root.geometry("600x500")
        self.crosshair_selection = tk.StringVar(value="Circle")

        self.screen_width, self.screen_height = size()

        self.crosshair_color = (255, 0, 0)
        self.crosshair_type = "Circle"
        self.crosshair_size = 20
        self.running = False

        self.crosshairs = Crosshairs()

        self.crosshair_options = self.crosshairs.get_available_crosshairs()

        self.setup_gui()
        self.crosshair_thread = None

    def setup_gui(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        crosshair_frame = ttk.Frame(main_frame)
        crosshair_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        search_bar = ttk.Entry(crosshair_frame)
        search_bar.pack(fill=tk.X, padx=5, pady=5)
        search_bar.insert(0, "Search...")
        search_bar.bind("<FocusIn>", lambda e: search_bar.delete(0, tk.END))
        search_bar.bind("<KeyRelease>", self.update_crosshair_list)

        scroll_canvas = tk.Canvas(crosshair_frame)
        scroll_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(crosshair_frame, orient=tk.VERTICAL, command=scroll_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollable_frame = ttk.Frame(scroll_canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: scroll_canvas.configure(scrollregion=scroll_canvas.bbox("all"))
        )
        scroll_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        scroll_canvas.configure(yscrollcommand=scrollbar.set)

        scroll_canvas.bind("<Enter>", lambda _: self.bind_mouse_wheel(scroll_canvas))
        scroll_canvas.bind("<Leave>", lambda _: self.unbind_mouse_wheel(scroll_canvas))

        self.crosshair_buttons = []
        self.populate_crosshair_options()

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        start_button = ttk.Button(button_frame, text="Start Overlay", command=self.start_overlay)
        start_button.pack(pady=5)

        stop_button = ttk.Button(button_frame, text="Stop Overlay", command=self.stop_overlay)
        stop_button.pack(pady=5)

        start_button.bind("<Enter>", lambda _: self.unbind_mouse_wheel(scroll_canvas))
        stop_button.bind("<Enter>", lambda _: self.unbind_mouse_wheel(scroll_canvas))
        start_button.bind("<Leave>", lambda _: self.bind_mouse_wheel(scroll_canvas))
        stop_button.bind("<Leave>", lambda _: self.bind_mouse_wheel(scroll_canvas))

    def bind_mouse_wheel(self, widget):
        """Bind mouse wheel to the scroll action."""
        self.root.bind_all("<MouseWheel>", lambda event: self.on_mouse_wheel(event, widget))

    def unbind_mouse_wheel(self, widget):
        """Unbind mouse wheel from the scroll action."""
        self.root.unbind_all("<MouseWheel>")

    def on_mouse_wheel(self, event, widget):
        """Handle mouse wheel scrolling."""
        widget.yview_scroll(-1 * (event.delta // 120), "units")

    def populate_crosshair_options(self, filter_text=""):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.crosshair_buttons = []
        for option in self.crosshair_options:
            if filter_text.lower() in option.lower():
                button = ttk.Radiobutton(
                    self.scrollable_frame,
                    text=option,
                    variable=self.crosshair_selection,
                    value=option,
                    command=self.update_crosshair_type
                )
                button.pack(anchor=tk.W, padx=5, pady=2)
                self.crosshair_buttons.append(button)

    def update_crosshair_list(self, event):
        search_text = event.widget.get()
        self.populate_crosshair_options(search_text)

    def update_crosshair_type(self):
        self.crosshair_type = self.crosshair_selection.get()

    def set_window_properties(self, hwnd):
        styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT)
        win32gui.SetLayeredWindowAttributes(hwnd, 0, 0, win32con.LWA_COLORKEY)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)

    def overlay_loop(self):
        pygame.init()
        screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height), pygame.NOFRAME
        )
        hwnd = pygame.display.get_wm_info()["window"]
        self.set_window_properties(hwnd)

        self.running = True
        while self.running:
            screen.fill((0, 0, 0, 0))
            self.crosshairs.draw_crosshair(
                screen,
                self.crosshair_type,
                self.screen_width,
                self.screen_height,
                self.crosshair_color,
                self.crosshair_size
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()

    def start_overlay(self):
        if not self.running:
            self.crosshair_thread = threading.Thread(target=self.overlay_loop, daemon=True)
            self.crosshair_thread.start()

    def stop_overlay(self):
        self.running = False
        if self.crosshair_thread:
            self.crosshair_thread.join()
            self.crosshair_thread = None

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CrosshairOverlayApp()
    app.run()