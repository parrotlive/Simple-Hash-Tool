# This code is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this work for commercial purposes. See the LICENSE file for more details.

from hashlib import sha256
import tkinter as tk
from tkinter import filedialog
import logging
import time

date = time.strftime('%Y-%m-%d')
logging.basicConfig(filename=f'logs/{date}.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def hashcalc():
        
    file_path = []
    curhash = ""
    inp = ""

    def uph(value,funct):
        global curhash
        curhash = value
        hashshow.config(text=f"SHA256 Hash: {curhash}")
        if funct == 1:
            logging.info(f"File: {file_path[-1]}  Hash: {curhash}")
        elif funct == 2:
            logging.info(f"input: '{inputextractor()}' Hash: {curhash}")   

    main = tk.Tk()
    main.title("SHA-256 Hash Generator")
    main.geometry("475x180")
    main.config(bg='black')

    tk.Button(main, text="Select File", bg='black', fg='lightblue', command=lambda: file_path.append(filedialog.askopenfilename())).pack(pady=5)
    tk.Button(main, text="Hash selected File", bg='black', fg='lightblue', command=lambda: uph(sha256(open(file_path[-1], 'rb').read()).hexdigest(),1) if file_path else None).pack(pady=5)
    z = tk.Entry(main, bg='black', fg='white',width=40)
    z.pack(pady=20)

    def inputextractor():
        inp = z.get()
        return inp

    tk.Button(main, text="Hash Text Field Input", bg='black', fg='lightblue',command=lambda: uph(sha256(inputextractor().encode('utf-8')).hexdigest(),2)).pack()
    hashshow = tk.Label(main, bg='black', fg='white')
    hashshow.pack(pady=5)

    main.mainloop()
