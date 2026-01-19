import tkinter as tk
from tkinter import ttk

def placeholder():
    pass

root = tk.Tk()
root.title("Text Organizer")
root.geometry("900x450")

main= ttk.Frame(root, padding=10)
main.pack(fill=tk.BOTH, expand=True)

# INPUT
ttk.Label(main, text="INPUT TEXT").grid(row=0, column=0, sticky="w")
input_text = tk.Text(main, wrap="word")
input_text.grid(row=1, column=0, sticky="nsew")

# BUTTONS
btn_frame = ttk.Frame(main)
btn_frame.grid(row=1, column=1, padx=10)

ttk.Button(btn_frame, text="CONSTRUCT", command=placeholder).pack(fill="x", pady=5)
ttk.Button(btn_frame, text="STRIP", command=placeholder).pack(fill="x", pady=5)
ttk.Button(btn_frame, text="SLPIT", command=placeholder).pack(fill="x", pady=5)

# OUTPUT
ttk.Label(main, text="OUTPUT TEXT").grid(row=0, column=2, sticky="w")
output_text = tk.Text(main, wrap="word")
output_text.grid(row=1, column=2, sticky="nsew")

# LAYOUT BEHAVIOUR
main.columnconfigure(0, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(1, weight=1)

root.mainloop()