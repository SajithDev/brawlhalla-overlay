import tkinter
from tkinter import ttk
import sv_ttk

from brawlhalla_overlay.api_calls import fetch_glory_stats

def create_overlay():
    root = tkinter.Tk()

    root.geometry("300x150+10+50")
    root.attributes('-alpha', 0.8)  # Transparency
    # root.overrideredirect(True)  # Frameless
    root.attributes('-topmost', True)  # Always on top

    label = ttk.Label(root, text="Loading Stats...")
    label.pack(pady=20)

    # Fetch stats and update label
    id = "3145331"
    player_stats = fetch_glory_stats(id)
    label.config(text=player_stats["data"]["name"])

    # This is where the magic happens
    sv_ttk.set_theme("dark")

    root.mainloop()

if __name__ == "__main__":
    create_overlay()