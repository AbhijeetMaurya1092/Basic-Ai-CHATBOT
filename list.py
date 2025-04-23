import tkinter as tk
import numpy 
from tkinter import scrolledtext
from PIL import Image, ImageTk
import google.generativeai as genai

# Configure your Gemini API
genai.configure(api_key="")

model = genai.GenerativeModel("gemini-1.5-pro")

# Initialize the main window
root = tk.Tk()
root.title("🤖 ORANGE - Your Robot Assistant")
root.geometry("600x700")
root.configure(bg="#1e1e2f")

# Load robot image (make sure it's in your project folder)
robot_img = Image.open("orange/bot.jpg")
robot_img = Image.fromarray(numpy.array(robot_img.resize((100, 100))))
robot_photo = ImageTk.PhotoImage(robot_img)

# Add robot label
robot_label = tk.Label(root, image=robot_photo, bg="#1e1e2f")
robot_label.pack(pady=10)

# Chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#2b2b3c", fg="white", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state='disabled')

# Entry field
entry_field = tk.Entry(root, bg="#3e3e50", fg="white", font=("Arial", 12))
entry_field.pack(padx=10, pady=10, fill=tk.X)

def send_message():
    user_msg = entry_field.get().strip()
    if user_msg == "":
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_msg}\n")
    chat_area.config(state='disabled')
    entry_field.delete(0, tk.END)

    # Get response from Gemini
    try:
        response = model.generate_content(user_msg)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = f"Error: {e}"

    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"ORANGE 🤖: {bot_reply}\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

# Send message on Enter key
entry_field.bind("<Return>", lambda event: send_message())

# Run the application
root.mainloop()
