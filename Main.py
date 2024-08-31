# This code is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License.
# You may not use this work for commercial purposes. See the LICENSE file for more details.

#import necessary libraries
import os
os.makedirs('logs', exist_ok=True)
import customtkinter as tk
import hashlib
import logging
import time
import configparser
import math
from tkinter import filedialog

#set up logging and configuration
date = time.strftime('%Y-%m-%d')
logging.basicConfig(filename=f'logs/{date}.log', level=logging.INFO, format='%(asctime)s - %(message)s')
config = configparser.ConfigParser()
config.read('config.ini')

#global variables
colors = [
    config['Colors']['primary'],
    config['Colors']['secondary'],
    config['Colors']['background'],
    config['Colors']['button_bg'],
    config['Colors']['highlight']
]

#create main window and configure it
window = tk.CTk()
tk.set_default_color_theme(config['General']['theme'])
window.config(bg=colors[0])
window.title("Hash Calculator")


#congigure the tabs
tabview = tk.CTkTabview(master=window, bg_color=colors[4], fg_color=colors[2],corner_radius=3, anchor="nw")
tabview.pack(pady=0, expand=True, fill="both")
tabview.add("Hash Calculator")
tabview.add("Calculator")
tabview.add("Color Selector")

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

    combobox = tk.CTkComboBox(master=tabview.tab("Hash Calculator"), bg_color=colors[2],fg_color=colors[3], values=["SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "SHA3-224", "SHA3-256", "SHA3-384", "SHA3-512", "SHAKE-128", "SHAKE-256", "BLAKE2b", "BLAKE2s", "MD5"], command=lambda choice: algoselect(choice)); combobox.pack(pady=5); combobox.set("Select Algorithm")
    tk.CTkButton(master=tabview.tab("Hash Calculator"), bg_color=colors[2],fg_color=colors[3],text="Select File", command=lambda: select_file()).pack(pady=5)
    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color=colors[2],fg_color=colors[3], text="Hash selected File", command=lambda: calchash(1)).pack(pady=5)
    hashinput = tk.CTkEntry(master=tabview.tab("Hash Calculator"),bg_color=colors[2],fg_color=colors[3], width=40);hashinput.pack(pady=20)
    tk.CTkButton(master=tabview.tab("Hash Calculator"),bg_color=colors[2],fg_color=colors[3], text="Hash Text Field Input",command=lambda: calchash(2)).pack()
    hashshow = tk.CTkLabel(master=tabview.tab("Hash Calculator"), bg_color=colors[2],fg_color=colors[3],text="",corner_radius=12);hashshow.pack(pady=5)

    def algoselect(choice):
        nonlocal algo
        algo = algomap.get(choice)
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

def calc():
    expression = ""
    memory = 0

    def update_display(value):
        current_text = display.get()
        new_text = current_text + value
        display.delete(0, tk.END)
        display.insert(0, new_text)

    def clear_display():
        display.delete(0, tk.END)

    def calculate():
        try:
            result = eval(display.get())
            logging.info(f"Calculation: {display.get()} = {result}")
            clear_display()
            display.insert(0, result)
        except Exception as e:
            logging.error(f"Error in calculation: {e}")
            clear_display()
            display.insert(0, "Error")

    def memory_clear():
        nonlocal memory
        memory = 0

    def memory_add():
        nonlocal memory
        memory += eval(display.get())
        logging.info(f"Memory add: {memory}")

    def memory_subtract():
        nonlocal memory
        memory -= eval(display.get())
        logging.info(f"Memory subtract: {memory}")

    def factorial():
        try:
            result = math.factorial(int(display.get()))
            logging.info(f"Factorial: {display.get()}! = {result}")
            clear_display()
            display.insert(0, result)
        except Exception as e:
            logging.error(f"Error in factorial: {e}")
            clear_display()
            display.insert(0, "Error")

    def power():
        try:
            base, exponent = map(float, display.get().split('^'))
            result = math.pow(base, exponent)
            logging.info(f"Power: {base}^{exponent} = {result}")
            clear_display()
            display.insert(0, result)
        except Exception as e:
            logging.error(f"Error in power calculation: {e}")
            clear_display()
            display.insert(0, "Error")

    display = tk.CTkEntry(master=tabview.tab("Calculator"), width=400)
    display.grid(row=0, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('^', 5, 1), ('!', 5, 2), ('M+', 5, 3),
        ('M-', 6, 3), ('M', 6, 2), ('MC', 6, 1)
    ]

    for (text, row, col) in buttons:
        if text == '=':
            action = calculate
        elif text == 'C':
            action = clear_display
        elif text == 'M+':
            action = memory_add
        elif text == 'M-':
            action = memory_subtract
        elif text == 'MC':
            action = memory_clear
        elif text == '!':
            action = factorial
        elif text == '^':
            action = power
        else:
            action = lambda t=text: update_display(t)

        tk.CTkButton(
            master=tabview.tab("Calculator"),
            text=text, width=100, height=80, command=action
        ).grid(row=row, column=col)

def color_selector():
    
    r = 0
    g = 0
    b = 0

    def restore():
        config['Colors']['primary'] = '#F45B69'
        config['Colors']['secondary'] = '#F6E8EA'
        config['Colors']['background'] = '#22181C'
        config['Colors']['button_bg'] = '#5A0001'
        config['Colors']['highlight'] = '#F13030'

        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        logging.info(f"Color restored to default")
        infog.configure(text="Settings will be applied after restarting the application")

    def change_color(color):
        nonlocal r, g, b
        config['Colors'][color] = rgb_to_hex(r, g, b)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        logging.info(f"changed {color} to {rgb_to_hex(r, g, b)}")
        infog.configure(text="Settings will be applied after restarting the application")

    def update_color():
        curcol = rgb_to_hex(r, g, b)
        presenter.configure(fg_color=curcol)
    
    def rgb_to_hex(r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)

    def r_event(self):
        nonlocal r
        r = int(float(self))
        update_color()
    def g_event(self):
        nonlocal g
        g = int(float(self))
        update_color()
    def b_event(self):
        nonlocal b
        b = int(float(self))
        update_color()


    tk.CTkSlider(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#FF0000', from_=0, to=255,command=r_event).grid(row=0, column=0, pady=5)
    tk.CTkSlider(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#00FF00', from_=0, to=255,command=g_event).grid(row=1, column=0, pady=5)
    tk.CTkSlider(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#0000FF', from_=0, to=255,command=b_event).grid(row=2, column=0, pady=5)
    presenter = tk.CTkFrame(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#000000'); presenter.grid(row=3, column=0, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#000000', text="Restore default Colors",command=restore).grid(row=0, column=1, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color=colors[3], text="Change primary Color", command=lambda: change_color('primary')).grid(row=1, column=1, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color=colors[3], text="Change secondary Color", command=lambda: change_color('secondary')).grid(row=2, column=1, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color=colors[3], text="Change background Color", command=lambda: change_color('background')).grid(row=0, column=2, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color=colors[3], text="Change button background Color", command=lambda: change_color('button_bg')).grid(row=1, column=2, pady=5)
    tk.CTkButton(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color=colors[3], text="Change highlight Color", command=lambda: change_color('highlight')).grid(row=2, column=2, pady=5)
    infog = tk.CTkLabel(master=tabview.tab("Color Selector"), bg_color=colors[2],fg_color='#000000', text=""); infog.grid(row=3, column=1,)


# Run the GUI
calc()
color_selector()
hashcalc()
window.mainloop()