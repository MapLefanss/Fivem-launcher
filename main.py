import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def connect_to_server():
    ip = entry_ip.get()
    port = entry_port.get()

    if not ip or not port:
        messagebox.showerror("Error", "Please enter both IP and Port.")
        return

    fivem_path = r"C:\Program Files\FiveM\FiveM.exe"
    if not os.path.exists(fivem_path):
        messagebox.showerror("Error", "FiveM is not installed or path is incorrect.")
        return

    try:
        subprocess.Popen([fivem_path, f"fivem://connect/{ip}:{port}"])
        messagebox.showinfo("Connection Status", f"Connecting to {ip}:{port}...")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Failed to start FiveM: {str(e)}")

def on_enter(e):
    connect_button.config(bg="#45a049", font=("Helvetica", 14, "bold"))

def on_leave(e):
    connect_button.config(bg="#4CAF50", font=("Helvetica", 12))

def animate_text():
    text = "Connecting..."
    current_text = animated_label.cget("text")
    if len(current_text) < len(text):
        new_text = current_text + text[len(current_text)]
        animated_label.config(text=new_text)
        root.after(200, animate_text)

root = tk.Tk()
root.title("MapLe - Connect to FiveM Server")
root.geometry("500x500")
root.config(bg="#1e1e1e")

header_label = tk.Label(root, text="MapLe - Connect to FiveM Server", font=("Helvetica", 18, "bold"), fg="white", bg="#1e1e1e")
header_label.pack(pady=20)

def change_header_color():
    current_color = header_label.cget("fg")
    new_color = "yellow" if current_color == "white" else "white"
    header_label.config(fg=new_color)
    root.after(1000, change_header_color)

change_header_color()

animated_label = tk.Label(root, text="", font=("Helvetica", 14), fg="yellow", bg="#1e1e1e")
animated_label.pack(pady=10)

label_ip = tk.Label(root, text="Enter Server IP:", font=("Helvetica", 12), fg="white", bg="#1e1e1e")
label_ip.pack()

entry_ip = tk.Entry(root, font=("Helvetica", 12), width=20, bd=2, relief="solid", bg="#333333", fg="white")
entry_ip.pack(pady=5)

label_port = tk.Label(root, text="Enter Port:", font=("Helvetica", 12), fg="white", bg="#1e1e1e")
label_port.pack()

entry_port = tk.Entry(root, font=("Helvetica", 12), width=20, bd=2, relief="solid", bg="#333333", fg="white")
entry_port.pack(pady=5)

connect_button = tk.Button(root, text="Connect", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=connect_to_server)
connect_button.pack(pady=20)

connect_button.bind("<Enter>", on_enter)
connect_button.bind("<Leave>", on_leave)

def move_button():
    current_x = connect_button.winfo_x()
    if current_x < 150:
        connect_button.place(x=current_x + 5, y=connect_button.winfo_y())
        root.after(20, move_button)
    else:
        connect_button.place(x=100, y=connect_button.winfo_y())

root.after(1000, move_button)

footer_label = tk.Label(root, text="Code created by MapLe", font=("Helvetica", 10), fg="grey", bg="#1e1e1e")
footer_label.pack(side="bottom", pady=10)

root.after(500, animate_text)

root.mainloop()
