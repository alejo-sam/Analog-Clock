import tkinter as tk
from tkinter import ttk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Reloj Analógico")
        
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.grid(row=0, column=0, columnspan=2)
        
        self.is_dark_mode = False
        self.mode_button = ttk.Button(root, text="Modo Oscuro", command=self.toggle_mode)
        self.mode_button.grid(row=1, column=0, pady=10)
        
        self.update_clock()
    
    def toggle_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.mode_button.config(text="Modo Claro" if self.is_dark_mode else "Modo Oscuro")
        self.update_clock()
    
    def update_clock(self):
        self.canvas.delete("all")
        self.draw_clock_face()
        self.draw_hands()
        self.root.after(1000, self.update_clock)
    
    def draw_clock_face(self):
        fill_color = "black" if self.is_dark_mode else "white"
        outline_color = "white" if self.is_dark_mode else "black"
        self.canvas.create_oval(50, 50, 350, 350, fill=fill_color, outline=outline_color)
        
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x = 200 + 140 * math.cos(angle)
            y = 200 + 140 * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i + 1), fill=outline_color, font=("Arial", 16))
    
    def draw_hands(self):
        now = time.localtime()
        sec_angle = math.radians(now.tm_sec * 6 - 90)
        min_angle = math.radians(now.tm_min * 6 - 90)
        hour_angle = math.radians((now.tm_hour % 12) * 30 + now.tm_min * 0.5 - 90)
        
        sec_x = 200 + 120 * math.cos(sec_angle)
        sec_y = 200 + 120 * math.sin(sec_angle)
        self.canvas.create_line(200, 200, sec_x, sec_y, fill="red", width=1)
        
        min_x = 200 + 100 * math.cos(min_angle)
        min_y = 200 + 100 * math.sin(min_angle)
        self.canvas.create_line(200, 200, min_x, min_y, fill="blue", width=2)
        
        hour_x = 200 + 60 * math.cos(hour_angle)
        hour_y = 200 + 60 * math.sin(hour_angle)
        self.canvas.create_line(200, 200, hour_x, hour_y, fill="green", width=4)

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    clock = AnalogClock(root)
    root.mainloop()
