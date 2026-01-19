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

# LOGIC 
def get_input():
    return input_text.get("1.0", tk.END).strip()

def set_output(text):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)

def construct():
    parts = [p.strip() for p in get_input().split(",") if p.strip()]
    set_output(" ".join(parts))

def strip_text():
    lines = get_input().splitlines()
    stripped_lines = [line.strip() for line in lines]
    set_output("\n".join(stripped_lines))

def split_text():
    parts = [p.strip() for p in get_input().split(",") if p.strip()]
    set_output("\n".join(parts))

# UTILITIES (COPY & CLEAR)
def copy_output():
    output = output_text.get("1.0", tk.END).strip()
    if output:
        root.clipboard_clear()
        root.clipboard_append(output)

def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# BUTTONS
btn_frame = ttk.Frame(main)
btn_frame.grid(row=1, column=1, padx=10)

ttk.Button(btn_frame, text="CONSTRUCT", command=construct).pack(fill="x", pady=5)
ttk.Button(btn_frame, text="STRIP", command=strip_text).pack(fill="x", pady=5)
ttk.Button(btn_frame, text="SPLIT", command=split_text).pack(fill="x", pady=5)

# OUTPUT HEADER _+ UTILS
output_header = ttk.Frame(main)
output_header.grid(row=0, column=2, sticky="ew")

ttk.Label(output_header, text="OUTPUT TEXT").pack(side="left")

utils_frame = ttk.Frame(output_header)
utils_frame.pack(side="right")

ttk.Button(utils_frame, text="COPY", command=copy_output).pack(side="right", padx=(5, 0))
ttk.Button(utils_frame, text="CLEAR ALL", command=clear_all).pack(side="right")

# OUTPUT TEXT
output_text = tk.Text(main, wrap="word")
output_text.grid(row=1, column=2, sticky="nsew")

# LAYOUT BEHAVIOUR
main.columnconfigure(0, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(1, weight=1)

root.mainloop()