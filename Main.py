# This code is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this work for commercial purposes. See the LICENSE file for more details.

#import necessary libraries
import os
os.makedirs('logs', exist_ok=True)
import customtkinter as tk
from hashlib import sha256
import logging
import time
from tkinter import filedialog

#set up logging
date = time.strftime('%Y-%m-%d')
logging.basicConfig(filename=f'logs/{date}.log', level=logging.INFO, format='%(asctime)s - %(message)s')

#global variables

#create main window and configure it
window = tk.CTk()
tk.set_default_color_theme("dark-blue")
window.config(bg='#00ffc8')
window.title("Hash Calculator")


#congigure the tabs
tabview = tk.CTkTabview(master=window, bg_color='#F13030', fg_color='#22181C',corner_radius=3, anchor="nw")
tabview.pack(pady=0, expand=True, fill="both")
tabview.add("Hash Calculator")
tabview.add("Calculator")



def hashcalc():
        
    file_path = []

    def uph(value,funct):
        global curhash
        curhash = value
        hashshow.configure(text=f"SHA256 Hash: {curhash}")
        if funct == 1:
            logging.info(f"File: {file_path[-1]}  Hash: {curhash}")
        elif funct == 2:
            logging.info(f"input: '{inputextractor()}' Hash: {curhash}")   

    tk.CTkButton(master=tabview.tab("Hash Calculator"), bg_color='#22181C',fg_color='#5A0001',text="Select File", command=lambda: file_path.append(filedialog.askopenfilename())).pack(pady=5)
    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', text="Hash selected File", command=lambda: uph(sha256(open(file_path[-1], 'rb').read()).hexdigest(),1) if file_path else hashshow.configure(text="No File selected")).pack(pady=5)
    z = tk.CTkEntry(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', width=40)
    z.pack(pady=20)

    def inputextractor():
        inp = z.get()
        return inp

    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', text="Hash Text Field Input",command=lambda: uph(sha256(inputextractor().encode('utf-8')).hexdigest(),2)).pack()
    global hashshow
    hashshow = tk.CTkLabel(master=tabview.tab("Hash Calculator"), bg_color='#22181C',fg_color='#5A0001',text="",corner_radius=12)
    hashshow.pack(pady=5)

hashcalc()
window.mainloop()
