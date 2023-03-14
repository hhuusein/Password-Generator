import random
import string
import sys
import tkinter as tk

root = tk.Tk()
root.title("Şifre Oluşturma Aracı")

def generate_password():
    password_characters = string.ascii_letters + string.digits
    if include_punctuation.get():
        password_characters += string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length.get()))
    password_display.config(state="normal")
    password_display.delete(0, tk.END)
    password_display.insert(0, password)
    password_display.config(state="readonly")

password_length_label = tk.Label(root, text="Şifre Uzunluğu:")
password_length_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

password_length = tk.IntVar()
password_length.set(8)  # varsayılan uzunluk 8 karakter
password_length_entry = tk.Entry(root, width=5, textvariable=password_length)
password_length_entry.grid(row=0, column=1, padx=0, pady=2, sticky=tk.W)

generate_button = tk.Button(root, text="Şifre Oluştur", command=generate_password)
generate_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

password_display_label = tk.Label(root, text="Oluşturulan Şifre:")
password_display_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)

password_display = tk.Entry(root, width=20, state="readonly", show=None)
password_display.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

include_punctuation = tk.BooleanVar()
include_punctuation.set(False)

punctuation_checkbox = tk.Checkbutton(root, text="Özel Karakterler İçerilsin mi?", variable=include_punctuation)
punctuation_checkbox.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

root.mainloop()
