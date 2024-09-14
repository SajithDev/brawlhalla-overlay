import tkinter as tk

from brawlhalla_overlay.api_calls import fetch_glory_stats

def create_overlay():
    root = tk.Tk()
    root.geometry("300x150+10+50")
    root.attributes('-alpha', 0.8)  # Transparency
    # root.overrideredirect(True)  # Frameless
    root.attributes('-topmost', True)  # Always on top

    label = tk.Label(root, text="Loading Stats...", font=("Helvetica", 14), fg="white", bg="black")
    label.pack(pady=20)

    player_id = "3145331"
    # Fetch stats and update label
    player_stats = fetch_glory_stats(player_id)
    label.config(text=player_stats['data']['name'])

    root.mainloop()

if __name__ == "__main__":
    create_overlay()