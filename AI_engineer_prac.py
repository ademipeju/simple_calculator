


import tkinter as tk 
#tkinter is a wrapper function for tcl/TK, Tcl/TK helps create buttons, main windows, etc, but for it to work, you need the 
#tkinter for it useability

#create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='lightblue')


#entry widget to display the result
entry = tk.Entry(root, width=20, font= ("Calibri", 24), borderwidth=3, relief = "ridge", bg='white', fg='black', justify='right')
entry.grid(row=0, column=0, columnspan=4)


#Global variable to store the current input and result
current_input = ""

def button_click(value):
    global current_input
    current_input += str(value)
    entry.delete(0, tk.END)
    entry.insert(0, current_input)


def delete_last():
    global current_input
    current_input = current_input[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current_input)


def clear():
    global current_input
    current_input = ""
    entry.delete(0, tk.END)


def calculate():
    global current_input
    try:
        result = str(eval(current_input))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        current_input = ""


def toggle_sign():
    global current_input
    if current_input.startswith('-'):
        current_input = current_input[1:]
    else:
        current_input = '-' + current_input
    entry.delete(0, tk.END)
    entry.insert(0, current_input)

def calculate_sqrt():
    global current_input
    try:
        result = str(eval(f"{current_input}**0.5"))
        current_input = result
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        current_input = ""

def calculate_percentage():
    global current_input
    try:
        result = str(eval(f"{current_input}/100"))
        current_input = result
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        current_input = ""




buttons = buttons = [
    '7', '8', '9', '/', '√',
    '4', '5', '6', '*','1',
    '2', '3', '-', '±','C',
     '0', '.', '=', '+','(', ')',
    '%', '⌫'
]

row = 1
col = 0
for button in buttons:
    if button == "C":
        tk.Button(root, text=button, width=5, height=2, command=clear).grid(row = row, column=col)
    elif button == "=":
        tk.Button(root, text=button, width=5, height=2, command=calculate).grid(row = row, column=col)
    elif button == "⌫":
        tk.Button(root, text=button, width=5, height=2, command=delete_last).grid(row = row, column=col)
    elif button == "±":
        tk.Button(root, text=button, width=5, height=2, command=toggle_sign).grid(row = row, column=col)
    elif button == "√":
        tk.Button(root, text=button, width=5, height=2, command=calculate_sqrt).grid(row = row, column=col)
    elif button == "%":
        tk.Button(root, text=button, width=5, height=2, command=calculate_percentage).grid(row = row, column=col)
    
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda x=button : button_click(x)).grid(row=row, column=col)


    col += 1
    if col >3:
        col = 0
        row += 1



root.mainloop()