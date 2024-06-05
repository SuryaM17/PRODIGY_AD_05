import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    url = url_entry.get()
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Create the tkinter window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.configure(bg="#FFFFFF")

# Style
style = ttk.Style()
style.configure("TFrame", background="#FFFFFF")
style.configure("Title.TLabel", font=("Arial", 20), background="#336699", foreground="white")
style.configure("TLabel", font=("Arial", 12), background="#FFFFFF", foreground="#333333")
style.configure("TButton", font=("Arial", 12), background="#336699", foreground="white")

# Title
title_frame = ttk.Frame(root)
title_frame.pack(fill="x")

title_label = ttk.Label(title_frame, text="QR Code Generator", style="Title.TLabel")
title_label.pack(pady=10)

# URL input field
url_frame = ttk.Frame(root)
url_frame.pack(pady=10)

url_label = ttk.Label(url_frame, text="Enter URL:", style="TLabel")
url_label.grid(row=0, column=0, padx=5)

url_entry = ttk.Entry(url_frame, width=30)
url_entry.grid(row=0, column=1, padx=5)

# Button to generate QR code
generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr_code, style="TButton")
generate_button.pack(pady=10)

# Label to display QR code
qr_label = ttk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
