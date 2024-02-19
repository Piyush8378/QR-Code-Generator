import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    # Get the input text
    text = entry.get()
    
    if text.strip() == "":
        messagebox.showerror("Error", "Please enter some text.")
        return
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert PIL image to Tkinter PhotoImage
    img_tk = ImageTk.PhotoImage(img)
    
    # Update the label with the QR code image
    qr_label.img = img_tk
    qr_label.config(image=img_tk)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Input text entry
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

# Generate button
generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 12))
generate_btn.pack(pady=5)

# Label to display QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
