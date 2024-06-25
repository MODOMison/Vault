import os
import shutil
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='interdimensional_vault.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def move_desktop_contents_to_interdimensional_vault(source_path, hidden_folder_path):
    try:
        # Create a new folder with current date and time
        now = datetime.now()
        timestamp = now.strftime(".%Y-%m-%d_%H-%M-%S")  # Start with a dot
        vault_folder_path = os.path.join(hidden_folder_path, f"Vault_{timestamp}")

        if not os.path.exists(vault_folder_path):
            os.makedirs(vault_folder_path)

        # Move all contents from the source directory to the vault folder
        for item in os.listdir(source_path):
            item_path = os.path.join(source_path, item)
            try:
                shutil.move(item_path, vault_folder_path)
                logging.info(f'Moved {item} to {vault_folder_path}')
            except Exception as e:
                logging.error(f'Failed to move {item}: {e}')

        messagebox.showinfo("Success", "All contents have been moved to the Interdimensional Vault.")
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        messagebox.showerror("Error", f"An error occurred: {e}")

def create_gui():
    root = tk.Tk()
    root.title("Interdimensional Vault")
    root.geometry('300x300')
    root.resizable(False, False)

    # Load the background image
    image_path = 'itsageodeNFT.png'  # Change this to the correct path of your image
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.LANCZOS)  # Resize to a 300x300 square
    bg_image = ImageTk.PhotoImage(image)

    # Create a canvas and set the background image
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    def on_move_button_click():
        # Get the path to the desktop
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        hidden_folder_name = '.hidden_desktop_contents'
        hidden_folder_path = os.path.join(os.path.expanduser('~'), hidden_folder_name)
        move_desktop_contents_to_interdimensional_vault(desktop_path, hidden_folder_path)

    # Set UCSD colors for buttons
    UCSD_GOLD = '#FFD700'
    UCSD_BLUE = '#003B5C'

    # Create a button and place it at the bottom right corner
    move_button = tk.Button(root, text="Activate Vault", command=on_move_button_click,
                            bg=UCSD_BLUE, fg="white", padx=10)
    move_button_window = canvas.create_window(290, 290, anchor="se", window=move_button)

    root.mainloop()

if __name__ == '__main__':
    create_gui()
