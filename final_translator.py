from tkinter import ttk
import tkinter as tk
from deep_translator import GoogleTranslator

root = tk.Tk()
root.title("Translator")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Spanish": "es"
}

# Input box
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Source dropdown
src_lang = ttk.Combobox(root, values=list(languages.keys()))
src_lang.set("English")
src_lang.pack(pady=5)

# Target dropdown
dest_lang = ttk.Combobox(root, values=list(languages.keys()))
dest_lang.set("Telugu")
dest_lang.pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Translate function
def translate():
    text = entry.get()
    src_code = languages[src_lang.get()]
    dest_code = languages[dest_lang.get()]
    translated = GoogleTranslator(source=src_code, target=dest_code).translate(text)
    result_label.config(text=translated)

# Translate button
btn = tk.Button(root, text="Translate", command=translate)
btn.pack(pady=5)

root.mainloop()
