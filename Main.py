# This code is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this work for commercial purposes. See the LICENSE file for more details.

#import necessary libraries
import os
os.makedirs('logs', exist_ok=True)
import customtkinter as tk
import hashlib
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
        
    algomap = {
    "SHA1": hashlib.sha1,
    "SHA224": hashlib.sha224,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512,
    "SHA3-224": hashlib.sha3_224,
    "SHA3-256": hashlib.sha3_256,
    "SHA3-384": hashlib.sha3_384,
    "SHA3-512": hashlib.sha3_512,
    "SHAKE-128": hashlib.shake_128,
    "SHAKE-256": hashlib.shake_256,
    "BLAKE2b": hashlib.blake2b,
    "BLAKE2s": hashlib.blake2s,
    "MD5": hashlib.md5
    }
    file_path = []
    global combobox 
    algo = None

    combobox = tk.CTkComboBox(master=tabview.tab("Hash Calculator"), values=["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512", "SHAKE-128", "SHAKE-256", "BLAKE2b", "BLAKE2s", "MD5"], command=lambda choice: algoselect(choice)); combobox.pack(pady=5); combobox.set("Select Algorithm")
    tk.CTkButton(master=tabview.tab("Hash Calculator"), bg_color='#22181C',fg_color='#5A0001',text="Select File", command=lambda: select_file()).pack(pady=5)
    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', text="Hash selected File", command=lambda: calchash(1)).pack(pady=5)
    hashinput = tk.CTkEntry(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', width=40);hashinput.pack(pady=20)
    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color='#22181C',fg_color='#5A0001', text="Hash Text Field Input",command=lambda: calchash(2)).pack()
    hashshow = tk.CTkLabel(master=tabview.tab("Hash Calculator"), bg_color='#22181C',fg_color='#5A0001',text="",corner_radius=12);hashshow.pack(pady=5)

    def algoselect(choice):
        nonlocal algo
        algo = algomap.get(choice)
        print(f"Selected Algorithm: {choice}")
        logging.info(f"Algorithm: {choice}")

    def select_file():
        file_path.append(filedialog.askopenfilename())


    def calchash(self):
        if algo is None:
            hashshow.configure(text="Algorithm not selected")
            return
        if self == 1:
            if file_path:
                hashnow = algo(open(file_path[-1], 'rb').read()).hexdigest()
                uph(hashnow, self)
            else:
                hashshow.configure(text="No File selected")
            
        elif self == 2:
            hashnow = algo(inputextractor().encode('utf-8')).hexdigest()
            uph(hashnow, self)

    def uph(value,funct):
        global curhash
        curhash = value
        hashshow.configure(text=f"SHA256 Hash: {curhash}")
        if funct == 1:
            logging.info(f"File: {file_path[-1]}  Hash: {curhash}")
        elif funct == 2:
            logging.info(f"input: '{inputextractor()}' Hash: {curhash}") 
      
    def inputextractor():
        inp = hashinput.get()
        return inp

hashcalc()
window.mainloop()